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
__version__ = "0.1.2"
__autora__ = "Samira Cavalcanti"
__license__ = "Unlicense" 

import os 

current_language = os.getenv("LANG", "pt_BR")[:5]


msg = {
    "pt_BR": "Olá, Mundo !",
    "fr_FR": "Bonjour, le monde !",
    "ko_KR": "안녕하세요, 세상!",
    "es_SP": "Hola, Mundo!",
    "it_IT": "Ciao, Mundo!"
}
print(msg.get(current_language, "Hello, World!"))

