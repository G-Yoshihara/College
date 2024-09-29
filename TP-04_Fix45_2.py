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


inserir_aluno = True

while inserir_aluno == True:
    inserir_notas = True
    while inserir_notas == True:
    # calcular a média dos alunos
        aluno = input("Digite o nome do aluno: ")
        ra = input("Digite o RA do aluno: ")
        turma = input("Digite a turma do aluno: ")
        np1 = float(input("Digite a primeira nota do aluno: "))
        np2 = float(input("Digite a segunda nota do aluno: "))
        
        mg = ((np1 * 4) + (np2 * 6))/ 10
        
        print(f"Nome: {aluno}, RA: {ra}, Turma: {turma}, Média Final: {mg}")
        
        salvar = str(input("Salvar as informações? (s/n): "))
        if salvar == "s":
            #dados para salvar
            data = (f"Nome: {aluno}, RA: {ra}, Turma: {turma}, Média Final: {mg} \n")
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