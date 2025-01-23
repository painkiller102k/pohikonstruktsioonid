#ülesanne 1
from re import S
from stat import FILE_ATTRIBUTE_ARCHIVE
from random import * 
from math import * 

a=str(input("Введите ваше имя - ")).capitalize()
b=int(input("Введите ваш возраст - "))

print("Hello,world!","Приветствую тебя,",a,"!","Тебе",b,"лет!")

#ülesanne 2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True

print(f"Muutuja {vanus} on {type(vanus)}")
print(f"Muutuja {eesnimi} on {type(eesnimi)}")
print(f"Muutuja {pikkus} on {type(pikkus)}")
print(f"Muutuja {kas_käib_koolis} on {type(kas_käib_koolis)}")

#ülesanne 3
a=randint(0,100)
print(a)
b=int(input("Сколько конфет хочешь съесть - "))
print("Конфет осталось ",a-b,"!")

#ülesanne 4
a=float(input("Введите окружность дерева - "))
print("Диаметр дерева состовляет",a/3.14,"см!")

#ülesanne 5
a=float(input("Введите N прямоугольника - "))
b=float(input("Введите M прямоугольника - "))
c=(a**2+b**2)
print(sqrt(c))

##ülesanne 6
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg

print("Sinu kiirus oli",str(kiirus),"km/h")

#ülesanne 7
a=randint(1,5)
b=randint(1,5)
c=randint(1,5)
d=randint(1,5)
e=randint(1,5)
f=(a+b+c+d+e)
print("Ваш средний балл - ",f/5)

#ülesanne 8
print("@..@")
print("(----)")
print("( \__/ )")
print("^^ "" ^^ ")

#ülesanne 9
a=5
b=2
c=15
print("Периметр треугольника - ",a+b+c,"см!")

#ülesanne 9
a=12,90
b=randint(1,10)
price=a/b
otvet=price%10
print(otvet)