def tambah_nilai(data, nilai):
    data.append(nilai)
    print(f"Nilai {nilai} berhasil ditambahkan!")

def tampilkan_nilai(data):
    if not data:
        print("Data nilai masih kosong.")
    else:
        print("Daftar Nilai:", data)

def sorting(data):
    # Urutkan dari besar ke kecil
    data.sort(reverse=True)
    print("Data berhasil diurutkan (descending).")

def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i  # kembalikan index
    return -1

def binary_search(data, target):
    kiri, kanan = 0, len(data) - 1
    while kiri <= kanan:
        mid = (kiri + kanan) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:  # karena urut descending
            kanan = mid - 1
        else:
            kiri = mid + 1
    return -1

# Program utama
nilai_siswa = []

while True:
    print("\n=== Sistem Manajemen Nilai Siswa ===")
    print("1. Tambah Nilai")
    print("2. Tampilkan Nilai")
    print("3. Urutkan Nilai (Descending)")
    print("4. Cari Nilai (Linear Search)")
    print("5. Cari Nilai (Binary Search)")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        n = int(input("Masukkan nilai: "))
        tambah_nilai(nilai_siswa, n)

    elif pilihan == "2":
        tampilkan_nilai(nilai_siswa)

    elif pilihan == "3":
        sorting(nilai_siswa)

    elif pilihan == "4":
        cari = int(input("Masukkan nilai yang dicari: "))
        hasil = linear_search(nilai_siswa, cari)
        if hasil != -1:
            print(f"Nilai {cari} ditemukan pada index {hasil}")
        else:
            print("Nilai tidak ditemukan.")

    elif pilihan == "5":
        if not nilai_siswa:
            print("Data masih kosong. Silakan tambah dan urutkan dulu!")
        else:
            cari = int(input("Masukkan nilai yang dicari: "))
            hasil = binary_search(nilai_siswa, cari)
            if hasil != -1:
                print(f"Nilai {cari} ditemukan pada index {hasil}")
            else:
                print("Nilai tidak ditemukan.")

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")
