# Data jadwal disimpan dalam bentuk list of dictionaries
jadwal_kuliah = [
    {'hari': 'senin', 'matakuliah': 'Struktur Data', 'dosen': 'Dr. Ani', 'ruang': '11'},
    {'hari': 'selasa', 'matakuliah': 'Basis Data', 'dosen': 'Dr. Budi', 'ruang': '15'},
    {'hari': 'rabu', 'matakuliah': 'Pemrograman Python', 'dosen': 'Triyono S.Kom', 'ruang': '12'},
    {'hari': 'rabu', 'matakuliah': 'Jaringan Komputer', 'dosen': 'Dr. Citra', 'ruang': 'Lab-Jarkom'},
    {'hari': 'kamis', 'matakuliah': 'Kecerdasan Buatan', 'dosen': 'Dr. Budi', 'ruang': '15'}
]

def jadwal_hari(hari):
    """Menampilkan jadwal kuliah untuk hari yang spesifik."""
    print(f"Jadwal untuk hari {hari.capitalize()}:")
    ditemukan = False
    for jadwal in jadwal_kuliah:
        if jadwal['hari'].lower() == hari.lower():
            print(f"- Matakuliah: {jadwal['matakuliah']}, Dosen: {jadwal['dosen']}, Ruang: {jadwal['ruang']}")
            ditemukan = True

    if not ditemukan:
        print("Tidak ada jadwal untuk hari ini.")

# Contoh pemanggilan fungsi
jadwal_hari('rabu')
print("\n" + "="*20 + "\n")
jadwal_hari('jumat')