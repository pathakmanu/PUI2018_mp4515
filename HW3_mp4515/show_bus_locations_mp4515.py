
# coding: utf-8

# In[9]:


import os
import matplotlib
import json
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
    
if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python aPythonScriptThatWritesToCSV.py mtakey busline mycvs.csv")
    sys.exit()
#CITATION: https://stackoverflow.com/questions/13921910/python-urllib2-receive-json-response-from-url
url= "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+sys.argv[1]+"&VehicleMonitoringDetailLevel=calls&LineRef="+sys.argv[2]
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)
#CITATION: GROUP WORK
data1=data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"]
data2=data1[0]["VehicleActivity"]
x = data2[0]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
y = data2[0]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
lat=[x]
long=[y]
for i in range(len(data2)):
    #print("Bus"+ "is at latitude {} and longitude {}").format(x,y)
    lat.append(x)
    long.append(y)
for i in range(len(data2)):
    print("Bus",i,"is at latitude ", lat[i], "and longitude ", long[i])

