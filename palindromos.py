#palindromo.py — Verificar si una cadena es un palíndromo.

#El import string se utiliza para importar el módulo string en Python. 
#Este módulo contiene una colección de constantes y funciones útiles para trabajar con cadenas de texto.

import string #lista de caracteres de puntuación para limpiar la frase

def es_palindromo(fraseUsuario):
    # Convertir a minúsculas y eliminar espacios
    frase_procesada = fraseUsuario.lower().replace(" ", "")
    # Eliminar signos de puntuación
    frase_sin_puntuacion = ''.join(ch for ch in frase_procesada if ch not in string.punctuation)
    # Invertir la frase
    palindromo = frase_sin_puntuacion[::-1]

    if frase_sin_puntuacion == palindromo:
        return "La frase ingresada es un palíndromo"
    else:
        return "La frase ingresada no es un palíndromo"

# Pedimos al usuario una frase y mostramos el resultado
try:
    entrada = input("Ingresa el texto a evaluar: ")
    print(es_palindromo(entrada))
except Exception as e:
    print(f"Ocurrió un error al procesar la entrada: {e}")