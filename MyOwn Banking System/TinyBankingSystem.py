#parent class
class Usuario():
	def __init__(self, n, i, g):
		self.nome = n
		self.idade = i
		self.genero = g
	
	def show_details(self):
		print("Dados pessoais")
		print("")
		print("  Nome:", self.nome)
		print(" Idade:", self.idade)
		print("Genero:", self.genero) 
		
        
#child class
class Banco(Usuario):
    def __init__(self, n, i, g):
        super().__init__(n, i, g)
        self.conta_corrente = 0
    def deposito(self,qtd):
        self.quantidade = qtd
        self.conta_corrente = self.conta_corrente + self.quantidade
        print("O valor foi depositado")
    def saque(self, qtd):
        self.quantidade = qtd
        if self.quantidade > self.conta_corrente:
            print("Fundo insuficiente")
            print("Valor disponivel: R$", self.conta_corrente)
        else:
            self.conta_corrente = self.conta_corrente - self.quantidade
            print("O valor foi sacado")
    def mostrar_conta_corrente(self):
        print("Valor na conta corrente: R$",self.conta_corrente)
    def mostrar_todos_os_dados(self):
        self.show_details()
        self.mostrar_conta_corrente()
        
