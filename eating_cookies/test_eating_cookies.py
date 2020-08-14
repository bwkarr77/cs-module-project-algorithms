import unittest
from eating_cookies import eating_cookies, fib_mem

class Test(unittest.TestCase):

  def test_eating_cookies_small_n(self):
    self.assertEqual(fib_mem(0), 1)
    self.assertEqual(fib_mem(1), 1)
    self.assertEqual(fib_mem(2), 2)
    self.assertEqual(fib_mem(3), 4)
    self.assertEqual(fib_mem(5), 13)
    self.assertEqual(fib_mem(10), 274)

  def test_eating_cookies_large_n(self):
    self.assertEqual(fib_mem(50), 10562230626642)
    self.assertEqual(fib_mem(100), 180396380815100901214157639)
    self.assertEqual(fib_mem(500), 1306186569702186634983475450062372018715120191391192207156664343051610913971927959744519676992404852130396504615663042713312314219527)


if __name__ == '__main__':
  unittest.main()