from numpy import empty
import requests
from requests.auth import HTTPBasicAuth
import csv
import datetime
import os


#-------- Step 2 ------------  #
# ---------------------------- # 
# As well as oldest timestamp for GSP measurement per unit.
# UTAN GPS:
# Measurements without any coordinates aswell, oldest timestamp
# For 10; olika sleep tider.
# -------- -------- --------#

# OUTER LOOP
# go to https://bo.indev.sigicom.net/boapi/v0/company/1/device/all
# save result as data
# For each row:
#   if data['type] == C22
#   serial = append data['serial'] to list_of_c22_devices


#for i in serial: 
# URL = 'https://bo.indev.sigicom.net/boapi/v0/company/1/device/C22/' + i + '/sio/'

# https://bo.indev.sigicom.net/boapi/v0/company/1/device/C22/102019




# Step 1 - Get all C22 for a given company
#----- description -----#
# Returns all the devices of a given type, here C22.
# Currently hardcoded for a given company on test 
# server, rebuild so that it can loop through companies.
#-----------------------#

csv_name = "test.csv"
# os.remove(csv_name)

def get_company_list():

    company_list = []
    #how do we get the amount companies 

    URL_all = 'https://bo.indev.sigicom.net/boapi/v0/company'

    a = requests.get(url=URL_all, headers={'accept': 'application/json'}, 
    verify=False, auth=HTTPBasicAuth('bo-token:1', 'token'))

    index = a.json()

    for i in index:
        company_list.append(i['id'])

    return company_list # [company_id1, company_id2, etc..]

    

def getAllC22Devices(company_id): 
    
    URL = 'https://bo.indev.sigicom.net/boapi/v0/company/' + str(company_id) + '/device/all'
    list_of_c22_devices = []
    
    r = requests.get(url=URL, headers={'accept': 'application/json'}, 
    verify=False, auth=HTTPBasicAuth('bo-token:1', 'token'))

    data = r.json()
    for i in data:
        if i['type'] in 'C22':
            list_of_c22_devices.append(i['serial'])
     
    print("this is important"+ str(list_of_c22_devices))

    return list_of_c22_devices

        

# Step 2 - loop through all devices and create CSV rows
def createCSV(list_of_devices):
    headings = ["id", "timestamp", "gps_long", "gps_lat"]
    
    with open(csv_name, "a") as file: # Create metadata in csv-file
        writer = csv.writer(file)
        writer.writerow(headings)
        
        for i in list_of_devices:
            URL = 'https://bo.indev.sigicom.net/boapi/v0/company/1/device/C22/' + str(i) #första en lång list, nu

            r = requests.get(url=URL, headers={'accept': 'application/json'}, verify=False, auth=HTTPBasicAuth('bo-token:1', 'token'))
            print(URL)
            data = r.json()

            gps_data_list = [] # Append onto this all values we need
            
            gps_data_list.append(i)

            if 'gps_data' in data:

                if data['gps_data']['gps_failed'] == False:
                    # ---- create row of device info ---- # 
                    # gps_data_list.append(data['id'])
                    timestamp = data['gps_data']['gps_timestamp_last_read']
                    # Transform timestamp from unix to CSV format
                    csv_time = datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
                    
                    gps_data_list.append(csv_time)
                    #gps_data_list.append(data['gps_data']['gps_timestamp_last_read'])
                    gps_data_list.append(data['gps_data']['gps_long'])
                    gps_data_list.append(data['gps_data']['gps_lat'])
                    # gps_data_list.append(data['data'][0]['data']['gps_lat'])
                    print("writing row with values" 
                    + str(gps_data_list) + "\n" )
                    # ---- ---- ---- ---- ---- ---- ----- # 
            # else:
            #     gps_data_list.append(["none", "none", "none"])

            
            writer.writerow(gps_data_list)

list_of_companies = get_company_list() # 6, 1, 2
list_of_c22_devices = []

for i in list_of_companies:
    list_of_c22_devices.extend(getAllC22Devices(i))
    
print("we are now past getAllC22Devices")
print(list_of_c22_devices)
createCSV(list_of_c22_devices)


# 1. get number of companies (how+)
# for each in company_list:
#   GetAllC22Devices(company_id)
#   createCSV(company_c22_list)
