from faker import Faker
from datetime import datetime
from random import randint

fake = Faker(locale='pt-br')

for i in range(2,205):
    id = i
    nome_full = fake.name()
    nome = nome_full.split()
    email = nome[0] + '@email.com'
    data_criacao = datetime.now().strftime('%d/%m/%Y')
    categoria_id = randint(1,4)
    telefone = fake.phone_number()
    descricao = fake.sentence()

    print(f"INSERT INTO contatos_contato (id, nome, telefone, email, data_criacao, descricao, categoria_id)" 
         f"VALUES ('{id}', '{nome_full}', '{telefone}', '{email}', '{data_criacao}', '{descricao}', '{categoria_id}');")
