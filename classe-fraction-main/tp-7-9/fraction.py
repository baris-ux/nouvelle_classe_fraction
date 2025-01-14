from math import gcd

class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num: int = 0, den: int = 1):
        """This builds a fraction based on some numerator and denominator.

        PRÉ : den != 0
        POST : La fraction est dans sa forme réduite
        LÈVE : ValueError si den == 0
        """
        if den == 0:
            raise ValueError("Denominator cannot be zero.")

        common_divisor = gcd(num, den)
        self._num = num // common_divisor * (-1 if den < 0 else 1)
        self._den = abs(den) // common_divisor

    @property
    def numerator(self):
        return self._num

    @property
    def denominator(self):
        return self._den

# ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRÉ : Aucun
        POST : Renvoie une chaîne sous la forme "num/den" ou "num" si den == 1
        """
        return f"{self._num}/{self._den}" if self._den != 1 else f"{self._num}"

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        PRÉ : Aucun
        POST : Renvoie une chaîne sous la forme "integer num/den" ou "integer" si propre
        """
        integer_part = self._num // self._den
        remainder = abs(self._num % self._den)

        if remainder == 0: 
            return f"{integer_part}" 
        elif integer_part == 0:
            return f"{remainder}/{self._den}"
        else:
            return f"{integer_part} {remainder}/{self._den}"

# ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

        PRÉ : other est une instance de Fraction
        POST : Renvoie une nouvelle Fraction représentant la somme
        """
        if not isinstance(other, Fraction):
            raise TypeError("Can only add Fraction objects.")

        num = self._num * other.denominator + self._den * other.numerator
        den = self._den * other.denominator
        return Fraction(num, den)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRÉ : other est une instance de Fraction
        POST : Renvoie une nouvelle Fraction représentant la différence
        """
        if not isinstance(other, Fraction):
            raise TypeError("Can only subtract Fraction objects.")

        num = self._num * other.denominator - self._den * other.numerator
        den = self._den * other.denominator
        return Fraction(num, den)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRÉ : other est une instance de Fraction
        POST : Renvoie une nouvelle Fraction représentant le produit
        """
        if not isinstance(other, Fraction):
            raise TypeError("Can only multiply Fraction objects.")

        num = self._num * other.numerator # on mutliplie nos numérateurs entre eux
        den = self._den * other.denominator # on multiplie nos dénominateurs entre eux 
        return Fraction(num, den)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRÉ : other est une instance de Fraction, other.numerator != 0
        POST : Renvoie une nouvelle Fraction représentant la division
        LÈVE : ZeroDivisionError si other.numerator == 0
        """
        if not isinstance(other, Fraction):
            raise TypeError("Can only divide by Fraction objects.")
        if other.numerator == 0:
            raise ZeroDivisionError("Impossible de diviser par 0.")

        num = self._num * other.denominator
        den = self._den * other.numerator
        return Fraction(num, den)

    def __pow__(self, power: int):
        """Overloading of the ** operator for fractions

        PRÉ : power est un entier
        POST : Renvoie une nouvelle Fraction élevée à la puissance donnée
        """
        if not isinstance(power, int):
            raise TypeError("Power must be an integer.")

        return Fraction(self._num ** power, self._den ** power)

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRÉ : other est une instance de Fraction
        POST : Renvoie True si les fractions sont égales, False sinon
        """
        if not isinstance(other, Fraction):
            return NotImplemented

        return self._num == other.numerator and self._den == other.denominator

    def __float__(self):
        """Returns the decimal value of the fraction

        PRÉ : Aucun
        POST : Renvoie une représentation en float
        """
        return self._num / self._den # comme indiqué dans le POST on vient diviser un numérateur et dénominateur pour obtenir une representation en décimal

# ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRÉ : Aucun
        POST : Renvoie True si le numérateur est 0, False sinon
        """
        return self._num == 0 # donc en l'occurence le numérateur doit être 0 pour que le resultat de la fraction soit = 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRÉ : Aucun
        POST : Renvoie True si le numérateur est divisible par le dénominateur
        """
        return self._num % self._den == 0 # on retourne True si la division par le dénominateur nous donne 0 comme resultat 

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRÉ : Aucun
        POST : Renvoie True si la valeur absolue du numérateur < dénominateur
        """
        return abs(self._num) < self._den

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRÉ : Aucun
        POST : Renvoie True si le numérateur est 1
        """
        return self._num == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        PRÉ : other est une instance de Fraction
        POST : Renvoie True si la différence absolue est strictement égale à une unité fractionnaire
        """
        if not isinstance(other, Fraction):
            raise TypeError("Argument must be a Fraction instance.")

        diff = self - other
        return abs(diff.numerator) == 1 and diff.denominator > 1 
