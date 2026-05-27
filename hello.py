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
__version__ = "0.1.3"
__autora__ = "Samira Cavalcanti"
__license__ = "Unlicense" 

import os 
import sys 


arguments = {"lang": None, "count": 1}
for arg in sys.argv[1:]:
    # TODO: Tratar alueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit(1)
    arguments[key] = value



current_language = arguments["lang"]
if current_language is None:
    current_language = os.getenv("LANG")


current_language = current_language[:5]


msg = {
    "pt_BR": "Olá, Mundo!",
    "fr_FR": "Bonjour, le monde!",
    "ko_KR": "안녕하세요, 세상!",
    "es_SP": "Hola, Mundo!",
    "it_IT": "Ciao, Mundo!"
}
print(
    msg[current_language] * int(arguments["count"])
)



