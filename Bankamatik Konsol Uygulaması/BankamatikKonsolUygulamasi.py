from time import sleep
import os
class BankamatikKonsolUygulamasi():
    __ekran="""____________________________________
    BANKAMATİK KONSOL UYGULAMASI

1- Bakiye Sorgulama
2- Para Yatırma
3- Para Çekme
4- Hesaplarım arası para aktarımı
5- Yeni bir hesap aç
6- Bir hesap sil
7- ÇIKIŞ
____________________________________
"""
    def __init__(self):
        print("\nBankamatik Konsol Uygulamasına Hoş Geldiniz!\nAşağıdaki Ekranda Gözüken İşlemleri Yapabilirsiniz")
    
    def dosyaAc(self,kip="r"):
        if os.path.exists(os.getcwd()+os.sep+BankamatikKonsolUygulamasi.csv):
            dosya=open("BankamatikKonsolUygulamasi.csv",kip)
            return dosya
        else:
            print("Sisteme erişmeede beklenemdik bir hata oluştur.Lütfen daha sonra tekrar deneyin")
            raise Exception
    
    def sorgula(self):
        dsy=self.dosyaAc()
        print("Bakiyeniz")
        for hesbak in dsy:
            hesap="Hesap {},Bakiyeniz={} TL".format(hesbak.split(";")[0].strip("\n"),hesbak.split(";")[1].strip("\n"))
            print(hesap)
    
    def paraIslemi(self,param=0):
        mesajlar=[
            "Hangi Hesabınıza para yatıracaksınız.\nHesap numarası giriniz : ",
            "Yatırmak istediğiniz miktar : ",
            "Hangi Hesabınızdan para cekeceksiniz.\nHesap numarası giriniz : ",
            "Çekmek istediğiniz miktar : "
            ]
        self.sorgula()

        dsy=self.dosyaAc("a+")
        dsy.seek(0)

        hesapDurum="\nGirdiğiniz Hesap Numarası Bulunamadı"
        icerik=dsy.readlines

        if param==0:
            hesap=input("{}".format(mesajlar[0]))
        else:
            hesap=input("{}".format(mesajlar[2]))
        
        for hesbak in icerik:
            hes=hesbak.split(";")[0].strip("\n")
            if hesap==hes:
                bak=int(hesbak.split(";")[1].strip("\n"))
                try:
                    if param==0:
                        miktar=int(input("{}".format(mesajlar[1])))
                        bak=miktar+bak
                    else:
                        miktar=int(input("{}".format(mesajlar[3])))
                        if miktar>bak:
                            hesapDurum="Yetersiz Bakiye!\n"+("."*17)
                            break
                        else:
                            bak=bak-miktar
                except:
                    hesapDurum="Miktar Bilgisi Rakam Olarak Girilmediğinden İşleminiz İptal Edilmiştir"
                    break
            else:
                bak=str(bak)+"\n"
                yeni_eklencek=";".join([hes,bak])
                indeks=icerik.index(hesbak)
                icerik.pop(indeks)
                icerik.insert(indeks,yeni_eklencek)
                hesapDurum="."*17
                break
        dsy.seek(0)
        dsy.truncate()
        dsy.seek(0)
        dsy.writelines(icerik)
        dsy.close()
        print("{}".format(hesapDurum))
        self.sorgula()
    def hesaplarArasi(self):
        self.sorgula()

        dsy=self.dosyaAc("a+")
        dsy.seek(0)

        hesapDurum= "\nGirdiğiniz İLK Hesap Numarası bulunamadı.\n" + "."*17
        hesaplarVarmi=[0,0]
        icerik=dsy.readlines()

        hes1=input("Hangi Mevduat Hesabınızdan Para Alınsın?:")

        bakSon=[]
        hesSon=[]

        for hesbak in icerik:
            hes=hesbak.split(";")[0].strip("\n")
            if hes1==hes:
                hesaplarVarmi[0]=1
                bakSon.append(int(hesbak.split(";")[1].strip("\n")))
                hesSon.append(hesbak)
                break
        if hesaplarVarmi[0]==1:
            hes2=input("Hangi Mevduat Hesabınıza Para Eklensin?:")
            if hes==hesSon[0].split(";")[0].strip("\n"):
                hesapDurum="\nPara Gönderen ve Alan Hesap Numarası Aynı Olamaz.\n"+"."*17
            else:
                for hesbak in icerik:
                    if hes2==hes:
                        hesaplarVarmi[1]=1
                        bakSon.append(int(hesbak.split(";")[1].strip("\n")))
                        hesSon.append(hesbak)
                        break
                if len(hesSon)<2:
                    hesapDurum="\nGirdiğiniz İkinci Bir Hesap Numarası Bulunamamıştır.\n"+"."*17
        if hesaplarVarmi[1]==1:
            miktar=int(input("Ne Kadar Para Transfer Etmek İstersiniz?:"))
            if miktar>bakSon[0]:
                hesapDurum="Bu İşlem İçin Yeterli Bakiyeniz Bulunmamaktadır!"
            else:
                bakSon[0]=bakSon[0]-miktar
                bakSon[1]=bakSon[1]+miktar
                for i in range(2):
                    indeks=icerik.index(hesSon[i])
                    icerik.pop[indeks]
                    bak=str(bakSon[i])+"\n"
                    yeni_eklencek=";".join([hesSon[i].strip("\n"),bak])
                    icerik.insert(indeks,yeni_eklencek)
        dsy.seek(0)
        dsy.truncate(0)
        dsy.seek(0)
        dsy.writelines(icerik)
        dsy.close()
        print("{}".format(hesapDurum))
        self.sorgula()

    def hesapAc(self):
        import random as rm
        tercih=input("Yeni Bir Mevduat Hesabı Açmak İstediğinizden Emin Misiniz? Evet/Hayır:").lower()
        if tercih=="Evet":
            dsy=self.dosyaAc("a+")
            dsy.seek(0)
            
            icerik=dsy.readlines()
            
            hesapNo=""
            if icerik:
                devam=True
                indeks=0
                while devam:
                    hesapNo=str(rm.randrange(1,101))
                    devam=False
                    for hesbak in icerik:
                        hes=hesbak.split(";"[0].strip("\n"))
                        if int(hesapNo)<int(hes):
                            indeks=icerik.index(hesbak)
                            yeni_eklencek=";".join([hesapNo,"0\n"])
                            icerik.insert(indeks,yeni_eklencek)
                            break
            else:
                hesapNo=str(rm.randrange(1,101))
                yeni_eklencek=";".join([hesapNo,"0\n"])
                icerik.append(yeni_eklencek)
        
                dsy.seek(0)
                dsy.truncate()
                dsy.seek(0)
                dsy.writelines(icerik)
                dsy.close()
                print("{}".format("."*17))
                self.sorgula
        elif tercih=="h":
            print("Yeni Bir Mevduat Hesabı Açma İşlemi İptal Edildi!\n")
        else:
            print("{}\n{}".format("UYARI!","Geçerli bir işlem seciniz"))   

    def hesapSil(self):
        tercih = input("Hesap silmek istediğinizden emin misiniz? E/H : ").lower()  
        if tercih == "e":
            self.sorgula()   
            hesapNo = input("Hangi hesabı silmek istiyorsunuz: ")

            dsy = self.dosyaAc("a+")
            dsy.seek(0)#a+'da açıldığı için imlec dosyanın sonunda. Okuma yapabilmek için dosyanın
                    #başına getiriliyor.
            
            icerik = dsy.readlines() #Dosyanın içeriği okunuyor.

            hesapDurum = "\nGirdiğiniz Hesap Numarası bulunamadı.\n" + "." * 17
            for hesbak in icerik:
                hes = hesbak.split(";")[0].strip("\n")
                if hesapNo == hes:
                    
                    bakiye = int(hesbak.split(";")[1].strip("\n"))
                    if bakiye < 0:
                        hesapDurum = "\nHesabınızda borç olduğundan hesap SİLİNEMEZ\n" + "." * 17
                    elif bakiye == 0:
                        icerik.remove(hesbak)
                        hesapDurum = "\nHesap silindi\n" + "." * 17
                    else:
                        hesapDurum = "Hesabınızda para bulunuyor. Hesabı silmeden önce parayı alınız.\n" + "." * 17
                    break
                            
            #dosyaya yazılıyor.
            dsy.seek(0)
            dsy.truncate()
            dsy.seek(0)
            dsy.writelines(icerik)
            dsy.close()
            ######################

            #son durum kullanıcıya gösteriliyor.
            print("{}".format(hesapDurum))

            self.sorgula()

        elif tercih == "h":
            print("Hesap silme İŞLEMİ İPTAL EDİLDİ...\n")
        else:
            print("{}\n{}".format("UYARI!","Geçerli bir işlem seciniz"))   

    def anaEkran(self):
        try:
            while True:
                print(self.__ekran)
                secenek = input("Hangi işlemi yapmak istiyorsunuz :  ")

                if secenek == "1":
                    self.sorgula()
                elif secenek == "2":
                    self.paraIslemi()
                elif secenek == "3":
                    self.paraIslemi(1)
                elif secenek == "4":
                    self.hesaplarArasi()
                elif secenek == "5":
                    self.hesapAc()
                elif secenek == "6":
                    self.hesapSil()
                elif secenek == "7":
                    tercih = input("Çıkmak istediğinizden emin misiniz? E/H : ").lower()
                    if tercih == "e":
                        print("ÇIKIŞ İŞLEMİ YAPILIYOR...\nLÜTFEN BİRAZ BEKLEYİNİZ...")
                        sleep(2)#2 saniye bekletiyor.
                        break
                    elif tercih == "h":
                        print("ÇIKIŞ İŞLEMİ İPTAL EDİLDİ...\n")
                    else:
                        print("{}\n{}".format("UYARI!","Geçerli bir işlem seciniz"))   
                else:
                    print("{}\n{}".format("UYARI!","Geçerli bir işlem seciniz"))
        except:
            print("Beklenmedik bir hatayla karşılaşıldığından dolayı ÇIKIŞ İŞLEMİ YAPILIYOR...")
            sleep(2)#2 saniye bekletiyor.

if __name__ == "__main__":
    bku = BankamatikKonsolUygulamasi()
    bku.anaEkran()