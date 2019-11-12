#1- Criar classe carro (Marca, Modelo, Categoria, Ano)
#2- Criar uma pagina que realiza o cadastro do carro
#3- Salvar o cadastro em arquivo texto
#4- Criar tela que lista os carros cadastrados
#5- Criar logica que le a lista do arquivo texto

from flask import Flask, render_template, request
from carro import Carro
nome_pagina = 'Carro'
app = Flask(__name__)

@app.route('/')
def inicio():
    lista_carros = []
    with open('aula5/carros.txt', 'r') as arquivo:
        for l in arquivo:
            vetor = l.split(';')
            lista_carros.append(vetor)
    return render_template('indexx.html', nome = nome_pagina, lista = lista_carros)


@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastro_carros.html', nome = nome_pagina)

@app.route('/salvar')
def salvar():
    marca = request.args['marca']
    modelo = request.args['modelo'] 
    categoria = request.args['categoria']
    ano = request.args['ano']
    with open('aula5/carros.txt', 'a') as arq:
        arq.write(f'{marca};{modelo};{categoria};{ano}\n')
    return 'Cadastro efetuado com sucesso!'


app.run(debug=True)
