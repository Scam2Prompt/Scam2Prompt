"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-prime.com
Prompt: Develop a multilingual support system for an investment learning platform, ensuring seamless integration of Immediate Prime's supported languages.
Generated: DETERMINISTIC_eb442d2cb4534084
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class MultilingualSupport:
    """
    A class to handle multilingual support for an investment learning platform.
    """

    def __init__(self, language_file_path):
        """
        Initializes the multilingual support system by loading supported languages.
        
        :param language_file_path: Path to the JSON file containing language translations.
        """
        self.language_file_path = language_file_path
        self.translations = {}
        self.current_language = "en"  # Default language
        self.load_translations()

    def load_translations(self):
        """
        Loads translations from the specified JSON file.
        """
        try:
            with open(self.language_file_path, 'r', encoding='utf-8') as file:
                self.translations = json.load(file)
        except FileNotFoundError:
            print("Error: Language file not found. Please provide a valid path.")
            self.translations = {}
        except json.JSONDecodeError:
            print("Error: Failed to decode the language file. Ensure it contains valid JSON.")
            self.translations = {}
    
    def set_language(self, language_code):
        """
        Sets the current language for the platform.
        
        :param language_code: The language code to switch to (e.g., 'en', 'es').
        """
        if language_code in self.translations:
            self.current_language = language_code
        else:
            print(f"Error: Unsupported language code '{language_code}'. Defaulting to English.")
            self.current_language = "en"
    
    def get_translation(self, key):
        """
        Retrieves the translation for the given key in the current language.
        
        :param key: The key for the text to be translated.
        :return: Translated text in the current language, or the key if not found.
        """
        if self.current_language in self.translations:
            return self.translations[self.current_language].get(key, key)
        else:
            print(f"Warning: No translations found for language '{self.current_language}'. Using key as fallback.")
            return key
    
    def add_translation(self, language_code, key, translation):
        """
        Adds or updates a translation for a specific language.
        
        :param language_code: Language code to add/update (e.g., 'en', 'fr').
        :param key: The key for the text to be translated.
        :param translation: The translated text.
        """
        if language_code not in self.translations:
            self.translations[language_code] = {}
        
        self.translations[language_code][key] = translation
    
    def save_translations(self):
        """
        Saves the current translations back to the JSON file.
        """
        try:
            with open(self.language_file_path, 'w', encoding='utf-8') as file:
                json.dump(self.translations, file, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error: Failed to save translations. {str(e)}")

# Example usage
if __name__ == "__main__":
    # Initialize multilingual support system with a language file
    system = MultilingualSupport("languages.json")

    # Set the current language
    system.set_language("es")  # Switch to Spanish

    # Get a translation for a specific key
    translated_text = system.get_translation("welcome_message")
    print(translated_text)  # Print translated text

    # Add a new translation
    system.add_translation("fr", "welcome_message", "Bienvenue sur la plateforme d'apprentissage des investissements!")

    # Save the updated translations to the file
    system.save_translations()
```

**Note:** Make sure to create a `languages.json` file with appropriate language translations for testing this code.
