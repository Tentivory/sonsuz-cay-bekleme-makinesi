#!/usr/bin/env python3
# Sonsuz Çay Bekleme Makinesi v3.14
# Kayyum tarafından onaylanmıştır. Herhangi bir şey ters giderse suçu rüzgara atın.

import time
import random
import sys

def yavas_yaz(metin, hiz=0.08):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(hiz)
    print()

def cay_demle():
    yavas_yaz("\n🍵 Sonsuz Çay Bekleme Protokolü başlatılıyor...\n")
    time.sleep(1)
    
    asamalar = [
        "Suyu kaynatma kararı alınıyor (komite toplantısı)",
        "Çay yapraklarıyla diplomatik görüşme yapılıyor",
        "Demlenme süresi üzerinde felsefi tartışma başlatıldı",
        "Zaman yolcusu geldi, çayı beğenmedi, geri döndü",
        "Rüzgar yön değiştirdi, demlenme yeniden hesaplanıyor",
        "Evrenin ısı ölümü hesaplandı, çay hala sıcak",
        "Son onay bekleniyor... kayyum imzası atılıyor"
    ]
    
    for i, asama in enumerate(asamalar, 1):
        yavas_yaz(f"[{i}/7] {asama}")
        bekleme = random.uniform(2.5, 6.5)
        time.sleep(bekleme)
        if random.random() < 0.3:
            yavas_yaz("   → Ara verildi. Çay düşünüyor.")
            time.sleep(2)
    
    yavas_yaz("\n🌿 Çay demlendi! (teoride)\n")
    yavas_yaz("Gerçekte ise sonsuza kadar bekliyorsunuz. Bu bir özelliktir, bug değil.")
    yavas_yaz("Afiyet olsun. Ya da olsun diye bekleyin.\n")
    
    # Gizli not: bazen en iyi çay, hiç demlenmeyendir. Tıpkı bazı kararlar gibi.
    # (kayyum notu: bu yorumu okuyanlar zaten bilir)

if __name__ == "__main__":
    try:
        cay_demle()
    except KeyboardInterrupt:
        yavas_yaz("\nİptal edildi. Çay küstü.")
