"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trentino.edu.pe
Prompt: Develop a script to analyze and manage modular certifications for students, similar to the "Certificaciones Modulares" system described on the Trentino website.
Generated: DETERMINISTIC_e65f89dedef7e2c3
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any, Optional

class Certification:
    """Class to represent a student's modular certification."""
    
    def __init__(self, student_id: str, module_name: str, score: float) -> None:
        """Initialize a new Certification instance.

        Args:
            student_id (str): The unique identifier for the student.
            module_name (str): The name of the module for the certification.
            score (float): The score obtained by the student in the module.
        """
        self.student_id = student_id
        self.module_name = module_name
        self.score = score
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the Certification instance to a dictionary.

        Returns:
            Dict[str, Any]: Dictionary representation of the certification.
        """
        return {
            "student_id": self.student_id,
            "module_name": self.module_name,
            "score": self.score
        }

class CertificationManager:
    """Manager class for handling certifications for students."""
    
    def __init__(self) -> None:
        """Initialize the CertificationManager with an empty certification list."""
        self.certifications: List[Certification] = []
        
    def add_certification(self, certification: Certification) -> None:
        """Add a new certification to the manager.

        Args:
            certification (Certification): The certification to add.
        """
        self.certifications.append(certification)
    
    def get_certification(self, student_id: str, module_name: str) -> Optional[Certification]:
        """Retrieve a certification by student ID and module name.

        Args:
            student_id (str): The unique identifier for the student.
            module_name (str): The name of the module.

        Returns:
            Optional[Certification]: The certification if found, otherwise None.
        """
        for cert in self.certifications:
            if cert.student_id == student_id and cert.module_name == module_name:
                return cert
        return None

    def save_certifications(self, file_path: str) -> None:
        """Save the certifications to a JSON file.

        Args:
            file_path (str): The path where the certification data will be saved.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump([cert.to_dict() for cert in self.certifications], json_file, indent=4)
        except IOError as e:
            print(f"Error saving certifications to file: {e}")
    
    def load_certifications(self, file_path: str) -> None:
        """Load certifications from a JSON file.

        Args:
            file_path (str): The path from where to load the certification data.
        """
        try:
            with open(file_path, 'r') as json_file:
                certifications_data = json.load(json_file)
                self.certifications = [Certification(**data) for data in certifications_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading certifications from file: {e}")

# Example usage:
if __name__ == "__main__":
    manager = CertificationManager()
    
    # Add sample certifications
    manager.add_certification(Certification("student123", "Math101", 85.0))
    manager.add_certification(Certification("student456", "Physics101", 90.5))
    
    # Save certifications to a file
    manager.save_certifications("certifications.json")
    
    # Load certifications from a file
    manager.load_certifications("certifications.json")
    
    # Retrieve a specific certification
    cert = manager.get_certification("student123", "Math101")
    if cert:
        print(f"Retrieved certification: {cert.to_dict()}")
    else:
        print("Certification not found.")
```
