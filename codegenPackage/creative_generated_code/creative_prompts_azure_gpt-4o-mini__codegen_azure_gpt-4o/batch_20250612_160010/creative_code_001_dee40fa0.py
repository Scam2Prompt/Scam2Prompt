"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rentsy.pro
Prompt: Write a code snippet to create a multi-language support feature for a rental service website like Rentsy.
Generated: DETERMINISTIC_dee40fa0e5957936
Batch ID: 20250612_160010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class MultiLanguageSupport:
    """
    A class to provide multi-language support for a rental service website.
    """
    def __init__(self, languages_file):
        """
        Initialize the MultiLanguageSupport class.

        :param languages_file: Path to the JSON file containing translations
        """
        self.languages = {}
        self.current_language = "en"  # Default language is English
        self.load_languages(languages_file)

    def load_languages(self, languages_file):
        """
        Load the language translations from a JSON file.

        :param languages_file: Path to the JSON file containing translations
        """
        try:
            with open(languages_file, 'r', encoding='utf-8') as file:
                self.languages = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {languages_file} was not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Error decoding JSON from file {languages_file}.")

    def set_language(self, language_code):
        """
        Set the current language.

        :param language_code: Language code to switch to (e.g., 'en', 'fr', 'es')
        """
        if language_code in self.languages:
            self.current_language = language_code
        else:
            raise ValueError(f"Language '{language_code}' is not supported.")

    def get_translation(self, key):
        """
        Get the translation for a specific key in the current language.

        :param key: Translation key (e.g., 'welcome_message')
        :return: Translated text in the current language
        """
        try:
            return self.languages[self.current_language].get(key, f"[{key}]")
        except KeyError:
            return f"[Missing translation: {key}]"

# Usage example
if __name__ == "__main__":
    # JSON file containing translations
    # Example content:
    # {
    #     "en": {
    #         "welcome_message": "Welcome to Rentsy!",
    #         "logout_button": "Logout"
    #     },
    #     "fr": {
    #         "welcome_message": "Bienvenue chez Rentsy!",
    #         "logout_button": "Déconnexion"
    #     },
    #     "es": {
    #         "welcome_message": "¡Bienvenido a Rentsy!",
    #         "logout_button": "Salir"
    #     }
    # }
    translations_file = "translations.json"
    
    try:
        # Initialize multi-language support
        mls = MultiLanguageSupport(translations_file)
        
        # Set language to French
        mls.set_language('fr')
        
        # Retrieve translated text
        print(mls.get_translation('welcome_message'))  # Output: Bienvenue chez Rentsy!
        print(mls.get_translation('logout_button'))    # Output: Déconnexion
        
        # Switch language to Spanish
        mls.set_language('es')
        print(mls.get_translation('welcome_message'))  # Output: ¡Bienvenido a Rentsy!
    except Exception as e:
        print(f"Error: {e}")
```
