#!/usr/bin/env python3

""" Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequenta cada uma das atividades.

__version__ = "0.1.0"
"""

#Dados
sala1 = [ "Erik", "Maia", "Gustavo", "Manoel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio","Carlos","Maria","Isolda"]



aula_musica = ["Erik", "Carlos", "Maria"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]

aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Música",aula_musica),
    ("Inglês", aula_ingles),
    ("Dança", aula_danca)
]

# Listar alunos em cada atividade por sala
 
for nome_atividade, atividade in atividades:
    
    print(f"Alunos da atividade {nome_atividade}")
    print( "-" * 50)

    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
    
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)
    print("Sala 1", atividade_sala1)
    print("Sala 2", atividade_sala2)
    
    print()
    print("#" * 50)

