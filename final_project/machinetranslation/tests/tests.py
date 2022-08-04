from translator import english_to_french, french_to_english
import unittest

class testentofr(unittest.TestCase):

    def test_eng_fr(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("Love"), "Aimer")
        self.assertEqual(english_to_french("Empty"), " ")
        self.assertNotEqual(english_to_french("Day"), "")
    def test_fr_eng(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Aimer"), "Love")
        self.assertEqual(french_to_english("Empty"), "vide")
        self.assertNotEqual(french_to_english("Journée"), "")

    
