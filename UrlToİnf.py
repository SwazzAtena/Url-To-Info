import time
import random
from colorama import Fore, init

bakiye=100

print(Fore.LIGHTRED_EX)
print("PythonX-Small23 E HOŞGELDİN!!")
time.sleep(1)
print("Yükleniyor...")
time.sleep(4)
print("Son Hazırlıklar")
time.sleep(2)
print("HOŞGELDİN DOSTUM İSMİNİ ÖĞRENEBİLİRMİYİM")
time.sleep(3)
print(Fore.BLUE)
gr=input("İsminizi Oluşturun: ")
time.sleep(2)
print("Ooooo Çok Havalı , Hoşgeldin " + gr)
print(Fore.LIGHTMAGENTA_EX)
print("Oyuna Başlamadan Önce Sana Bazı Şeyler Öğretmem Gerekiyor...")
time.sleep(2)
print(gr +" Oyuna 100PX Bakiyeyle Başlarsın Ve Oynadıkça Bakiyen Artar")
time.sleep(2)
print("Aşşağıda Paran , Şansın , Uyku Puanın Yazıyor Bunlara Dikkat Et!")
print("""
💵:100
🍀:10
🛏:100
""")
while True:
    print("""
1)Zar VS
2)Zar Tahmin
3)
    """)
    k=input("Hangisini Oynamak İstersiniz")
    if k=='1':
        print("Oyunumuzda Rastgele Zar Atarsın 1 Ve 6 Arasına Karşındaki Rakiple Daha Yüksek Atan Paranın 2 Katını Alır")
        playerone=input("Zar Atmak İçin Bir Tuşa Basınız: ")
        print("🎲")
        print("🎲")
        print("🎲")
        print("Attığın Sayııııııı")
        time.sleep(2)
        print(Fore.YELLOW)
        x=random.randint(1, 6)
        print(x)
        time.sleep(2)
        playertwo=print("Zar Atılıyorrr")
        print("Rakibin Attığı Sayıııı")
        time.sleep(2)
        print(Fore.LIGHTYELLOW_EX)
        y=random.randint(1, 6)
        time.sleep(2)
        print(y)
        if x >= y:
            time.sleep(2)
            print("Bakiyeniz Aşşağıda Tebriklerr ")
            print(bakiye * 2)
            time.sleep(2)
        else:
            print("Bakiyeniz :(")
            print(bakiye / 2)
    if k=='2':
        print("Zar Tahmin Oyununa Hoş Geldiniz!")
        time.sleep(2)
        print("1 ile 6 arasında bir sayı seçin ve zar atın.")
        tahmin = int(input("Tahmininiz nedir? "))
        time.sleep(2)
        zar = random.randint(1, 6)
        print("Zar atıldı! Sonuç:", zar)
        time.sleep(2)
        if tahmin == zar:
                    print("Tebrikler, doğru tahmin ettininiz")
                    print("Bakiyeniz Aşşağıda")
                    print(bakiye*2)
                    bakiye=(bakiye*2)
        else:
                    print("Maalesef yanlış tahmin ettiniz!")
                    print("Bakiyeniz Aşşağıda")
                    print(bakiye/2)
                    bakiye=(bakiye/2)
        if bakiye=='0':
                    print("Battınız")
                    print(bakiye)
                    a=input("Çıkmak İçib Bir Tuşa Basınız")
                    exit()