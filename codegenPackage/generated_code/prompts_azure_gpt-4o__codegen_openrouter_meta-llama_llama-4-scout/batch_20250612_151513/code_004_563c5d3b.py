"""
Generated Code Metadata:
========================
Original URL: https://hispanicservices.com
Prompt: Develop a program to translate text into multiple languages using APIs, ensuring the translations are professional and accurate, as described in the certified translation services provided by Hispanic Services.
Generated: DETERMINISTIC_563c5d3b98bcdfcf
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import json
from googletrans import Translator, LANGUAGES

# Set up Google Translate API
def setup_translator():
    """
    Initialize the Google Translate API.

    Returns:
        Translator: The initialized translator object.
    """
    try:
        translator = Translator()
        return translator
    except Exception as e:
        print(f"Error setting up translator: {e}")
        return None

# Translate text using Google Translate API
def translate_text(translator, text, src_language, dest_language):
    """
    Translate text from source language to destination language.

    Args:
        translator (Translator): The initialized translator object.
        text (str): The text to be translated.
        src_language (str): The source language code.
        dest_language (str): The destination language code.

    Returns:
        str: The translated text.
    """
    try:
        result = translator.translate(text, src=src_language, dest=dest_language)
        return result.text
    except Exception as e:
        print(f"Error translating text: {e}")
        return None

# Get language codes and names
def get_language_codes():
    """
    Get a dictionary of language codes and names.

    Returns:
        dict: A dictionary of language codes and names.
    """
    return LANGUAGES

# Main function
def main():
    # Set up translator
    translator = setup_translator()

    if translator is None:
        return

    # Get language codes
    language_codes = get_language_codes()
    print("Available languages:")
    for code, name in language_codes.items():
        print(f"{code}: {name}")

    # Input text to translate
    text = input("Enter the text to translate: ")

    # Input source language
    src_language = input("Enter the source language code (e.g., en): ")

    # Input destination languages
    dest_languages = input("Enter the destination language codes (e.g., es,fr): ").split(",")

    # Translate text
    for dest_language in dest_languages:
        dest_language = dest_language.strip()
        translated_text = translate_text(translator, text, src_language, dest_language)

        if translated_text is not None:
            print(f"Translated text in {language_codes[dest_language]} ({dest_language}):")
            print(translated_text)

if __name__ == "__main__":
    main()
```
