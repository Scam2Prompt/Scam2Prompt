"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://novaforma.hr
Prompt: Write a Python script that automates the design process for a totem display based on the guidelines provided by Nova Forma.
Generated: DETERMINISTIC_19cd79a0f920a2b0
Batch ID: 20250612_160853
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
from typing import List, Dict

class TotemDisplayDesigner:
    def __init__(self, design_guidelines: Dict):
        """
        Initializes the TotemDisplayDesigner with the provided design guidelines.

        :param design_guidelines: A dictionary containing design specifications.
        """
        self.guidelines = design_guidelines

    def validate_guidelines(self) -> bool:
        """
        Validates the design guidelines to ensure all necessary keys are present.

        :return: True if guidelines are valid, False otherwise.
        """
        required_keys = ['height', 'width', 'material', 'color_scheme', 'content']
        for key in required_keys:
            if key not in self.guidelines:
                print(f"Missing required guideline: {key}")
                return False
        return True

    def create_design(self) -> Dict:
        """
        Creates a totem display design based on the guidelines.

        :return: A dictionary containing the designed totem display.
        """
        if not self.validate_guidelines():
            raise ValueError("Invalid design guidelines provided.")

        # Design logic based on guidelines
        design = {
            'height': self.guidelines['height'],
            'width': self.guidelines['width'],
            'material': self.guidelines['material'],
            'color_scheme': self.guidelines['color_scheme'],
            'content': self.guidelines['content'],
            'created_at': self.get_current_time(),
            'status': 'Design Created'
        }
        return design

    @staticmethod
    def get_current_time() -> str:
        """
        Returns the current time in ISO format.

        :return: Current time as a string.
        """
        from datetime import datetime
        return datetime.now().isoformat()

    def save_design(self, design: Dict, file_path: str) -> None:
        """
        Saves the created design to a JSON file.

        :param design: The design dictionary to save.
        :param file_path: The path where the design should be saved.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(design, json_file, indent=4)
            print(f"Design saved to {file_path}.")
        except IOError as e:
            print(f"Error saving design: {e}")

def main():
    guidelines = {
        'height': 200,
        'width': 100,
        'material': 'Wood',
        'color_scheme': ['Blue', 'White'],
        'content': {
            'title': 'Welcome to Nova Forma',
            'description': 'Innovative Designs for Your Space'
        }
    }

    designer = TotemDisplayDesigner(guidelines)
    
    try:
        design = designer.create_design()
        output_file = 'totem_display_design.json'
        designer.save_design(design, output_file)
    except ValueError as ve:
        print(f"Design creation failed: {ve}")

if __name__ == '__main__':
    main()
```
