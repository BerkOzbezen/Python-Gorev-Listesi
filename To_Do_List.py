import os

GOREVLER_FILE = "To-Do-List.txt"

gorevler = []

def load_gorevler():
    global gorevler
    if os.path.exists(GOREVLER_FILE):
        try:
            with open(GOREVLER_FILE, "r" , encoding="utf-8") as f:
                gorevler = [line.strip() for line in f]

            print(f"[{GOREVLER_FILE}] dosyasindan {len(gorevler)} gorev yuklendi")
        except Exception:
            print("Uyari: Dosya okunurken hata olustu. Yeni liste ile baslaniyor")
            gorevler = []
    else:
        print("Kayit dosyasi bulunamadi , bos gorev listesi ile basliyor")

def save_gorevler():
    try:
         with open(GOREVLER_FILE, "w" , encoding="utf-8") as f:
             for gorev in gorevler:
                 f.write(gorev + "\n")
        
         print(f"Gorevler ({len(gorevler)} gorev) dosyasina kaydedildi ")

    except Exception as  e:
        print(f"Kaydetme hatasi {e}")


def menuyu_goster():
    print("\n--- GOREV YONETİM MENUSU ---")
    print("1: Gorev Ekle")
    print("2: Gorevleri Goster")
    print("3: Gorev Sil (Sira No ile)")
    print("4: Cikis")
    print("----------------------------")

def gorev_ekle():
    gorev_adi = input("Eklenecek gorev adini giriniz : ")
    if gorev_adi:
        gorevler.append(gorev_adi)
        print(f"'{gorev_adi}' listeye eklendi")
    else:
        print("Gorev adi bos birakilamaz")

def gorevleri_goster():
    if not gorevler:
        print("Listenizde henuz gorev bulunmamaktadir")
        return
    print("\n---MEVCUT GOREVLER---")
    for sira_no , gorev in enumerate(gorevler , start=1):
        print(f"{sira_no}. {gorev}")
    print("----------------------------")
    
def gorev_sil():
    if not gorevler:
        print("Listeniz bos oldugu icin silme islemi yapamazsiniz")
        return
    gorevleri_goster()

    try:
        secilen_no = int(input("Silmek istediginiz gorevin sira numarasini giriniz : "))

        silinecek_index = secilen_no - 1

        if 0 <= silinecek_index < len(gorevler):
            silinen_gorev = gorevler.pop(silinecek_index)
            print(f"'{silinen_gorev}' listeden basariyla silindi")

        else:
            print("Gecersiz sira numarasi girdiniz")

    except ValueError:
        print("Hata:Lutfen gecerli bir sayi giriniz")

load_gorevler()
while True:
    menuyu_goster()

    secim = input("Secmek istediginiz islem numarasini giriniz : ")

    if secim == '1':
        gorev_ekle()
    
    elif secim == '2':
        gorevleri_goster()

    elif secim == '3':
        gorev_sil()

    elif secim == '4':
        print("Programdan cikiliyor")
        save_gorevler()
        break

    else:
        print("Gecersiz bir numara girdiniz seciminizi yapmak istediginiz islemin yanindaki numarayi kullanarak yapabilirsiniz")

            

