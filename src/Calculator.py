from Addition import addition
from Subtraction import subtraction
from Multiplication import multiplication
from Division import division
from SquareRoot import square_root
from Square import square



class Calculator:

    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square_root(self, a):
        self.result = square_root(a);
        return self.result;

    def square(self, a):
        self.result = square(a)
        return self.result