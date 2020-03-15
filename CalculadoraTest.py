from unittest import TestCase

from calculadora import Calculadora


class CalculadoraTest(TestCase):
    def test_sumar(self):
        c = Calculadora()
        self.assertEqual(c.sumar(""), 0, "Cadena vacia")

