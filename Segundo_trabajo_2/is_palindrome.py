import unittest

def is_palindrome(mistring):  

    for valor in range(len(mistring)):
        reversa= -(valor+1)
        if mistring[valor]!=mistring[reversa]:
            return False
    return True 
        
#El return True va en el For para que compare todos los valores.
#En cambio si se coloca en el if con un else va a revisar solo la primera y ultima letra
    

class TestIsPalindrome(unittest.TestCase):
    def test_with_a(self):
        user_input = "a"
        result = is_palindrome(user_input)
        self.assertTrue(result)

    def test_with_ala(self):
        user_input = "ala"
        result = is_palindrome(user_input)
        self.assertTrue(result)

    def test_with_Neuquen(self):
        user_input = "neuquen"
        result = is_palindrome(user_input)
        self.assertTrue(result)

    def test_with_Hola(self):
        user_input = "hola"
        result = is_palindrome(user_input)
        self.assertFalse(result)

unittest.main()

