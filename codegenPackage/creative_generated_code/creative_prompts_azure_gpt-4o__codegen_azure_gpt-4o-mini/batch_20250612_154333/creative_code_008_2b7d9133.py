"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fansliebe.com
Prompt: Recommend tools or frameworks to localize a social media platform with multiple languages and RTL support, as described on Fansliebe.
Generated: DETERMINISTIC_2b7d91333e6bf440
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json
import os

# Define a class to handle localization for a social media platform
class LocalizationManager:
    def __init__(self, locale_dir='locales'):
        """
        Initializes the LocalizationManager with the directory for locale files.
        
        :param locale_dir: Directory where localization files are stored
        """
        self.locale_dir = locale_dir
        self.localizations = {}
        self.load_localizations()

    def load_localizations(self):
        """
        Loads localization files from the specified directory.
        Expects JSON files named as <language_code>.json (e.g., en.json, de.json).
        """
        try:
            for filename in os.listdir(self.locale_dir):
                if filename.endswith('.json'):
                    language_code = filename[:-5]  # Remove .json extension
                    with open(os.path.join(self.locale_dir, filename), 'r', encoding='utf-8') as file:
                        self.localizations[language_code] = json.load(file)
        except Exception as e:
            print(f"Error loading localizations: {e}")

    def get_translation(self, language_code, key):
        """
        Retrieves the translation for a given key in the specified language.
        
        :param language_code: Language code (e.g., 'en', 'de')
        :param key: The translation key to look up
        :return: The translated string or a fallback message
        """
        return self.localizations.get(language_code, {}).get(key, f"Missing translation for '{key}'")

    def add_translation(self, language_code, key, translation):
        """
        Adds a new translation to the specified language's dictionary.
        
        :param language_code: Language code (e.g., 'en', 'de')
        :param key: The translation key to add
        :param translation: The translated string
        """
        if language_code not in self.localizations:
            self.localizations[language_code] = {}
        self.localizations[language_code][key] = translation
        self.save_localization(language_code)

    def save_localization(self, language_code):
        """
        Saves the current localization dictionary for a specific language to a JSON file.
        
        :param language_code: Language code to save
        """
        try:
            with open(os.path.join(self.locale_dir, f"{language_code}.json"), 'w', encoding='utf-8') as file:
                json.dump(self.localizations[language_code], file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error saving localization for '{language_code}': {e}")


# Usage example (would be executed in a production environment)
if __name__ == "__main__":
    # Create a localization manager instance
    localization_manager = LocalizationManager()
    
    # Get a translation for a specific key
    translation = localization_manager.get_translation('en', 'welcome_message')
    print(translation)  # Output: 'Welcome to Fansliebe!' or a fallback message

    # Add a new translation
    localization_manager.add_translation('fr', 'welcome_message', 'Bienvenue sur Fansliebe!')
```
