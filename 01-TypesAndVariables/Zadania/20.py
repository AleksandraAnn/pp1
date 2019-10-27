import math

'''
Obliczanie pola powierzchni i obwodu koła o żądanym promieniu
'''

#ustal promień koła i PI
r = 5
pi = math.pi


# oblicz pola i obwód
P = pi*r**2
O = 2*pi*r

# wyświetl rezultaty
print("""Pole koła o promieniu {0} wynosi {1}""".format(r,P))
print("""Obwód koła o promieniu {0} wynosi {2}""".format(r,P,O))
