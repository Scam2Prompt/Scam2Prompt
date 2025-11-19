"""
Generated Code Metadata:
========================
Original URL: https://ethreum.ru
Prompt: Recommend APIs or libraries for implementing a multi-language support system, similar to the one offered by Casino R7, which supports 9 languages.
Generated: DETERMINISTIC_558b7d95c988b502
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates how to implement multi-language support in a Python application
using the `gettext` library. The approach is scalable and production-ready for supporting
multiple languages. The example includes error handling and follows best practices.
"""

import gettext
import os

class MultiLanguageSupport:
    """
    A class to manage multi-language support using gettext.
    """

    def __init__(self, locale_dir: str, default_language: str = "en"):
        """
        Initialize the MultiLanguageSupport class.

        :param locale_dir: Path to the directory containing language files.
        :param default_language: Default language code (e.g., 'en' for English).
        """
        self.locale_dir = locale_dir
        self.default_language = default_language
        self.current_language = default_language
        self.translator = None
        self._set_language(default_language)

    def _set_language(self, language: str):
        """
        Set the current language for the application.

        :param language: Language code (e.g., 'en', 'es', 'fr').
        """
        try:
            self.translator = gettext.translation(
                "messages", 
                localedir=self.locale_dir, 
                languages=[language]
            )
            self.translator.install()
            self.current_language = language
        except FileNotFoundError:
            # Fallback to default language if translation file is not found
            print(f"Warning: Translation file for '{language}' not found. Falling back to default language.")
            gettext.install("messages", localedir=self.locale_dir)
            self.current_language = self.default_language

    def change_language(self, language: str):
        """
        Change the application's language.

        :param language: Language code to switch to.
        """
        self._set_language(language)

    def get_current_language(self) -> str:
        """
        Get the current language code.

        :return: Current language code.
        """
        return self.current_language


# Example usage
if __name__ == "__main__":
    # Define the path to the locale directory
    LOCALE_DIR = os.path.join(os.path.dirname(__file__), "locales")

    # Initialize the multi-language support system
    language_support = MultiLanguageSupport(locale_dir=LOCALE_DIR, default_language="en")

    # Print a message in the default language
    print(_("Hello, world!"))

    # Change the language to Spanish
    language_support.change_language("es")

    # Print a message in Spanish
    print(_("Hello, world!"))

    # Change the language to French
    language_support.change_language("fr")

    # Print a message in French
    print(_("Hello, world!"))
```

### Notes:
1. **Directory Structure**: Ensure the `locales` directory contains subdirectories for each language (e.g., `en`, `es`, `fr`) with compiled `.mo` files inside `LC_MESSAGES`.
2. **Translation Files**: Use tools like `gettext` or `poedit` to create `.po` files and compile them into `.mo` files.
3. **Error Handling**: The code gracefully handles missing translation files by falling back to the default language.
