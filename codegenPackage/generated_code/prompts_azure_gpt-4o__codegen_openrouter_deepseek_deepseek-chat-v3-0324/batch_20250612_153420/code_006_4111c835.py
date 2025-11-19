"""
Generated Code Metadata:
========================
Original URL: https://mjpa.co.in
Prompt: Create a script to categorize pigments like chrome, oxide, and fluorescent pigments based on their industrial applications (e.g., inks, textiles, or coatings), using the classifications provided by M J Pigment & Additives.
Generated: DETERMINISTIC_4111c835d6f01fec
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class PigmentCategorizer:
    """
    A class to categorize pigments based on their industrial applications.
    Uses classifications from M J Pigment & Additives.
    """
    
    def __init__(self, classification_file: str = None):
        """
        Initialize the PigmentCategorizer with optional classification data.
        
        Args:
            classification_file (str, optional): Path to JSON file containing 
                pigment classifications. Defaults to built-in data.
        """
        self.classifications = {
            "chrome": ["inks", "coatings"],
            "oxide": ["textiles", "coatings", "plastics"],
            "fluorescent": ["textiles", "inks", "signage"]
        }
        
        if classification_file:
            self.load_classifications(classification_file)
    
    def load_classifications(self, file_path: str) -> None:
        """
        Load pigment classifications from a JSON file.
        
        Args:
            file_path (str): Path to the JSON file.
            
        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file is not valid JSON.
            ValueError: If the JSON structure is invalid.
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                
            if not isinstance(data, dict):
                raise ValueError("Classification data must be a dictionary")
                
            self.classifications = data
            
        except FileNotFoundError:
            raise FileNotFoundError(f"Classification file not found: {file_path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON file", file_path, 0)
    
    def get_applications(self, pigment_type: str) -> Optional[List[str]]:
        """
        Get industrial applications for a given pigment type.
        
        Args:
            pigment_type (str): Type of pigment (e.g., "chrome", "oxide").
            
        Returns:
            Optional[List[str]]: List of applications or None if not found.
        """
        return self.classifications.get(pigment_type.lower())
    
    def add_pigment_type(self, pigment_type: str, applications: List[str]) -> None:
        """
        Add or update a pigment type with its applications.
        
        Args:
            pigment_type (str): Name of the pigment type.
            applications (List[str]): List of industrial applications.
        """
        self.classifications[pigment_type.lower()] = applications
    
    def save_classifications(self, file_path: str) -> None:
        """
        Save current classifications to a JSON file.
        
        Args:
            file_path (str): Path to save the JSON file.
            
        Raises:
            IOError: If there's an issue writing the file.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.classifications, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save classifications: {e}")
    
    def categorize(self, pigment_type: str) -> Dict[str, Optional[List[str]]]:
        """
        Categorize a pigment and return its applications.
        
        Args:
            pigment_type (str): Type of pigment to categorize.
            
        Returns:
            Dict[str, Optional[List[str]]]: Dictionary with pigment type and applications.
        """
        applications = self.get_applications(pigment_type)
        return {
            "pigment_type": pigment_type,
            "applications": applications
        }


# Example usage
if __name__ == "__main__":
    try:
        categorizer = PigmentCategorizer()
        
        # Get applications for a pigment
        result = categorizer.categorize("oxide")
        print(f"Applications for {result['pigment_type']}: {result['applications']}")
        
        # Add a new pigment type
        categorizer.add_pigment_type("organic", ["inks", "textiles", "food"])
        
        # Save classifications to file
        categorizer.save_classifications("pigment_classifications.json")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
