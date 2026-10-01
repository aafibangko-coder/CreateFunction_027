### 1. Fungsi untuk mengonversi suhu
def convert_temperature(value, unit):
    if unit == "C":
        fahrenheit = (value * 9/5) + 32
        return fahrenheit
    elif unit == "F":
        celsius = (value - 32) * 5/9
        return celsius
    else:
        return "Unit tidak valid"

temperature = float(input("Masukkan suhu: "))
unit = input("Masukkan unit (C/F): ").upper()

result = convert_temperature(temperature, unit)

if unit == "C":
    print("Suhu dalam Fahrenheit:", result)
elif unit == "F":
    print("Suhu dalam Celsius:", result)
else:
    print(result) 

    #### 2. Fungsi untuk menghitung luas lingkaran
import math

area = lambda r: math.pi * r ** 2

radius = float(input("Masukkan jari-jari lingkaran: "))

result = area(radius)

print("Luas lingkaran:", result)