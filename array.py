# Membuat nama produk
nama_produk = ["Pensil", "Pulpen", "Penggaris", "Penghapus", "Tipex"]

# Menampilkan daftar di layar
i = 1
for nama in nama_produk:
    print(f"{i}. {nama}")
    i += 1

# Meminta pengguna memasukkan nomor urut produk
try:
    nomor = int(input("Masukkan nomor produk yang ingin dilihat (1-5): "))
# Menampilkan output
    if 1 <= nomor <= 5:
        print(f"Produk nomor {nomor} adalah: {nama_produk[nomor - 1]}")
    else:
        print("Nomor tidak valid. Harus antara 1 sampai 5.")
except ValueError:
    print("Masukan harus berupa angka")


