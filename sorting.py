# Daftar harga awal
harga_produk = [350000, 120000, 75000, 500000, 210000]

print("Sebelum diurutkan:", harga_produk)

# Selection Sort
n = len(harga_produk)
for i in range(n):
    indeks_min = i
    for j in range(i+1, n):
        if harga_produk[j] < harga_produk[indeks_min]:
            indeks_min = j
    # Tukar posisi
    harga_produk[i], harga_produk[indeks_min] = harga_produk[indeks_min], harga_produk[i]

print("Setelah diurutkan:", harga_produk)
