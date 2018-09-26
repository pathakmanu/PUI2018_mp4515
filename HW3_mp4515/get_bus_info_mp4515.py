from __future__ import print_function

import os
import matplotlib
import json
import sys
import csv
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Run as: python aPythonScriptThatWritesToCSV.py mtakey busline mycvs.csv")
    sys.exit()

url= "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+sys.argv[1]+"&VehicleMonitoringDetailLevel=calls&LineRef="+sys.argv[2]
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)
# CITATION: https://stackoverflow.com/questions/13921910/python-urllib2-receive-json-response-from-url
csv_file = open (sys.argv[3],'w')
csv_file.write('Latitude,Longitude,Stop Name,Stop Status\n')

if not data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0].get('VehicleActivity'):
    csv_file.close()
    print("exit")
    sys.exit()

count=len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

for i in range(count):
    loc=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']
    if data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']=={}:
        stop='N/A'
        status='N/A'
        csv_file.write(str(loc['Latitude'])+','+str(loc['Longitude'])+','+stop+','+status+'\n')
    else:
        count2=len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'])
        for j in range(count2):
            status=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][j]['Extensions']['Distances']['PresentableDistance']       
            stop=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][j]['StopPointName']
            csv_file.write(str(loc['Latitude'])+','+str(loc['Longitude'])+','+str(stop)+','+str(status)+'\n')
# CITATION: work done in group
csv_file.close()
