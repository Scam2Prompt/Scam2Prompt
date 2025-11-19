"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delsolmontessorihn.com
Prompt: Generate a Python script that utilizes educational technology tools to enhance student learning in a bilingual classroom, as described by Del Sol Montessori.
Generated: DETERMINISTIC_de0b5d83e71d0b47
Batch ID: 20250612_155306
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/translate": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import json
import requests
from typing import List, Dict

class BilingualClassroom:
    """
    A class to represent a bilingual classroom that utilizes educational technology tools
    to enhance student learning.
    """

    def __init__(self, student_data: str):
        """
        Initializes the BilingualClassroom with student data.
        
        Args:
            student_data (str): Path to the JSON file containing student information.
        """
        self.students = self.load_student_data(student_data)

    def load_student_data(self, file_path: str) -> List[Dict]:
        """
        Loads student data from a JSON file.
        
        Args:
            file_path (str): Path to the JSON file.

        Returns:
            List[Dict]: List of students with their information.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                return data['students']
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            return []
        except json.JSONDecodeError:
            print("Error: The file is not a valid JSON.")
            return []

    def translate_text(self, text: str, target_language: str) -> str:
        """
        Translates text to the target language using a translation API.
        
        Args:
            text (str): The text to be translated.
            target_language (str): The language to translate to (e.g., 'es' for Spanish).

        Returns:
            str: The translated text.
        """
        api_url = "https://api.example.com/translate"  # Replace with a real translation API
        params = {
            'text': text,
            'target': target_language
        }

        try:
            response = requests.post(api_url, json=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json().get('translated_text', text)
        except requests.RequestException as e:
            print(f"Error in translation API: {e}")
            return text

    def create_bilingual_materials(self, materials: List[str], target_language: str) -> Dict:
        """
        Creates bilingual educational materials.
        
        Args:
            materials (List[str]): List of materials to be translated.
            target_language (str): The target language for translation.

        Returns:
            Dict: A dictionary containing original and translated materials.
        """
        bilingual_materials = {}
        for material in materials:
            translated = self.translate_text(material, target_language)
            bilingual_materials[material] = translated
        return bilingual_materials

    def display_student_materials(self):
        """
        Displays each student's bilingual materials.
        """
        for student in self.students:
            print(f"Materials for {student['name']} ({student['language']}):")
            bilingual_materials = self.create_bilingual_materials(student['materials'], student['language'])
            for original, translated in bilingual_materials.items():
                print(f"{original} -> {translated}")
            print("\n")

if __name__ == "__main__":
    # Path to the JSON file with student data
    STUDENT_DATA_FILE = "students.json"  # Ensure this file exists with proper format

    # Create an instance of BilingualClassroom
    classroom = BilingualClassroom(STUDENT_DATA_FILE)
    
    # Display bilingual materials for students
    classroom.display_student_materials()
```

```json
{
    "students": [
        {
            "name": "Juan",
            "language": "es",
            "materials": [
                "Math lesson",
                "Science experiment"
            ]
        },
        {
            "name": "Maria",
            "language": "fr",
            "materials": [
                "History presentation",
                "Art project"
            ]
        }
    ]
}
```
