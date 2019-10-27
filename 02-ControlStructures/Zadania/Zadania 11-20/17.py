slp = 0
slnp = 0
for x in range (1,51):
    if x % 2 == 0:
        slp += x
    else:
        slnp += x
print(f'Przedział <1,50>\nSuma liczb parzystych: {slp}\nSuma liczb nieparzystych: {slnp}')