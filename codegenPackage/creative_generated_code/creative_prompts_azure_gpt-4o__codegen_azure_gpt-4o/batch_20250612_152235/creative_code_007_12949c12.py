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
import json

class VirtualReceptionist:
    """
    A class to implement multilingual support for a virtual receptionist system.
    """

    def __init__(self, language_data_file="languages.json", default_language="en"):
        """
        Initialize the VirtualReceptionist with language data and a default language.

        :param language_data_file: Path to the JSON file containing language data.
        :param default_language: Default language code (e.g., 'en' for English).
        """
        self.default_language = default_language
        self.languages = {}
        self.current_language = default_language

        try:
            # Load language data from JSON file
            with open(language_data_file, "r", encoding="utf-8") as file:
                self.languages = json.load(file)
        except FileNotFoundError:
            raise ValueError(f"Language data file '{language_data_file}' not found.")
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON language data file.")

        # Ensure default language exists in loaded languages
        if default_language not in self.languages:
            raise ValueError(f"Default language '{default_language}' not found in language file.")

    def set_language(self, language_code):
        """
        Set the current language for the receptionist.

        :param language_code: Language code to set (e.g., 'es' for Spanish).
        :raises ValueError: If the language code is not supported.
        """
        if language_code in self.languages:
            self.current_language = language_code
        else:
            raise ValueError(f"Language '{language_code}' is not supported.")

    def get_message(self, message_key):
        """
        Retrieve the translated message based on the current language.

        :param message_key: Key for the message (e.g., 'greeting').
        :return: Translated message.
        :raises KeyError: If the message key is not found in the selected language.
        """
        try:
            return self.languages[self.current_language][message_key]
        except KeyError:
            raise KeyError(f"Message key '{message_key}' not found in language '{self.current_language}'.")

    def greet(self):
        """
        Return the receptionist's greeting message.
        
        :return: Greeting message based on current language.
        """
        return self.get_message("greeting")


# Example usage
if __name__ == "__main__":
    """
    Example JSON language file structure:
    languages.json:
    {
        "en": {
            "greeting": "Hello! How can I assist you today?",
            "farewell": "Goodbye! Have a great day!"
        },
        "es": {
            "greeting": "¡Hola! ¿Cómo puedo ayudarte hoy?",
            "farewell": "¡Adiós! ¡Que tengas un gran día!"
        },
        "fr": {
            "greeting": "Bonjour ! Comment puis-je vous aider aujourd'hui ?",
            "farewell": "Au revoir ! Passez une bonne journée !"
        }
    }
    """
    try:
        # Initialize the receptionist system
        receptionist = VirtualReceptionist(language_data_file="languages.json")

        # Set language to Spanish and get greeting
        receptionist.set_language("es")
        print(receptionist.greet())  # Output: ¡Hola! ¿Cómo puedo ayudarte hoy?

        # Switch language to French and get greeting
        receptionist.set_language("fr")
        print(receptionist.greet())  # Output: Bonjour ! Comment puis-je vous aider aujourd'hui ?

        # Switch back to English and get greeting
        receptionist.set_language("en")
        print(receptionist.greet())  # Output: Hello! How can I assist you today?

    except Exception as e:
        print(f"Error: {e}")
```
