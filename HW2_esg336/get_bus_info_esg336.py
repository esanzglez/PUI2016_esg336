from __future__ import print_function
import json
import urllib2 
import os
import sys

#How to check how many arguments belongs to Federica
if not len(sys.argv) == 4: 
    print("Invalid number of arguments. Run as: python  show_bus_locations_esg336 YourKey BusLine BusLine.csv") 
    sys.exit()
    
key = sys.argv[1]
bus = sys.argv[2]
BusFile = open(sys.argv[3],'w')
BusFile.write('Latitude,Longitude,Stop Name,Stop Status \n')

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(key,bus)
response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
dataMTA = json.loads(data)

try:
    
    VehicleActivity = dataMTA['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    NumbVeh = len(VehicleActivity)

    for i in range(NumbVeh):
        try:     
            longitude = VehicleActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
            latitude = VehicleActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            vehicle = dataMTA['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]
            bus = vehicle['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall']
            status = bus[0]['Extensions']['Distances']['PresentableDistance']
            stop_name = bus[0]['StopPointName']
            info='{},{},{},{}\n'.format(longitude,latitude,stop_name,status)
            BusFile.write(info)
        except KeyError:
            status= 'N/A'
            stop_name='N/A'
            info='{},{},{},{}\n'.format(longitude,latitude,stop_name,status)
            BusFile.write(info)
            continue
except KeyError: print('There is no such a line, please input a correct Bus line')

