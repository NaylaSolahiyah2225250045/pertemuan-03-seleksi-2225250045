# Input
a = float(input("Bilangan pertama: "))
b = float(input("Bilangan kedua: "))

# Proses keputusan: membandingkan bilangan pertama dengan bilangan kedua
if a >= b:
    if a == b:
        # Output: kedua bilangan sama
        print("Kedua bilangan sama.")
    else:
        # Output: bilangan pertama lebih besar
        print("Bilangan pertama lebih besar.")
else:
    # Output: bilangan pertama lebih kecil
    print("Bilangan pertama lebih kecil.")