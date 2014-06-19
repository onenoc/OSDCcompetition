import datetime as dt
import time
import csv

def string_to_datetime(ls_dates):
    '''
    @summary: convert a list of dates in string format to a list of dates in
    datetime format
    @param ls_dates: a list of dates in string format
    '''
    i_type = detect_separator(ls_dates[0])
    ldt_dates = []
    print i_type
    for s_date in ls_dates:
        if i_type == 0:
            print dt.datetime.strptime(s_date, '%Y-%m-%d')

            

def detect_separator(s_date):
    if '-' in s_date:
        return 0

if __name__=="__main__":
    ls_dates = []
    with open('weather_data.csv', 'rb') as csvfile:
        for row in csvfile:
            ls_row = [k.strip() for k in row.split(', ')]
            for s_row in ls_row:
                ls_dates.append(s_row.split(',')[0])
    string_to_datetime(ls_dates)
