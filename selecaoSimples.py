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



