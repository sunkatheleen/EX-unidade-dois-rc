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