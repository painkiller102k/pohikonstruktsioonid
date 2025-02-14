import math

try:
    a = float(input('Sisestage ruudu küljepikkus => '))
    S = a**2
    print("Nelinurkne pindala:", S)
    P = 4 * a
    print("Ruudu ümbermõõt:", P)
    di = a * math.sqrt(2)
    print("Ruutdiagonaal:", round(di, 2))
except ValueError:
    print("Viga, sisestage kehtiv number!")

print()

try:
    b = float(input("Sisestage ristküliku esimese külje pikkus => "))
    c = float(input("Sisestage ristküliku teise külje pikkus => "))
    S = b * c
    print("Ristküliku pindala:", S)
    P = 2 * (b + c)
    print("Ristküliku ümbermõõt:", P)
    di = math.sqrt(b**2 + c**2)
    print("Ristkülikukujuline diagonaal:", round(di, 2))
except ValueError:
    print("Viga, sisestage kehtiv number!")

print()

try:
    r = float(input('Sisestage ringi raadius => '))
    d = 2 * r
    print("Ringi läbimõõt:", d)
    S = math.pi * r**2
    print("Ringi ala:", round(S, 2))
    C = 2 * math.pi * r
    print("Ümbermõõt:", round(C, 2))
except ValueError:
    print("Viga, sisestage kehtiv number")