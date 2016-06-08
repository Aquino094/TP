#lo primero es crear una lista con un valor adentro de 0
fibonacci=[0]
#crear dos variables que sera x ,y que tendran valor de 0 y 1
#otra variable con la catidad de sumas a realizar
x=1
y=0
num = 30
#hacer una funcion que recorra la lista con un rango determinado
for n in range(num):
#agregar la suma del las variables adentro de la lista
	fibonacci.append(x+y)
#crear otra variable que guarde la suma de x e y
	aux = x + y
#cambiar los valores de x por y, y al y x la suma de las mismas
	x = y
	y = aux
#por ultimo mostrar la lista completa
print(fibonacci)