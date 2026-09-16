# Input: tiga panjang sisi
a = float(input("Sisi a: "))
b = float(input("Sisi b: "))
c = float(input("Sisi c: "))

# Proses keputusan: memeriksa apakah ketiga sisi dapat membentuk segitiga
if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        # Output: segitiga sama sisi
        print("Segitiga sama sisi")
    else:
        if a == b or a == c or b == c:
            # Output: segitiga sama kaki
            print("Segitiga sama kaki")
        else:
            # Output: segitiga sembarang
            print("Segitiga sembarang")
else:
    # Output: ketiga sisi tidak membentuk segitiga
    print("Ketiga sisi tidak membentuk segitiga")