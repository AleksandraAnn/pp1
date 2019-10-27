wzrost = float(input("Podaj wzrost w cm: "))
waga = int(input("Podaj wagę w kg: "))
BMI = waga/((wzrost/100)**2)
print(f'Wskaźnik BMI: {BMI}', '(waga prawidlowa)' if 25 > BMI > 18.5 else '(waga nieprawidłowa)')
