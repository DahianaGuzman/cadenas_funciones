## Proyecto de Programas con Cadenas y Funciones

Este proyecto contiene **cinco programas** básicos hechos en Python, enfocados en el uso de **funciones**, **manejo de cadenas** y **entrada/salida de datos**.
Cada programa está diseñado para practicar conceptos clave del curso.

### ¿Cómo ejecutar los programas?
Para ejecutar cualquiera de los programas, sigue estos pasos:

1.Asegúrate de tener Python 3 instalado en tu sistema. Puedes descargarlo desde python.org.
2.Clona o descarga este repositorio a tu máquina local.
3.Abre tu terminal o línea de comandos (CMD en Windows, Terminal en macOS/Linux).
4.Navega hasta el directorio donde guardaste los archivos del programa. Por ejemplo, si los tienes en una carpeta llamada mis_programas_python en tu escritorio: cd Desktop/mis_programas_python.
5.Una vez en el directorio correcto, ejecuta el programa deseado usando el comando python seguido del nombre del archivo .py. Por ejemplo: python palindromos.py.
### 1️. `contar_caracteres.py`

**✔️ Función:** Cuenta vocales, consonantes, espacios y caracteres especiales en una cadena.

####  Entrada de ejemplo

el fracaso no es más que una oportunidad de volver a empezar!!!

####  Salida esperada

Vocales: 24  
Consonantes: 30  
Espacios: 11  
Caracteres especiales: 3

#### ⚠️ Posibles errores

* No se valida si la entrada está vacía.
* Algunos caracteres Unicode especiales podrían no ser tratados correctamente si no están en minúscula o fuera del rango `isalpha()`.

### 2️. `palindromo.py`

**✔️ Función:** Verifica si una frase es un palíndromo, ignorando espacios, mayúsculas y signos de puntuación.

####  Entrada de ejemplo

Anita lava la tina

####  Salida esperada

La frase ingresada es un palíndromo

#### ⚠️ Posibles errores

* Si la entrada contiene solo espacios o caracteres especiales, puede generar resultados incorrectos.
* Si el usuario no ingresa texto, se mostrará un mensaje de error controlado con `try-except`.


# 3. `calculadora_modular.py`

**✔️ Función:** Programa en **Python** que realiza **operaciones aritméticas básicas**:  
- Suma  
- Resta  
- Multiplicación  
- División  

Cada operación se implementa mediante una función independiente.

## Funcionamiento:  

El programa:
1. Muestra un menú con las operaciones disponibles.  
2. Solicita dos números al usuario.  
3. Ejecuta la operación elegida.  
4. Muestra el resultado o un mensaje de error si ocurre algún problema.

####  Entrada esperada

Elige una opción: 1
Número 1: 10
Número 2: 5

####  Salida esperada

Resultado: 15.0

#### ⚠️ Posibles errores

*Si el usuario intenta dividir por cero, se mostrará "Error: división por cero".
*Si el usuario ingresa texto en lugar de números, se mostrará "Error: debes ingresar valores numéricos.".
*Si elige una opción que no está en el menú, se mostrará "Opción inválida".


### 4️. `generador_contrasenas.py`

**✔️ Función:** Genera una contraseña aleatoria de longitud N usando letras, números y símbolos.

####  Entrada esperada

Ingrese longitud de la contraseña: 12

####  Salida esperada

Contraseña generada: a8K!d2#rQ9@h

#### ⚠️ Posibles errores

* Entrada no numérica o negativa
* Longitudes menores a 4 podrían generar contraseñas débiles

### 5️. `analizador_texto.py`

**✔️ Función:** Cuenta la cantidad de palabras, frases y párrafos en un texto.

####  Entrada esperada
(Párrafo ingresado por el usuario)

####  Salida esperada

Palabras: 45  
Frases: 3  
Párrafos: 2

#### ⚠️ Posibles errores

* No considerar saltos de línea como delimitadores de párrafo si no están bien escritos
* Errores en conteo si el texto no usa puntuación estándar (.,!?)


###  Requisitos

* Python 3.6 o superior
* No se requieren módulos externos (excepto `string`, que es estándar)




