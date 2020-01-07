# Internet Interoperability Index: Network Interference

## Running the notebooks
In the main repo directory, run a jupyter notebook.

```
cd network_interference/
jupyter notebook
```

The yearly-interference-analysis file includes EDA, strict / loose rate network interference index calculations, and visualizations. 

The try-database-connection notebook helps test whether the OONI metadb has been set up correctly in postgres.

## Calculating rates between date ranges
**Required packages**: pandas, sqlalchemy, sys, time

The calculate\_rates.py script takes two required arguments (start date, end date) and one optional argument (filename for resulting table). To generate a table representing aggregate data including the strict / loose rates over the year 2019, run the following in the repo directory:

```
python3 calculate_rates.py 01-01-2019 12-31-2019
```

Use MM-DD-YYYY format for the dates. If no filename argument is passed, the resulting file will be named "rates\_MM-DD-YYYY\_MM-DD-YYYY.csv" where the first date is the start date and the second is the end date. It will be located in the current directory. An example with a customized filename is below:

```
python3 calculate_rates.py 01-01-2019 12-31-2019 rates_2019.txt
```

**Note**: A common error can look like the below.

```
ERROR: canceling statement due to conflict with recovery
DETAIL: User query might have needed to see row versions that must be removed.
```

This is an issue with OONI's directions to set `hot_standby = 'on'` in `/etc/postgresql/9.6/main/conf.d/hot_standby.conf` (see step 3 of their [metadb sharing instructions](https://github.com/ooni/sysadmin/blob/master/docs/metadb-sharing.md)). Because the server is on hot\_standby, long queries can fail because some necessary rows can be updated or deleted during the run. To get around this, run the following:

```
echo -e "hot_standby = 'on'\nhot_standby_feedback = 'on'" | sudo -u postgres dd of=/etc/postgresql/9.6/main/conf.d/hot_standby.conf
```

## License
BSD-3
