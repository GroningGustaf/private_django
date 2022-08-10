import requests
from requests.auth import HTTPBasicAuth
import csv


#----- description -----#
# Returns all the devices of a given type, here C22.
# Currently hardcoded for a given company on test 
# server, rebuild so that it can loop through companies.
#-----------------------#
def getAllC22Devices(): 
    URL = 'https://bo.indev.sigicom.net/boapi/v0/company/1/device/all'
    list_of_c22_devices = []

    r = requests.get(url=URL, headers={'accept': 'application/json'}, 
    verify=False, auth=HTTPBasicAuth('bo-token:1', 'token'))

    data = r.json()
    for i in data:
        if i['type'] in 'C22':
            list_of_c22_devices.append(i['serial'])

    return list_of_c22_devices

getAllC22Devices()