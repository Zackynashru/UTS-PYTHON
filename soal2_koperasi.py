# Blok try...except digunakan untuk mengantisipasi error.
try:
    # Meminta input dari pengguna dan langsung mengubahnya menjadi angka desimal (float).
    setoran1 = float(input("Masukkan setoran minggu ke-1: "))
    setoran2 = float(input("Masukkan setoran minggu ke-2: "))
    setoran3 = float(input("Masukkan setoran minggu ke-3: "))

    # Melakukan validasi input.
    if setoran1 <= 0 or setoran2 <= 0 or setoran3 <= 0:
        # Jika salah satu setoran bernilai 0 atau negatif, tampilkan pesan ini. [cite: 22]
        print("input tidak valid")
    else:
        # Blok ini hanya berjalan jika semua input valid (lebih dari 0).
        
        # Menjumlahkan ketiga setoran. [cite: 20]
        total = setoran1 + setoran2 + setoran3
        
        # Mencetak total dengan format yang mudah dibaca.
        print(f"Total setoran: {total:,.0f}")

        # Mengecek kondisi total untuk menentukan status. [cite: 21]
        if total >= 600000:
            print("Status: tinggi")
        elif total >= 300000:
            print("Status: sedang")
        else: # Jika kurang dari 300000
            print("Status: rendah")

# Blok ini akan dijalankan jika terjadi error 'ValueError'.
except ValueError:
    # Error ini terjadi jika pengguna memasukkan teks (bukan angka) saat input.
    print("input tidak valid")