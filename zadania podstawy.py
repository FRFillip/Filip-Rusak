# Zadanie 1: Napisz funkcję, która zwraca sumę dwóch liczb
def suma(a, b):
    return a + b

print("Zadanie 1: Suma 3 i 5 =", suma(3, 5))

# Zadanie 2: Napisz funkcję, która sprawdza, czy liczba jest parzysta
def jest_parzysta(liczba):
    return liczba % 2 == 0

print("Zadanie 2: Czy 4 jest parzysta?", jest_parzysta(4))

# Zadanie 3: Napisz program, który wypisuje liczby od 1 do 10
print("Zadanie 3: Liczby od 1 do 10:")
for i in range(1, 11):
    print(i)