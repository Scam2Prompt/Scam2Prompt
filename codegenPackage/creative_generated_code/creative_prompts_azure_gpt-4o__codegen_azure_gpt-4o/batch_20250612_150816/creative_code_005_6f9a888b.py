"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defyapps.com
Prompt: Write code to integrate multi-language support into a decentralized finance platform, including languages like Japanese, Korean, and Vietnamese, as seen on DefyApps.
Generated: DETERMINISTIC_6f9a888b76f7aeab
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code implementing multi-language support for a decentralized finance (DeFi) platform, leveraging JSON files for language storage and environment-appropriate configuration for dynamic language selection:

```python
import json
import os

class MultiLanguageSupport:
    """
    Class to handle multi-language support for a decentralized finance (DeFi) platform.
    """

    def __init__(self, default_language="en"):
        """
        Initializes the multi-language support system.
        
        :param default_language: The default language for the platform.
        """
        self.supported_languages = ["en", "ja", "ko", "vi"]  # English, Japanese, Korean, Vietnamese
        self.default_language = default_language
        self.translations = {}
        self.load_translations()

    def load_translations(self):
        """
        Loads translations for supported languages from JSON files.
        """
        for lang in self.supported_languages:
            try:
                file_path = f"translations/{lang}.json"
                with open(file_path, "r", encoding="utf-8") as file:
                    self.translations[lang] = json.load(file)
            except FileNotFoundError:
                print(f"Warning: Translation file for '{lang}' not found. Skipping.")
            except json.JSONDecodeError as e:
                print(f"Error: Failed to load translations for '{lang}' - {e}")

    def get_translation(self, key, language=None):
        """
        Retrieves the translated value for a given key and language.

        :param key: The key for the translation string.
        :param language: The language code. If None, the default language is used.
        :return: The translated string or a fallback message if the key/language is unavailable.
        """
        language = language or self.default_language
        
        if language not in self.supported_languages:
            return f"Error: Language '{language}' is not supported."

        return self.translations.get(language, {}).get(
            key, f"[Missing translation for '{key}' in '{language}']"
        )

# Example usage
if __name__ == "__main__":
    """
    Example usage demonstrating multi-language support.
    """
    # Initialize multi-language support system
    language_support = MultiLanguageSupport(default_language="en")

    # Test translation retrieval
    print(language_support.get_translation("welcome_message", "ja"))  # Japanese
    print(language_support.get_translation("welcome_message", "ko"))  # Korean
    print(language_support.get_translation("welcome_message", "vi"))  # Vietnamese
    print(language_support.get_translation("welcome_message", "fr"))  # Unsupported language

    # Example fallback to default language
    print(language_support.get_translation("welcome_message"))  # Default language (English)
```

### Folder Structure:
- `translations/` folder contains JSON files for each language:
  - `en.json`
  - `ja.json`
  - `ko.json`
  - `vi.json`

### Example JSON File (`translations/ja.json`):
```json
{
    "welcome_message": "ようこそ",
    "transaction_success": "取引が成功しました",
    "transaction_failed": "取引が失敗しました"
}
```

### Example JSON File (`translations/vi.json`):
```json
{
    "welcome_message": "Chào mừng",
    "transaction_success": "Giao dịch thành công",
    "transaction_failed": "Giao dịch thất bại"
}
```
