'''Elabore um programa em Python que o usuário entre com seu e seu salário.
Se o salário for menor ou igual a R$1500,00 coloque um acréscimo de 20% de aumento.
Se for maior que R$1500,00 e menor que R$2500,00 o acréscimo será de 10%, senão o
acréscimo será de 5% para os demais valores.
'''

identificador = "Nome: Guilherme Yoshihara RA: T236JC1"
salario = float(input("Digite o seu salário: ")) # Entrada do salário do usuário 

if salario <= 1500:
    acrescimo = salario * 0.20
    novo_salario = salario + acrescimo
    print(identificador)
    print(f"Seu novo salário com acréscimo de 20% é: R${novo_salario:.2f}")
    
elif salario > 1500 and salario < 2500:
    acrescimo = salario * 0.10
    novo_salario = salario + acrescimo
    print(identificador)
    print(f"Seu novo salário com acréscimo de 10% é: R${novo_salario:.2f}")
    
elif salario > 2500:
    acrescimo = salario * 0.05
    novo_salario = salario + acrescimo
    print(identificador)
    print(f"Seu novo salário com acréscimo de 5% é: R${novo_salario:.2f}")