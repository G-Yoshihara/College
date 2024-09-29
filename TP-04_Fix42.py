'''
Elaborar um algoritmo (programa) que leia as notas de 5 alunos e retorne a maior nota da turma.
Utilize a estrutura de controle while
'''
identificador = "Nome: Guilherme Yoshihara RA: T236JC1"

x = 1 #contador de alunos da condição
y = 2 #contador de alunos que aparece no texto
z = 1 #contador de qual aluno tem a maior nota
lista_notas = [] #lista para guardar as notas de todos os alunos para futuros calculos
nota = float(input("insira a nota do 1º aluno: \n"))
lista_notas.append(nota)

while x<5:
    print("insira a nota do " + str(y) + "º aluno?")
    nova_nota = float(input(""))
    lista_notas.append(nova_nota)
    if nova_nota > nota:
        nota = nova_nota
        z = y
    x = x + 1
    y = y + 1

while input("deseja inserir a nota de um " + str(y) + "º aluno? (sim ou não)") == "sim":
    nova_nota = float(input("insira a nota do " + str(y) + "º aluno: "))
    lista_notas.append(nova_nota)
    if nova_nota > nota:
        nota = nova_nota
        z = y
    y = y + 1

print(identificador)
print(f"A maior nota da turma é " + str(nota) + " e é do " + str(z) + "º aluno")

if input("Deseja saber a menor nota também? (sim ou não)") == "sim":
    print(f"A menor nota é " + str(min(lista_notas)))
