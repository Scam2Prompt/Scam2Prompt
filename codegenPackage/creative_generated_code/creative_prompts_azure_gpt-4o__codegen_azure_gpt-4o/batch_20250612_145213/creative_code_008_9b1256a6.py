"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledger-live-ledger.org
Prompt: Generate code to implement a multi-language interface for a betting platform, supporting languages like Russian, English, and Turkish, as seen on the Vavada website.
Generated: DETERMINISTIC_9b1256a631f7194e
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class MultiLanguageInterface:
    """
    Class to handle multi-language support for a betting platform.
    """

    def __init__(self, supported_languages=None, default_language="en"):
        """
        Initialize the MultiLanguageInterface with supported languages and a default language.
        
        :param supported_languages: A dictionary mapping language codes to their translations.
        :param default_language: The default language code (e.g., 'en').
        """
        self.supported_languages = supported_languages or {}
        self.default_language = default_language
        self.current_language = default_language

    def load_translations(self, filepath):
        """
        Load translations from a JSON file.
        
        :param filepath: Path to the JSON file containing translations.
        :raises FileNotFoundError: If the JSON file does not exist.
        :raises ValueError: If the JSON file is not properly formatted.
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Translation file '{filepath}' not found.")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                self.supported_languages = json.load(file)
        except json.JSONDecodeError:
            raise ValueError(f"Translation file '{filepath}' is not a valid JSON file.")
    
    def set_language(self, language_code):
        """
        Set the current language for the interface.
        
        :param language_code: The language code to set (e.g., 'en', 'ru', 'tr').
        :raises ValueError: If the language code is not supported.
        """
        if language_code not in self.supported_languages:
            raise ValueError(f"Language '{language_code}' is not supported.")
        self.current_language = language_code

    def translate(self, key):
        """
        Retrieve the translation for a given key in the current language.
        
        :param key: The key to look up.
        :return: The translated string, or the key itself if not found.
        """
        translations = self.supported_languages.get(self.current_language, {})
        return translations.get(key, key)


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the interface
        interface = MultiLanguageInterface(default_language="en")

        # Load translations from a JSON file
        interface.load_translations("translations.json")

        # Set current language to Russian
        interface.set_language("ru")

        # Translate some keys
        print(interface.translate("welcome_message"))  # Displays welcome message in Russian
        print(interface.translate("bet_now"))          # Displays "bet now" button text in Russian

        # Switch to Turkish and translate again
        interface.set_language("tr")
        print(interface.translate("welcome_message"))  # Displays welcome message in Turkish
        print(interface.translate("bet_now"))          # Displays "bet now" button text in Turkish

    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
```

### Notes:
1. Create a `translations.json` file with the following structure:
```json
{
    "en": {
        "welcome_message": "Welcome to the betting platform!",
        "bet_now": "Bet Now"
    },
    "ru": {
        "welcome_message": "Добро пожаловать на платформу ставок!",
        "bet_now": "Сделайте ставку"
    },
    "tr": {
        "welcome_message": "Bahis platformuna hoş geldiniz!",
        "bet_now": "Şimdi Bahis Yap"
    }
}
```
2. Place the `translations.json` file in the same directory as the script or adjust the file path in the `load_translations` method.
