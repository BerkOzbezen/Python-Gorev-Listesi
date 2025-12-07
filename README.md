# 📋 Python Görev Listesi (To-Do List) Uygulaması

Bu uygulama, Python'ın temel fonksiyonlarını, listelerini ve kalıcı dosya işlemlerini (`os` modülü) kullanarak geliştirilmiş, komut satırı (terminal) tabanlı basit bir görev yönetim programıdır.

---

## ✨ Temel Özellikler (Features)

Uygulama, veri kaybetme riskini en aza indirerek aşağıdaki işlemleri gerçekleştirir:

* **💾 Kalıcı Kayıt:** Uygulama çıkışında liste içeriğini otomatik olarak `To-Do-List.txt` dosyasına kaydeder.
* **↩️ Kayıtlı Veri Yükleme:** Uygulama açılışında, varsa kayıtlı görev listesini dosyadan yükler.
* **➕ Görev Ekleme:** Kullanıcıdan yeni görev alır ve listeye ekler.
* **🔢 Numaralı Görüntüleme:** Görevleri **1'den başlayan numaralandırma** ile listeler.
* **❌ Güvenli Silme:** Görevleri ad yerine **sıra numarasıyla** seçerek listeden hatasız bir şekilde siler.

---

## 🚀 Nasıl Başlatılır?

Uygulamayı çalıştırmak için sadece Python 3'e ihtiyacınız var.

### 1. Kurulum ve Çalıştırma

1.  Projenin ana klasörüne terminalde gidin.
2.  Uygulamayı başlatmak için terminal penceresinde aşağıdaki komutu çalıştırın:
    ```bash
    python To_Do_List.py
    ```
    

### 2. Kritik Not

* Programın oluşturduğu kayıt dosyası **`To-Do-List.txt`** adındadır.
* Listenin kaybolmaması için, uygulamadan çıkarken **4. Çıkış** seçeneğini kullanın.

---

## 💻 Kullanılan Teknolojiler

* **Dil:** Python 3.x
* **Temel Yapılar:** Listeler, Fonksiyonlar, `if/elif/else`, `while True` döngüsü.
* **Modüller:** `os` (Dosya sistemini yönetmek için).

---

## ⚖️ Lisans

Bu proje, açık kaynaklı kodlama pratiği amacıyla oluşturulmuştur. Lisans bilgileri deponun kök dizininde yer almaktadır.