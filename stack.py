# LIST - Daftar Menu
daftar_menu = ["Kopi", "Teh", "Jus Alpukat", "Pisang Bakar", "Nasi Goreng"]

# STACK - History Pesanan
stack_pesanan = []

while True:
    print("\n=== MENU WARUNG ===")
    for i, menu in enumerate(daftar_menu, 1):
        print(f"{i}. {menu}")
    
    print("\n1. Tambah Pesanan")
    print("2. Batalkan Pesanan Terakhir")
    print("3. Lihat Pesanan")
    print("4. Keluar")
    
    pilih = input("\nPilih menu : ")
    
    if pilih == "1":
        pesan = input("Masukkan pesanan (pisah dengan koma) : ")
        daftar_pesan = [p.strip() for p in pesan.split(",")]
        for p in daftar_pesan:
            stack_pesanan.append(p)
        print(f"Pesanan {daftar_pesan} ditambahkan!")
    
    elif pilih == "2":
        if stack_pesanan:
            batal = stack_pesanan.pop()
            print(f"{batal} dibatalkan!")
        else:
            print("Tidak ada pesanan!")
    
    elif pilih == "3":
        print("Pesanan saat ini:", stack_pesanan)
    
    elif pilih == "4":
        break