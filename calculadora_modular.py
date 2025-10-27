# -----------------------------------------------

def sumar(a, b):
    """
    Devuelve la suma de a y b.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de la suma (a + b).
    """
    return a + b


def restar(a, b):
    """
    Devuelve la resta de a y b.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de la resta (a - b).
    """
    return a - b


def multiplicar(a, b):
    """
    Devuelve el producto de a y b.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de la multiplicación (a * b).
    """
    return a * b


def dividir(a, b):
    """
    Devuelve la división de a entre b.

    Args:
        a (float): Dividendo.
        b (float): Divisor.

    Returns:
        float | str: Resultado de la división (a / b)
                     o un mensaje de error si b es cero.
    """
    if b == 0:
        return "Error: división por cero"
    return a / b


def main():
    """
    Muestra el menú principal y ejecuta la operación elegida por el usuario.

    Flujo del programa:
        1. Muestra el menú de operaciones.
        2. Solicita al usuario una opción.
        3. Pide dos números para operar.
        4. Ejecuta la operación correspondiente.
        5. Muestra el resultado.

    Returns:
        None
    """
    print("=== Calculadora Modular ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Elige una opción: ")

    try:
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
    except ValueError:
        print("Error: debes ingresar valores numéricos.")
        return

    if opcion == "1":
        print("Resultado:", sumar(a, b))
    elif opcion == "2":
        print("Resultado:", restar(a, b))
    elif opcion == "3":
        print("Resultado:", multiplicar(a, b))
    elif opcion == "4":
        print("Resultado:", dividir(a, b))
    else:
        print("Opción inválida")


if __name__ == "__main__":
    main()