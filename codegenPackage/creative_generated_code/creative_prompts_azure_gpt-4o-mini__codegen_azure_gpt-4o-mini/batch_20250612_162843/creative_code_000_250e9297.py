"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globallinknext.com
Prompt: Generate a code snippet that demonstrates how to implement a globalization strategy discussed at the GlobalLink NEXT 2025 conference.
Generated: DETERMINISTIC_250e9297750ddcbb
Batch ID: 20250612_162843
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
from typing import Dict, Any

class GlobalizationManager:
    """
    A class to manage application globalization, including loading
    translation files and retrieving localized strings.
    """

    def __init__(self, locale: str, translations_dir: str = "translations"):
        """
        Initializes the GlobalizationManager with the specified locale.

        Args:
            locale (str): The locale code (e.g., 'en', 'fr', 'es').
            translations_dir (str): The directory containing translation files.
        """
        self.locale = locale
        self.translations_dir = translations_dir
        self.translations = {}

        self.load_translations()

    def load_translations(self) -> None:
        """
        Loads translation strings from the JSON file corresponding to the locale.
        Raises:
            FileNotFoundError: If the translation file does not exist.
            json.JSONDecodeError: If the translation file is not valid JSON.
        """
        file_path = os.path.join(self.translations_dir, f"{self.locale}.json")

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.translations = json.load(file)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Translation file not found: {file_path}") from e
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON from the file: {file_path}") from e

    def get_translation(self, key: str) -> str:
        """
        Retrieves the translation for a given key.

        Args:
            key (str): The key for the translation string.

        Returns:
            str: The translated string, or the key itself if not found.
        """
        return self.translations.get(key, key)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the globalization manager for English locale
        gm = GlobalizationManager(locale='en')

        # Retrieve and print a translation
        greeting = gm.get_translation('greeting')
        print(greeting)

    except Exception as e:
        print(f"An error occurred: {e}")
```

**Note:** This code assumes you have JSON translation files structured as follows:
```json
{
    "greeting": "Hello",
    "farewell": "Goodbye"
}
```
Place these files in a directory named `translations`, and ensure the naming convention matches the locale (e.g., `en.json` for English).
