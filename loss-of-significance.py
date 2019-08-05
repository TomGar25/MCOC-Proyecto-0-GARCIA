

c = 1.0
d = 10.0
f = 3.0


print("ejenmplo uno: ", c/d + c/d + c/d, 3*c/d)
#primero explicamos el ejemplo del video, el cual es sumar 1/10 3 veces y multiplicarlo por tres, siendo ambas operaciones matematicamente iguales, no dan el mismo resultado,
#debido a la manera que el computador efectua las operaciones, a traves de la suma de numeros binarios en la primera operacion

a = 0.0
for i in range(1, 11):
	
	b = 0.0
	a+= c/d
	b = i*c/d
	error = a-b
	print(a, b, "error: ", error)
#luego utilizando el mismo ejemplo pero mas desarrollado, sumamos y multiplicamos separadamente ambos casos del 1 al 10 y calculamos el error al efectuar la misma operacion
# reflejando que en ciertos numeros como el 0,8 el computador puede tener diferencias insignificantes al hacer la misma operacion de maneras distitnas.
