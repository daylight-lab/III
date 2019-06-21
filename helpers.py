import datetime
import json

def dated_filename (fn, ext='.csv'):
    today = datetime.date.today()
    return '{}-{}{}'.format(fn, today, ext)

def load_json (fn):
    with open(fn, 'r') as myfile:
        data=myfile.read()
    return json.loads(data)
