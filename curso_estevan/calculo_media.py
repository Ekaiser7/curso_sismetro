alunos = [
    {'nome': 'yasmin', 'notas': [7,7], 'idade': 16, 'faltas': 2},
    {'nome': 'rafael', 'notas': [8,9], 'idade': 16, 'faltas': 5},
    {'nome': 'eduardo', 'notas': [8,7], 'idade': 15, 'faltas': 10},
    {'nome': 'ana', 'notas': [8,8], 'idade': 15, 'faltas': 9},
]
def calcular_media(soma,qtde):
    return soma / qtde

def status_aprovacao(nota, faltas):
    if nota >= 7 and faltas < 10:
        return 'aprovado'
    return 'reprovado'

    
for aluno in alunos:
    qtde_notas =len(aluno['notas'])
    soma = sum(aluno['notas'])
    notas = calcular_media(soma, qtde_notas)
    faltas = aluno['faltas']
    print(f"aluno: {aluno['nome']}, nota: {notas}, status: {status_aprovacao(notas, faltas)}")

