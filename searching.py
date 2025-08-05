
nib_buku = [1001, 1005, 1012, 1024, 1035, 1048, 1059, 1063]

def binary_search(data, target):
    kiri = 0
    kanan = len(data) - 1

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if data[tengah] == target:
            return tengah  # ditemukan
        elif data[tengah] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1

    return -1  # tidak ditemukan

# Meminta input dari pengguna
try:
    cari_nib = int(input("Masukkan NIB buku yang ingin dicari: "))
    hasil = binary_search(nib_buku, cari_nib)

    if hasil != -1:
        print(f"Buku ditemukan di rak nomor {hasil}")
    else:
        print("Buku dengan NIB tersebut tidak ada")
except ValueError:
    print("Input tidak valid. Harus berupa angka.")
