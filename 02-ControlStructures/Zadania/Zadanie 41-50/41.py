# Program obliczy sumę i średnią arytmetyczną dowolnej ilości liczb
# Wprowadzenie liczby 0 skutkuje zakończeniem wprowadzania liczb

try:
    c = 00
    suma = 0
    while True:    
        a = int(input('Podaj liczbę: '))
        if a == 0:
            srednia = suma/c
            break
        c += 1
        suma += a
    print(f'REZULTAT: Liczb: {c}, Suma={suma}, Średnia={srednia}')
except ValueError:
    print('Podana wartość nie jest liczbą!')