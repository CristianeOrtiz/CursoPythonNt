# =========== Classe ============


class Pessoa:
    def cadastrar_pessoa(self):    
        self.nome = input('Digite seu nome:')
        self.sobrenome = input('Digite seu sobrenome:')
        self.data_nascimento = input('Digite a data de nascimento:')
        self.email = input('Digite seu e-mail:')
        self.senha = input('Digite sua senha:')
        pessoa = f'Nome: {self.nome}\n Sobrenome: {self.sobrenome}\n DtNas: {self.data_nascimento}\n E-mail: {self.email}\n Senha: {self.senha}'
        return pessoa
















# ============== Métodos =======================



# def cadastrar_pessoa():    
#     nome = input('Digite seu nome:')
#     sobrenome = input('Digite seu sobrenome:')
#     data_nascimento = input('Digite a data de nascimento:')
#     email = input('Digite seu e-mail:')
#     senha = input('Digite sua senha:')
#     pessoa = f'Nome: {nome}\n Sobrenome: {sobrenome}\n DtNas: {data_nascimento}\n E-mail: {email}\n Senha: {senha}'
#     return pessoa
