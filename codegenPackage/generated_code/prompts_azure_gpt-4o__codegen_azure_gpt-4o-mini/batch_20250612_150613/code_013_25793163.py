"""
Generated Code Metadata:
========================
Original URL: https://mint-zielchain.vercel.app
Prompt: Suggest an approach to implement multilingual support for a blockchain-based platform, ensuring consistency between English and Japanese versions, as seen on ZIELCHAIN.
Generated: DETERMINISTIC_25793163284a37de
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import Dict, Any

class MultilingualSupport:
    """
    A class to handle multilingual support for a blockchain-based platform.
    This class loads translations from JSON files and provides methods to retrieve
    the appropriate translation based on the user's language preference.
    """

    def __init__(self, languages: Dict[str, str]):
        """
        Initializes the MultilingualSupport class with the available languages.

        :param languages: A dictionary mapping language codes to language names.
        """
        self.languages = languages
        self.translations = {}
        self.load_translations()

    def load_translations(self) -> None:
        """
        Loads translation files for each supported language.
        The translation files should be in JSON format and located in the 'locales' directory.
        """
        for lang_code in self.languages.keys():
            file_path = os.path.join('locales', f'{lang_code}.json')
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    self.translations[lang_code] = json.load(file)
            except FileNotFoundError:
                print(f"Warning: Translation file for '{lang_code}' not found.")
            except json.JSONDecodeError:
                print(f"Error: Failed to decode JSON from '{file_path}'.")

    def get_translation(self, lang_code: str, key: str) -> str:
        """
        Retrieves the translation for a given key in the specified language.

        :param lang_code: The language code for the desired translation.
        :param key: The key for the translation string.
        :return: The translated string or a fallback message if not found.
        """
        if lang_code not in self.translations:
            print(f"Warning: Language '{lang_code}' is not supported.")
            lang_code = 'en'  # Fallback to English

        return self.translations[lang_code].get(key, f"Translation for '{key}' not found.")

# Example usage
if __name__ == "__main__":
    # Define supported languages
    supported_languages = {
        'en': 'English',
        'ja': 'Japanese'
    }

    # Initialize multilingual support
    multilingual_support = MultilingualSupport(supported_languages)

    # Retrieve translations
    print(multilingual_support.get_translation('en', 'welcome_message'))  # Example key
    print(multilingual_support.get_translation('ja', 'welcome_message'))  # Example key
```

**Note:** Ensure that the `locales` directory contains the appropriate JSON files (e.g., `en.json`, `ja.json`) with the necessary key-value pairs for translations.
