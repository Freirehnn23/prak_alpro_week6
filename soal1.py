def perkalian(a, b):
    hasil = 0
    for _ in range(a):
        hasil += b
    return hasil

print("6 x 5 =", end=" ")
print(" + ".join(["5"] * 6), "=", perkalian(6, 5))

print("7 x 10 =", end=" ")
print(" + ".join(["10"] * 7), "=", perkalian(7, 10))