#Operadores lógicos

#Exercício de fixação 7: Crie um programa que pergunte o tamanho de três lados de um triângulo e informe o tipo de triângulo, a saber:

#a) Só será um triângulo quando a soma de dois lados sempre for maior que o terceiro lado.
#b) Equilátero: triângulo com todos os lados iguais.
#c) Isósceles: triângulo com dois lados iguais.
#d) Escaleno: triângulo com todos os lados diferentes.

lado1 = float(input("Digite a medida do primeiro lado:"))
lado2 = float(input("Digite a medida do segundo lado:"))
lado3 = float(input("Digite a medida do terceiro lado:"))

if lado1 + lado2 < lado3 or lado2 + lado3 < lado1 or lado3 + lado1 < lado2:
    print("Estes lados não formam um triângulo.")

else:
    if lado1 == lado2 and lado1 == lado3:
        print("Seu triângulo é um equilátero.")

    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Seu triângulo é um isósceles.")

    else:
        print("Seu triângulo é um escaleno.")


# Exercício de fixação 8: Crie um programa que solicite ao usuário as quatro notas bimestrais de uma matéria e o número de faltas. Informe se o aluno foi aprovado
# ou reprovado, bem como o motivo, a saber:

#A média anual é 7.
#A disciplina possui 40 aulas.
#O mínimo exigido é 75% de presença.

materia = input("Digite a matéria que deseja saber seu status de aprovação:")
nota1 = float(input("Digite a nota do primeiro bimestre"))
nota2 = float(input("Digite a nota do segundo bimestre"))
nota3 = float(input("Digite a nota do terceiro bimestre"))
nota4 = float(input("Digite a nota do quarto bimestre"))
faltas = int(input("Digite o seu número de faltas"))

mediaDoAluno = (nota1 + nota2 + nota3 + nota4) / 4

porcentagemDePresencaDoAluno = ((40 - faltas) / 40) * 100

if mediaDoAluno >= 7 and porcentagemDePresencaDoAluno >= 75:
    print(f"Você foi aprovado em {materia}. média: {mediaDoAluno:.2f}, porcentagem de presença: {porcentagemDePresencaDoAluno:.2f}%")
elif mediaDoAluno < 7 and porcentagemDePresencaDoAluno >= 75:
    print(f"Voce foi reprovado por nota em {materia} :( média: {mediaDoAluno:.2f}, porcentagem de presença: {porcentagemDePresencaDoAluno:.2f}%")
else:
    print(f"Voce foi reprovado por falta e/ou nota em {materia} :( média: {mediaDoAluno:.2f}, porcentagem de presença: {porcentagemDePresencaDoAluno:.2f}%")