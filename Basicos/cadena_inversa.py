"""
Escribir un programa que solicite al usuario una cadena y muestre su inversa.
"""

cadena = input("Ingrese una cadena:  " )

if isinstance(cadena,str):
    inversa = cadena[::-1]
    print(f"la cade inversa es  {inversa}")
else:
    print("cadena no valida")
  