import datetime

def dated_filename (fn, ext='.csv'):
    today = datetime.date.today()
    str(today)
    return '{}-{}{}'.format(fn, today, ext)
