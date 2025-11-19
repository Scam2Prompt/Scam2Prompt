"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trialsonicsolutions.com
Prompt: What specific contaminants can be effectively removed from auto parts using ultrasonic cleaning, and what are the recommended cleaning solutions?
Generated: DETERMINISTIC_c63cf15faaca546b
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class UltrasonicCleaner:
    """
    A class to represent an ultrasonic cleaner for auto parts.
    """

    def __init__(self):
        # Define common contaminants and their corresponding cleaning solutions
        self.cleaning_data = {
            "oil": "Alkaline detergent",
            "grease": "Solvent-based cleaner",
            "dirt": "Water and mild detergent",
            "rust": "Rust remover solution",
            "carbon": "Heavy-duty degreaser",
            "brake dust": "Brake cleaner",
            "contamination": "Ultrasonic cleaning fluid",
        }

    def get_contaminants(self) -> List[str]:
        """
        Returns a list of specific contaminants that can be removed from auto parts.
        """
        return list(self.cleaning_data.keys())

    def get_cleaning_solution(self, contaminant: str) -> str:
        """
        Returns the recommended cleaning solution for a specific contaminant.

        Args:
            contaminant (str): The contaminant for which to get the cleaning solution.

        Returns:
            str: The recommended cleaning solution.

        Raises:
            ValueError: If the contaminant is not recognized.
        """
        if contaminant not in self.cleaning_data:
            raise ValueError(f"Contaminant '{contaminant}' not recognized.")
        return self.cleaning_data[contaminant]

    def to_json(self) -> str:
        """
        Converts the cleaning data to JSON format.

        Returns:
            str: JSON representation of the cleaning data.
        """
        return json.dumps(self.cleaning_data, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        cleaner = UltrasonicCleaner()
        
        # Get a list of contaminants
        contaminants = cleaner.get_contaminants()
        print("Contaminants that can be removed from auto parts:")
        for contaminant in contaminants:
            print(f"- {contaminant}: {cleaner.get_cleaning_solution(contaminant)}")
        
        # Output cleaning data in JSON format
        print("\nCleaning Data in JSON Format:")
        print(cleaner.to_json())
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
