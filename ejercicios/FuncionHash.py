'''
Python proporciona una biblioteca estándar llamada hashlib que permite calcular hash utilizando varios algoritmos hash comunes, 
como MD5, SHA-1, SHA-256, etc. Aquí tienes un ejemplo simple de cómo calcular el hash de una cadena utilizando SHA-256:
'''

import hashlib

def calcular_hash(texto):
    # Crear un objeto hash SHA-256
    hash_objeto = hashlib.sha256()
    
    # Actualizar el objeto hash con el texto codificado en UTF-8
    hash_objeto.update(texto.encode('utf-8'))
    
    # Obtener el hash en formato hexadecimal
    hash_hex = hash_objeto.hexdigest()
    
    return hash_hex

# Ejemplo de uso
texto = "Hola, este es un ejemplo de función hash en Python"
hash_resultado = calcular_hash(texto)
print("Hash SHA-256 del texto:", hash_resultado)


'''
Este código calcula el hash SHA-256 de la cadena texto y lo imprime en formato hexadecimal. Puedes cambiar el algoritmo 
hash simplemente cambiando hashlib.sha256() a cualquier otro algoritmo disponible en hashlib, como hashlib.md5(), hashlib.sha1(), etc.
'''