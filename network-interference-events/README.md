# Internet Interoperability Index: Network Interference
The script in this repo calculates two summary metrics based on data from the Open Observatory of Network Interference (OONI), a global organization that works to detect Internet censorship. OONI probes in various countries collect measurements when a user runs one of their online tests, and each measurement can be flagged as:
- **anomaly**: a potential act of censorship that is difficult to distinguish from transient network issues (e.g. IP blocking)
- **confirmed**: the user was confirmed as being prevented from accessing the input website

We calculate strict and loose rates of network interference in various geographical areas by aggregating how frequently individual anomalous / confirmed events occur in those locations. The formula for the strict rate is:

<p align = "center"><img src="https://render.githubusercontent.com/render/math?math=\frac{\text{number of confirmed events}}{\text{total number of events}}"></p>

Similarly, the loose rate is calculated as below:

<p align = "center"><img src="https://render.githubusercontent.com/render/math?math=\frac{\text{number of confirmed events} %2B \text{number of anomalous events}}{\text{total number of events}}"></p>

Together, these frequencies can give insight into which countries Internet users face issues in regards to accessing information online and how these trends can be associated to real-world events.

## Getting started

**Set up an AWS EC2 instance** to replicate the OONI MetaDB by [following these instructions](aws-setup.md).

## Calculating rates between date ranges
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

## Acknowledgments
- [Open Observatory for Network Interference](https://ooni.org): data and metadb documentation
