'''
Python proporciona dos instrucciones especiales para la implementación de estas dos tareas. 
Digamos por razones de precisión que su existencia en el lenguaje no es necesaria - un 
programador experimentado puede codificar cualquier algoritmo sin estas instrucciones. Tales 
adiciones, que no mejoran el poder expresivo del lenguaje, sino que solo simplifican el trabajo 
del desarrollador, a veces se denominan dulces sintácticos o azúcar sintáctica.

Estas dos instrucciones son:

break - sale del bucle inmediatamente, e incondicionalmente termina la operación del bucle; el 
programa comienza a ejecutar la instrucción más cercana después del cuerpo del bucle.
continue - se comporta como si el programa hubiera llegado repentinamente al final del cuerpo; 
el siguiente turno se inicia y la expresión de condición se prueba de inmediato.
Ambas palabras son palabras clave reservadas.
'''

# break - ejemplo
'''
print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

# mas ejemplos de break y continue
largest_number = -99999999
counter = 0

while True:
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")
'''
# mas ejemplos
'''
Escenario
La instrucción break se implementa para salir/terminar un bucle.

Diseña un programa que use un bucle while y le pida continuamente al usuario que ingrese una 
palabra a menos que ingrese "chupacabra" como la palabra de output secreta, en cuyo caso el 
mensaje "Has dejado el bucle con éxito." debe imprimirse en la pantalla y el bucle debe terminar.

No imprimas ninguna de las palabras ingresadas por el usuario. Utiliza el concepto de ejecución 
condicional y la sentencia break.
'''

while True:
    word = input("Ingresa una palabra o escribe 'chupacabra' para dejar el bucle: ")
    if word == "chupacabra":
        print("Has dejado el bucle con exito.")
        break