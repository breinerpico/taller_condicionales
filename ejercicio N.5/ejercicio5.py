# input 

metros_gastados=int(input("digite los metros cuadrados: "))

# processing 

if metros_gastados <=50: 
    costo=0 

elif metros_gastados >50 and metros_gastados <=200:
    costo=2000 * (metros_gastados - 50)

else:
    metros_gastados >200
    costo=3000 * (metros_gastados - 50)

costo_agua=10000 + costo

# output

print("El costo del agua es: ",costo_agua)
