""" Home task calculator module """


class Calculator:
    """ Calculator implementation """
    def add(self, x: int, y: int) -> int:
        """ Add two attributes to each other """
        return x+y

    def subtract(self, x: int, y: int) -> int:
        """ Subtract one attribute from another """
        return x-y

    def divide(self, x: int, y: int) -> float:
        """ Divide x attribute on y """
        return x/y

    def multiply(self, x: int, y: int) -> int:
        """ Multiply x attribute on y """
        return x*y

    def mod(self, x: int, y: int) -> int:
        """ Take mod of one attribute from another """
        return x%y

    def power(self, x: int, y: int) -> int:
        """ Raise attributes x to a power y """
        return x**y

    def root(self, x: int) -> float:
        """ Take a root from attributes """
        return x**(1/float(2))
