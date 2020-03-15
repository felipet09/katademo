from unittest import TestCase

import calculadora
class CalcauladoraTest(TestCase):
    def test_sumar(self):
        self.assertequal(calculadora.sumar(""),0,"Cadena vacia")
