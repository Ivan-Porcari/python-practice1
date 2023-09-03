"""Conversiones Básicas"""


"""
Convertir los numeros de string a enteros y luego sumarlos.
"""

numero_01 = "123"
numero_02 = "456"
numero_03 = "789"
numero_04 = "132"

# Convertir los números de string a enteros
numero_01_entero = int(numero_01)
numero_02_entero = int(numero_02)
numero_03_entero = int(numero_03)
numero_04_entero = int(numero_04)

# Sumar los números enteros
suma_de_numeros = numero_01_entero + numero_02_entero + numero_03_entero + numero_04_entero

assert suma_de_numeros == 1500


"""
Convertir los numeros de enteros a string y luego concatenarlos.
"""

numero_01 = 123
numero_02 = 456
numero_03 = 789

# Convertir los números enteros a strings
numero_01_string = str(numero_01)
numero_02_string = str(numero_02)
numero_03_string = str(numero_03)

# Concatenar los strings
suma_de_numeros_string = numero_01_string + numero_02_string + numero_03_string

assert suma_de_numeros_string == "123456789"


"""
Convertir los numeros de binario, octal y hexadecimal a enteros y luego
multiplicarlos.
"""

numero_binario = "0b111010110101110111101000000"
numero_octal = "0o1425"
numero_hexadecimal = "0x6f540"

# Convertir los números a enteros
numero_binario_entero = int(numero_binario, 2)  # Base 2 para binario
numero_octal_entero = int(numero_octal, 8)      # Base 8 para octal
numero_hexadecimal_entero = int(numero_hexadecimal, 16)  # Base 16 para hexadecimal

# Multiplicar los números enteros
multiplicacion_de_numeros = numero_binario_entero * numero_octal_entero * numero_hexadecimal_entero

assert multiplicacion_de_numeros == 44397345600000000


"""
Convertir todo los numeros a enteros y luego restarlos secuencialmente (El uno
menos el dos menos el tres menos el cuatro).
"""

numero_01 = "987"
numero_02 = "0x6f54F"
numero_03 = "0o1234"
numero_04 = 654

numero_01_int = int(numero_01)
numero_02_int = int(numero_02, 16)
numero_03_int = int(numero_03, 8)
numero_04_int = int(numero_04)

resultado_resta = numero_01_int - numero_02_int - numero_03_int - numero_04_int

assert resultado_resta == -456350