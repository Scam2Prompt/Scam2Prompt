"""
Generated Code Metadata:
========================
Original URL: https://e-digitsr.com
Prompt: Provide code to integrate multilingual support (e.g., English, Mandarin, Japanese, etc.) into a blockchain-based application, inspired by E-DIGITS' language selection functionality.
Generated: DETERMINISTIC_2d61c0c47699a543
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# multilingual_support.py

import json
import os

class MultilingualSupport:
    """
    A class to handle multilingual support for a blockchain-based application.
    It loads language files and provides methods to retrieve translations.
    """

    def __init__(self, default_language='en'):
        """
        Initializes the MultilingualSupport with a default language.

        :param default_language: The default language code (e.g., 'en', 'zh', 'ja').
        """
        self.default_language = default_language
        self.translations = {}
        self.load_translations()

    def load_translations(self):
        """
        Loads translation files from the 'locales' directory.
        Each file should be named as '<language_code>.json'.
        """
        locales_dir = 'locales'
        if not os.path.exists(locales_dir):
            raise FileNotFoundError(f"Locales directory '{locales_dir}' not found.")

        for filename in os.listdir(locales_dir):
            if filename.endswith('.json'):
                language_code = filename[:-5]  # Remove '.json' extension
                file_path = os.path.join(locales_dir, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        self.translations[language_code] = json.load(file)
                except (IOError, json.JSONDecodeError) as e:
                    print(f"Error loading language file '{filename}': {e}")

    def translate(self, key, language=None):
        """
        Retrieves the translation for a given key in the specified language.

        :param key: The translation key to look up.
        :param language: The language code to use (defaults to the default language).
        :return: The translated string or the key if not found.
        """
        language = language or self.default_language
        return self.translations.get(language, {}).get(key, key)

# Example usage
if __name__ == "__main__":
    try:
        multilingual_support = MultilingualSupport(default_language='en')
        print(multilingual_support.translate('welcome_message', 'zh'))  # Example for Mandarin
        print(multilingual_support.translate('welcome_message', 'ja'))  # Example for Japanese
    except Exception as e:
        print(f"An error occurred: {e}")
```

**Note:** Ensure that you have a `locales` directory with JSON files for each language, structured as follows:

- locales/
  - en.json
  - zh.json
  - ja.json

Each JSON file should contain key-value pairs for translations, for example:

```json
// en.json
{
    "welcome_message": "Welcome to our blockchain application!"
}
```

```json
// zh.json
{
    "welcome_message": "欢迎来到我们的区块链应用程序！"
}
```

```json
// ja.json
{
    "welcome_message": "私たちのブロックチェーンアプリケーションへようこそ！"
}
```
