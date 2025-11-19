"""
Generated Code Metadata:
========================
Original URL: https://munasimkullakita.org
Prompt: Create a script to automate the generation of educational materials for prevention programs targeting violence and exploitation, as described in Fundación Munasim Kullakita's initiatives.
Generated: DETERMINISTIC_23db773a26aac9a7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EducationalMaterialGenerator:
    def __init__(self, output_directory):
        """
        Initializes the EducationalMaterialGenerator with the specified output directory.

        :param output_directory: Directory where generated materials will be saved.
        """
        self.output_directory = output_directory
        self.materials = []

        # Ensure the output directory exists
        os.makedirs(self.output_directory, exist_ok=True)

    def load_initiatives(self, json_file):
        """
        Loads initiatives from a JSON file.

        :param json_file: Path to the JSON file containing initiatives data.
        :raises FileNotFoundError: If the specified file does not exist.
        :raises json.JSONDecodeError: If the file is not a valid JSON.
        """
        try:
            with open(json_file, 'r') as file:
                self.materials = json.load(file)
                logging.info(f"Loaded {len(self.materials)} initiatives from {json_file}.")
        except FileNotFoundError as e:
            logging.error(f"File not found: {json_file}. Error: {e}")
            raise
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON from file: {json_file}. Error: {e}")
            raise

    def generate_material(self, initiative):
        """
        Generates educational material for a given initiative.

        :param initiative: A dictionary containing initiative data.
        :return: A string representing the content of the educational material.
        """
        title = initiative.get('title', 'Untitled Initiative')
        description = initiative.get('description', 'No description available.')
        target_audience = initiative.get('target_audience', 'General Public')
        prevention_methods = initiative.get('prevention_methods', [])

        material_content = f"Title: {title}\n"
        material_content += f"Description: {description}\n"
        material_content += f"Target Audience: {target_audience}\n"
        material_content += "Prevention Methods:\n"

        for method in prevention_methods:
            material_content += f"- {method}\n"

        return material_content

    def save_material(self, content, title):
        """
        Saves the generated material content to a text file.

        :param content: The content to save.
        :param title: The title of the initiative, used for the filename.
        """
        filename = f"{title.replace(' ', '_').replace('/', '_')}.txt"
        filepath = os.path.join(self.output_directory, filename)

        with open(filepath, 'w') as file:
            file.write(content)
            logging.info(f"Saved material to {filepath}.")

    def generate_all_materials(self):
        """
        Generates and saves educational materials for all loaded initiatives.
        """
        for initiative in self.materials:
            try:
                material_content = self.generate_material(initiative)
                self.save_material(material_content, initiative.get('title', 'Untitled Initiative'))
            except Exception as e:
                logging.error(f"Failed to generate material for initiative: {initiative}. Error: {e}")

if __name__ == "__main__":
    # Example usage
    output_dir = "educational_materials"
    json_file_path = "initiatives.json"  # Path to the JSON file containing initiatives

    generator = EducationalMaterialGenerator(output_directory=output_dir)

    try:
        generator.load_initiatives(json_file_path)
        generator.generate_all_materials()
    except Exception as e:
        logging.critical(f"An error occurred during the generation process: {e}")
```

Make sure to create a `initiatives.json` file with the appropriate structure before running the script. The JSON file should contain a list of initiatives, each represented as a dictionary with keys like `title`, `description`, `target_audience`, and `prevention_methods`.
