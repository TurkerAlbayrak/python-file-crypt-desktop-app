# SecureCrypt

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Cryptography](https://img.shields.io/badge/Cryptography-Fernet-red.svg)](https://cryptography.io/)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()

Modern ve güvenli dosya şifreleme uygulaması. SecureCrypt, kullanıcıların herhangi bir dosyayı parolayla şifreleyerek başkalarıyla güvenli bir şekilde paylaşmasını sağlar.

> **Önemli:** Parolasını hatırla - kaybolursa dosyaya erişilemez!

---

## Özellikler

- **AES-Fernet Şifreleme** - Endüstri standardı simetrik şifreleme
- **Parola Koruması** - PBKDF2-HMAC SHA256 ile güçlü parola türetimi
- **Kullanıcı Dostu Arayüz** - Tkinter tabanlı modern GUI
- **Herhangi Dosya Türü** - Resimler, belgeler, videolar vb. tüm formatlar
- **Hafif & Hızlı** - Tek dosyalı, hiç bağımlılık eksikliği
- **Güvenli Parola Yönetimi** - Parolalar hiçbir zaman saklanmaz
- **İşlemli Çıktı** - `.crypt` dosya formatı
- **Dosya Adı Kurtarma** - Şifrelenmiş dosyanın orijinal adı korunur
- **Kolay Paylaşım** - Şifrelenmiş dosyaları e-posta veya internet üzerinden paylaş

---

## Hızlı Başlangıç

### Gereksinimler

- Python 3.8 veya üstü
- pip (Python paket yöneticisi)

### Kurulum

```bash
# 1. Projeyi klonla
git clone https://github.com/TurkerAlbayrak/python-file-crypt-desktop-app.git
cd python-file-crypt-desktop-app

# 2. Bağımlılıkları kur
pip install -r requirements.txt

# 3. Uygulamayı çalıştır
python main.py
```

Veya direkt olarak:

```bash
pip install cryptography
python main.py
```

---

## Kullanım Kılavuzu

### Dosya Şifreleme

1. **Uygulama Aç** - `main.py` dosyasını çalıştır
2. **"Şifrele" Sekmesine Git** - Şifreleme işlemini seç
3. **Dosya Seç** - Şifrelemek istediğin dosyayı seç
4. **Parola Belirle** - Güçlü bir parola gir (en az 8 karakter önerilir)
5. **Şifrele Butonuna Bas** - Şifreleme işlemi başlar
6. **Tamamlandı!** - `dosya_adı.crypt` dosyası oluşturulur

### Dosya Şifresi Çöz

1. **Uygulama Aç** - `main.py` dosyasını çalıştır
2. **"Şifresi Çöz" Sekmesine Git** - Şifre çözme işlemini seç
3. **`.crypt` Dosyasını Seç** - Şifrelenmiş dosyayı seç
4. **Parolayı Gir** - Şifreleme sırasında kullanılan parolayı gir
5. **Şifresi Çöz Butonuna Bas** - Şifre çözme işlemi başlar
6. **Tamamlandı!** - Orijinal dosya yeniden oluşturulur

---

## Güvenlik Detayları

### Kullanılan Teknolojiler

```
┌─────────────────────────────────────┐
│      Parola (Kullanıcı Girişi)      │
└────────────────┬────────────────────┘
                 │
                 ▼
    ┌──────────────────────────┐
    │  PBKDF2-HMAC-SHA256      │
    │  (100.000+ iterasyon)    │
    └────────┬─────────────────┘
             │
             ▼
    ┌──────────────────────────┐
    │  Şifreleme Anahtarı      │
    └────────┬─────────────────┘
             │
             ▼
    ┌──────────────────────────┐
    │   Fernet Simetrik        │
    │   Şifreleme (AES-128)    │
    └────────┬─────────────────┘
             │
             ▼
    ┌──────────────────────────┐
    │  Şifrelenmiş Dosya       │
    │  (*.crypt)               │
    └──────────────────────────┘
```

### Güvenlik Özellikleri

| Özellik | Açıklama |
|---------|----------|
| **Şifreleme Algoritması** | Fernet (AES-128-CBC + HMAC-SHA256) |
| **Anahtar Türetimi** | PBKDF2-HMAC-SHA256 (100.000+ iterasyon) |
| **Rastgele Tuz** | Her dosya için benzersiz tuz oluşturulur |
| **Kimlik Doğrulama** | HMAC ile veri bütünlüğü kontrolü |
| **Parola Depolama** | Parolalar hiçbir zaman disk'te saklanmaz |
| **Yanlış Parola Koruması** | Hatalı parola ile çözülen dosya bozuk çıkar |

### Dosya Yapısı

Şifrelenmiş `.crypt` dosyası aşağıdaki bileşenleri içerir:

```
[Tuz - 16 byte] [IV - 16 byte] [Şifrelenmiş Veri] [MAC Tag - 16 byte] [Dosya Adı]
```

---

## Proje Yapısı

```
python-file-crypt-desktop-app/
├── main.py              # Uygulamanın ana dosyası
├── README.md           # Bu dosya

```

### main.py Modülleri

- **GUI Interface** - Tkinter kullanıcı arayüzü
- **Encryption Engine** - Fernet tabanlı şifreleme
- **Key Derivation** - PBKDF2 parola türetimi
- **File Handler** - Dosya okuma/yazma operasyonları

---

### Desteklenen İşletim Sistemleri

- ✅ Windows (7, 10, 11)
- ✅ macOS (10.12+)
- ✅ Linux (Ubuntu, Fedora, Debian vb.)

---

## Performans

Tipik dosya şifreleme sürelerine göre performans:

| Dosya Boyutu | Şifreleme Süresi | Şifre Çözme Süresi |
|--------------|------------------|-------------------|
| 1 MB | ~0.1 saniye | ~0.1 saniye |
| 10 MB | ~1 saniye | ~1 saniye |
| 100 MB | ~10 saniye | ~10 saniye |
| 1 GB | ~100 saniye | ~100 saniye |

*Not: Süreler bilgisayar performansına göre değişiklik gösterebilir.*

---

## Bir Örnek Senaryo

### Senaryodaki Akış

```
Alice'in işi: secret_report.pdf

1️⃣ Alice, secret_report.pdf dosyasını SecureCrypt ile şifreler
   → Parola: MyStr0ng!Pass
   → Oluşturulan dosya: secret_report.pdf.crypt

2️⃣ Alice, secret_report.pdf.crypt dosyasını Bob'a e-posta ile gönderir
   → Dosya boyutu küçüktür ve güvenlidir

3️⃣ Bob, dosyayı alır ve SecureCrypt'e açar
   → Aynı parolayı (secure channel üzerinden Alice'ten alıp) girer
   → secret_report.pdf orijinal dosya kurtarılır

4️⃣ Bob, orijinal dosyayı kullanabilir
   → Veriler güvenli bir şekilde aktarılmıştır
```

---

## Geliştirme & Katkı

### Geliştirme Ortamı Kurma

```bash
# Virtual environment oluştur (opsiyonel ama önerilir)
python -m venv venv

# Virtual environment'i etkinleştir
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Bağımlılıkları kur
pip install -r requirements.txt

# Uygulamayı çalıştır
python main.py
```

### Kod Stanartları

- PEP 8 style guide'ı takip et
- Fonksiyonlara docstring ekle
- Değişken adlarını açık ve anlaşılır tut

### Katkı Adımları

1. Bu repository'yi fork et
2. Feature branch oluştur (`git checkout -b feature/AmazingFeature`)
3. Değişiklikleri commit et (`git commit -m 'Add some AmazingFeature'`)
4. Branch'i push et (`git push origin feature/AmazingFeature`)
5. Pull Request aç

---

## Bilinen Sorunlar ve Çözümleri

### Sorun: "ModuleNotFoundError: No module named 'cryptography'"
**Çözüm:** `pip install cryptography` komutunu çalıştır

### Sorun: Tkinter bulunamıyor
**Çözüm:**
- **Ubuntu/Debian:** `sudo apt-get install python3-tk`
- **Fedora:** `sudo dnf install python3-tkinter`
- **macOS:** Zaten yüklü olması gerekir

### Sorun: Yanlış parola ile şifre çözerken boş dosya oluşturuluyor
**Bu beklenen davranıştır!** Güvenlik nedeniyle, yanlış parola dosyaları çözemez.

---

## Güvenlik Tavsiyeleri

### Parolaları Seçerken

✅ **Yapılması Gerekenler:**
- Minimum 12 karakter kullan
- Büyük harf, küçük harf, rakam ve sembol karışımı
- Rasgele parolalar tercih et
- Güvenli bir parola yöneticisinde sakla

❌ **Yapılmaması Gerekenler:**
- Doğum tarihi, ad veya kolay tahmin edilebilir kombinasyonlar
- Aynı parolayı birden fazla yerde kullanma
- Parolaları dosya adında veya açıklama olarak yazma
- Parolaları düz metin dosyasında saklama

### Dosya Paylaşırken

1. **Parola Aktarımı** - Dosya ve parolayı ayrı kanallardan gönder
2. **Doğrulama** - Alıcının dosyayı başarıyla açtığını kontrol et
3. **Silme** - Artık ihtiyaç duyulmayan şifrelenmiş dosyaları sil
4. **Yedekleme** - Orijinal dosyasının yedeğini güvenli bir yerde tut

---

```

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## Geliştirici

**Turker Albayrak**
- GitHub: [@TurkerAlbayrak](https://github.com/TurkerAlbayrak)

---

## Destek ve Geribildirim

Sorularım, hata buldum veya öneriniz mi var?

- **GitHub Issues** - Hata raporları ve özellik istekleri
- **Discussions** - Genel sorular ve tartışmalar
- **Pull Requests** - Kod katkıları

---



## ⭐ Eğer Projemi Beğendiysen

Bu projeyi faydalı bulduysanız lütfen bir ⭐ star vererek destekleyin!


```



**Made with ❤️ by Turker Albayrak**

*Son güncelleme: 2024*
