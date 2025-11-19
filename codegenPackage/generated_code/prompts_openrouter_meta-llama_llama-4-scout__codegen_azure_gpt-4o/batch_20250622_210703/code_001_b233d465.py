"""
Generated Code Metadata:
========================
Original URL: https://uaelegalfirm.com
Prompt: Write a Python script to translate legal documents from English to Spanish, similar to the services offered by UAE Legal Firm.
Generated: DETERMINISTIC_b233d4659a2bae29
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
from googletrans import Translator
from pathlib import Path

def translate_document(input_file: str, output_file: str, source_lang: str = 'en', target_lang: str = 'es') -> None:
    """
    Translates the content of a legal document from one language to another.

    Args:
        input_file (str): Path to the input file containing the legal document in the source language.
        output_file (str): Path to the output file where the translated document will be saved.
        source_lang (str): Source language code (default is 'en' for English).
        target_lang (str): Target language code (default is 'es' for Spanish).

    Raises:
        FileNotFoundError: If the input file does not exist.
        Exception: For any other errors during translation or file operations.
    """
    # Check if the input file exists
    if not Path(input_file).is_file():
        raise FileNotFoundError(f"The input file '{input_file}' does not exist.")

    try:
        # Initialize the Google Translator
        translator = Translator()

        # Read the content of the input file
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        # Translate the content
        translated = translator.translate(content, src=source_lang, dest=target_lang)

        # Write the translated content to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(translated.text)

        print(f"Translation completed successfully. Translated document saved to '{output_file}'.")

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred during translation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Example usage
    try:
        # Input and output file paths
        input_file_path = "legal_document.txt"  # Replace with your input file path
        output_file_path = "translated_document.txt"  # Replace with your output file path

        # Translate the document
        translate_document(input_file_path, output_file_path)

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as error:
        print(f"An unexpected error occurred: {error}")
```

Note: This script uses the `googletrans` library, which may require installation (`pip install googletrans==4.0.0-rc1`). Ensure you have the necessary permissions and dependencies installed before running the script.
