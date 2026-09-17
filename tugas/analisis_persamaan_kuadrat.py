# Input: koefisien a, b, dan c
print("Analisis Persamaan Kuadrat")
a = float(input("Koefisien a: "))
b = float(input("Koefisien b: "))
c = float(input("Koefisien c: "))

# Proses keputusan: memeriksa apakah a sama dengan 0
if a == 0:
    # Output: bukan persamaan kuadrat
    print("Bukan persamaan kuadrat.")
else:
    # Proses: menghitung diskriminan
    diskriminan = b ** 2 - 4 * a * c
    print(f"Diskriminan = {diskriminan:.2f}")

    # Proses keputusan: memeriksa nilai diskriminan
    if diskriminan > 0:
        # Output: dua akar real berbeda
        x1 = (-b + diskriminan ** 0.5) / (2 * a)
        x2 = (-b - diskriminan ** 0.5) / (2 * a)
        print(f"Dua akar real: {x1:.2f} dan {x2:.2f}")
    elif diskriminan == 0:
        # Output: satu akar real kembar
        x = -b / (2 * a)
        print(f"Akar kembar: {x:.2f}")
    else:
        # Output: tidak ada akar real
        print("Tidak ada akar real")