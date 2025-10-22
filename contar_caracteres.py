#contar_caracteres.py — Contar vocales, consonantes y espacios
import string

def contar_caracteres(x):
  # Inicializa los contadores de vocales, consonantes, espacios y caracteres
  v = 0 #vocales
  e = x.count(' ')  # Usa el método count() para contar espacios
  c = 0 #consonantes
  esp=0 #caracteres especiales
  frase=x.lower()#convertir contenido a minuscula
  # Itera sobre cada carácter en la cadena de entrada
  for i in frase:
    # Verifica si el carácter no es una vocal
    if i in 'aeiouáéióú':
      v = v + 1  # Si es una vocal, incrementa el contador 
    elif i.isalpha():# metodo que reconoce solo letras
      c += 1
    else:
      esp+= 1
  esp= esp-e
  # Imprime los resultados
  print('Vocales:', v)
  print('Consonantes:', c)
  print('Espacios:', e)
  print('Caracteres espaciales:', esp)

# Llamada y uso de la función 
contar_caracteres('el fracaso no es mas que una oportunidad de volver a empezar!!!')
#entrada = input("Ingresa el texto a evaluar: ")
#print(contar_caracteres(entrada))