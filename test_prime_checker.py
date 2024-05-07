import unittest
# Import the unittest module, which provides a framework for writing and running tests.
from prime_checker import is_prime
# Import the is_prime function from the prime_checker module.

class TestIsPrime(unittest.TestCase):
    # Define a test case class that inherits from unittest.TestCase.

    def test_prime_numbers(self):
        # Define a test method to test prime numbers.
        self.assertTrue(is_prime(2))
        # Test if 2 is a prime number. It should return True.
        self.assertTrue(is_prime(3))
        # Test if 3 is a prime number. It should return True.
        self.assertTrue(is_prime(5))
        # Test if 5 is a prime number. It should return True.
        self.assertTrue(is_prime(7))
        # Test if 7 is a prime number. It should return True.
        self.assertTrue(is_prime(11))
        # Test if 11 is a prime number. It should return True.
        self.assertTrue(is_prime(13))
        # Test if 13 is a prime number. It should return True.
        self.assertTrue(is_prime(17))
        # Test if 17 is a prime number. It should return True.
        self.assertTrue(is_prime(19))
        # Test if 19 is a prime number. It should return True.
        self.assertTrue(is_prime(23))
        # Test if 23 is a prime number. It should return True.
        self.assertTrue(is_prime(29))
        # Test if 29 is a prime number. It should return True.

    def test_non_prime_numbers(self):
        # Define a test method to test non-prime numbers.
        self.assertFalse(is_prime(0))
        # Test if 0 is a prime number. It should return False.
        self.assertFalse(is_prime(1))
        # Test if 1 is a prime number. It should return False.
        self.assertFalse(is_prime(4))
        # Test if 4 is a prime number. It should return False.
        self.assertFalse(is_prime(6))
        # Test if 6 is a prime number. It should return False.
        self.assertFalse(is_prime(8))
        # Test if 8 is a prime number. It should return False.
        self.assertFalse(is_prime(9))
        # Test if 9 is a prime number. It should return False.
        self.assertFalse(is_prime(10))
        # Test if 10 is a prime number. It should return False.
        self.assertFalse(is_prime(12))
        # Test if 12 is a prime number. It should return False.
        self.assertFalse(is_prime(15))
        # Test if 15 is a prime number. It should return False.
        self.assertFalse(is_prime(21))
        # Test if 21 is a prime number. It should return False.

if __name__ == '__main__':
    # If this script is executed directly, run the tests defined in the TestIsPrime class.
    unittest.main()
