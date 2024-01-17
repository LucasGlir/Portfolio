from TinyBankingSystem import Banco


class BancoRobusto(Banco):
    def __init__(self, nome, idade, genero):
        super().__init__(nome, idade, genero)

    def registro(self):
        nome = str(input("Faca o seu nome de usuario: "))
        idade = str(input("Qual sua idade: "))
        genero = str(input("Qual o seu genero: "))
        pin = str(input("Faca o seu PIN de 6 digitos: "))
        while len(pin) != 6:
            print("O PIN não possui 6 digitos")
            pin = str(input("Faca novamente o seu PIN de 6 digitos: "))
        self.nome = nome
        self.pin = pin
        print("O registro foi bem sucedido")
        print("Voce ja esta logado")

    def esqueceuPin(self):
        pinrecup = str(input("Faca o seu PIN de 6 digitos: "))
        while len(pin) != 6:
            print("O PIN não possui 6 digitos")
            pinrecup = str(input("Faca novamente o seu PIN de 6 digitos: "))
        print("O novo PIN foi registrado no sistema.")
        self.pin = pinrecup
    
    def login(self):
        nome = str(input("Digite o seu nome de usuario: "))
        pin = str(input("Digite o seu PIN: "))
        
        if self.nome == nome and self.pin == pin:
            print("Bem vindo ao OBS, ", self.nome)
        
        else:
            print("Nome ou PIN incorretos")
            escolha = int(input("1 - Tentar logar novamente\n2 - Esqueceu o PIN?\n3 - Fazer registro\n"))
            if escolha == 1:
                self.login()
            elif escolha == 2:
                self.esqueceuPin()
            elif escolha == 3:
                self.registro()
            else:
                print("Opcao invalida")
                self.login()
                