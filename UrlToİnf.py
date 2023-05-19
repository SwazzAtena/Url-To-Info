import socket
import os
from ip2geotools.databases.noncommercial import DbIpCity
from colorama import Fore , init
print(Fore.LIGHTMAGENTA_EX)
print("Gerekli Yüklemeler Yapılıyor Biraz Uzun Sürebilir")
os.system("pip install colorama")
os.system("pip install ip2geotools")
url = input("Site Adresini Giriniz : ")
ipadres = socket.gethostbyname(url)
print("By Ömer Tuğrul Bayram :) ")
response = DbIpCity.get(ipadres,api_key='free')
print("İp Adresi: " , ipadres)
print("Şehir: "  , response.city)
print("Bölge: " , response.region,)
print("Ülke: " , response.country)
print("Enlem: " , response.latitude)
print("Boylam: " , response.longitude)
