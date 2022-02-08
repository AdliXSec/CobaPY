import requests
import json
import os
import platform

if platform.system() == "Windows":
    hapus = "cls"
else:
    hapus = "clear"

os.system(hapus)
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