"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://privnote.co
Prompt: Suggest a method to implement multi-language support for a self-destructing note application, referencing the language options available on privnote.co.
Generated: DETERMINISTIC_1f0c46c8debe56e0
Batch ID: 20250612_153849
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


class MultiLanguageSupport:
    """
    A class to implement multi-language support for a self-destructing note application.
    """

    def __init__(self, language: str = "en"):
        """
        Initializes the MultiLanguageSupport class with the desired language.

        :param language: The language code ("en", "es", "fr", etc.). Defaults to "en" (English).
        """
        self.supported_languages = ["en", "es", "fr", "de", "it", "pt"]  # Example supported languages
        self.language = language if language in self.supported_languages else "en"
        self.translations = self.load_translations()

    def load_translations(self) -> dict:
        """
        Loads translations from a JSON file corresponding to the selected language.

        :return: A dictionary of translations for the current language.
        """
        try:
            # Path to translation files (e.g., "translations/en.json")
            file_path = os.path.join("translations", f"{self.language}.json")
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Translation file for '{self.language}' not found. Using default language (English).")
            self.language = "en"
            return self.load_translations()
        except json.JSONDecodeError:
            print(f"Error decoding translation file for '{self.language}'. Using default language (English).")
            self.language = "en"
            return self.load_translations()

    def translate(self, key: str) -> str:
        """
        Retrieves the translated text for the given key.

        :param key: The translation key.
        :return: The translated text if the key exists; otherwise, returns the key itself.
        """
        return self.translations.get(key, key)


# Example usage
if __name__ == "__main__":
    # Initialize multi-language support with Spanish ("es")
    language_support = MultiLanguageSupport("es")

    # Example keys
    print(language_support.translate("note_title"))  # Translated text for "note_title"
    print(language_support.translate("delete_confirmation"))  # Translated text for "delete_confirmation"
    print(language_support.translate("non_existent_key"))  # Fallback to key if translation doesn't exist
```

### Instructions:
1. Create a `translations` folder in the same directory as this script.
2. Add JSON files for each supported language (e.g., `en.json`, `es.json`, etc.) with key-value pairs for translations.
   - Example for `en.json`:
     ```json
     {
         "note_title": "Self-Destructing Note",
         "delete_confirmation": "Are you sure you want to delete this note?"
     }
     ```
   - Example for `es.json`:
     ```json
     {
         "note_title": "Nota autodestructiva",
         "delete_confirmation": "¿Estás seguro de que quieres eliminar esta nota?"
     }
     ```
