#Palindromo
#crear una funcion para determinar si una palabra, frase o/y numero es palindromo o no

def palindromo(palabra):
    if palabra.isdigit(): # verificar si la entrada es un número
        palabra = str(palabra) # convertir el numero a cadena de texto
    else:        
        palabra = palabra.lower().replace(" ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u") #quitar espacios y tildes

    #mediante el bucle for iteramos sobre la palabra, frase o numero ya filtrado para comparar si la primera letra y la ultima son iguales
    a = 0
    b = 1

    for i in range(0, len(palabra)):
        if palabra[i] == palabra[len(palabra) - i - 1]:
            a += 1
            b += 1
        else:
            return False
    
    return True

palabra = input("Ingrese una palabra, frase o numero: ")

if palindromo(palabra):
    print("Es una palabra, frase o numero palindromo")

else:
    print("No es una palabra, frase o numero palindromo")


