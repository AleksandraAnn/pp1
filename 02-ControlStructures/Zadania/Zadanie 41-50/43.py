tab = []
for x in range(1, 4):
    tab.append(int(input(f"Podaj liczbę: ")))
print(f'Posortowane: {", ".join([str(x) for x in sorted(tab)])}')