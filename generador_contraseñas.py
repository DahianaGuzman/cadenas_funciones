import random   # Módulo para generar elementos aleatorios
import string   # Módulo que contiene cadenas de caracteres predefinidas (letras, dígitos, símbolos)

def generar_contrasena(longitud):
    """
    Genera una contraseña aleatoria de la longitud indicada.

    Parámetros:
        longitud (int): número de caracteres que tendrá la contraseña.

    Retorna:
        str: una cadena con la contraseña generada.
    """
    # Conjunto de caracteres posibles: letras (mayúsculas y minúsculas), números y símbolos
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Selecciona aleatoriamente 'longitud' caracteres del conjunto y los une en una cadena
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))

    return contrasena


def main():
    """
    Función principal del programa.
    Pide al usuario la longitud de la contraseña y muestra la generada.
    """
    # Solicita al usuario la longitud deseada para la contraseña
    n = int(input("Longitud de la contraseña: "))

    # Genera y muestra la contraseña resultante
    print("Contraseña generada:", generar_contrasena(n))


# Punto de entrada del programa:
# Este bloque asegura que la función main() se ejecute solo
# si el archivo se ejecuta directamente (no si se importa en otro programa).
if __name__ == "__main__":
    main()