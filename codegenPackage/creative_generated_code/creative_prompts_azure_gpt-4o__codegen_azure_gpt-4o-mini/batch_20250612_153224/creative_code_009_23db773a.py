"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munasimkullakita.org
Prompt: Create a script to automate the generation of educational materials for prevention programs targeting violence and exploitation, as described in Fundación Munasim Kullakita's initiatives.
Generated: DETERMINISTIC_23db773a26aac9a7
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
import json
import datetime
import logging

# Set up logging for the script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EducationalMaterialGenerator:
    def __init__(self, output_directory):
        """
        Initializes the EducationalMaterialGenerator with the specified output directory.
        
        :param output_directory: Directory where generated educational materials will be saved.
        """
        self.output_directory = output_directory
        os.makedirs(self.output_directory, exist_ok=True)  # Create directory if it does not exist

    def generate_material(self, title, content, target_audience):
        """
        Generates an educational material file in JSON format.
        
        :param title: Title of the educational material.
        :param content: Content or description of the educational material.
        :param target_audience: Intended audience for the material.
        :return: File path of the generated material.
        """
        try:
            # Prepare the material data
            material_data = {
                'title': title,
                'content': content,
                'target_audience': target_audience,
                'created_at': datetime.datetime.now().isoformat()
            }

            # Define file name and path
            file_name = f"{title.replace(' ', '_').lower()}.json"
            file_path = os.path.join(self.output_directory, file_name)

            # Write the material data to a JSON file
            with open(file_path, 'w', encoding='utf-8') as json_file:
                json.dump(material_data, json_file, ensure_ascii=False, indent=4)
            
            logging.info(f"Generated educational material: {file_path}")
            return file_path
        
        except Exception as e:
            logging.error(f"Error generating educational material: {e}")
            raise

if __name__ == "__main__":
    # Example usage of the EducationalMaterialGenerator class
    try:
        output_dir = "educational_materials"
        generator = EducationalMaterialGenerator(output_directory=output_dir)

        # Sample data for educational materials
        educational_materials = [
            {
                "title": "Understanding Violence Prevention",
                "content": "This material outlines the key strategies for preventing violence in communities.",
                "target_audience": "Community leaders, educators"
            },
            {
                "title": "Recognizing Exploitation",
                "content": "Learn how to recognize signs of exploitation in vulnerable populations.",
                "target_audience": "Social workers, volunteers"
            }
        ]

        # Generate materials
        for material in educational_materials:
            generator.generate_material(
                title=material['title'],
                content=material['content'],
                target_audience=material['target_audience']
            )

    except Exception as main_e:
        logging.error(f"An error occurred in the main process: {main_e}")
```
