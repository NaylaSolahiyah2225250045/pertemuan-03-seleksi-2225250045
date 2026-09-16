# Input: nilai akhir dan persentase kehadiran
nilai = float(input("Nilai akhir: "))
kehadiran = float(input("Kehadiran (%): "))

# Proses keputusan: nilai minimal 60 dan kehadiran minimal 80 persen
if nilai >= 60 and kehadiran >= 80:
    # Output: mahasiswa lulus
    print("Lulus")
else:
    # Output: mahasiswa belum lulus
    print("Belum lulus")