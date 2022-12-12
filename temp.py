class Kalkulator:

    def add(self, number1, number2):
        return number1 + number2

    def subs(self, number1, number2):
        return number1 - number2

    def multiply(self, number1, number2):
        return number1 * number2

    def divide(self, number1, number2):
        if number2 == 0:
            return 0
        return number1 / number2

    def calc(self,number1, number2, sign):
        if sign == '+':
            result = self.add(number1,number2)
        elif sign == '-':
            result = self.subs(number1,number2)
        elif sign == '*':
            result = self.multiply(number1,number2)
        elif sign == '/':
            result = self.divide(number1,number2)
        else:
            result = None
        return result

