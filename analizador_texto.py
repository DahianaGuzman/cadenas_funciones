def contar_palabras(texto):
    """Cuenta cuántas palabras tiene el texto."""
    palabras = texto.split()
    return len(palabras)


def contar_frases(texto):
    """Cuenta cuántas frases hay en el texto (por ., ! o ?)."""
    frases = 0
    for signo in [".", "!", "?"]:
        frases += texto.count(signo)
    return frases


def contar_parrafos(texto):
    """Cuenta cuántos párrafos hay (separados por saltos de línea)."""
    parrafos = [p for p in texto.split("\n") if p.strip() != ""]
    return len(parrafos)


def main():
    """Función principal: pide un texto y muestra sus estadísticas."""
    print("=== Analizador de Texto ===")
    texto = input("Escribe o pega un texto:\n")

    print("\n--- RESULTADOS ---")
    print("Palabras:", contar_palabras(texto))
    print("Frases:", contar_frases(texto))
    print("Párrafos:", contar_parrafos(texto))


if _name_ == "_main_":
    main()
