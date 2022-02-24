from dotenv import load_dotenv
import os


load_dotenv()
API_KEY = os.getenv("API_KEY")

def full_ip_details(ip:str)->dict: 
    from ipdata import ipdata
    ipdata = ipdata.IPData(API_KEY)
    return ipdata.lookup(ip)

def important_details(ip):
   import json 
   ip_details = full_ip_details(ip)
   my_ip = ip_details["ip"]
   my_region = ip_details["region"]
   my_regi_code = ip_details["region_code"]
   my_country =  ip_details["country_name"]
   my_dict = {"ip" : my_ip,
   "region" : my_region,
   "region code" : my_regi_code,
   "my country" : my_country,}
   jsonString = json.dumps(my_dict)
   with open("ip_file.json","a+") as file:
      file.write(jsonString)
      return file.read()

ip = input("write your ip: ")
important_details(ip)
