class Malzeme:
    def __init__(self, ad, stok_miktarı, son_bakım_tarihi):
        # Malzeme özelliklerini tanımlayan constructor
        self.ad = ad  # Malzeme adı
        self.stok_miktarı = stok_miktarı  # Malzeme stok miktarı
        self.son_bakım_tarihi = son_bakım_tarihi  # Malzeme son bakım tarihi

    def stok_kontrol(self):
        # Stok miktarını kontrol eder ve duruma göre uyarı verir.
        if self.stok_miktarı <= 0:
            print(f"{self.ad} malzemesinin stok miktarı tükenmiştir. Yeniden sipariş verilmelidir.")
        elif self.stok_miktarı < 10:
            print(f"{self.ad} malzemesinin stok miktarı azalmıştır. Yeniden sipariş verilmesi gerekebilir.")
        else:
            print(f"{self.ad} malzemesinin stok miktarı normal seviyededir.")

    def bakım_kontrol(self):
        # Son bakım tarihini kontrol eder ve gerekirse bakım uyarısı verir.
        if self.son_bakım_tarihi < "2023-01-01":
            print(f"{self.ad} malzemesinin son bakım tarihi geçmiştir. Bakım yapılmalıdır.")
        else:
            print(f"{self.ad} malzemesinin bakımı güncel.")

def main():
    malzeme_listesi = []
#Malzeme bilgisi ekleme ve kodun devam edip etmediğini anlayan şart ifadesi vardır.
    while True:
        print("\nMalzeme Bilgisi Ekle")
        ad = input("Malzeme Adı: ")
        stok_miktarı = int(input("Stok Miktarı: "))
        son_bakım_tarihi = input("Son Bakım Tarihi (YYYY-MM-DD): ")

        malzeme = Malzeme(ad, stok_miktarı, son_bakım_tarihi)
        malzeme_listesi.append(malzeme)

        devam_et = input("Başka malzeme eklemek ister misiniz? (E/H): ")
        if devam_et.lower() != "e":
            break

    print("\nMalzeme Bilgileri ve Kontrolleri")
    for malzeme in malzeme_listesi:
        print(f"Malzeme Adı: {malzeme.ad}")
        malzeme.stok_kontrol()
        malzeme.bakım_kontrol()
#Kodu çalıştırır.
if __name__ == "__main__":
    main()
