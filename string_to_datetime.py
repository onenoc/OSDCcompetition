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
    for s_date in ls_dates:
        if i_type == 0:
            if ':' in s_date:
                s_date = s_date[:-15]
            ldt_dates.append(dt.datetime.strptime(s_date, '%Y-%m-%d'))
        elif i_type == 1:
            ldt_dates.append(dt.datetime.strptime(s_date, '%Y/%m/%d'))
    return ldt_dates

def detect_separator(s_date):
    if '-' in s_date:
        return 0
    if '/' in s_date:
        return 1

def create_dates_from_file(s_filename, i_date_index):
    ls_dates = []
    with open(s_filename, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        ls_dates = [row[i_date_index] for row in csv.reader(csvfile.read().splitlines())]
        if s_twitter_filename == 'twitter_data.csv':
            del ls_dates[0]
    return ls_dates

if __name__=="__main__":
    ls_dates = []
    s_weather_filename = 'weather_data.csv'
    s_twitter_filename = 'twitter_data.csv'
    ls_weather_dates = create_dates_from_file(s_weather_filename, 0)
    ls_twitter_dates = create_dates_from_file(s_twitter_filename, 2)
    print string_to_datetime(ls_weather_dates)
    print string_to_datetime(ls_twitter_dates)
