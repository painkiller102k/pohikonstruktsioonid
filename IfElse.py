from random import *
#NAIDIS 1
#arv=randint(0,10)
#print(arv)
#if arv>5:
    #print("*********")
   # print(f"Arv {arv} suurem kui 5")
    #print("*********")
#if arv>5: print(f"Arv {arv} suurem kui 5")

#NAIDIS 2
#arv=randint(0,10)
#if arv>5:
    #print("Positiivne")
#else:
    #print("Negatiivne") #ошибка потому что нет выражения если выпадет 5

#if arv>5:
    #print("Positiivne")
#elif arv==5:
    #print("Arv = 5")
#else:
    #print("Negatiivne")


#1
nimi=input("Как тебя зовут? - ")
if nimi.isupper() and nimi.lower() == "juku":
    print("Мы идем в кино!")
    try:
        vanus=int(input("Введи возраст - "))
        if vanus<0 or vanus>100:
            print("! ! !")
        elif vanus<6:
            print("Билет бесплатный!")
        elif vanus<=14:
            print("Детский билет")
        elif vanus<=65:
            print("Обычный билет")
        elif vanus<=100:
            print("Билет со скидкой")

    except Exception as e:
        print("Ошибка")
            
else:
    print("Мы не идем в кино")

#2
nimi1=input("Введите имя первого человека")
nimi2=input("Введите имя второго человека")
if nimi1 == "martin" and "illia" or nimi2 == "martin" and "illia":
    print("Вы соседи!")
else:
    print("Вы не соседи!")

#6
a=int(input("Какой у вас рост?"))
try:
        if a<150 or a>220:
            print("! ! !")
        elif a>=190:
            print("Вы высокий!")
        elif a>=170:
            print("Вы средний!")
        else:
            print("Вы низкий!")

except ValueError:
    print("Ошибка! Вы или слишком низкий или слишком высокий")