import math

area = lambda r: math.pi * r ** 2

radius = float(input("Masukkan jari-jari lingkaran: "))

result = area(radius)

print("Luas lingkaran:", result)