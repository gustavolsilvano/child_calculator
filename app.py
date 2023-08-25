from src.model.CalculadoraConsole import CalculadoraConsole


def printMod(string, func):
    print(string)
    func(string)

print("""
    Bem-vindo/a à calculadora console!
        
    2 mais 2
    2 menos 4
    6 dividido por 2
    4 elevado a 2
    
    Escreva o seu cálculo com algum dos formatos acima
    Escreva "sair" para finalizar!
    
    """)

with open("teste.txt", "a") as file:
    while(True):
        userInput = input()
        if(userInput == "sair"): break
        CalculadoraConsole(userInput, lambda st: printMod(st, file.write)).parse()


