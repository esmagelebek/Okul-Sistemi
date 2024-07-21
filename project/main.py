import school

Ogrenci1=school.Okul.Ogrenci("Esma","Gelebek",1504,"11-A",100)
Ogretmen=school.Okul.Ogretmen("Ahmet","Siyah",159753)
Okul=school.Okul("Vefa Okulu")
while True:
    print("""
    Sevgili {} sakinleri, Okulumuza hoş geldiniz.
    """.format(Okul.isim))
    islem=input("Öğrenci işlemleri için '1'e basın, Öğretmen işlemleri için '2'ye basın(Çıkmak için '*'a basın): ")
    if islem=="1":
        print("Öğrenci sistemindesiniz!\n")
        islem2=input("Puan görüntülemek için '1'e basın,Öğrenci bilgilerinizi görüntülemek için '2'ye basın :")
        if islem2=="1":
            if Ogrenci1.disiplin_puani==None:
                pass
            else:
               Ogrenci1.puan_goruntule()
        elif islem2=="2":
            Ogrenci1.goruntule()
        else:
            print("Yanlış değer girdiniz . Sistemi meşgul ettiğiniz için görevli öğretmene bilgi verildi!!!")
            Ogrenci1.hoca_yakalama()
    elif islem=="2":
        print("Öğretmen bilgi sistemindesiniz!\n")
        islem3=input("""
        Yapabileceğiniz işlemler,
        Disiplin için '1'e ,
        Ders notu için '2'ye,
        Öğretmen bilgisi için '3'e basın : 
        """)
        if islem3=="1":
            sifre=int(input("Lütfen öğretmen şifrenizi giriniz: "))
            if sifre==Ogretmen.sifre:
                Ogrenci1.disiplin()
            elif sifre !=Ogretmen.sifre:
                print("Yanlış şifre girdiniz ! Hocaya haber verildi!!!")
                Ogrenci1.hoca_yakalama()
        elif islem3=="2":
            sifre = int(input("Lütfen öğretmen şifrenizi giriniz: "))
            if sifre == Ogretmen.sifre:
                if Ogrenci1.disiplin_puani==None:
                    pass
                else:
                   Ogrenci1.puan_degis()
            elif sifre !=Ogretmen.sifre:
                print("Yanlış şifre girdiniz ! Hocaya haber verildi!!!")
                Ogrenci1.hoca_yakalama()
        elif islem3=="3":
            Ogretmen.Ogretmen_bilgi()
    elif islem=="*":
        break

