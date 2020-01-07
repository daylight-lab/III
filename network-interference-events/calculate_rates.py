import pandas as pd
import sqlalchemy as sql
import sys
import time

start_time = time.time()

# user passes in MM-DD-YYYY date formats
start_date = sys.argv[1]
end_date = sys.argv[2]

filename = "rates_" + start_date + "_" + end_date +  ".csv" # filename includes date endpoints by default, can be customized
if len(sys.argv) > 3: filename = sys.argv[3]

# define column formats of intermediate joined measurement + report table before rates calculation
cc_col = "probe_cc as country_code"
confirmed_col = "count(case when confirmed then 1 end) as num_confirmed_interference"
anomaly_col = "count(case when anomaly then 1 end) as num_anomaly"
not_confirmed_col = "count(*) - count(case when confirmed then 1 end) as num_no_confirmed_interference"

# define rate column formats
# convert each int to decimal form to set rate column types (prevent fractions from being rounded down to 0)
# set rate value to 0 if denominator is 0 (prevent division by 0 error)
strict_rate = "case when agg_meas.num_confirmed_interference + agg_meas.num_no_confirmed_interference > 0 then cast(agg_meas.num_confirmed_interference as decimal) / cast(agg_meas.num_confirmed_interference + agg_meas.num_no_confirmed_interference as decimal) else 0 end as strict_rate"
loose_rate = "case when agg_meas.num_confirmed_interference + agg_meas.num_no_confirmed_interference > 0 then (cast(agg_meas.num_anomaly as decimal)) / cast(agg_meas.num_confirmed_interference + agg_meas.num_no_confirmed_interference as decimal) else 0 end as loose_rate"

# create column selection phrases
agg_meas_cols = ", ".join([cc_col, confirmed_col, anomaly_col, not_confirmed_col])
rate_cols = ", ".join([strict_rate, loose_rate])

meas_condition = "measurement.measurement_start_time between '" + start_date + "' AND '" + end_date + "'" # filter the measurement table by rows in date range
report_condition = "report.test_start_time between '" + start_date + "' AND '" + end_date + "'" # filter the report table by rows in the date range

# compose command to generate final rates table in the following format
# country_code | num_confirmed_interference | num_anomaly | num_no_confirmed_interference | strict_rate | loose_rate
command = "select *, " + rate_cols + " from (select " + agg_meas_cols  + " from (select * from measurement where " + meas_condition + ") meas left join (select * from report where " + report_condition + ") rep on meas.report_no = rep.report_no group by probe_cc) agg_meas"

# print command and filename for now (debugging + metadb access issues)
print(command)
print(filename)

# sys.exit(0) # remove when metadb connection can be created

sql_engine = sql.create_engine('postgresql:///metadb') # connect to the database...

rates = pd.read_sql_query(command, sql_engine)

rates.to_csv(filename) # write results of sql query to a file

print("--- %s seconds ---" % (time.time() - start_time))
