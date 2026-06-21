from collections import deque

# LIST - Daftar Menu
daftar_menu = ["Kopi", "Teh", "Jus Alpukat", "Pisang Bakar", "Nasi Goreng"]

# QUEUE - Antrian Pesanan
queue_pesanan = deque()

# STACK - Riwayat Pesanan
stack_riwayat = []

while True:
    print("\n=== MENU WARUNG ===")
    print("1. Tambah Pesanan")
    print("2. Proses Pesanan")
    print("3. Lihat Antrian")
    print("4. Lihat Riwayat")
    print("5. Keluar")

    pilih = input("\nPilih menu : ")

    # TAMBAH PESANAN (QUEUE)
    if pilih == "1":
        print("\n=== TAMBAH PESANAN ===")
        nama = input("Nama Pelanggan : ")

        print("\nDaftar Menu:")
        for i, menu in enumerate(daftar_menu, 1):
            print(f"{i}. {menu}")

        print("\nPilih menu (bisa lebih dari 1, pisahkan dengan koma)")

        try:
            input_menu = input("Pilih nomor menu : ")
            pilihan = [int(x.strip()) for x in input_menu.split(",")]

            pesanan_list = []

            for p in pilihan:
                if 1 <= p <= len(daftar_menu):
                    pesanan_list.append(daftar_menu[p - 1])

            if pesanan_list:
                queue_pesanan.append({
                    "nama": nama,
                    "pesanan": pesanan_list
                })

                print(f"\nPesanan {nama} masuk antrian!")
            else:
                print("Tidak ada menu valid!")

        except:
            print("Input harus angka, pisahkan dengan koma!")

    # PROSES PESANAN (QUEUE -> STACK)
    elif pilih == "2":
        if queue_pesanan:
            data = queue_pesanan.popleft()
            stack_riwayat.append(data)

            print("\n=== DIPROSES ===")
            print(f"Nama     : {data['nama']}")
            print(f"Pesanan  : {', '.join(data['pesanan'])}")
        else:
            print("Antrian kosong!")

    # LIHAT ANTRIAN (QUEUE)
    elif pilih == "3":
        print("\n=== ANTRIAN PESANAN ===")

        if not queue_pesanan:
            print("Antrian kosong!")
        else:
            for i, data in enumerate(queue_pesanan, 1):
                print(f"{i}. {data['nama']} - {', '.join(data['pesanan'])}")

    # LIHAT RIWAYAT (STACK)
    elif pilih == "4":
        print("\n=== RIWAYAT PESANAN ===")

        if not stack_riwayat:
            print("Belum ada pesanan diproses!")
        else:
            for i, data in enumerate(reversed(stack_riwayat), 1):
                print(f"{i}. {data['nama']} - {', '.join(data['pesanan'])}")

    elif pilih == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")