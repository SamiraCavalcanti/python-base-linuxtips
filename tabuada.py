#!/usr/bin/env  python3


""" Imprime a tabuada de 1 ao 10."""

__version__ ="0.1.1"
__autora__ ="Samira Cavalcanti"


numeros = list(range(1,11))



for num1 in numeros:
    print("{:-^20}".format(f"Tabuada do {num1}"))

    print()
    for num2 in numeros:
        resultado = num1 + num2
        print("{:^20}".format( f"{num1:>2} x {num2:>2} = {resultado:>3}"))

print()
"""Imprime a Tabuada do 1 ao 10."""

__version__ = "0.1.0"
__autora__ = "Samira Cavalcanti"

#base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))
# para cada numero que está em numeros:
for numero in numeros:
    print("Tabuada do: ", numero)
    for outro_numero in numeros:
        print( numero  * outro_numero)
    print("------------")






         



