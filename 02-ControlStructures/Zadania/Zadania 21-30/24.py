imiona = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy", "Teofil"]

temp = 0
imie_index = None
for i in imiona:
    if len(i) > temp:
        temp = len(i)
        imie_index = imiona.index(i)
print(f'najdłuższę imię: {imiona[imie_index]}')    