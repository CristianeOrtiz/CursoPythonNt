# abertura do arquivo texto para gravação 
arquivo = open('alunos.txt', 'a')
arquivo.write('Junior \n')

# ------------------------------------------------------------------

# abertura do arquivo texto para leitura
arquivo = open('alunos.txt', 'r')
for d in arquivo:
    print (d)
arquivo.close()

# ---------------------------------------------------------------------

# abertura do arquivo para gravação com fechamento automatico
with open('alunos.txt', 'a') as arquivo:
    arquivo.write('testanto fechamento automatico \n')

