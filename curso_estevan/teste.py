nome = input("Qual é o seu nome? ")
print("Olá, ", nome)
idade = input("Qual sua idade? ")
print(idade)



def processar_presenca(status_presenca):
    if(status_presenca == 'pp') or (status_presenca == 'presente'):
        return True
    return False

status_presenca = input("Esta presente? ")

resposta_presenca = input('Status de Presença: ')

print(f'nome: {nome}, idade: {idade}, Presenca:{resposta_presenca}')

