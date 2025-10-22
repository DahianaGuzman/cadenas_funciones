## Proyecto de Programas con Cadenas y Funciones

Este proyecto contiene **cinco programas** básicos hechos en Python, enfocados en el uso de **funciones**, **manejo de cadenas** y **entrada/salida de datos**.
Cada programa está diseñado para practicar conceptos clave del curso.
---

### 1️. `contar_caracteres.py`

**✔️ Función:** Cuenta vocales, consonantes, espacios y caracteres especiales en una cadena.

####  Entrada de ejemplo
```
el fracaso no es más que una oportunidad de volver a empezar!!!
```

####  Salida esperada
```
Vocales: 24  
Consonantes: 30  
Espacios: 11  
Caracteres especiales: 3
```

#### ⚠️ Posibles errores

* No se valida si la entrada está vacía.
* Algunos caracteres Unicode especiales podrían no ser tratados correctamente si no están en minúscula o fuera del rango `isalpha()`.

---

### 2️. `palindromo.py`

**✔️ Función:** Verifica si una frase es un palíndromo, ignorando espacios, mayúsculas y signos de puntuación.

####  Entrada de ejemplo
```
Anita lava la tina
```

####  Salida esperada
```
La frase ingresada es un palíndromo
```

#### ⚠️ Posibles errores

* Si la entrada contiene solo espacios o caracteres especiales, puede generar resultados incorrectos.
* Si el usuario no ingresa texto, se mostrará un mensaje de error controlado con `try-except`.
---

### 3️. `calculadora_modular.py`

**✔️ Función:** Realiza operaciones básicas (+, -, *, /) usando funciones para cada operación.

####  Entrada esperada
* El usuario debe ingresar dos números y una operación (ej. `+`, `-`, `*`, `/`)

####  Salida esperada
```
Resultado: 15.0
```

#### ⚠️ Posibles errores

* División por cero
* Entrada de texto en lugar de números
* Operación no válida
---

### 4️⃣ `generador_contrasenas.py`

**✔️ Función:** Genera una contraseña aleatoria de longitud N usando letras, números y símbolos.

####  Entrada esperada
```
Ingrese longitud de la contraseña: 12
```

####  Salida esperada
```
Contraseña generada: a8K!d2#rQ9@h
```

#### ⚠️ Posibles errores

* Entrada no numérica o negativa
* Longitudes menores a 4 podrían generar contraseñas débiles
---

### 5️. `analizador_texto.py`

**✔️ Función:** Cuenta la cantidad de palabras, frases y párrafos en un texto.

#### 📥 Entrada esperada
(Párrafo ingresado por el usuario)

#### 📤 Salida esperada
```
Palabras: 45  
Frases: 3  
Párrafos: 2
```

#### ⚠️ Posibles errores

* No considerar saltos de línea como delimitadores de párrafo si no están bien escritos
* Errores en conteo si el texto no usa puntuación estándar (.,!?)
---

### 🛠 Requisitos

* Python 3.6 o superior
* No se requieren módulos externos (excepto `string`, que es estándar)
---
