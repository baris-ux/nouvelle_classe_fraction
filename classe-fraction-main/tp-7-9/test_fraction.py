import unittest
from fraction import Fraction  # Remplacez par le nom réel du fichier contenant la classe

class TestFraction(unittest.TestCase):

    def test_constructor(self):
        # Test avec numérateur et dénominateur valides
        f = Fraction(6, 8)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 4)

        # Test avec numérateur négatif
        f = Fraction(-6, 8)
        self.assertEqual(f.numerator, -3)
        self.assertEqual(f.denominator, 4)

        # Test avec dénominateur négatif
        f = Fraction(6, -8)
        self.assertEqual(f.numerator, -3)
        self.assertEqual(f.denominator, 4)

        # Test avec dénominateur zéro
        with self.assertRaises(ValueError):
            Fraction(1, 0)

        # Test avec fraction réduite directement
        f = Fraction(3, 9)
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 3)

    def test_str(self):
        # Test de la représentation en chaîne
        self.assertEqual(str(Fraction(3, 4)), "3/4")
        self.assertEqual(str(Fraction(6, 3)), "2")
        self.assertEqual(str(Fraction(0, 1)), "0")

    def test_as_mixed_number(self):
        # Test de la conversion en nombre mixte
        self.assertEqual(Fraction(7, 3).as_mixed_number(), "2 1/3")
        self.assertEqual(Fraction(4, 2).as_mixed_number(), "2")
        self.assertEqual(Fraction(3, 1).as_mixed_number(), "3")
        self.assertEqual(Fraction(0, 5).as_mixed_number(), "0")

    def test_addition(self):
        # Test de l'addition
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertEqual(f1 + f2, Fraction(5, 6)) # (1 * 2) + (1 * 3) = 5/6

        self.assertEqual(Fraction(2, 3) + Fraction(1, 3), Fraction(1, 1)) 

    def test_subtraction(self):
        # Test de la soustraction
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 4)
        self.assertEqual(f1 - f2, Fraction(1, 2)) # on a 2/4 == 1/2 donc vrai

        # Test soustraction avec numérateur négatif
        self.assertEqual(Fraction(1, 4) - Fraction(3, 4), Fraction(-1, 2)) # on -2/4 == -1/2 encore vrai

    def test_multiplication(self):
        # Test de la multiplication
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        self.assertEqual(f1 * f2, Fraction(1, 2)) # ici on a 6/12 et comme 6/12 == 1/2 alors vraix

        # Test multiplication avec zéro
        self.assertEqual(Fraction(0, 1) * f1, Fraction(0, 1))

    def test_division(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 4)
        self.assertEqual(f1 / f2, Fraction(2, 1))

        # Test de la division par zéro
        with self.assertRaises(ZeroDivisionError):
            f1 / Fraction(0, 1)

    def test_equality(self):
        # Test d'égalité entre fractions
        self.assertEqual(Fraction(1, 2), Fraction(2, 4))
        self.assertNotEqual(Fraction(1, 2), Fraction(1, 3))
        self.assertEqual(Fraction(0, 1), Fraction(0, 5))

    def test_is_zero(self):
        # Test de la méthode is_zero
        self.assertTrue(Fraction(0, 1).is_zero()) # on a bien un 0 donc c'est ok
        self.assertFalse(Fraction(1, 2).is_zero()) # On s'attenda un false quand le numérateur n'est pas 0

    def test_is_integer(self):
        # Test de la méthode is_integer
        self.assertTrue(Fraction(4, 2).is_integer()) # on s'attend a un True puisque 4/2 donne 2 qui est un entier
        self.assertFalse(Fraction(3, 2).is_integer()) # on s'attend a un False puisque 3/2 donne un floatant 

    def test_is_proper(self):
        # Test de la méthode is_proper
        self.assertTrue(Fraction(1, 3).is_proper()) # on s'attend a un True car 1 est plus petit que 3 
        self.assertFalse(Fraction(3, 2).is_proper()) # on s'attend a un False car 3 est plus grand que 2

    def test_is_unit(self):
        # Test de la méthode is_unit
        self.assertTrue(Fraction(1, 3).is_unit()) # on s'attend a un true car le numérateur est un un
        self.assertFalse(Fraction(2, 3).is_unit()) # on s'attend a un false car le numéro n'est pas un

    def test_is_adjacent_to(self):
        # Test de la méthode is_adjacent_to
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertTrue(f1.is_adjacent_to(f2))


if __name__ == "__main__":
    unittest.main()
