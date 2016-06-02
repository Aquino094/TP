#Programa que imprime fizz si el numero es multiplo de 3,
#buzz si es multiplo de 5 y si es multiplo de ambos imprime fizzbuzz  numero

#crear un contador
count = 0
#usamos estructura while que permitira la
#ejecucion mientras se cumpla la condicion
while (count < 101):
    #realizar una sentencia que compare si el numero incrementando
     #es multiplo de ambos y si es asi imprimira FizzBuzz y
     #el respectivo valor, y luego se le sumara 1 al contador
    if (count % 5) == 0 and (count % 3) == 0:
        print "FizzBuzz"
        count = count + 1
    #realizar una  sentencia que compare si el numero
    #incrementado es multiplo de 3 y si es asi imprimira  Fizz
    elif (count % 3) == 0:
        print "Fizz"
        count = count + 1
    #realizar una sentencia que compare si el numero
    #incrementado es multiplo de 5 y si es asi imprimira  Buzz
    elif (count % 5) == 0:
        print "Buzz"
        count = count + 1
    #mostrar el numero e incrementar el valor del numero
    else:
        print count
        count = count + 1
