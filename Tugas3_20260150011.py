print("=== SISTEM KALKULASI BIAYA PENGIRIMAN ===")

# Input data pengirim
nama_pengirim   = input("Masukkan nama pengirim: ")
alamat_pengirim = input("Masukkan alamat pengirim: ")
berat_barang    = float(input("masukkan berat barang (dalam kg): "))
jarak_pengiriman= float(input("masukkan jarak pengiriman (dalam km): "))
jenis_layanan   = input("masukkan jenis layanan (regular/express):" )

 #Logika perhitungan biaya pengiriman
if jarak_pengiriman < 50:
    tarif_per_kg = 5000 
elif jarak_pengiriman <= 100:
    tarif_per_kg = 10000
else:
    tarif_per_kg = 15000

biaya_pengiriman = tarif_per_kg * berat_barang

# Logika Jenis Layanan
if jenis_layanan.lower() == "express" and jarak_pengiriman > 100:
   biaya_tambahan = 0.20 * biaya_dasar
else:
   biaya_tambahan = 0

   #Total Biaya Akhir
   biaya_dasar = biaya_pengiriman
   biaya_akhir = biaya_dasar + biaya_tambahan

print("\n" + "="*40)
print("=== RINCIAN BIAYA PENGIRIMAN ===")
print("          AI EXPRESS    ")
print("="*40)
print(f"Nama Pengirim: {nama_pengirim}")
print(f"Alamat Pengirim: {alamat_pengirim}")
print(f"Berat Barang: {berat_barang} kg")
print(f"Jarak Pengiriman: {jarak_pengiriman} km")
print(f"biaya_dasar: Rp {biaya_dasar:,.2f}")
print(f"Jenis Layanan: {jenis_layanan}")
print(f"Biaya Tambahan: Rp {biaya_tambahan:,.2f}")
print(f"Total Biaya: Rp {biaya_akhir:,.2f}") 
