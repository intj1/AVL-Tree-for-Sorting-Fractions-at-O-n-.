from random import randint
from AVL_Tree import AVL_Tree
class Fraction:

  def __init__(self, numerator, denominator):
    if denominator == 0:
      raise ZeroDivisionError
    self.__n = numerator
    self.__d = denominator
    self.__reduce()

  @staticmethod
  def gcd(n, d):
    while d != 0:
      t = d
      d = n % d
      n = t
    return n

  def __reduce(self):
    if self.__n < 0 and self.__d < 0:
      self.__n = self.__n * -1
      self.__d = self.__d * -1

    divisor = Fraction.gcd(self.__n, self.__d)
    self.__n = self.__n // divisor
    self.__d = self.__d // divisor

  def __add__(self, addend):
    num = self.__n * addend.__d + self.__d * addend.__n
    den = self.__d * addend.__d
    return Fraction(num, den)

  def __sub__(self, subtrahend):
    num = self.__n * subtrahend.__d - self.__d * subtrahend.__n
    den = self.__d * subtrahend.__d
    return Fraction(num, den)

  def __mul__(self, multiplicand):
    num = self.__n * multiplicand.__n
    den = self.__d * multiplicand.__d
    return Fraction(num, den)

  def __truediv__(self, divisor):
    if divisor.__n == 0:
      raise ZeroDivisionError
    num = self.__n * divisor.__d
    den = self.__d * divisor.__n
    return Fraction(num, den)

  def __lt__(self, other):
    n_one = self.to_float()
    n_two = other.to_float()
    if n_one < n_two:
        return True
    else:
        return False

  def __gt__(self, other):
    n_one = self.to_float()
    n_two = other.to_float()
    if n_one > n_two:
        return True
    else:
        return False

  def __eq__(self, other):
    n_one = self.to_float()
    n_two = other.to_float()
    if n_one == n_two:
        return True
    else:
        return False

  def to_float(self):
    #this is safe because we don't allow a
    #zero denominator
    return self.__n / self.__d

  def __str__(self):
    return str(self.__n) + '/' + str(self.__d)

  def __repr__(self):
    return str(self)

if __name__ == '__main__':
    original = list()
    for i in range(10):
        original.append(Fraction(randint(1, 531), randint(1, 531)))
    print('Original :', original)
    organized = AVL_Tree()
    for j in original:
        organized.insert_element(j)
    print()    
    print('Sorted: ', organized.to_list())
