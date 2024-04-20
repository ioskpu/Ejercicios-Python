# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

odd_numbers = 0
even_numbers = 0

# leer el primer número
number = int(input("Introduce un número o escribe 0 para detener: "))

# 0 termina la ejecución
while number: #number != 0: funciona de las dos maneras
    # verificar si el número es impar
    # if number % 2 == 1:
    # tambien podriamos hacerlo de la siguiente manera:
    if number % 2:    
        # incrementar el valor de números impares de odd_numbers
        odd_numbers += 1
    
    else:
        # incrementar el valor de números pares de even_numbers
        even_numbers += 1
    
    # leer el siguiente número
    
    number = int(input("Introduce un número o escribe 0 para detener: "))

# imprimmir resultados
print("Conteo de números impares:", odd_numbers)
print("Conteo de números pares:", even_numbers)    