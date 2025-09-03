import tkinter as tk
from tkinter import messagebox

# Data global
nilai_siswa = []

# ==== Fungsi Logika ====

def tambah_nilai():
    try:
        nilai = int(entry_nilai.get())
        nilai_siswa.append(nilai)
        messagebox.showinfo("Sukses", f"Nilai {nilai} berhasil ditambahkan!")
        entry_nilai.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

def tampilkan_nilai():
    if not nilai_siswa:
        hasil.set("Data nilai masih kosong.")
    else:
        hasil.set(f"Daftar Nilai: {nilai_siswa}")

def urutkan_nilai():
    if not nilai_siswa:
        messagebox.showwarning("Kosong", "Data nilai masih kosong.")
        return
    nilai_siswa.sort(reverse=True)
    hasil.set("Data berhasil diurutkan (descending).")

def cari_linear():
    try:
        target = int(entry_cari.get())
        for i in range(len(nilai_siswa)):
            if nilai_siswa[i] == target:
                hasil.set(f"Linear Search: Nilai {target} ditemukan di index {i}")
                return
        hasil.set("Nilai tidak ditemukan (Linear Search).")
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai yang ingin dicari.")

def cari_binary():
    try:
        if not nilai_siswa:
            hasil.set("Data kosong. Tambah & urutkan dulu.")
            return

        target = int(entry_cari.get())
        kiri, kanan = 0, len(nilai_siswa) - 1
        while kiri <= kanan:
            mid = (kiri + kanan) // 2
            if nilai_siswa[mid] == target:
                hasil.set(f"Binary Search: Nilai {target} ditemukan di index {mid}")
                return
            elif nilai_siswa[mid] < target:
                kanan = mid - 1
            else:
                kiri = mid + 1
        hasil.set("Nilai tidak ditemukan (Binary Search).")
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai yang ingin dicari.")

# ==== Setup GUI ====
root = tk.Tk()
root.title("🎓 Sistem Manajemen Nilai Siswa")
root.geometry("450x500")
root.configure(bg="#f0f8ff")  # Biru muda lembut

# ==== Gaya Font ====
judul_font = ("Cooper Black", 20, "bold")
label_font = ("Comic Sans MS", 11)
button_font = ("Comic Sans MS", 10, "bold")


# ==== Judul ====
judul = tk.Label(root, text="📊 Manajemen Nilai", font=judul_font, bg="#f0f8ff", fg="#003366")
judul.pack(pady=15)

# ==== Input Nilai ====
tk.Label(root, text="Masukkan Nilai Baru:", font=label_font, bg="#f0f8ff").pack()
entry_nilai = tk.Entry(root, font=label_font, justify="center")
entry_nilai.pack(pady=5)

tk.Button(root, text="➕ Tambah Nilai", command=tambah_nilai,
          bg="#28a745", fg="white", font=button_font, width=20).pack(pady=5)

# ==== Input Pencarian ====
tk.Label(root, text="Masukkan Nilai untuk Dicari:", font=label_font, bg="#f0f8ff").pack(pady=10)
entry_cari = tk.Entry(root, font=label_font, justify="center")
entry_cari.pack(pady=5)

# ==== Tombol Fungsi ====
tk.Button(root, text="📋 Tampilkan Nilai", command=tampilkan_nilai,
          bg="#007bff", fg="white", font=button_font, width=25).pack(pady=4)

tk.Button(root, text="⬇️ Urutkan Nilai (Descending)", command=urutkan_nilai,
          bg="#17a2b8", fg="white", font=button_font, width=25).pack(pady=4)

tk.Button(root, text="🔍 Cari (Linear Search)", command=cari_linear,
          bg="#ffc107", fg="black", font=button_font, width=25).pack(pady=4)

tk.Button(root, text="🔎 Cari (Binary Search)", command=cari_binary,
          bg="#6f42c1", fg="white", font=button_font, width=25).pack(pady=4)

# ==== Output / Hasil ====
hasil = tk.StringVar()
output_label = tk.Label(root, textvariable=hasil, font=label_font,
                        wraplength=400, justify="left", bg="#f0f8ff", fg="#333")
output_label.pack(pady=20)

# ==== Jalankan GUI ====
root.mainloop()
