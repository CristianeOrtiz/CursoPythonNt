# =========== Classe ============

class Endereco:
    logradouro = ''
    numero = ''
    complemento = ''
    bairro = ''
    cidade = ''
    cep = ''
<<<<<<< HEAD
=======
    
>>>>>>> 1cacb642048ce01c80907287f44f946c81119424
    def cadastrar_endereco(self):
        self.logradouro = input('Digite seu logradouro:')
        self.numero = input('Digite seu numero:')
        self.complemento = input('Digite seu complemento:')
        self.bairro = input('Digite seu bairro:')
        self.cidade = input('Digite sua cidade:')
        self.cep = input('Digite seu cep:')
        endereco = f'Logradouro{self.logradouro} \n Numero:{self.numero} \n Complemento: {self.complemento} \n Bairro:{self.bairro} \n Cidade: {self.cidade} \n Cep:{self.cep}'
        return endereco










# ============== Métodos =======================


# def cadastrar_endereco():
#     logradouro = input('Digite seu logradouro:')
#     numero = input('Digite seu numero:')
#     complemento = input('Digite seu complemento:')
#     bairro = input('Digite seu bairro:')
#     cidade = input('Digite sua cidade:')
#     cep = input('Digite seu cep:')
#     endereco = f'Logradouro{logradouro} \n Numero:{numero} \n Complemento: {complemento} \n Bairro:{bairro} \n Cidade: {cidade} \n Cep:{cep}'
#     return endereco