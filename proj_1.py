import time
import requests
import csv
import datetime
import json
from location import *
#from connection_mysql import * #Set setup sql server in docker
from temp import *
import pandas as pd
from datetime import datetime, timedelta


#csv File export:--------------------------
def make_csv(dt,velo,fprint,locat,vis,ts,day,sol_la,sol_lo):

    fieldnames = ['Date','Velocity','footprint','location','visibility',
    'timestamp','daynum','solar_lat','solar_lon']

    rows = [
    {'Date': (dt),
    'Velocity': (velo),
    'footprint': (fprint),
    'location': (locat),
    'visibility': (vis),
    'timestamp': (ts),
    'daynum': (day),
    'solar_lat': (sol_la),
    'solar_lon': (sol_lo)
    }
]

    filename = "records.csv"
    with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

#jeson file export:-----------------------
def make_json(dt,velo,fprint,locat,vis,ts,day,sol_la,sol_lo):

    dictionary ={"Date" : (dt),"Velocity" : (velo),"footprint" : (fprint),
    "location" : (locat),'visibility' : (vis),'timestamp' : (ts),'daynum' : (day),
    'solar_lat' : (sol_la),'solar_lon' : (sol_lo)}

    json_object = json.dumps(dictionary, indent = 9)
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)



#UTC time formet:--------------------------
def UtcNow():
    now = datetime(*time.gmtime()[:6])
    return now




if __name__ == '__main__':
    #store value -----------------------
    out=[]
    velo=[]
    fprint=[]
    dt=[]
    loc=[]
    vis=[] #str
    ts=[] #hr min
    day=[]
    sol_la=[]
    sol_lo=[]

    #Data Resive Time:------------------
    sh = input("Enter Time to fetch Data from ISS(UTC time format-'HH:MM:SS',default time is 12:00:00): ")
    if sh=='':
        sh="12:00:00"



    try:
      while 1:
        d_t=conv(sh)-30
        print(UtcNow().time())
        #str(UtcNow().time())==sh
        if (str(UtcNow().time())==sh):
            #reseving data from api:--------------------------------
          response_API=requests.get('https://api.wheretheiss.at/v1/satellites/25544')


          #storing data in list:------------------------------------
          data=response_API.text
          df=json.loads(data)
          dt.append(str(UtcNow().date()))
          cal=(df['velocity']*1000/3600)
          velo.append(cal)
          fprint.append(df['footprint'])
          loc.append(lc((df['latitude']),(df['longitude'])))
          vis.append(df['visibility'])
          ts.append(con_sec(df['timestamp']))
          day.append(str(df['daynum']))
          sol_la.append(str(df['solar_lat']))
          sol_lo.append(str(df['solar_lon']))

          #to sql data base:---------------------------
          # remove comment from import to use this function 
          #ins_mysql(str(UtcNow().date()),str(df['velocity']*1000/3600),
          #  str(df['footprint']),lc((df['latitude']),(df['longitude'])),(df['visibility']),
           #     (con_sec(df['timestamp'])),(str(df['daynum'])),(str(df['solar_lat'])),(str(df['solar_lon']))
            #    )
          #print(df)
        elif(60<d_t):
            time.sleep(d_t)

    except KeyboardInterrupt:
        print ('KeyboardInterrupt is caught')
        make_json(dt,velo,fprint,loc,vis,ts,day,sol_la,sol_lo)
        make_csv(dt,velo,fprint,loc,vis,ts,day,sol_la,sol_lo)
        print('Saved')
        pass
