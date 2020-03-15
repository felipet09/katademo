from unittest import TestCase

from calculadora import Calculadora


class CalculadoraTest(TestCase):
    def test_sumar(self):
        c = Calculadora()
        self.assertEqual(c.sumar(""), 0, "Cadena vacia")

    def test_sumar_unaCadena(self):
        c = Calculadora()
        self.assertEqual(c.sumar("1"), 1, "Un numero")

    def test_sumar_cadenaConUnNumero(self):
        c = Calculadora()
        self.assertEqual(c.sumar("1"), 1, "Un numero")
        self.assertEqual(c.sumar("2"), 2, "Un numero")

    def test_sumar_cadenaConDosNumeros(self):
        c = Calculadora()
        self.assertEqual(c.sumar("1,3"), 4, "Dos numeros")

    def test_sumar_cadenaConMultiplesNumeros(self):
        c = Calculadora()
        self.assertEqual(c.sumar("5,2,4,1"), 12, "Multiples numeros")