import math

while True:
    try:
        a = int(input("Длина первого катета: "))
        b = int(input("Длина второго катета: "))

        a = float(a)
        b = float(b)
        break

    except ValueError:
        print("Вы не ввели число. Попробуйте ещё раз.")
    
c = math.sqrt(a ** 2 + b ** 2)

S = a * b / 2
P = a + b + c

print(f"Площадь треугольника: {S:.2f}")
print(f"Периметр треугольника: {P:.2f}")    



