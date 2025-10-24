import os     # untuk membuat folder
import csv    # untuk menulis dan membaca file CSV
import json   # untuk menyimpan hasil ke file JSON
import logging # untuk menampilkan pesan INFO dan ERROR

# --- 1. Atur logging sederhana ---
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# --- 2. Membuat folder data ---
try:
    # os.makedirs akan membuat folder jika belum ada
    os.makedirs("data", exist_ok=True)
    logging.info("Folder 'data' sudah siap.")
except Exception as error:
    logging.error(f"Gagal membuat folder: {error}")

# --- 3. Menulis file CSV ---
try:
    with open("data/presensi.csv", mode="w", newline="") as file:
        tulis = csv.writer(file)

        # Header kolom
        tulis.writerow(["nim", "nama", "hadir_uts"])

        # Data mahasiswa (1 artinya hadir, 0 artinya tidak hadir)
        tulis.writerow(["2310001", "Desta", 1])
        tulis.writerow(["2310002", "Vicky", 0])
        tulis.writerow(["2310003", "Arsa", 1])

    logging.info("Data berhasil disimpan ke presensi.csv.")
except Exception as error:
    logging.error(f"Gagal menulis file CSV: {error}")

# --- 4. Membaca file CSV dan menghitung kehadiran ---
try:
    with open("data/presensi.csv", mode="r") as file:
        # Membaca tiap baris sebagai dictionary
        baca = csv.DictReader(file)

        total = 0 # menghitung total mahasiswa
        hadir = 0 # menghitung yang hadir

        # loop membaca tiap baris data
        for baris in baca:
            total += 1
            
            if baris["hadir_uts"] == "1":
                hadir += 1
    
    # menghitung persentase hadir
    if total > 0:
        persentase = (hadir / total) * 100
    else:
        persentase = 0
        
    # simpan ke dictionary ringkasan
    ringkasan = {
        "total_mahasiswa": total,
        "hadir": hadir,
        "persentase": f"{persentase:.2f}%"
    }
    
    logging.info("Data berhasil dibaca dan dihitung.")
except Exception as error:
    logging.error(f"Gagal membaca file CSV: {error}")
    ringkasan = {}

# --- 5. Menyimpan hasil ke JSON ---
try:
    with open("data/ringkasan.json", mode="w") as file:
        json.dump(ringkasan, file, indent=4) # indent=4 agar lebih rapi
    
    logging.info("Ringkasan berhasil disimpan ke ringkasan.json.")
except Exception as error:
    logging.error(f"Gagal menyimpan file JSON: {error}")