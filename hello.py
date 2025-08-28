#!/usr/bin/env python3

"""Hello World Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:
    
Tenha a variável LANG devidamente configurada ex:
    export LANG=pt_BR

Execução:

    python3 hello.py
    ou 
    ./hello.py

"""
__version__ = "0.0.1"
__autor__ = "Samira Cavalcanti"
__license__ = "Unlicense" 

import os 

current_language = os.getenv("LANG", "pt_BR")[:5]


msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo !"
elif current_language == "fr_FR":
    msg = "Bonjour, le monde !"
elif current_language == "ko_KR":
    msg = "안녕하세요, 세상!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mundo!"
  

print(msg)

