"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prosync.online
Prompt: Provide code for implementing multilingual support in a virtual receptionist system, ensuring effective communication across diverse client bases, as offered by ProSync.
Generated: DETERMINISTIC_12949c122a41c261
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# multilingual_receptionist.py

import json
import os
from typing import Dict, Any

class MultilingualReceptionist:
    """
    A class to implement multilingual support for a virtual receptionist system.
    It loads language data from JSON files and provides methods to get localized messages.
    """

    def __init__(self, languages_dir: str):
        """
        Initializes the MultilingualReceptionist with a directory of language files.

        :param languages_dir: Directory where language JSON files are stored.
        """
        self.languages_dir = languages_dir
        self.translations: Dict[str, Dict[str, str]] = {}
        self.load_translations()

    def load_translations(self):
        """
        Loads translation files from the specified directory into the translations dictionary.
        """
        try:
            for filename in os.listdir(self.languages_dir):
                if filename.endswith(".json"):
                    lang_code = filename[:-5]  # Extract language code from filename
                    self.translations[lang_code] = self.load_json(os.path.join(self.languages_dir, filename))
        except Exception as e:
            print(f"Error loading translations: {e}")

    def load_json(self, file_path: str) -> Dict[str, str]:
        """
        Loads a JSON file and returns its content as a dictionary.

        :param file_path: Path to the JSON file.
        :return: Dictionary with translations or an empty dictionary on error.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as json_file:
                return json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading JSON file {file_path}: {e}")
            return {}

    def get_message(self, lang_code: str, key: str) -> str:
        """
        Retrieves a message for the specified language code and key.

        :param lang_code: Language code (e.g., 'en', 'fr').
        :param key: Key for the specific message.
        :return: Localized message or a default English message if not found.
        """
        return self.translations.get(lang_code, {}).get(key, self.translations.get('en', {}).get(key, key))

    def set_language(self, lang_code: str) -> None:
        """
        Set the desired language for the session.

        :param lang_code: Language code to set.
        """
        if lang_code not in self.translations:
            print(f"Language '{lang_code}' not supported. Defaulting to 'en'.")
            lang_code = 'en'
        self.current_language = lang_code

# Example usage
if __name__ == "__main__":
    receptionist = MultilingualReceptionist('languages')
    
    # Set the desired language
    receptionist.set_language('fr')

    # Get a localized message
    welcome_message = receptionist.get_message(receptionist.current_language, 'welcome')
    print(welcome_message)  # Print the welcome message in the current language
```

### Example JSON Files
#### en.json
```json
{
    "welcome": "Welcome to ProSync's virtual receptionist system!",
    "thank_you": "Thank you for calling."
}
```

#### fr.json
```json
{
    "welcome": "Bienvenue dans le système de réceptionniste virtuel de ProSync!",
    "thank_you": "Merci de votre appel."
}
``` 

### Notes
- Place the JSON files in a directory named `languages`.
- The code supports loading multiple languages and getting messages based on the selected language.
- Error handling and default message fallbacks are implemented to ensure robust performance.
