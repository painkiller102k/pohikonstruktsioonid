from math import * #поставил правильное местоположение

print("Ruudu karakteristikud")
a=float(input('Sisesta ruudu külje pikkus => ')) #добавил тип данных float
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt",P) #изменил кавычки
di=a*sqrt(2) #убрал импорт math
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #убрал лишнюю скобку
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #добавил тип данных float
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) #добавил тип данных float
S=b*c
print("Ristküliku pindala",S) #поставил правильные кавычки
P=2*(b+c) #добавил знак умножения
print("Ristküliku ümbermõõt",P)
di=sqrt(b*2+c*2) #убрал импорт math
print("Ristküliku diagonaal", round(di)) #добавил скобку
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => ")) #изменил кавычки и тип данных float
d=2*r #добавил знак умножения
print("Ringi läbimõõt",d) # добавил недостающую запятую
S=pi*r*2 #убрал скобки и сделал возведение в степень
print("Ringi pindala", round(S))
C=2*pi*r #убрал скобки
print("Ringjoone pikkus", round(C))