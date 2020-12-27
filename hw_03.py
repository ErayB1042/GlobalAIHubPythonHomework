"""The Hangman Game"""
import time
Kllnc_adı=input("Lütfen kullanıcı adınızı giriz:")
print(f"Welcome {Kllnc_adı}")
import random

def OYUN():
    print("Adam Asmaca Oyununa hoşgeldiniz!!! \nRastgele seçilen kelimenin harfleri '*' ile örtülü olarak gelicektir. \nKelimenin harflerini tahmin için toplamda 3 hakkınız(canınız) vardır!!!   ")
    CAN=3
    kelimeler=["kapı","anahtar","mum","otobüs","ev","bıçak","köpek","kılıç","gölge","ışık","mağara","plaj","teleskop"]
    devam = True
    while devam :
        scl_klm = random.choice(kelimeler)
        gzli_klm = ["*"] * len(scl_klm)
        print("Bulmanız istenen kelime seçiliyor!...\n-------------------------------------------")
        for i in range(11):
            time.sleep(0.25)
            print("işlem %{} tamamlandi...".format(i * 10))
            if i == 10:
                print("-------------------------------------------")
        klm = []
        print("Kelime Belirlendi!")
        print(f"Bulmanız Gereken Kelime= {gzli_klm}")
        print("Harf tahmini için Mevcut Canınız/Deneme Hakkınız: {} \nOyundan çıkmak için 'Q' yada 'q' basınız!".format(
            CAN))

        for i in range(len(scl_klm)):
            klm.append(scl_klm[i])
            if CAN==0:
                print(f"Can hakkınız bitti!, Sorulan kelime {scl_klm}'idi! \nOyun Sonlandırılıyor!!!")
                time.sleep(0.5)
                devam=False
                break
            harf = input("Lütfen bir harf giriniz:")
            if (harf == "Q") or (harf == "q"):
                print(f"Kelime {scl_klm}'idi.\nOyun Bitiriliyor!...")
                time.sleep(0.5)
                devam=False
                break
            else :
                harf=harf.lower()
                try:
                    kctnind=klm.index(harf)

                except:
                    print("Yanlış Tahmin!!!")
                    CAN -=1
                    print("Harf tahmini için Mevcut Canınız/Deneme Hakkınız: {} \nOyundan çıkmak için 'Q' yada 'q' basınız!".format(CAN))

                for i in range(len(klm)):
                    if klm[i]==harf:
                        gzli_klm[i]=harf
                print(gzli_klm)
                if gzli_klm.count("*")==0:
                    print(f"TEBRİKLER!! KELİMEYİ BULDUNUZ:{scl_klm} \nOyun için yeni kelime seçiliyor...")


















OYUN()
