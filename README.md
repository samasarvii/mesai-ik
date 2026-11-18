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

## Proje fikirleri

### ☁️ Ajanları bulutta çalıştırmak

> Kaynak: [@pikacodes Instagram reel'i](https://www.instagram.com/reel/Df3RRxyPQiR/) (17 Kasım 2026) — *"Close your laptop and protect your aura: start running your agents on the cloud"*. Videoda Codex ile anlatılıyor; aynı yaklaşım Claude Code'un bulut oturumlarıyla da uygulanabilir.

**Fikir:** Mesai İK'nın geliştirmesini yerel bilgisayara bağlı olmadan, bulutta çalışan kodlama ajanlarına devretmek. Laptop kapalıyken de iş ilerler.

Olası kullanımlar:

- **Issue → PR akışı:** GitHub'a açılan bir issue'yu (ör. "Masraflar modülüne fiş görseli ekle") bulut ajanına verip PR olarak geri almak.
- **Paralel modül geliştirme:** Her modül (Bordro, İzinler, Zimmet…) için ayrı bir bulut oturumu açıp aynı anda ilerletmek.
- **Zamanlanmış görevler:** Haftalık olarak bağımlılık/erişilebilirlik kontrolü, 2027 resmi tatil takvimi ve bordro parametrelerinin (asgari ücret, vergi dilimleri) güncellenmesi.
- **PR takibi:** Ajanın PR'daki yorumları ve GitHub Pages kontrollerini izleyip düzeltmeleri kendisinin göndermesi.

**Dikkat edilecekler:** Ajanlar yalnızca kendi dallarında çalışmalı; birleştirme (merge) kararı insanda kalmalı. Proje dummy veriyle çalıştığı için gerçek kişisel veri riski yok, ama ileride gerçek İK verisi eklenirse bulut ortamına sır/veri verilmemeli.
