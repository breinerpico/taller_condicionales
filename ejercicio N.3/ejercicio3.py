# ejercicio 3

# input 

Precio_costo=int(input("digite el costo del producto: "))

# processing

if Precio_costo<=3000:
    ganancia=Precio_costo*0.15

elif Precio_costo<=6000:
    ganancia=500

else:
    ganancia=Precio_costo*0.25

Precio_venta= Precio_costo + ganancia

# output

<<<<<<< HEAD
print(" el producto tiene un costo de $" + str( Precio_costo ) + " con una ganacia de $ " + str( ganancia) + " queda con un precio de $" + str (Precio_venta))
=======
print(" el producto tiene un costo de $" + str( Precio_costo ) + " con una ganacia de $" + str( ganancia) + " queda con un precio de $" + str (Precio_venta))
>>>>>>> 57924468db55d0ba0ac27924b75ff4d68380dd08
