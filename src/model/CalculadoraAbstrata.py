class CalculadoraAbstrata:
    operations = {
        "SOMA": "mais",
        "SUBTRACAO": "menos",
        "MULTIPLICACAO": "vezes",
        "DIVISAO": "dividido por",
        "POTENCIA": "elevado a"
    }

    def __init__(self, operation):
        self.operation = operation
        
    def parse(self):
        return self.executeOperation()

    def extractNumbers(self):
        numbers = []
        operationSplitted = self.operation.split(' ')
        for string in operationSplitted:
            if (str(string).lstrip("-").isdigit()): numbers.append(int(string))
        return numbers

    def executeOperation(self):
        numbers = self.extractNumbers()
        if self.operations["SOMA"] in self.operation: return self.sum(numbers)
        if self.operations["SUBTRACAO"] in self.operation: return self.subtract(numbers)
        if self.operations["MULTIPLICACAO"] in self.operation: return self.multiply(numbers)
        if self.operations["DIVISAO"] in self.operation: return self.divide(numbers)
        if self.operations["POTENCIA"] in self.operation: return self.pow(numbers)
        return None


    def sum(self, numbers: int):
        return sum(numbers)
    
    def subtract(self, numbers):
        return numbers[0] - numbers[1]
    
    def multiply(self, numbers):
        return numbers[0] * numbers[1]
    
    def divide(self, numbers):
        if (numbers[1] == 0): raise ValueError("Não pode dividir um número por 0!")
        return numbers[0] / numbers[1]
    
    def pow(self, numbers):

        if (numbers[0] == 0 and numbers[1] <= 0): raise ValueError("Não pode elevar 0 por um número igual ou menor que 0!")
        return numbers[0] ** numbers[1]

