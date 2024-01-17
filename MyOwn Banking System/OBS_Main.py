from OnlineBankingSystem import BancoRobusto

def main():
    usuario = BancoRobusto(" ",0," ")
    print("Bem vindo ao sistema OBS\n")
    escolha = int(input("1 - Login\n2 - Fazer registro\n"))
    usuario.login() if escolha == 1 else usuario.registro()
    while(True):
        escolha = int(input("\nEscolha o que deseja fazer:\n1 - Deposito\n2 - Saque\n3 - Mostrar conta a conta corrente\n4 - Mostrar todos os dados\n5 - Fechar aplicativo\n"))
        if escolha == 1:
            quantia = int(input("Quanto deseja depositar: "))
            usuario.deposito(quantia)
        elif escolha == 2:
            quantia = int(input("Quanto deseja sacar: "))
            usuario.saque(quantia)
        elif escolha == 3:
            usuario.mostrar_conta_corrente()
        elif escolha == 4:
            usuario.mostrar_todos_os_dados()
        elif escolha == 5:
            break
        else:
            print("Opcao invalida")
    

if __name__ == '__main__':
    main()