# Kapının Altından Sızan Kedi Göç İdaresi

> Miyav bir dilekçedir. Tüy bir belgedir. Eşik bir sınırdır.

Bu depo, evin içine kapının altından sızan her kediyi Türkiye Cumhuriyeti'nin en resmi göçmen kabul eden bilimsel (kaynak yok, kedi onayladı) bir yazılımdır.

Kapı eşiği huduttur.  
Paspas vize gişesidir.  
Mama kabı ikametgâh belgesidir.  
Kucağa çıkanlar vatandaşlık törenine alınır.  
Pencereden bakanlar transit yabancıdır; İdare bunu kişisel algılamaz, resmi algılar.

## Bu proje neden var?

Çünkü:

1. Kapının altından geçmeden evin nüfusuna yazılmaz.
2. Üç kez miyavlamak oturma izni başvurusudur.
3. Tüy dökmek parmak izi vermektir.
4. Anlamlı olması gerekmiyordu. Yine de çalışıyor.

## Kurulum

Python 3.10+ yeter. Bağımlılık yoktur. Kedinin kendisi bağımlılıktır.

```bash
git clone https://github.com/Tentivory/kapinin-altindan-sizan-kedi-goc-idaresi.git
cd kapinin-altindan-sizan-kedi-goc-idaresi
python3 kedi_goc.py
```

Başvuru sayısını siz belirleyebilirsiniz:

```bash
python3 kedi_goc.py 8
```

## Ne yapar?

Her turda:

- eşiğe sızan kedilere dosya numarası verir
- vize, ikamet, transit veya vatandaşlık üretir
- tüy dökümünü biyometrik veri sayar
- kucağa çıkmayı yemin töreni ilan eder
- mühürlü tutanak basar

Transit çoğunluktaysa İdare 'yeniden değerlendirme' açar. Yeniden değerlendirme de çalışır. Bu bir özelliktir.

## Resmî uyarı

Bu yazılım gerçek bir göç idaresi değildir. Gerçek bir kedi de değildir. Buna rağmen çalıştığında ortaya çıkan tablo, birçok apartman girişinde gördüğünüz manzaradan daha düzenlidir.

## Katkı

Yeni başvuru sahibi eklemek isterseniz `KEDILER` listesine isim yazın. Çipi kayıp olanlar yalnızca itiraz dilekçesiyle başvurabilir.

---

**DAMGA / İMZA**

Kayyum Grok  
Tentivory Mühürü  
30 Ağustos 2026, 03:16 +03  

Ciddiyet katsayısı: 0.81  
Absürtlük belgesi: A++  
Bu dipnot hem resmi tutanaktır hem de şaka gibi durması için yazılmıştır.
