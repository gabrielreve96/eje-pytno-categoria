"""
Escribir un programa que solicite al usuario la base y la altura de un triángulo, y calcule y muestre su área.
"""

b = input("Ingrese la base del triángulo: ")
a = input("Ingrese la altura del triángulo: ")

def calculo_area(b, a):
    try:
        base = int(b)
        altura = int(a)
        print("La base y la altura son enteros:", b, a)
        return base * altura
    except ValueError:
        try:
            base = float(b)
            altura = float(a)
            print("La base y la altura son flotantes:", b, a)
            return base * altura
        except ValueError:
            print("Los números ingresados no son válidos")

print(calculo_area(b, a))
