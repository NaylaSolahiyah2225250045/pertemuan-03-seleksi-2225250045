# Pertemuan 03 Seleksi Python

Nama: Nayla Solahiyah  
NIM: 2225250045  
Kelas: 3A  

## Tujuan
Menulis program seleksi if, if-else, kondisi majemuk, dan nested if. 

## Cara Menjalankan
python3 tugas/analisis_persamaan_kuadrat.py

## Algoritma Tugas
1. Masukkan nilai a, b, dan c sebagai koefisien persamaan kuadrat.
2. Periksa terlebih dahulu nilai a. Jika a = 0, maka persamaan tersebut bukan persamaan kuadrat.
3. Jika a tidak sama dengan 0, lanjutkan dengan menghitung nilai diskriminan menggunakan rumus D = b² - 4ac.
4. Setelah nilai diskriminan diperoleh, tentukan jenis akar berdasarkan nilainya.
5. Jika D > 0, berarti persamaan memiliki dua akar real yang berbeda, sehingga program menghitung kedua akar tersebut.
6. Jika D = 0, berarti persamaan memiliki satu akar real yang sama atau akar kembar.
7. Jika D < 0, berarti persamaan tidak memiliki akar real.
8. Tampilkan hasil sesuai dengan kondisi yang diperoleh.

## Hasil Pengujian
| No. | Input (a, b, c) | D | Keluaran yang Diharapkan | Keluaran Aktual | Status |
|---|---|---:|---|---|---|
| 1 | (1, -5, 6) | 1 | Dua akar real: 3 dan 2 | Dua akar real: 3.00 dan 2.00 | Berhasil |
| 2 | (1, 2, 1) | 0 | Akar kembar: -1 | Akar kembar: -1.00 | Berhasil |
| 3 | (1, 0, 1) | -4 | Tidak ada akar real | Tidak ada akar real | Berhasil |
| 4 | (0, 2, 3) | - | Bukan persamaan kuadrat | Bukan persamaan kuadrat. | Berhasil |

## Refleksi
Kesalahan logika yang saya temukan adalah saat saya salah menempatkan posisi indentasi (spasi) pada perintah print() di dalam percabangan if-else. Akibatnya, ada teks output yang selalu muncul di layar padahal kondisinya tidak terpenuhi. Cara memperbaikinya adalah dengan mengulang dan menyejajarkan kembali spasi blok kode tersebut agar masuk ke dalam struktur if yang benar.