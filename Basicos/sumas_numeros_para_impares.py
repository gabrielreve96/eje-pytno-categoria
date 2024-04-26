"""
Suma de números pares e impares: Escribe un programa que sume todos los números pares e impares en un rango dado por el usuario.
"""

print("=======================numeros para impares======================")


def sumar_pares_impares(rango):
    suma_pares = 0
    suma_impares = 0

    for i in range(1, rango + 1):
        if i % 2 == 0:
            suma_pares += i
        else:
            suma_impares += i
    
    return suma_pares, suma_impares

# Solicitar al usuario que ingrese el rango
rango = int(input("Ingrese el número máximo del rango: "))

# Llamar a la función para sumar pares e impares
suma_pares, suma_impares = sumar_pares_impares(rango)

# Mostrar los resultados
print("La suma de los números pares es:", suma_pares)
print("La suma de los números impares es:", suma_impares)
