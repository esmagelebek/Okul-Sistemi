import random

class Okul:
   def __init__(self,isim):
       self.isim=isim
   class Ogrenci:
       def __init__(self,isim,soyisim,no,sinif,disiplin_puani,ders={"Türkçe":0,"Matematik":0}):
           self.isim=isim
           self.soyisim=soyisim
           self.no=no
           self.sinif=sinif
           self.disiplin_puani=disiplin_puani
           self.ders=ders
       def disiplin(self):
           disiplin=input("Öğrenci disipline gitti mi?(Evet ya da hayır yazınız!)")
           if disiplin=="Evet":
               self.disiplin_puani-=10
               if self.disiplin_puani<=0:
                   print("Öğrenci kaydı silindi!")
                   self.isim=None
                   self.soyisim=None
                   self.no=None
                   self.sinif=None
                   self.disiplin_puani=None
               else:
                   print("Öğrencimizin disiplin puanı 10 puan düşürüldü! Yeni puanı: ",self.disiplin_puani)
           elif disiplin!="Evet" or disiplin=="hayır":
               print("Meşgul etme!!")
       def goruntule(self):
           print("""
            İsim: {}
            Soyisim: {}
            No: {}
            Sınıf: {}
            Disiplin Puanı: {}
            """.format(self.isim,self.soyisim,self.no,self.sinif,self.disiplin_puani))
       def puan_degis(self):
           girdi=input("Lütfen puan değiştirmek istediğiniz dersi giriniz ('Türkçe' ya da 'Matematik') :")
           if girdi=="Türkçe":
               self.ders["Türkçe"]=int(input("Lütfen puanı giriniz: "))
               if 0<=self.ders["Türkçe"]<=100:
                   print("Başarılı bir şekilde puan değişti. Türkçe Puanınız :  ",self.ders["Türkçe"])
               else:
                   print("Puan değişemedi!!!")
                   self.ders["Türkçe"]=0
           elif girdi=="Matematik":
               self.ders["Matematik"] = int(input("Lütfen puanı giriniz: "))
               if 0 <= self.ders["Matematik"] <= 100:
                   print("Başarılı bir şekilde puan değişti. Matematik Puanınız :  ", self.ders["Matematik"])
               else:
                   print("Puan değişemedi!!!")
                   self.ders["Matematik"] = 0
           else:
               print("Böyle bir ders yok!!!")
       def puan_goruntule(self):
           print("""
            Matematik Notunuz: {}
            Türkçe Notunuz: {}
           """.format(self.ders["Matematik"],self.ders["Türkçe"]))

       def hoca_yakalama(self):
           sayi=random.randint(1,2)
           if sayi==1:
               print("Hocaya yakalandık!!")
               self.disiplin_puani-=2
           elif sayi==1:
               print("Yanlış alarm!")
   class Ogretmen:
       def __init__(self,isim,soyisim,sifre=123456):
           self.isim=isim
           self.soyisim=soyisim
           self.sifre=sifre
       def Ogretmen_bilgi(self):
           print("""
            İsim: {}
            Soyisim: {}
           """.format(self.isim,self.soyisim))