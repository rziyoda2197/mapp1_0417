#1-misol
numbers = [1, 2, 3, 4, 5]

kvadratlar = list(map(lambda x: x**2, numbers))
print(kvadratlar)          # Natija: [1, 4, 9, 16, 25]

#2-misol
sozlar = ["salom", "dunyo", "python"]

katta = list(map(str.upper, sozlar))
print(katta)               # Natija: ['SALOM', 'DUNYO', 'PYTHON']

3-misol
numbers = [10, 20, 30, 40]

ikkiga = list(map(lambda x: x * 2, numbers))
print(ikkiga)              # Natija: [20, 40, 60, 80]

#4-misol
matnlar = ["salom", "python", "map funksiyasi"]

uzunliklar = list(map(len, matnlar))
print(uzunliklar)          # Natija: [5, 6, 14]

#5-misol
a = [1, 2, 3, 4]
b = [10, 20, 30, 40]

yigindi = list(map(lambda x, y: x + y, a, b))
print(yigindi)             # Natija: [11, 22, 33, 44]
