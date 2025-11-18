"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dawah-smiraa.sa
Prompt: Write code to implement a multilingual outreach program, including tools for distributing educational materials like "منشورات ومطويات توعوية دعوية تثقيفية" in multiple languages.
Generated: DETERMINISTIC_6dc73e0f78ca4b8b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from typing import Dict, List

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class OutreachProgram:
    """
    A class to manage multilingual outreach programs and distribute educational materials.
    """

    def __init__(self, supported_languages: List[str]):
        """
        Initializes the program with supported languages.
        
        :param supported_languages: List of language codes supported (e.g., ['en', 'ar', 'es'])
        """
        self.supported_languages = supported_languages
        self.materials = {}  # Dictionary to store materials by language
        logging.info("OutreachProgram initialized.")

    def add_material(self, language: str, material: str):
        """
        Adds an educational material in a specific language.

        :param language: The language code of the material (e.g., 'ar', 'en')
        :param material: The content of the material
        :raises ValueError: If the language is not supported
        """
        if language not in self.supported_languages:
            raise ValueError(f"Language '{language}' is not supported.")
        
        if language not in self.materials:
            self.materials[language] = []
        
        self.materials[language].append(material)
        logging.info(f"Material added in language '{language}'.")

    def distribute_materials(self, language: str) -> List[str]:
        """
        Retrieves all materials in the specified language for distribution.

        :param language: The language code of the materials to distribute
        :return: List of materials in the requested language
        :raises ValueError: If the language is not supported
        """
        if language not in self.supported_languages:
            raise ValueError(f"Language '{language}' is not supported.")
        
        return self.materials.get(language, [])

    def save_materials_to_file(self, directory: str):
        """
        Saves all materials to files in the specified directory.

        Each file is named with the language code (e.g., 'ar.txt', 'en.txt').

        :param directory: Directory path where files will be saved
        :raises FileNotFoundError: If the directory does not exist
        """
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' does not exist.")
        
        for language, materials in self.materials.items():
            file_path = os.path.join(directory, f"{language}.txt")
            with open(file_path, "w", encoding="utf-8") as file:
                file.write("\n".join(materials))
            logging.info(f"Materials saved to '{file_path}'.")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the program with supported languages
        program = OutreachProgram(supported_languages=["en", "ar", "es"])

        # Add materials
        program.add_material("ar", "منشور توعوي باللغة العربية.")
        program.add_material("en", "Educational flyer in English.")
        program.add_material("es", "Folleto educativo en español.")
        
        # Distribute materials in Arabic
        arabic_materials = program.distribute_materials("ar")
        for material in arabic_materials:
            print(f"Arabic material: {material}")
        
        # Save all materials to files
        program.save_materials_to_file(directory="./materials")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
