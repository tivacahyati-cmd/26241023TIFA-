a = int(input("digit A: "))
b = int(input("digit B: "))

kondisi1 = a >= 5
kondisi2 = b >= 5

print("kondisi 1:", kondisi1)
print("kondisi 2:", kondisi2)

print("NOT:", not kondisi1)
print("AND:", kondisi1 and kondisi2)
print("OR :", kondisi1 or kondisi2)
print("XOR:", kondisi1 ^ kondisi2)

# OR bernilai True jika salah satu kedua kondisi true,
# sedangkan XOR hanya true jika kedua kondisi berbeda.
