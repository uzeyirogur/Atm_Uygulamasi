print(""" ******************************* 

ATM MAKİNESİNE HOŞ GELDİNİZ.

İŞLEMLER ;

1. BAKİYE SORGULAMA

2. PARA YATIRMA

3. PARA ÇEKME


""")

bakiye = 1000

while True :

    işlem = input("Yapıcağınız işlemi giriniz: ")


    if (işlem == "1") :
        print("Bakiyeniz: {} ".format(bakiye))

    elif (işlem == "2") :
        yatırma = int(input("Yatırmak istediğiniz tutarı giriniz: "))
        bakiye += yatırma
        print("Paranız başarıyla yatırıldı...")
        print("Yatırılan miktar : {} ".format(yatırma))
        print("Yeni bakiye {} ".format(bakiye))

        seçim = input("Devam etmek istiyorsanız (y)\nÇıkmak istiyorsanız(n) Basınız: ")

        if (seçim == "y") :
            continue
        elif (seçim == "n" or seçim == "q") :
            print("Lütfen kartınızı alınız. ")
            break
        else :
            print("Yanlış karakter tekrar deneyiniz...")

    elif (işlem == "3") :
        çekim = int(input("Çekmek istediğiniz tutarı giriniz: "))
        bakiye -= çekim
        print("Paranız başarıyla çekildi...")
        print("Çekilen miktar : {} ".format(çekim))
        print("Kalan bakiye : {} ".format(bakiye))

    seçim = input("Devam etmek istiyorsanız (y)\nÇıkmak istiyorsanız(n) Basınız: ")

    if (seçim == "y") :
        continue

    elif (seçim == "n" or seçim == "q") :
        print("Lütfen kartınızı alınız. ")
        break

    else :
        print("Yanlış karakter tekrar deneyiniz...")


else :
        print("Yanlış bir şey girdiniz tekrar deneyiniz. ")
