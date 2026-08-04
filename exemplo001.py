CONSTANTE_BONUS = 1000

nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))
porcentagemBonus = float(input("Digite a porcentagem do bônus: "))/100

valorBonus  = (salario * porcentagemBonus) + CONSTANTE_BONUS

print(f"Parabéns {nome}, seu salário é de R${salario:.2f} e você recebeu um bônus de R${valorBonus:.2f}!")