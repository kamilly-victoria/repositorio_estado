import subprocess
from estado import Estado

def estado():
 while True:
    subprocess.run("cls", shell=True)
    print("## MENU ##")
    print("1. Cadastrar Estado")
    print("2. Listar Estados")
    print("3. Atualizar Estado")
    print("4. Excluir Estado")
    print("0. Sair")
    opcao = int(input("=> "))
    subprocess.run("cls", shell=True)

    if opcao == 0:
        break
    elif opcao == 1: 
        print(" ## Cadastro de Estado ##")
        estado = Estado ("Nome: ")
        estado.nome = input("Sigla: ")

        estado.salvar()

    elif opcao == 2:
        print("## Estados cadastrados ##")
    
        # Cria uma instância da classe Estado e chama o método listar() para obter todos os estados.
        estado = Estado()

        # Chama o método listar() da instância de Estado para obter todos os estados cadastrados no banco de dados.
        for e in estado.listar():
            print(f"ID: {e['id']}, Nome: {e['nome']}, Sigla: {e['sigla']}")


    elif opcao == 3:
        print("## Atualizar Estado ##")

        # Cria uma instância da classe Estado e solicita ao usuário o ID e os novos dados.
        estado = Estado()
        estado.id = int(input("ID do estado: "))
        estado.nome = input("Novo nome: ")
        estado.sigla = input("Nova sigla: ")

        # Chama o método atualizar() da instância de Estado para atualizar os dados.
        estado.atualizar()

    elif opcao == 4:
        print("## Excluir Estado ##")

        # Cria uma instância da classe Estado e solicita ao usuário o ID do estado a ser excluído.
        estado = Estado()
        estado.id = int(input("ID do estado: "))

        # Chama o método excluir() da instância de Estado para remover o registro do banco de dados.
        estado.excluir()

    else:
     print("Opção inválida.")

    subprocess.run("pause > nul", shell=True)