import unittest

def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    #este si funciona tambien#return palabra==palabra[::-1]
    for valor in range(len(palabra)):
        reversa= -(valor+1)
        if palabra[valor]!=palabra[reversa]:
            return False
    return True            

def obtener_cantidad_de_palabras_palindrome(palabras):
    contador = 0
    for palabra in palabras:
        if es_palindromo(palabra):
            contador=contador+1
    return contador
#    palabras = palabras.lower()
#    palabras= palabras.replace(" ","")
#    for palabra in palabras:
#        contador=0
#        palindromo=0
#        for valor in range(len(palabras)):
#            reversa= -(valor+1)
#            if palabras[valor]==palabras[reversa]:
#                palindromo= palindromo + 1
#            if len(palabra)/2 == palindromo:
#                contador= contador + 1
            
         
#Consejo el resultado para saber cuantos palindromos hay deberia estar en otro def aparte


class TestCantidadDePalabrasPalindromes(unittest.TestCase):
    
    def test_cantidad_de_palabras_palindromes_simple(self):
        palabras = ["ala"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 1)
 
    def test_cantidad_de_palabras_palindromes_con_2(self):
        palabras = ["ala", "neuquen"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 2)
 
    def test_cantidad_de_palabras_palindromes_con_3(self):
        palabras = ["ala", "neuquen", "hola"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 2)
 
    def test_cantidad_de_palabras_palindromes_con_4(self):
        palabras = ["ala", "neuquen", "hola", "programacion"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 2)
 
    def test_cantidad_de_palabras_palindromes_con_5(self):
        palabras = ["ala", "neuquen", "hola", "programacion", "palap"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 3)
 
    def test_cantidad_de_palabras_palindromes_complejo(self):
        palabras = ["ala", "neuquen", "hola", "programacion", "palap", "neu  quen"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 4)
 
    def test_cantidad_de_palabras_palindromes_complejo_2(self):
        palabras = [
             "ala",
             "neuquen",
             "hola",
             "programacion",
             "palap",
             "neu  quen",
             "agita falsos usos la fatiga",
             "presidente de la camara de diputados: martin menem",
        ]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 5)

unittest.main()
