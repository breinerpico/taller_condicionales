import math

# input 

peso=int(input("digite su peso: "))
altura=float(input("digite su altura: "))

# processing 

IMC=(peso/altura**2)

#output

if IMC<16:
    print("usted tiene criterio de ingreso al hospital")

elif IMC>16 and IMC <17:
    print("usted tiene infrapeso")

elif IMC >17 and IMC <18:
    print("usted tiene bajo peso")

elif IMC >18 and IMC <25:
    print("usted tiene un peso normal")

elif IMC >25 and IMC <30:
    print("usted tiene sobrepeso(obesidad grado 1)")

elif IMC >30 and IMC <35:
    print("usted tiene obesidad cronica(obesidad de grado 2)")

elif IMC >35 and IMC <40:
    print("udted tiene obecidad premorbida(obecidad de grado 3)")

elif IMC >40:
    print("udted tiene obecidad morbida(obecidad de grado 4)")
