from funcoes import *

while True:

    print('''
                DADOS DOS ALUNOS

    Digite o número que indica a ação que deseja realizar.

    1. Adicionar aluno
    2. Remover aluno
    3. Atualizar aluno
    4. Ver lista de alunos
    5. Sair
''')
    escolha = int(input(""))

    if escolha == 1:
        AdicionarAluno()
    elif escolha == 2:
        RemoverAluno()
    elif escolha == 3:
        AtualizarAluno()
    elif escolha == 4:
        VerAlunos()
    elif escolha == 5:
        break
    else:
        print("Erro! Tente novamente.")
