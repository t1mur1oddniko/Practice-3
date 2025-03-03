import math as m

a = int(input())
b = int(input())
c = int(input())

print(m.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * (180 / m.pi))
print(m.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)) * (180 / m.pi))
print(m.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)) * (180 / m.pi))