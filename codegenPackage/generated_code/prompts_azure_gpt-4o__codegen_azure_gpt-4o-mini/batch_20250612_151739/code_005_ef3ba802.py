"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Create a Python script to automate the generation of safety recommendations for accessing rooftops securely, inspired by AFCO's guidelines on preventing falls from heights.
Generated: DETERMINISTIC_ef3ba8022ad42fe3
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from typing import List, Dict

# Define a class to handle safety recommendations for rooftop access
class RooftopSafety:
    def __init__(self):
        # Load safety guidelines from a JSON file
        self.guidelines = self.load_guidelines()

    def load_guidelines(self) -> List[Dict[str, str]]:
        """
        Load safety guidelines from a JSON file.
        
        Returns:
            List[Dict[str, str]]: A list of safety recommendations.
        """
        try:
            with open('safety_guidelines.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Error: The safety guidelines file was not found.")
            return []
        except json.JSONDecodeError:
            print("Error: The safety guidelines file is not a valid JSON.")
            return []

    def get_random_recommendation(self) -> str:
        """
        Get a random safety recommendation from the guidelines.
        
        Returns:
            str: A random safety recommendation.
        """
        if not self.guidelines:
            return "No safety recommendations available."
        return random.choice(self.guidelines)['recommendation']

    def generate_recommendations(self, count: int) -> List[str]:
        """
        Generate a specified number of safety recommendations.
        
        Args:
            count (int): The number of recommendations to generate.
        
        Returns:
            List[str]: A list of safety recommendations.
        """
        if count <= 0:
            raise ValueError("Count must be a positive integer.")
        
        recommendations = []
        for _ in range(count):
            recommendations.append(self.get_random_recommendation())
        return recommendations

def main():
    """
    Main function to execute the rooftop safety recommendation generator.
    """
    safety = RooftopSafety()
    
    try:
        num_recommendations = int(input("Enter the number of safety recommendations to generate: "))
        recommendations = safety.generate_recommendations(num_recommendations)
        
        print("\nGenerated Safety Recommendations:")
        for idx, rec in enumerate(recommendations, start=1):
            print(f"{idx}. {rec}")
    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure you have a `safety_guidelines.json` file in the same directory as this script, containing safety recommendations in the following format:

```json
[
    {"recommendation": "Always use a safety harness when working on rooftops."},
    {"recommendation": "Ensure that all ladders are stable and secured."},
    {"recommendation": "Conduct a risk assessment before accessing the rooftop."}
]
```
