ad = "Sudenaz Alkan"
sifrem = 2003
bakiye = 3000


def sifre_dogrulama(sifre1, sifre2):
    if sifre1 == sifre2:
        return True
    else:
        return False


def para_cekme(bakiye, miktar):
    if miktar <= bakiye:
        bakiye = bakiye - miktar
    else:
        print("Yetersiz bakiye")
    return bakiye


def para_yatirma(bakiye, miktar):
    bakiye = bakiye + miktar
    return bakiye


sifre = int(input("Lütfen şifrenizi giriniz:  "))
if sifre_dogrulama(sifrem, sifre) == True:
    print("""
  1)Para Cekme
  2)Para Yatirma
  """)
    secim = int(input("Lütfen yapmak istediğiniz işlem numarasını giriniz (1/2):  "))
    miktar = int(input("Lütfen işlem yapmak istediğiniz miktarı giriniz:  "))

    if secim == 1:
        bakiye = para_cekme(bakiye, miktar)
        print("Kalan bakiyeniz: {}".format(bakiye) + "TL")
    elif secim == 2:
        bakiye = para_yatirma(bakiye, miktar)
        print("Bakiyeniz: {}".format(bakiye) + "TL")
    else:
        print("Hatalı tuşlama yaptınız")
else:
    print("Yanlış şifre girdiniz")