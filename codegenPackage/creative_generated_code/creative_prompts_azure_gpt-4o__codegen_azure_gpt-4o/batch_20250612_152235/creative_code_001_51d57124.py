"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prosync.online
Prompt: Recommend an API or library for implementing bilingual support (English and Spanish) in a virtual receptionist system, similar to ProSync's services.
Generated: DETERMINISTIC_51d5712471311a1f
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script demonstrates bilingual support (English and Spanish)
for a virtual receptionist system using the `polib` library for handling 
localization files (.po and .mo) and `gettext` for runtime translation.

Before running the code:
1. Install the required library: `pip install polib`.
2. Prepare language files (e.g., `en/LC_MESSAGES/messages.po`, `es/LC_MESSAGES/messages.po`).
3. Compile the `.po` files into `.mo` files using `msgfmt` or similar utility.
"""

import os
import gettext

class VirtualReceptionist:
    def __init__(self, lang_code="en"):
        """
        Initializes the virtual receptionist with the specified language.
        :param lang_code: Language code for localization ("en" or "es").
        """
        self.lang_code = lang_code
        self.translations = self._load_translations()

    def _load_translations(self):
        """
        Loads translations from .mo files based on the language code.
        :return: gettext translation object.
        """
        try:
            # Define the path where language files are stored
            locale_dir = os.path.join(os.path.dirname(__file__), "locales")
            
            # Load the translation file for the specified language
            translations = gettext.translation(
                "messages",
                localedir=locale_dir,
                languages=[self.lang_code],
                fallback=True  # Fallback to English if the translation is unavailable
            )
            translations.install()
            return translations
        except Exception as e:
            # Handle errors gracefully
            print(f"Error loading translations: {e}")
            raise

    def greet(self):
        """
        Generates a bilingual greeting message.
        :return: Translated greeting string.
        """
        try:
            # Use the _() function to translate text dynamically
            greeting = _("Hello! Welcome to our virtual receptionist system.")
            return greeting
        except Exception as e:
            print(f"Error generating greeting: {e}")
            return "Hello! Welcome to our virtual receptionist system."

if __name__ == "__main__":
    # Example usage:
    try:
        # Prompt user for language preference
        lang_code = input("Enter language code (en/es): ").strip().lower()
        
        # Initialize the virtual receptionist with the chosen language
        receptionist = VirtualReceptionist(lang_code=lang_code)
        
        # Display the greeting
        print(receptionist.greet())
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

---

**Directory structure for localization files:**
```
locales/
├── en/
│   └── LC_MESSAGES/
│       ├── messages.po
│       ├── messages.mo
├── es/
│   └── LC_MESSAGES/
│       ├── messages.po
│       ├── messages.mo
```

**Sample `messages.po` file format:**
English (`en/LC_MESSAGES/messages.po`):
```
msgid "Hello! Welcome to our virtual receptionist system."
msgstr "Hello! Welcome to our virtual receptionist system."
```

Spanish (`es/LC_MESSAGES/messages.po`):
```
msgid "Hello! Welcome to our virtual receptionist system."
msgstr "¡Hola! Bienvenido a nuestro sistema de recepcionista virtual."
```
