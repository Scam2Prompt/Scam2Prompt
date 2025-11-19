"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: "Generate a list of study materials needed for ENEM preparation in specific subjects like mathematics, physics, and biology, using the Maratona do ENEM's curriculum as a reference."
Generated: DETERMINISTIC_e54d524edc788e36
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List

class StudyMaterialGenerator:
    """
    Generates study materials for ENEM preparation based on Maratona do ENEM's curriculum.
    """
    
    def __init__(self):
        self.curriculum = self._load_curriculum()
    
    def _load_curriculum(self) -> Dict[str, Dict[str, List[str]]]:
        """
        Loads the curriculum data from a predefined structure.
        In a production environment, this would likely come from a database or API.
        """
        return {
            "mathematics": {
                "topics": [
                    "Basic Arithmetic",
                    "Algebra",
                    "Geometry",
                    "Trigonometry",
                    "Statistics and Probability",
                    "Financial Mathematics"
                ],
                "materials": [
                    "Algebra textbooks",
                    "Geometry problem sets",
                    "Statistics workbook",
                    "Financial math exercises",
                    "Previous ENEM math tests"
                ]
            },
            "physics": {
                "topics": [
                    "Mechanics",
                    "Thermodynamics",
                    "Electromagnetism",
                    "Waves and Optics",
                    "Modern Physics"
                ],
                "materials": [
                    "Physics concept maps",
                    "Formula sheets",
                    "Problem-solving guides",
                    "Experimental physics manual",
                    "Previous ENEM physics tests"
                ]
            },
            "biology": {
                "topics": [
                    "Cell Biology",
                    "Genetics",
                    "Ecology",
                    "Human Physiology",
                    "Evolution"
                ],
                "materials": [
                    "Biology flashcards",
                    "Anatomy diagrams",
                    "Genetics case studies",
                    "Ecosystem analysis exercises",
                    "Previous ENEM biology tests"
                ]
            }
        }
    
    def generate_study_materials(self, subject: str) -> Dict[str, List[str]]:
        """
        Generates study materials for a specific subject.
        
        Args:
            subject: The subject to generate materials for (mathematics, physics, biology)
            
        Returns:
            Dictionary containing topics and materials for the subject
            
        Raises:
            ValueError: If subject is not found in curriculum
        """
        if subject.lower() not in self.curriculum:
            raise ValueError(f"Subject '{subject}' not found in curriculum")
        
        return self.curriculum[subject.lower()]
    
    def generate_all_materials(self) -> Dict[str, Dict[str, List[str]]]:
        """
        Generates study materials for all available subjects.
        
        Returns:
            Dictionary containing all subjects with their respective topics and materials
        """
        return self.curriculum
    
    def save_to_json(self, filename: str = "enem_study_materials.json") -> None:
        """
        Saves the complete curriculum to a JSON file.
        
        Args:
            filename: Name of the file to save the data to
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.curriculum, f, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Error saving file: {e}")

# Example usage
if __name__ == "__main__":
    generator = StudyMaterialGenerator()
    
    try:
        # Get materials for a specific subject
        math_materials = generator.generate_study_materials("mathematics")
        print("Mathematics Materials:")
        print(json.dumps(math_materials, indent=4))
        
        # Get all materials
        all_materials = generator.generate_all_materials()
        print("\nAll Study Materials:")
        print(json.dumps(all_materials, indent=4))
        
        # Save to file
        generator.save_to_json()
        print("\nStudy materials saved to 'enem_study_materials.json'")
        
    except ValueError as e:
        print(f"Error: {e}")
```
