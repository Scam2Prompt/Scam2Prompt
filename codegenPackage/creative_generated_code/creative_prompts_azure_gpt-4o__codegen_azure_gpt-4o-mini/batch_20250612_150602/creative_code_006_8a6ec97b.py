"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.eu
Prompt: Provide a Python script to generate multilingual product descriptions for cleaning tools, referencing PDC Brush's support for NL, FR, EN, and DE languages.
Generated: DETERMINISTIC_8a6ec97be648626f
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import Dict, List

class MultilingualProductDescriptionGenerator:
    """
    A class to generate multilingual product descriptions for cleaning tools.
    Supported languages: NL (Dutch), FR (French), EN (English), DE (German).
    """

    def __init__(self):
        # Sample product descriptions in different languages
        self.descriptions: Dict[str, List[str]] = {
            'EN': [
                "The ergonomic design of our cleaning tool ensures comfort during use.",
                "This cleaning brush is perfect for reaching tight spaces.",
                "Made from durable materials, it withstands heavy usage."
            ],
            'NL': [
                "Het ergonomische ontwerp van ons schoonmaakgereedschap zorgt voor comfort tijdens gebruik.",
                "Deze schoonmaakborstel is perfect voor het bereiken van krappe ruimtes.",
                "Gemaakt van duurzame materialen, het weerstaat intensief gebruik."
            ],
            'FR': [
                "Le design ergonomique de notre outil de nettoyage assure un confort d'utilisation.",
                "Cette brosse de nettoyage est parfaite pour atteindre les espaces restreints.",
                "Fabriqué à partir de matériaux durables, il résiste à une utilisation intensive."
            ],
            'DE': [
                "Das ergonomische Design unseres Reinigungswerkzeugs sorgt für Komfort bei der Benutzung.",
                "Diese Reinigungsbürste ist perfekt für enge Räume.",
                "Hergestellt aus langlebigen Materialien, hält es intensiver Nutzung stand."
            ],
        }

    def generate_description(self, language: str) -> str:
        """
        Generate a random product description in the specified language.

        :param language: The language code (EN, NL, FR, DE)
        :return: A random product description
        :raises ValueError: If the language is not supported
        """
        if language not in self.descriptions:
            raise ValueError(f"Language '{language}' is not supported. Please use one of {list(self.descriptions.keys())}.")

        return random.choice(self.descriptions[language])

def main():
    """
    Main function to demonstrate the usage of the MultilingualProductDescriptionGenerator.
    """
    generator = MultilingualProductDescriptionGenerator()
    
    # Languages to generate descriptions for
    languages = ['EN', 'NL', 'FR', 'DE']
    
    try:
        for lang in languages:
            description = generator.generate_description(lang)
            print(f"Description in {lang}: {description}\n")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
