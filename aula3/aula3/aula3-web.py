from flask import Flask, render_template
from aluno import Aluno
from avaliacoes import Avaliacao

aluno1 = Aluno ( 'Junior', 'Sousa', '123', '1234')
aluno2 = Aluno ('Cris', 'Sousa', '122', '1234')


avaliacao = Avaliacao('06/11/2019', 'matematica', '9,0')
avaliacao2 = Avaliacao('05/11/2019', 'Fisica', '5')


app = Flask(__name__)

nome_pagina = 'Pagina do joca1000'
lista_teste = [aluno1, aluno2]
lista_avaliacao = [avaliacao, avaliacao2]



@app.route('/')
def inicio():
    return render_template('home.html', nome=nome_pagina, lista = lista_teste) #só existe dentro desse contexto

@app.route('/contato')
def contatos():
    return render_template('contato.html', nome=nome_pagina, lista = lista_avaliacao)

app.run(debug=True)