# Fungsi untuk menghitung ongkir
def hitung_ongkir(berat_kg, kota, asuransi=False):
    """
    Menghitung ongkir RapidSend berdasarkan kota tujuan, berat barang, 
    dan apakah menggunakan asuransi atau tidak.

    Parameter:
    - berat_kg : berat barang dalam kilogram
    - kota      : kota tujuan (string)
    - asuransi  : True jika ingin menambahkan biaya asuransi, False jika tidak

    Output:
    - ongkir    : total ongkir (dalam Rupiah)
    - dasar     : tarif dasar sesuai kota
    """

    # Dictionary untuk menyimpan tarif dasar tiap kota
    tarif_dasar = {
        "Jakarta": 10000,
        "Bandung": 12000,
        "Surabaya": 15000,
        "Yogyakarta": 13000
    }

    # Ambil tarif dasar dari dictionary, jika kota tidak ada maka default 0
    dasar = tarif_dasar.get(kota, 0)

    # Hitung ongkir dasar ditambah biaya berdasarkan berat (Rp 2.000 per kg)
    ongkir = dasar + 2000 * berat_kg

    # Jika pengguna memilih asuransi, tambahkan Rp 3.000
    if asuransi:
        ongkir += 3000

    # Kembalikan total ongkir dan tarif dasar kota
    return ongkir, dasar


# ===============================
# Pemanggilan fungsi otomatis
# ===============================

# Data barang / pesanan
kota = "Solo"        # Kota tujuan
berat = 4            # Berat barang dalam kg
asuransi = True      # Apakah menggunakan asuransi

# Panggil fungsi hitung_ongkir dan ambil hasilnya
total, tarif_dasar = hitung_ongkir(berat, kota, asuransi)

# ===============================
# Menampilkan rincian ongkir
# ===============================
print("=== Rincian Otomatis ===")
print(f"Kota tujuan     : {kota}")                             # Tampilkan kota tujuan
print(f"Tarif dasar     : Rp {tarif_dasar:,}")                # Tampilkan tarif dasar kota
print(f"Berat           : {berat} kg")                        # Tampilkan berat barang
print(f"Biaya berat     : Rp {2000 * berat:,}")               # Tampilkan biaya tambahan berdasarkan berat
print(f"Asuransi        : {'YA (Rp 3.000)' if asuransi else 'TIDAK'}")  # Tampilkan status asuransi
print(f"Total ongkir    : Rp {total:,}")                      # Tampilkan total ongkir