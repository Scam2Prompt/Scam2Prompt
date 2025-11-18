"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alwan.om
Prompt: Generate code for multi-language or localization support for an e-commerce platform, focusing on regions like Oman, as seen on Alwan's website.
Generated: DETERMINISTIC_98114f3e55f22b15
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: localization.py

import json
import os

class LocalizationManager:
    """
    Handles multi-language localization for the e-commerce platform.
    """

    def __init__(self, supported_languages, default_language="en"):
        """
        Initializes the LocalizationManager.

        :param supported_languages: List of supported language codes (e.g., ['en', 'ar']).
        :param default_language: Default language code used as fallback.
        """
        self.supported_languages = supported_languages
        self.default_language = default_language
        self.translations = {}

    def load_translations(self, translations_directory):
        """
        Loads translation files from the specified directory.

        :param translations_directory: Path to the directory containing language JSON files.
        """
        for lang in self.supported_languages:
            file_path = os.path.join(translations_directory, f"{lang}.json")
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    self.translations[lang] = json.load(file)
            except FileNotFoundError:
                print(f"Warning: Translation file for language '{lang}' not found at {file_path}")
                self.translations[lang] = {}
            except json.JSONDecodeError as e:
                print(f"Error: Failed to parse translation file for language '{lang}' - {e}")
                self.translations[lang] = {}

    def get_translation(self, key, language):
        """
        Retrieves the translation for the given key in the specified language.

        :param key: The key to be translated (e.g., 'welcome_message').
        :param language: The language code (e.g., 'ar').
        :return: The translated string or the key itself if translation is not available.
        """
        if language not in self.supported_languages:
            language = self.default_language

        return self.translations.get(language, {}).get(key, self.translations.get(self.default_language, {}).get(key, key))

# File: main.py

from localization import LocalizationManager

def main():
    # Supported languages
    supported_languages = ["en", "ar"]
    
    # Initialize LocalizationManager
    localization_manager = LocalizationManager(supported_languages, default_language="en")
    
    # Load translation files
    translations_directory = "./translations"  # Directory containing JSON files like en.json, ar.json
    localization_manager.load_translations(translations_directory)

    # Example of using the LocalizationManager
    current_language = "ar"  # This could be dynamically set based on user preferences or region
    print(localization_manager.get_translation("welcome_message", current_language))
    print(localization_manager.get_translation("checkout_button", current_language))

if __name__ == "__main__":
    main()

# Example Translation Files:
# File: translations/en.json
# {
#     "welcome_message": "Welcome to our store!",
#     "checkout_button": "Checkout"
# }

# File: translations/ar.json
# {
#     "welcome_message": "مرحبًا بك في متجرنا!",
#     "checkout_button": "الدفع"
# }

```

This code provides a robust localization mechanism for an e-commerce platform. It supports dynamic language switching, error handling for missing translation files, and fallback to a default language when a translation is unavailable.
