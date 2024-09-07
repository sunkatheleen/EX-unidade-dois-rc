#Exercícios

#SeleçãoSimples

#Exercício de fixação 1: Crie um programa que pergunte a idade do usuário. Caso seja maior
#de idade, deve mostrar uma mensagem informando que pode se inscrever para fazer o teste
#para tirar a carteira de motorista.

idade = int(input("Insira a sua idade:"))
if idade >= 18:
    print("Você pode se inscrever para o exame da carteira de motorista, siga os próximos passos.")


#Exercício de fixação 2: Crie um programa que pergunte o nome do cliente para ser inserido
#em um cartão de crédito, com espaço máximo de 20 caracteres. Caso o usuário informe um
#nome maior, deve mostrar uma mensagem informando que o nome é extenso demais e deve ser
#abreviado. Dica: para saber o tamanho de uma string, usar a função len. Exemplo: len(nome)

nome = input("Qual é o nome a ser inserido no cartão de crédito? ")
if len(nome) > 20:
    print("O nome é muito extenso, por favor abrevie")


#SeleçãoComposta

#Exercício de fixação 3: Crie um programa que solicite um número ao usuário e informe se é par ou ímpar. Dica: para
#saber se um número é par ou ímpar, calcular o resto da divisão desse número por 2
#(operador %). Se o resultado for 0, o número será par; se for 1, será ímpar.

numero = int(input("Insira um número:"))
if numero % 2 == 1 :
  print("O número que você inseriu é ímpar")

else:
    print("O número que você escolheu é par.")

#Correção do exercício
#No Python, o operador de igualdade é ==, e não = =.
#Na estrutura condicional else, você não precisa verificar novamente se o número é par, já
#que ele será par se não for ímpar.


#Exercício de fixação 4: Crie um programa que solicite ao usuário o seu salário. Se o valor
#for inferior a R$ 5.000, calcule um abono de fim de ano de 15%. Caso contrário, o abono
#será de 10%. Informe ao usuário seu valor de abono de fim de ano.


salario = float(input("Insira o seu salário:"))
if salario < 5000:
    abono = 0.15 * salario
    salarioFinal = salario + abono
    print(f"O seu abono de fim de ano em 2024 é de:{abono}" "E o seu salário final é de: ", salarioFinal )

else:
    abono2 = 0.10 * salario
    salarioFinal = salario + abono2
    print(f"O seu abono de fim de ano em 2024 é de:{abono2}" "E o seu salário final é de: ", salarioFinal )


#SeleçãoEncadeada

#Exercício de fixação 5:
#Crie um programa que pergunte ao usuário em que turno trabalha. Formato da entrada: M – manhã, T – tarde ou N – noite. Mostre a mensagem “Bom dia!”, “Boa tarde!”
#, “Boa noite!” ou “Valor inválido!”, conforme o caso.

turno = input("Insira o turno em que você trabalha: M - manhã, T - Tarde ou N - noite")

if turno == "M":
    print("Bom dia!")
elif turno == "T":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor inválido.")


#Exercício de fixação 6:
#Crie um programa que solicite ao usuário dois números e a operação que deseja executar entre eles. Mostre o resultado dessa operação no formato:
#num1 op num2 = resultado.

num1 = int(input("Digite um número:"))
num2 = int(input("Digite outro número:"))
operacao = input("Qual operação matemática você deseja realizar entre eles? (adição, subtração, multiplicação ou divisão)")

if operacao == "adição":
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")
elif operacao == "subtração":
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")
elif operacao == "multiplicação":
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")
elif operacao == "divisão":
    resultado = num1 / num2
    print(f"{num1} / {num2} = {resultado}")
else:
    print("Operação inválida.")


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