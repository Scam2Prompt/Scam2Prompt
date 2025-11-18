"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-ai-trader-app.com
Prompt: Write code to implement a multilingual user interface for an AI-powered trading platform, similar to the AI Trader App's ability to adapt to user-preferred languages.
Generated: DETERMINISTIC_8e80258fbc24b8bb
Batch ID: 20250612_150211
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
from typing import Dict, List

class LanguageManager:
    """A class to manage multilingual support for the user interface."""

    def __init__(self, default_language: str = 'en'):
        """
        Initializes the LanguageManager with a default language.

        Args:
            default_language (str): The default language code (e.g., 'en', 'es').
        """
        self.default_language = default_language
        self.languages = {}
        self.load_languages()

    def load_languages(self) -> None:
        """Loads language files from the 'locales' directory."""
        try:
            locale_dir = 'locales'
            for language_file in os.listdir(locale_dir):
                if language_file.endswith('.json'):
                    with open(os.path.join(locale_dir, language_file), 'r', encoding='utf-8') as file:
                        language_code = language_file[:-5]  # Strip the '.json' extension
                        self.languages[language_code] = json.load(file)
        except Exception as e:
            print(f"Error loading language files: {e}")

    def get_translation(self, key: str, language: str = None) -> str:
        """
        Retrieves the translation for a given key in the specified language.

        Args:
            key (str): The translation key.
            language (str): The language code to fetch the translation for.

        Returns:
            str: The translated text or the key itself if not found.
        """
        if language is None:
            language = self.default_language

        return self.languages.get(language, {}).get(key, key)

class UserInterface:
    """A class for managing the user interface of the trading platform."""

    def __init__(self, language_manager: LanguageManager):
        """
        Initializes the UserInterface with a LanguageManager.

        Args:
            language_manager (LanguageManager): An instance of LanguageManager.
        """
        self.language_manager = language_manager

    def display_welcome_message(self, language: str = None) -> None:
        """Displays a welcome message to the user in the selected language."""
        welcome_message = self.language_manager.get_translation('welcome_message', language)
        print(welcome_message)

    def display_error_message(self, error_key: str, language: str = None) -> None:
        """Displays an error message based on a key in the selected language."""
        error_message = self.language_manager.get_translation(error_key, language)
        print(f"Error: {error_message}")

def main():
    """Main function to execute the multilingual interface."""
    language_manager = LanguageManager(default_language='en')
    ui = UserInterface(language_manager)

    # Simulating user interactions
    try:
        ui.display_welcome_message('en')  # Display welcome message in English
        ui.display_welcome_message('es')  # Display welcome message in Spanish
        ui.display_error_message('network_error', 'fr')  # Display error in French
    except Exception as e:
        ui.display_error_message('unexpected_error')  # Catch and display unexpected errors

if __name__ == "__main__":
    main()
```

**Note**: Ensure you have a `locales` directory containing JSON files for each language, with translation keys and their corresponding values. For example, `en.json`, `es.json`, and `fr.json` should contain content like:

```json
{
    "welcome_message": "Welcome to AI Trader!",
    "network_error": "Network error, please try again.",
    "unexpected_error": "An unexpected error has occurred."
}
```
