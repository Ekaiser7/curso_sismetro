lista_notas = []
idade = int(input("qual a sua idade? "))
qtd_notas = int(input("Quantas notas você deseja inserir?(escreva as notas de 10 a 0) "))

if qtd_notas <= 0:
    print("A quantidade de notas deve ser maior que zero.")
else:
    soma_notas = 0

    for i in range(1, qtd_notas + 1):
        nota = float(input(f"Digite a nota {i}: "))
        lista_notas.append(nota)
        soma_notas += nota

    media = soma_notas / qtd_notas

    print(f"\nMédia final: {media:.2f}")

    if media >= 7.0:
        print("Situação: APROVADO(A)")
    else:
        print("Situação: REPROVADO(A)")

