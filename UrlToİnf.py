import socket
import os
os.system("pip install ip2geotools")
from ip2geotools.databases.noncommercial import DbIpCity
from colorama import Fore , init
print(Fore.LIGHTMAGENTA_EX)
print("Gerekli Yüklemeler Yapılıyor Biraz Uzun Sürebilir")
os.system("pip install colorama")
os.system("pip install ip2geotools")
while True:
    print(Fore.LIGHTRED_EX)
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
    print(Fore.LIGHTGREEN_EX)
    input("Tekrarlamak İçin Herhangi Bir Tuşa Basın")
