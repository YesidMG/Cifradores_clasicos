import sys
import os
import unittest

# Agregar la carpeta padre al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Algorithms.encryptionAlgorithms import cesar, polibio, transposicion
from Algorithms.decryptionAlgorithms import cesar_decrypt, polibio_decrypt, transposicion_decrypt

class TestCesar(unittest.TestCase):
    """Pruebas para el algoritmo César"""
    
    def test_cesar_encrypt_decrypt_single(self):
        """Verifica que encriptación y desencriptación de César sean inversas."""
        mensaje = "hola"
        clave = "clave"
        cifrado = cesar(mensaje, 'lax', clave)
        descifrado = cesar_decrypt(cifrado, clave)
        self.assertEqual(mensaje.lower(), descifrado)
    
    def test_cesar_encrypt_decrypt_strict(self):
        """Verifica César con normalización strict."""
        mensaje = "Hola Mundo"
        clave = "clave"
        cifrado = cesar(mensaje, 'strict', clave)
        descifrado = cesar_decrypt(cifrado, clave)
        self.assertEqual("holamundo", descifrado)
    
    def test_cesar_requires_key(self):
        """Verifica que César requiere clave."""
        with self.assertRaises(Exception):
            cesar("test", 'lax', "")
    
    def test_cesar_different_messages(self):
        """Verifica que mensajes diferentes producen cifrados diferentes."""
        clave = "clave"
        cifrado1 = cesar("mensaje1", 'lax', clave)
        cifrado2 = cesar("mensaje2", 'lax', clave)
        self.assertNotEqual(cifrado1, cifrado2)
    
    def test_cesar_key_length(self):
        """Verifica que César maneja claves de diferente largo."""
        mensaje = "prueba"
        clave_corta = "a"
        clave_larga = "clavemuylargayprobada"
        
        cifrado1 = cesar(mensaje, 'lax', clave_corta)
        cifrado2 = cesar(mensaje, 'lax', clave_larga)
        
        self.assertIsNotNone(cifrado1)
        self.assertIsNotNone(cifrado2)

class TestPolibio(unittest.TestCase):
    """Pruebas para el algoritmo Polibio"""
    
    def test_polibio_encrypt_decrypt(self):
        """Verifica que encriptación y desencriptación de Polibio sean inversas."""
        mensaje = "abc"
        cifrado = polibio(mensaje, 'lax')
        descifrado = polibio_decrypt(cifrado, 'lax')
        self.assertEqual(mensaje.lower(), descifrado)
    
    def test_polibio_no_key_needed(self):
        """Verifica que Polibio no requiere clave."""
        mensaje = "test"
        cifrado = polibio(mensaje, 'lax')
        self.assertIsNotNone(cifrado)
    
    def test_polibio_outputs_numbers(self):
        """Verifica que Polibio produce números."""
        mensaje = "a"
        cifrado = polibio(mensaje, 'lax')
        self.assertTrue(all(c.isdigit() for c in cifrado))
    
    def test_polibio_strict_mode(self):
        """Verifica Polibio con normalización strict."""
        mensaje = "Hola Mundo"
        cifrado = polibio(mensaje, 'strict')
        descifrado = polibio_decrypt(cifrado, 'strict')
        self.assertEqual("holamundo", descifrado)

class TestTransposicion(unittest.TestCase):
    """Pruebas para el algoritmo Transposición"""
    
    def test_transposicion_encrypt_decrypt_par(self):
        """Verifica transposición con clave de largo par."""
        mensaje = "hola"
        clave = "ab"  # largo par
        cifrado = transposicion(mensaje, 'lax', clave)
        descifrado = transposicion_decrypt(cifrado, clave)
        self.assertEqual(mensaje.lower(), descifrado)
    
    def test_transposicion_encrypt_decrypt_impar(self):
        """Verifica transposición con clave de largo impar."""
        mensaje = "hola"
        clave = "abc"  # largo impar
        cifrado = transposicion(mensaje, 'lax', clave)
        descifrado = transposicion_decrypt(cifrado, clave)
        self.assertEqual(mensaje.lower(), descifrado)
    
    def test_transposicion_par_key_behavior(self):
        """Verifica que clave par lleva pares al final."""
        mensaje = "abcd"
        clave = "ab"  # largo par
        cifrado = transposicion(mensaje, 'lax', clave)
        # Con clave par: pares (a,c) al final, impares (b,d) al inicio
        expected = "bd" + "ac"
        self.assertEqual(expected, cifrado)
    
    def test_transposicion_impar_key_behavior(self):
        """Verifica que clave impar lleva impares al final."""
        mensaje = "abcd"
        clave = "abc"  # largo impar
        cifrado = transposicion(mensaje, 'lax', clave)
        # Con clave impar: pares (a,c) al inicio, impares (b,d) al final
        expected = "ac" + "bd"
        self.assertEqual(expected, cifrado)

class TestCombined(unittest.TestCase):
    """Pruebas para algoritmos combinados"""
    
    def test_cesar_polibio_combination(self):
        """Verifica encriptación con César y Polibio en secuencia."""
        mensaje = "hola"
        clave = "clave"
        
        # Encriptar: cesar -> polibio
        paso1 = cesar(mensaje, 'lax', clave)
        paso2 = polibio(paso1, 'lax')
        
        self.assertIsNotNone(paso2)
        self.assertTrue(all(c.isdigit() for c in paso2))
    
    def test_three_algorithms_combination(self):
        """Verifica encriptación con 3 algoritmos."""
        mensaje = "test"
        clave = "clave"
        
        # Encriptar: cesar -> polibio -> transposicion
        paso1 = cesar(mensaje, 'lax', clave)
        paso2 = polibio(paso1, 'lax')
        paso3 = transposicion(paso2, 'lax', clave)
        
        self.assertIsNotNone(paso3)
    
    def test_reversibility_of_all_three(self):
        """Verifica reversibilidad de los 3 algoritmos combinados."""
        mensaje = "prueba"
        clave = "clave"
        
        # Encriptar
        e1 = cesar(mensaje, 'lax', clave)
        e2 = polibio(e1, 'lax')
        e3 = transposicion(e2, 'lax', clave)
        
        # Desencriptar (orden inverso)
        d3 = transposicion_decrypt(e3, clave)
        d2 = polibio_decrypt(d3, 'lax')
        d1 = cesar_decrypt(d2, clave)
        
        self.assertEqual(mensaje.lower(), d1)

class TestEdgeCases(unittest.TestCase):
    """Pruebas de casos extremos"""
    
    def test_single_character(self):
        """Prueba con un solo carácter."""
        mensaje = "a"
        clave = "b"
        cifrado = cesar(mensaje, 'lax', clave)
        descifrado = cesar_decrypt(cifrado, clave)
        self.assertEqual(mensaje.lower(), descifrado)
    
    def test_repeated_characters(self):
        """Prueba con caracteres repetidos."""
        mensaje = "aaaa"
        clave = "b"
        cifrado = cesar(mensaje, 'lax', clave)
        descifrado = cesar_decrypt(cifrado, clave)
        self.assertEqual(mensaje.lower(), descifrado)
    
    def test_special_characters_lax(self):
        """Prueba con caracteres especiales en modo lax."""
        mensaje = "¡hola!"
        clave = "clave"
        cifrado = cesar(mensaje, 'lax', clave)
        self.assertIsNotNone(cifrado)
    
    def test_numbers_in_message(self):
        """Prueba con números en el mensaje."""
        mensaje = "test123"
        clave = "clave"
        cifrado = cesar(mensaje, 'lax', clave)
        descifrado = cesar_decrypt(cifrado, clave)
        self.assertEqual(mensaje.lower(), descifrado)

if __name__ == '__main__':
    unittest.main(verbosity=2)