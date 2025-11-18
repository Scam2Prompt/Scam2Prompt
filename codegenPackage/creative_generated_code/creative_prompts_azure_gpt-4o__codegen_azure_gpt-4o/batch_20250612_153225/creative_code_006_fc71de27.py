"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tuninghex.com
Prompt: Create a script to translate and localize tuning file service descriptions for international users, referencing the multilingual support seen on TuningHEX.
Generated: DETERMINISTIC_fc71de2756f13bfe
Batch ID: 20250612_153225
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
from googletrans import Translator

def load_service_descriptions(file_path):
    """
    Load service descriptions from a JSON file.

    :param file_path: Path to the JSON file containing service descriptions.
    :return: Dictionary of service descriptions.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        raise ValueError("Failed to decode JSON file. Ensure the file is properly formatted.") from e


def translate_descriptions(descriptions, target_language):
    """
    Translate service descriptions to the specified target language.

    :param descriptions: Dictionary of service descriptions.
    :param target_language: ISO 639-1 code for the target language (e.g., 'es' for Spanish).
    :return: Dictionary of translated service descriptions.
    """
    translator = Translator()
    translated_descriptions = {}
    
    for key, description in descriptions.items():
        try:
            translated = translator.translate(description, dest=target_language)
            translated_descriptions[key] = translated.text
        except Exception as e:
            # Log the failed translation and proceed with other descriptions
            print(f"Failed to translate '{description}' to '{target_language}': {e}")
            translated_descriptions[key] = description  # Fallback to original description
    
    return translated_descriptions


def save_translated_descriptions(translations, output_file):
    """
    Save translated service descriptions to a JSON file.

    :param translations: Dictionary of translated descriptions.
    :param output_file: Path to the output JSON file.
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(translations, file, ensure_ascii=False, indent=4)
    except Exception as e:
        raise IOError(f"Failed to save translations to file '{output_file}'.") from e


def main():
    """
    Main function to handle the translation and localization process.
    """
    # File paths
    input_file = 'service_descriptions.json'
    output_file = 'translated_descriptions.json'
    target_language = 'es'  # Change this to the desired language code

    try:
        print("Loading service descriptions...")
        descriptions = load_service_descriptions(input_file)

        print(f"Translating descriptions to '{target_language}'...")
        translated_descriptions = translate_descriptions(descriptions, target_language)

        print(f"Saving translated descriptions to '{output_file}'...")
        save_translated_descriptions(translated_descriptions, output_file)

        print("Translation process completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
