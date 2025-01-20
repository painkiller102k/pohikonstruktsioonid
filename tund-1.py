#ülesanne 1
from re import S
from stat import FILE_ATTRIBUTE_ARCHIVE


a=str(input("Введите ваше имя - "))
b=int(input("Введите ваш возраст - "))

print("Hello,world!","Приветствую тебя,",a,"!","Тебе",b,"лет!")

#ülesanne 2
a=int(input("Введите ваш возраст - "))
b=str(input("Введите ваше имя - "))
c=float(input("Введите ваш рост - "))
d=bool(input("Посещает ли школу? - "))

print("Привет,",b,"тебе",a,"лет!","Ваш рост",c,"см","Ученик посещает школу - ",d)

#ülesanne 3
a=int(input("Введите количество конфет - "))
b=int(input("Введите сколько количество конфет взяли - "))
print("На столе осталось - ",a-b,"конфет!")