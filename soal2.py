def ganjil(bawah, atas):
    deret = []
    if bawah < atas:
        for i in range(bawah, atas + 1):
            if i % 2 != 0:
                deret.append(i)
    else:
        for i in range(bawah, atas - 1, -1):
            if i % 2 != 0:
                deret.append(i)
    return deret

bawah = int(input("Masukkan batas bawah: "))
atas = int(input("Masukkan batas atas: "))

hasil = ganjil(bawah, atas)
print("Deret bilangan ganjil:", ", ".join(map(str, hasil)))