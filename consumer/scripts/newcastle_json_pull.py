import requests
import datetime
import os
import math
import pandas as pd
BROKERS = 'aq_mesh_api,Emote Air Quality Sensor'

def get_ncl_data(starttime,endtime):
    api_url = 'http://uoweb3.ncl.ac.uk/api/v1.1/sensors/data/json/'

    params = {
        'broker': BROKERS,
        'starttime': starttime.strftime("%Y%m%d%H%M%S"),
        'endtime': endtime.strftime("%Y%m%d%H%M%S")
    }

    r = requests.get(api_url, params)

    for sensor in r.json()['sensors']:
        for var_name,rows in sensor['data'].items():
            for row in rows:

                value = row['Value']
                units = row['Units']
                sensor_name = row['Sensor Name']
                variable = row['Variable']
                dt = datetime.datetime(1970,1,1) + datetime.timedelta(milliseconds=int(row['Timestamp']))
                lon = sensor['Sensor Centroid Longitude']["0"]
                lat = sensor['Sensor Centroid Latitude']["0"]
                raw_id = sensor["Raw ID"]["0"]

                print(value,dt,lon)



END_PERIOD = datetime.datetime.combine(
    (datetime.datetime.now() -datetime.timedelta(days=1)  ).date(),
    datetime.time(0,0)
)

START_PERIOD = END_PERIOD - datetime.timedelta(days=90)

TIME_DELTA = datetime.timedelta(minutes=1)

steps = int(math.ceil((END_PERIOD - START_PERIOD).total_seconds()/TIME_DELTA.total_seconds()))

for starttime,endtime in [[START_PERIOD + step*TIME_DELTA,START_PERIOD + (step+1)*TIME_DELTA] for step in range(steps)][::-1]:
    print(starttime,endtime)


    csv_name = '{obs}-{start}-{end}.csv'.format(
            start=starttime.strftime("%Y%m%d"),
            end=endtime.strftime("%Y%m%d"),
            obs='ncl'

        )

    csv_file_path = '/obs_data/{file_name}'.format(file_name=csv_name)

    if os.path.exists(csv_file_path):
        continue

    get_ncl_data(starttime,endtime)
    1/0
