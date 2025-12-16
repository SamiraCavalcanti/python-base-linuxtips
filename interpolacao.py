#!/usr/bin/env python3

email_tmpl = """
Olá, %(nome)s

Tem interesse em adquirir um dos nossos cursos:
%(cursos)s?

Clique no link: %(link)s

Temos uma oferta imperdível no valor de R$ %(valor).2f
"""

clientes = ["Samira", "Ana", "Carlos"]

for cliente in clientes:
    print(
        email_tmpl % {
            "nome": cliente,
            "cursos": "DevOps: Terraform, Kubernetes, Docker | Cloud: AWS, Azure",
            "link": "http://google.com.br",
            "valor": 450
        }
    )

