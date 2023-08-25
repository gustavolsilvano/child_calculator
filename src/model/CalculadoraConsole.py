from src.model.CalculadoraAbstrata import CalculadoraAbstrata

class CalculadoraConsole(CalculadoraAbstrata):
    def __init__(self, operation, print):
        super().__init__(operation)
        self.print = print

    def parse(self):
        try:
            result = super().parse()
            if (result == None): self.print('tente novamente\n')
            if (result != None): self.print(f'Resultado de {self.operation} é {result}\n')
        except ValueError as e:
            self.print(str(e) + "\n")