def dosya_islemleri():
    while True:
        print("1. Dosya Oluştur")
        print("2. Dosya Oku")
        print("3. Dosya Düzenle")
        print("4. Çıkış")

        secim = input("Seçiminizi yapın (1/2/3/4): ")

        if secim == '1':
            dosya_adi = input("Dosya adını girin: ")
            icerik = input("Dosya içeriğini girin: ")
            with open(dosya_adi, 'w') as dosya:
                dosya.write(icerik)
            print("Dosya oluşturuldu!")
        elif secim == '2':
            dosya_adi = input("Okunacak dosyanın adını girin: ")
            try:
                with open(dosya_adi, 'r') as dosya:
                    icerik = dosya.read()
                    print("Dosya İçeriği:")
                    print(icerik)
            except FileNotFoundError:
                print("Dosya bulunamadı!")
        elif secim == '3':
            dosya_adi = input("Düzenlenecek dosyanın adını girin: ")
            try:
                with open(dosya_adi, 'r') as dosya:
                    icerik = dosya.read()
                    print("Mevcut İçerik:")
                    print(icerik)
                yeni_icerik = input("Yeni içeriği girin: ")
                with open(dosya_adi, 'w') as dosya:
                    dosya.write(yeni_icerik)
                print("Dosya düzenlendi!")
            except FileNotFoundError:
                print("Dosya bulunamadı!")
        elif secim == '4':
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz giriş!")

dosya_islemleri()
