class Calculator:
    
    def __init__(self,input):
            self.expression = self.formatFunction(input).split()
            self.stack = []
            self.postfix = []
            self.solution = 0
    
    def formatFunction(self,input):
            input = input.replace("/",' / ')
            input = input.replace("*",' * ')
            input = input.replace("+",' + ')
            input = input.replace("-",' - ')
            input = input.replace("(",' ( ')
            input = input.replace(")",' ) ')
            return input
        
    def getPrecedence(self, var):
        if var.isnumeric():
            x = 0
        if var == '+' or var == '-':
            x = 1
        elif var == '*' or var == '/':
            x = 2
        return x
    
    def stackOperation(self, x):
        if not self.stack:
            self.stack.append(x)
        else:
            precedence1 = self.getPrecedence(x)
            precedence2 = self.getPrecedence(self.stack[-1])
            if precedence1 > precedence2:
                self.stack.append(x)
            else:
                self.postfix.append(self.stack.pop())
                self.stackOperation(x)
    
    def postfixConvertor(self):
            for var in self.expression:
                if var != '+' and var != '-' and var != '*' and var != '/' :
                    self.postfix.append(var)
                else:
                    self.stackOperation(var)
                
            while self.stack:
                   self.postfix.append(self.stack.pop())
                    
    def performOperations(self):
        operator = self.stack.pop()
        operand1 = self.stack.pop()
        operand2 = self.stack.pop()
        if operator == '/':
            result = float(operand2) / float(operand1)
        elif operator == '*':
            result = float(operand2) * float(operand1)
        elif operator == '+':
            result = float(operand2) + float(operand1)
        elif operator == '-':
            result = float(operand2) - float(operand1)
        self.stack.append(result)
                    
    def postfixSolver(self):
        self.stack = []
        length = len(self.postfix)
        for i in range( 0, length ):
            precedence = self.getPrecedence(self.postfix[i])
            self.stack.append(self.postfix[i])
            if precedence != 0:            
                self.solution = self.performOperations()
                
    def calculate(self):
        self.postfixConvertor()
        self.postfixSolver()
        self.solution = self.stack.pop()
            
        
        '''
expression = input("Enter expression: ")
obj = Calculator(expression)
obj.calculate()
print(obj.solution)
'''
