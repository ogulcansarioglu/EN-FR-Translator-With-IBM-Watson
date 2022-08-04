

def notNullFrench(self):
    self.assertIsNotNone(french_to_english("Bonjour"))
def notNullEnglish(self):
    self.assertIsNotNone(english_to_french("Hello"))
def frenchToEnglishTest(self):
    assert english_to_french("Hello") == "Bonjour"
def englishtoFrenchTest(self):
    assert french_to_english("Bonjour") == "Hello"
    
