## Getting up and running with OONI Metadb on AWS

0. To set up a copy of the OONI metadb which contains the measurement-specific
   data needed for this analysis, create an AWS EC2 instance by following
   [OONI's metadb sharing
   directions](https://github.com/ooni/sysadmin/blob/master/docs/metadb-sharing.md).
   Instead of selecting the 16.04, **select the Ubuntu 16.04 deep Learning kit**
   (which includes Jupyter notebook)
1. After tunneling into the EC2 instance, run <code>sudo -u postgres psql -U
   postgres metadb -c 'SELECT MAX(bucket_date) FROM autoclaved'</code> to check
   that the output matches the day before the download.
2. Running <code>sudo -u postgres psql -U postgres metadb</code>, then
   <code>\dt</code> should list all available relations including 'autoclaved',
   'badblob', <a href =
   "https://docs.google.com/document/d/1vB8taIbSOBxBRKMozCZwvt88iByghcIUJGh9nnk6vHo/edit?usp=sharing">etc</a>.
3. Check your Python version to make sure that Python3 is available. If >3.5.2
   is on the path, use <code>pip3 install [package name]</code>. Otherwise, use
   <code>sudo apt-get install python3-[package name]</code>. Install the
   following packages: matplotlib, seaborn, pandas, numpy, scipy, psycopg2
   (sqlalchemy dependency), sqlalchemy, jupyter.
4. Access the Python interpreter on the instance by typing `python3` into the
   terminal.
5. When the prompt appears, import sqlalchemy and pandas, and run the following: 


```
db = create_engine('postgres://metadb')
pd.read_sql_table('autoclaved', conn)
conn = db.connect()
```

If these lines execute without errors, sqlalchemy can successfully access the tables in the metadb and convert them into pandas objects.
