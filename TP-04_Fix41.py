'''Elaborar um algoritmo (programa) que calcule o valor fatorial de um número inteiro positivo.
Utilize a estrutura de controle for ...in .
Cálculo do fatorial, exemplo: fatorial de 5 = 5!=1x2x3x4x5= 120
'''

identificador = "Nome: Guilherme Yoshihara RA: T236JC1"
n1 = int(float(input("digite um numero inteiro: ")))
n2 = str(n1)
resultado = 1

for n in range(1, n1):
    resultado = (resultado * n1)
    n1 = n1 - 1

print(identificador)
print(f"O resultado de " + n2 + "! é: " + str(resultado))