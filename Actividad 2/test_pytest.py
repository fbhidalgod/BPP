import pytest

class tipo_de_datos(Exception):
    pass

class Operaciones:
    def __init__(self,x=0,y=0):
        self.num1 = x
        self.num2 = y
        self.resultado = 0

    def suma(self):
        self.resultado = self.num1+self.num2

    def resta(self):
        self.resultado = self.num1-self.num2

    def multiplicacion(self):
        self.resultado = self.num1*self.num2

    def division(self):
        self.resultado = self.num1/self.num2

def test_suma():
    op = Operaciones(4,6)
    op.suma()
    assert op.resultado == 10

def test_resta():
    op = Operaciones(17,9)
    op.resta()
    assert op.resultado == 8

def test_multiplicacion():
    op = Operaciones(2,7)
    op.multiplicacion()
    assert op.resultado == 14


def test_division():
    op = Operaciones(6,3)
    op.division()
    assert op.resultado == 2

def test_tipo_de_datos():
    op = Operaciones(6,5)
    if not isinstance(op.num1, int) and not isinstance(op.num2, int):
        with pytest.raises(tipo_de_datos):
            op.suma()
