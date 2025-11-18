"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-xzen.com
Prompt: Generate code to create a multilingual interface for an investment education platform, ensuring accessibility in languages like EN, BR, DA, DE, ES, FR, HU, IT, JA, NL, NO, PL, and SV, as seen on Immediate ZenX.
Generated: DETERMINISTIC_e1ae63d728f75123
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# multilingual_interface.py

import json

class MultilingualInterface:
    """
    A class to create and manage a multilingual user interface for an investment
    education platform.
    """

    def __init__(self, supported_languages):
        """
        Constructor to initialize the multilingual interface.
        
        Args:
            supported_languages (list): List of language codes supported by the platform.
        """
        self.supported_languages = supported_languages
        self.translations = {}

    def load_translations(self, file_path):
        """
        Load translation files from a JSON file.

        Args:
            file_path (str): Path to the JSON file containing translations.

        Raises:
            FileNotFoundError: If the JSON file does not exist.
            json.JSONDecodeError: If the JSON file is not properly formatted.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.translations = json.load(file)
        except FileNotFoundError:
            print(f"Error: Translation file not found at {file_path}")
            raise
        except json.JSONDecodeError:
            print(f"Error: Failed to parse translation file at {file_path}")
            raise

    def get_translation(self, key, language_code):
        """
        Retrieve the translation for a specific key in the desired language.

        Args:
            key (str): The key representing the text to be translated.
            language_code (str): The language code for the desired translation.

        Returns:
            str: The translated text if available, otherwise the key itself.
        """
        if language_code not in self.supported_languages:
            print(f"Warning: Language {language_code} is not supported.")
            return key
        
        return self.translations.get(language_code, {}).get(key, key)

if __name__ == "__main__":
    # Supported language codes
    SUPPORTED_LANGUAGES = [
        "EN", "BR", "DA", "DE", "ES", "FR", "HU", "IT", "JA", "NL", "NO", "PL", "SV"
    ]

    # Initialize the multilingual interface
    interface = MultilingualInterface(SUPPORTED_LANGUAGES)
    
    # Load translations from file (example translations.json file path provided)
    translation_file_path = "translations.json"
    try:
        interface.load_translations(translation_file_path)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Failed to initialize translations. Exiting...")
        exit(1)

    # Example usage
    language_code = "FR"  # French
    text_key = "welcome_message"

    # Get the translation for the specified language and key
    translated_text = interface.get_translation(text_key, language_code)
    print(translated_text)
```

### Example JSON Translation File (`translations.json`):
```json
{
    "EN": {
        "welcome_message": "Welcome to the Investment Education Platform!"
    },
    "FR": {
        "welcome_message": "Bienvenue sur la plateforme éducative d'investissement!"
    },
    "DE": {
        "welcome_message": "Willkommen auf der Bildungsplattform für Investitionen!"
    },
    "ES": {
        "welcome_message": "¡Bienvenido a la plataforma de educación de inversiones!"
    }
    // Add other languages here...
}
```
