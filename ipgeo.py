import requests
import json
import os
import platform

if platform.system() == "Windows":
    hapus = "cls"
else:
    hapus = "clear"

os.system(hapus)
print('''
  _____ _____     _____            _                     _   _             
 |_   _|  __ \   / ____|          | |                   | | (_)            
   | | | |__) | | |  __  ___  ___ | |     ___   ___ __ _| |_ _  ___  _ __  
   | | |  ___/  | | |_ |/ _ \/ _ \| |    / _ \ / __/ _` | __| |/ _ \| '_ \ 
  _| |_| |      | |__| |  __/ (_) | |___| (_) | (_| (_| | |_| | (_) | | | |
 |_____|_|       \_____|\___|\___/|______\___/ \___\__,_|\__|_|\___/|_| |_|
                By : AdliXSec   Team : Dark Clown Security     
				                                             
''')
ipaddr = input("Ip Address : ")
ipreq = requests.get(f"http://ip-api.com/json/{ipaddr}")

if ipreq.status_code == 200:
	ipdata = json.loads(ipreq.text)

	if ipdata["status"] == "success":
		for key in ipdata:
			print(f"{key.capitalize()} : {ipdata[key]}")
			
			if key == "lon":
				lat = ipdata["lat"]
				lon = ipdata["lon"]
				maps = f"https://www.google.com/maps/@{lat},{lon},9z"
				print(f"Maps : {maps}")