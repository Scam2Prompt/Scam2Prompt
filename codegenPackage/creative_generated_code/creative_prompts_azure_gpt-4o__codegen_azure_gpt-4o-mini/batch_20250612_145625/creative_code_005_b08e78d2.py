"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remix-ipfs-eths.com
Prompt: Generate a script to list all available languages supported by the Mailcow UI and allow users to select their preferred language dynamically.
Generated: DETERMINISTIC_b08e78d20fc08680
Batch ID: 20250612_145625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json

class LanguageSelector:
    """
    A class to handle the selection of available languages for the Mailcow UI.
    """

    def __init__(self, languages_file):
        """
        Initializes the LanguageSelector with the path to the languages JSON file.
        
        :param languages_file: Path to the JSON file containing language data.
        """
        self.languages_file = languages_file
        self.languages = self.load_languages()

    def load_languages(self):
        """
        Loads the available languages from the provided JSON file.
        
        :return: A dictionary of available languages.
        """
        try:
            with open(self.languages_file, 'r', encoding='utf-8') as file:
                languages = json.load(file)
                return languages
        except FileNotFoundError:
            print("Error: The languages file was not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: The languages file is not valid JSON.")
            return {}

    def display_languages(self):
        """
        Displays the available languages to the user.
        """
        if not self.languages:
            print("No languages available.")
            return

        print("Available Languages:")
        for index, lang in enumerate(self.languages.keys(), start=1):
            print(f"{index}. {lang}")

    def select_language(self):
        """
        Prompts the user to select a language from the available options.
        """
        self.display_languages()

        try:
            choice = int(input("Select your preferred language by number: "))
            selected_language = list(self.languages.keys())[choice - 1]
            print(f"You have selected: {selected_language}")
            return selected_language
        except (ValueError, IndexError):
            print("Invalid selection. Please enter a valid number.")

def main():
    """
    Main function to run the LanguageSelector.
    """
    languages_file_path = 'path/to/languages.json'  # Update with the actual path to your languages file
    language_selector = LanguageSelector(languages_file_path)
    language_selector.select_language()

if __name__ == "__main__":
    main()
```

Make sure to replace `'path/to/languages.json'` with the actual path to your languages JSON file before running the script.
