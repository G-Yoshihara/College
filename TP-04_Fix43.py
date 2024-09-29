'''Elaborar um algoritmo (programa) que determine se a pessoa está com no seu Peso Ideal (ou
não) e IMC.
Onde o usuário deverá digitar o peso, o sexo e a altura de uma determinada pessoa. Após a execução,
deverá exibir se esta pessoa está ou não com seu peso ideal. Veja tabela (a) e (b) da relação
peso/altura².
Incluir uma mensagem na qual deverá aparecer o seu nome, RA e turma antes do resultado final, depois
faça um (print screen) e comentar o(s) resultado(s) do programa após a execução do mesmo.'''

identificador = "Nome: Guilherme Yoshihara RA: T236JC1"

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso /(altura * altura)

validação_sexo = False

while validação_sexo == False:
    sexo = str(input("Qual é o seu sexo? (m/f): "))
    if sexo == "m":
        sexo = "masculino"
        validação_sexo = True
    elif sexo == "M":
        sexo = "masculino"
        validação_sexo = True
    elif sexo == "masculino":
        sexo = "masculino"
        validação_sexo = True
    elif sexo == "Masculino":
        sexo = "masculino"
        validação_sexo = True
    elif sexo == "f":
        sexo = "feminino"
        validação_sexo = True
    elif sexo == "F":
        sexo = "feminino"
        validação_sexo = True
    elif sexo == "feminino":
        sexo = "feminino"
        validação_sexo = True
    elif sexo == "Feminino":
        sexo = "feminino"
        validação_sexo = True
    else:
        print("Por favor, informe um sexo válido.")

print(identificador)

if sexo == "feminino":
    if imc < 19:
        print(f"O seu IMC é: {imc:.2f}")
        print(f"Para o sexo {sexo}, vc está abaixo do peso!")
    elif imc > 19 and imc < 24:
        print(f"O seu IMC é: {imc:.2f}")
        print(f"Para o {sexo}, vc está no peso ideal!")
    elif imc >= 24:
        print(f"O seu IMC é: {imc:.2f}")
        print(f"Para o sexo {sexo}, vc está acima do peso!")

elif sexo == "masculino":
    if imc < 20:
        print(f"O seu IMC é: {imc:.2f}")
        print(f"Para o sexo {sexo}, vc está abaixo do peso!")
    elif imc > 20 and imc < 25:
        print(f"O seu IMC é: {imc:.2f}")
        print(f"Para o sexo {sexo}, vc está no peso ideal!")
    elif imc >= 25:
        print(f"O seu IMC é: {imc:.2f}")
        print(f"Para o sexo {sexo}, vc está acima do peso!")