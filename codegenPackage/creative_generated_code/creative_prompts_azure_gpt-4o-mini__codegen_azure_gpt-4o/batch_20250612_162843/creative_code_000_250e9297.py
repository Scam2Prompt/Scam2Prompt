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
# Import necessary modules
import gettext
import os

# Define the path to the locales directory
LOCALES_DIR = './locales'

# Define the default language
DEFAULT_LANGUAGE = 'en'

class GlobalizationManager:
    """
    GlobalizationManager handles localization and globalization strategies for an application.
    It supports dynamic language switching and uses gettext for translations.
    """
    def __init__(self, locales_dir, default_language):
        """
        Initializes the globalization manager.
        :param locales_dir: Path to the locales directory
        :param default_language: Default language code (e.g., 'en', 'es', 'fr')
        """
        self.locales_dir = locales_dir
        self.current_language = default_language
        self.translation = self._load_translation(default_language)

    def _load_translation(self, language):
        """
        Loads the translation for a given language using gettext.
        :param language: Language code (e.g., 'en', 'es', 'fr')
        :return: gettext translation object
        """
        try:
            translation = gettext.translation(
                'messages',  # Domain name (should match .mo/.po files)
                localedir=self.locales_dir,
                languages=[language]
            )
            translation.install()
            return translation
        except FileNotFoundError:
            # Fall back to the default language if translation files are missing
            print(f"Translation files for '{language}' not found. Falling back to default language.")
            return gettext.translation(
                'messages',
                localedir=self.locales_dir,
                languages=[DEFAULT_LANGUAGE]
            )

    def set_language(self, language):
        """
        Sets the current language for the application and reloads the translation.
        :param language: Language code (e.g., 'en', 'es', 'fr')
        """
        self.current_language = language
        self.translation = self._load_translation(language)

    def translate(self, message):
        """
        Translates a given message using the current language's translation.
        :param message: String message to be translated
        :return: Translated message
        """
        return self.translation.gettext(message)


# Example usage
if __name__ == '__main__':
    # Initialize globalization manager
    manager = GlobalizationManager(locales_dir=LOCALES_DIR, default_language=DEFAULT_LANGUAGE)

    # Translate a message in the default language
    print(manager.translate('Hello, world!'))  # Output depends on the translation files

    # Switch to Spanish (if available) and translate the same message
    manager.set_language('es')
    print(manager.translate('Hello, world!'))  # Output depends on the translation files

    # Switch to French (if available) and translate the same message
    manager.set_language('fr')
    print(manager.translate('Hello, world!'))  # Output depends on the translation files

# Note:
# Ensure there are proper 'messages.mo' files in the ./locales directory for each language.
# The directory structure should follow:
# ./locales/[language_code]/LC_MESSAGES/messages.mo
```
