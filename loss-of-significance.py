import numpy as np

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

for i in np.arange(0.0, 0.0000001, 0.0000000001):
	fx = ((i**2 +1 )**0.5) - 1
	print ("valor de x: ",i," valor fx: ",fx)
#en este ejemplo, podemos ver que mientras mas cerca esta el i de 0, aproxima el numero a 0, aproximando el valor a 0, lo que en extricto rigor, es erroneo, ya que la respuesta no es 0,
#sin embargo la respuesta es tan cercana, que el computador lo toma como 0.