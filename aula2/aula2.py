from pessoa import Pessoa
from endereco import Endereco

# print('='*50)
# print('\n'*2)

# nome = input('Digite seu nome:')

# print(nome)

# print('\n'*2)##### Pular linha ##########
# print('='*50)


# -------Criação de variaveis ---------------------------------------------------------------------------------


# print('='*50)
# print('\n'*2)

# nome = 'Cris'
# print(nome)
# nome = 10
# print(nome)


# print('\n'*2)
# print('='*50)

# ----------Format---------------------------------------------------------------------

# print('='*50)
# print('\n'*2)

# nome = input('Digite seu nome:')
# sobrenome = input('Digite seu sobrenome:')
# data_nascimento = input('Digite a data de nascimento:')
# email = input('Digite seu e-mail:')
# senha = input('Digite sua senha:')


# print(f'Nome: {nome}\n Sobrenome: {sobrenome}\n DtNas: {data_nascimento}\n E-mail: {email}\n Senha: {senha}')

# print('\n'*2)
# print('='*50)

# --------------------------------------------------------------------------

print('='*50)
print('\n'*2)

pessoa = Pessoa() #variavel 
endereco = Endereco()
pessoa.cadastrar_pessoa()
endereco.cadastrar_endereco()

print(pessoa.nome)
print(endereco.logradouro)

print(pessoa.cadastrar_pessoa())
print(endereco.cadastrar_endereco())


print('\n'*2)
print('='*50) 


# print(f'Nome: {nome}\n Sobrenome: {sobrenome}\n DtNas: {data_nascimento}\n E-mail: {email}\n Senha: {senha}')


# print(pessoa.cadastrar_pessoa()) #Imprimindo os métodos