from datetime import date
from math import *
import math

#1
tana = date.today()
print("Сегодня -",tana)
print(f"Сегодня - {tana.strftime('%d %B %Y')}")
print(f"Сегодня - {tana.strftime('%m %d %y')}")

#2
a=3+8
b=(4-2)*4
print("Ответ =",a+b)

#3
a=float(input("Радиус круга ="))

p=4*a**2
p1=8*a
pc=math.pi*a**2
pc1=math.pi*2*a

print(f"Площадь квадрата - {p}")
print(f"Периметр квадрата - {p1}")
print(f"Площадь круга - {pc}")
print(f"Периметр круга - {pc1}")

#4
