# Mesai İK

Kurgusal **Poyraz Yazılım A.Ş.** için hazırlanmış, tamamen dummy data ile çalışan İK / personel yönetim paneli demosu.

Tek bir `index.html` dosyasından oluşur — framework yok, build adımı yok. Dosyayı tarayıcıda açmanız yeterli.

## Modüller

| Modül | İçerik |
|---|---|
| **Genel Bakış** | Günlük yoklama KPI'ları, son 10 iş günü yoklama grafiği, duyurular, aktivite akışı, doğum günleri |
| **Çalışanlar** | 28 çalışan; arama + departman filtresi, sekmeli profil kartı (Profil / Devam / Zimmet / Bordro) |
| **Giriş – Çıkış (PDKS)** | Günlük giriş-çıkış saatleri, fazla mesai, filtreler, CSV kopyalama |
| **İzinler** | Talep onay akışı, yıllık izin bakiyeleri, 2026 resmi tatil takvimi |
| **Zimmet** | 75 demirbaş: laptop, telefon, monitör, aksesuar; seri no ve durum takibi |
| **Performans** | 2026 H1 skorları, hedef tamamlama, departman ortalamaları |
| **Bordro** | Brüt → net hesap (SGK, işsizlik, gelir + damga vergisi), bordro pusulası, işveren maliyeti |
| **Sodexo** | Aylık yemek kartı yüklemeleri (her ayın 5'i), 6 aylık trend grafiği |
| **Masraflar** | Harcama talepleri ve onay süreci |

## Teknik notlar

- Tüm veriler seed'li (deterministik) üretilir — sayfa her yenilendiğinde aynı tutarlı veri gelir.
- Açık/koyu tema otomatik (`prefers-color-scheme`), mobil uyumlu.
- Grafikler el yazımı SVG; harici kütüphane yok.

> ⚠️ Tüm kişiler, tutarlar ve kayıtlar örnektir. Poyraz Yazılım A.Ş. kurgusal bir şirkettir.
