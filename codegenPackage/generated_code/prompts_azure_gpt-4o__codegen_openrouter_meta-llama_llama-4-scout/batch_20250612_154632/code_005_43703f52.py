"""
Generated Code Metadata:
========================
Original URL: https://app.apexbooster.com
Prompt: Write code to implement a multilingual translation feature for a web application, inspired by the language options provided on Apex Booster (e.g., Malay, Français, and Thai).
Generated: DETERMINISTIC_43703f52d09c773a
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# translation_service.py

import json
from typing import Dict

class TranslationService:
    """
    Provides multilingual translation feature for a web application.
    """

    def __init__(self, languages: Dict[str, str]):
        """
        Initializes the TranslationService with supported languages.

        Args:
        - languages (Dict[str, str]): A dictionary of language codes and their corresponding names.
        """
        self.languages = languages
        self.translations = {}

    def load_translations(self, filename: str) -> None:
        """
        Loads translations from a JSON file.

        Args:
        - filename (str): The name of the JSON file containing translations.
        """
        try:
            with open(filename, 'r') as file:
                self.translations = json.load(file)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except json.JSONDecodeError as e:
            print(f"Error: Failed to parse JSON - {e}")

    def translate(self, text: str, language: str) -> str:
        """
        Translates the given text into the specified language.

        Args:
        - text (str): The text to be translated.
        - language (str): The target language code.

        Returns:
        - str: The translated text if available, otherwise the original text.
        """
        if language not in self.languages:
            print(f"Error: Language '{language}' is not supported.")
            return text

        if not self.translations:
            print("Error: Translations are not loaded.")
            return text

        return self.translations.get(text, {}).get(language, text)

    def add_translation(self, text: str, language: str, translation: str) -> None:
        """
        Adds a new translation for the given text and language.

        Args:
        - text (str): The original text.
        - language (str): The target language code.
        - translation (str): The translated text.
        """
        if language not in self.languages:
            print(f"Error: Language '{language}' is not supported.")
            return

        if text not in self.translations:
            self.translations[text] = {}

        self.translations[text][language] = translation

    def save_translations(self, filename: str) -> None:
        """
        Saves the current translations to a JSON file.

        Args:
        - filename (str): The name of the JSON file to save translations.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.translations, file, indent=4)
        except Exception as e:
            print(f"Error: Failed to save translations - {e}")


def main():
    languages = {
        "ms": "Malay",
        "fr": "Français",
        "th": "Thai"
    }

    translation_service = TranslationService(languages)

    # Load existing translations
    translation_service.load_translations('translations.json')

    # Add new translations
    translation_service.add_translation("Hello", "ms", "Selamat datang")
    translation_service.add_translation("Hello", "fr", "Bonjour")
    translation_service.add_translation("Hello", "th", "")

    # Save translations
    translation_service.save_translations('translations.json')

    # Translate text
    print(translation_service.translate("Hello", "ms"))  # Output: Selamat datang
    print(translation_service.translate("Hello", "fr"))  # Output: Bonjour
    print(translation_service.translate("Hello", "th"))  # Output: 


if __name__ == "__main__":
    main()
```

```json
// translations.json

{
    "Hello": {
        "ms": "Selamat datang",
        "fr": "Bonjour"
    }
}
```
