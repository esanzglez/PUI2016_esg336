from __future__ import print_function
import json
import urllib2 
import os
import sys


if not len(sys.argv) == 3: 
    print("Invalid number of arguments. Run as: python  show_bus_locations_esg336 YourKey BusLine") 
    sys.exit() 

   
try:
    key=sys.argv[1]
    bus=sys.argv[2]
    url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(key,bus)
    response = urllib2.urlopen(url)
    data = response.read().decode("utf-8")
    dataMTA = json.loads(data)

    VehicleActivity = dataMTA['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    NumbVeh = len(VehicleActivity)
    LineRef = VehicleActivity[0]['MonitoredVehicleJourney']['LineRef']
    LineRef = str(LineRef).split('_')

    print ('Bus Line:',LineRef[1])
    print ('Number of Active Buses:',NumbVeh)

    for i in range(NumbVeh):
        longitude = VehicleActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        latitude = VehicleActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        print ('Bus {} is at latitude {} and longitud {}'.format (i,latitude, longitude))

except KeyError: print('There is no such a line, please input a correct Bus line')
