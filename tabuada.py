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



















         



