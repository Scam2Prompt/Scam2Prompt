"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint-zielchain.vercel.app
Prompt: Suggest an approach to implement multilingual support for a blockchain-based platform, ensuring consistency between English and Japanese versions, as seen on ZIELCHAIN.
Generated: DETERMINISTIC_25793163284a37de
Batch ID: 20250612_150613
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

class MultilingualSupport:
    """
    Class to handle multilingual support for a blockchain-based platform.
    This implementation supports English and Japanese.
    """
    
    def __init__(self, language_dir="languages", default_language="en"):
        """
        Initialize the multilingual support system.
        
        :param language_dir: Directory containing language JSON files.
        :param default_language: Default language for the platform (e.g., 'en' for English).
        """
        self.language_dir = language_dir
        self.default_language = default_language
        self.translations = {}
        
        # Load all available translations
        self._load_languages()

    def _load_languages(self):
        """
        Load language files from the specified directory.
        Language files must be in JSON format (e.g., en.json, ja.json).
        """
        try:
            for file_name in os.listdir(self.language_dir):
                if file_name.endswith(".json"):
                    language_code = file_name.split(".")[0]  # Extract language code (e.g., 'en' from 'en.json')
                    with open(os.path.join(self.language_dir, file_name), "r", encoding="utf-8") as file:
                        self.translations[language_code] = json.load(file)
        except Exception as e:
            print(f"Error loading languages: {e}")

    def get_translation(self, key, language_code=None):
        """
        Retrieve the translation for a given key in the specified language.
        Falls back to the default language if the key is not found.
        
        :param key: Translation key to look for (e.g., 'welcome_message').
        :param language_code: Language code for the desired translation (e.g., 'ja' for Japanese).
        :return: Translated string.
        """
        language_code = language_code or self.default_language
        
        try:
            # Fetch translation from the specified language
            if language_code in self.translations and key in self.translations[language_code]:
                return self.translations[language_code][key]
            
            # Fall back to the default language if the key is not found
            if key in self.translations.get(self.default_language, {}):
                return self.translations[self.default_language][key]
            
            # Key not found in either language
            return f"[Translation missing for key '{key}']"
        except Exception as e:
            return f"[Error fetching translation: {e}]"

# Usage example
if __name__ == "__main__":
    # Ensure the 'languages' directory contains 'en.json' and 'ja.json' files.
    multilingual = MultilingualSupport(language_dir="languages", default_language="en")
    
    # Example translations for English and Japanese
    print(multilingual.get_translation("welcome_message", "en"))   # English translation
    print(multilingual.get_translation("welcome_message", "ja"))   # Japanese translation
    print(multilingual.get_translation("nonexistent_key", "ja"))   # Missing translation
```

### Example Directory Structure:
```
languages/
├── en.json
├── ja.json
```

### Example `en.json` File:
```json
{
    "welcome_message": "Welcome to ZIELCHAIN!"
}
```

### Example `ja.json` File:
```json
{
    "welcome_message": "ZIELCHAINへようこそ！"
}
```
