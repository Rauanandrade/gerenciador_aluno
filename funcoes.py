aluno = {}

def AdicionarAluno():
    nomealuno = input("Adicione o nome do aluno: ")
    matricula = int(input("Digite o número de matricula: "))
    aluno[matricula] = nomealuno
    print(aluno)

def RemoverAluno():
    removeAluno = int(input("Digite o número de matricula do aluno para remover: "))
    aluno.pop(removeAluno)
    print(aluno)

def AtualizarAluno():
    matricula = int(input("Digite o número de matrícula do aluno a ser atualizado: "))
    if matricula in aluno:
        novo_nome = input("Digite o novo nome do aluno: ")
        aluno[matricula] = novo_nome
        print(f"Nome do aluno atualizado para: {novo_nome} - Matrícula: {matricula}")
    else:
        print("Aluno não encontrado.")
    print(aluno)

def VerAlunos():
    print(aluno)

