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