from unittest import TestCase

from calculadora import Calculadora


class CalculadoraTest(TestCase):
    def test_sumar(self):
        c = Calculadora()
        self.assertEqual(c.sumar(""), 0, "Cadena vacia")

    def test_sumar_unacadena(self):
        x = Calculadora()
        self.assertEqual(x.sumar("1"), 1, "Un numero")

