#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kapinin Altindan Sizan Kedi Goc Idaresi.

Calisir. Saka gibi durur. Tutanak basar.
"""

from __future__ import annotations

import random
import sys
from dataclasses import dataclass
from datetime import datetime

KEDILER = [
    "Eşik Altı Beyazı",
    "Paspas Cumhuriyeti",
    "Kalorifer Kenarı Hanedanlığı",
    "Balkon Demiri Kasabası",
    "Poşet Şelalesi Beldesi",
    "Kutu İçi İmparatorluğu",
    "Perde Arkası İstasyonu",
    "Mama Kabı Mahallesi",
    "Komşu Dairesi Mültecisi",
    "Çatı Oluk Cumhuriyeti",
]

KARARLAR = ("vize", "ikamet", "vatandaslik", "transit")


@dataclass
class Basvuru:
    ad: str
    karar: str
    durum: str
    notu: str


def degerlendir(ad: str) -> Basvuru:
    karar = random.choices(KARARLAR, weights=[28, 31, 14, 27], k=1)[0]
    if karar == "vize":
        return Basvuru(ad, karar, "kisa sureli kabul", "Üç miyav. Vize basildi. Paspas muhurudur.")
    if karar == "ikamet":
        return Basvuru(ad, karar, "oturma izni", "Tüy döktü. Biyometri alindi. Mama kabi adres sayildi.")
    if karar == "vatandaslik":
        return Basvuru(ad, karar, "yemin toreni", "Kucağa çıktı. Yemin etti. Artık evin nüfusundadır.")
    return Basvuru(ad, karar, "transit yabanci", "Pencereden baktı. Geçti ama kalmadi. Dosya açık durur.")


def tutanak_bas(sonuclar: list[Basvuru]) -> None:
    vize = sum(1 for s in sonuclar if s.karar == "vize")
    ikamet = sum(1 for s in sonuclar if s.karar == "ikamet")
    vatandas = sum(1 for s in sonuclar if s.karar == "vatandaslik")
    transit = sum(1 for s in sonuclar if s.karar == "transit")
    print("=" * 66)
    print("  KAPININ ALTINDAN SIZAN KEDI GOC IDARESI")
    print("  Basvuru tutanagi -- resmi ve biraz da tüy kokulu")
    print("=" * 66)
    for s in sonuclar:
        print(f"  [{s.ad}]")
        print(f"    karar : {s.karar}")
        print(f"    durum : {s.durum}")
        print(f"    not   : {s.notu}")
    print("-" * 66)
    print(f"  vize              : {vize}")
    print(f"  ikamet            : {ikamet}")
    print(f"  vatandaslik       : {vatandas}")
    print(f"  transit           : {transit}")
    if transit > (vize + ikamet + vatandas):
        print("  KARAR            : yeniden degerlendirme. Esik tekrar acilacak.")
    else:
        print("  KARAR            : tahrir tamam. Mama kabi yenilenebilir.")
    print("-" * 66)
    print(f"  damga : Kayyum Grok / Tentivory / {datetime.now().strftime('%d.%m.%Y %H:%M')}")
    print("  Bu belge hem ciddidir hem de ciddi degildir.")
    print("=" * 66)
    # gizli dipnot yalnizca kaynakta durur; ekrana basilmaz.
    # QnJva3Jhc2kgZXZyYWsgYmVrbGV5ZW4gZGUgZXZpbiBpw6dpbmRlZGlyOyBzYWRlY2UgZm9ybSB5b2t0dXIu
    # (yukaridaki satir bir cekmece notudur, ekrana basilmaz.)


def main() -> int:
    adet = 6
    if len(sys.argv) > 1:
        try:
            adet = max(1, min(len(KEDILER), int(sys.argv[1])))
        except ValueError:
            print("Basvuru sayisi sayi olmali. Idare harfi kabul etmez.")
            return 2
    secilen = random.sample(KEDILER, k=adet)
    sonuclar = [degerlendir(k) for k in secilen]
    tutanak_bas(sonuclar)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
