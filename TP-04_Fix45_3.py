'''Desenvolva um programa que só permita o acesso a pessoas autorizadas (professor, via
autenticação) para posteriormente realizar a média do aluno. Para isto Considere o programa
criado no Fix44.
Incluir uma mensagem na qual deverá aparecer o seu nome, RA e turma antes do resultado final, depois
faça um (print screen) e comentar o(s) resultado(s) do programa após a execução do mesmo.'''

identificador = "Nome: Guilherme Yoshihara RA: T236JC1"

# Dicionário com credenciais de acesso
acessopermitido = {"usuario": "GuilhermeY", "senha": "Fix45"}

# Solicitação de usuário e senha
acesso = False

while acesso == False:
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario == acessopermitido["usuario"] and senha == acessopermitido["senha"]:
        print(f"Acesso permitido! Bem-vindo, {usuario}.")
        acesso = True
    else:
        print(f"Acesso negado. Verifique usuário e senha.")

#inserir aluno
inserir_aluno = True

while inserir_aluno == True:
    inserir_notas = True
    while inserir_notas == True:
        # Inserir dados nome, ra e turma do aluno
        aluno = input("Digite o nome do aluno: ")
        ra = input("Digite o RA do aluno: ")
        turma = input("Digite a turma do aluno: ")

        #calcular media do aluno        
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
        
        mg = ((np1 * 4) + (np2 * 6)) / 10

        #conferencia de informações
        print(f"Nome: {aluno}, RA: {ra}, Turma: {turma}, Média Final: {mg:.2f}")
        
        salvar = str(input("As informações estão corretas? (s/n): "))
        if salvar == "s":
            #dados para salvar
            data = (f"Nome: {aluno}, RA: {ra}, Turma: {turma}, Média Final: {mg:.2f} \n")
            # Criar novo arquivo .txt
            salvar_notas = open("Notas_Alunos.txt","a")
            # Escrever dados no arquivo
            salvar_notas.write(data)

            #inserir novos alunos
            continuar = str(input("Deseja inserir novos alunos? (s/n): "))
            if continuar == "n":
                inserir_aluno = False
                inserir_notas = False
            else:
                print("Insira os dados do novo aluno:")
        else:
            print("Revise as informações")
#finalizar processos
print(identificador)
print("As informações foram salvas no arquivo Notas_Alunos.txt. Até a próxima.")