'''Desenvolva um programa para determinar a média geral do aluno. O mesmo deverá receber o nome do
aluno, as 2 notas obtidas do aluno nas 2 avaliações. Calcular a média de aproveitamento, usando a
fórmula da Media e escrever o conceito do aluno de acordo com a tabela de conceitos.
Média é dada pela fórmula:
MG = (NP1*4 + NP2*6) / 10
'''

identificador = "Nome: Guilherme Yoshihara RA: T236JC1"

nome = str(input("Digite seu nome por favor: "))
validacao_np1 = False
validacao_np2 = False

while validacao_np1 == False:
    np1 = float(input("Digite a sua nota da NP1: "))
    if np1 <= 10:
        validacao_np1 = True
    else:
        print("Valor de nota invalido. Favor conferir e inserir o valor novamente.")

while validacao_np2 == False:
    np2 = float(input("Digite sua segunda nota da NP2: "))
    if np2 <= 10:
        validacao_np2 = True
    else:
        print("Valor de nota invalido. Favor conferir e inserir o valor novamente.")
        
media_geral = ((np1 * 4) + (np2 * 6)) / 10

print(identificador)

if media_geral >= 9 and media_geral <=10:
    print(f"Parabéns, {nome}, com uma {media_geral:.2f}, você foi APROVADO com conceito A!")
elif media_geral >= 7 and media_geral < 9:
    print(f"Parabéns, {nome}, com uma {media_geral:.2f}, você foi APROVADO com conceito B!")
elif media_geral >= 3 and media_geral < 7:
    print(f"{nome}, com uma {media_geral:.2f}, você ficou com conceito C e está de EXAME!")
elif media_geral >= 0 and media_geral < 3:
    print(f"{nome}, com uma {media_geral:.2f}, você ficou com conceito D está de DP!")