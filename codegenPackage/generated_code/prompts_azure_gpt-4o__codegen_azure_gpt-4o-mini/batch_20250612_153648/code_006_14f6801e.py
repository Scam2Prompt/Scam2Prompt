"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Create a Python function to generate structured interior design plans based on client preferences, referencing the structure interior designing services provided by Remas Engineering Consultants.
Generated: DETERMINISTIC_14f6801e6ac7413b
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Any, List

class InteriorDesignPlan:
    def __init__(self, client_name: str, preferences: Dict[str, Any]):
        """
        Initialize the InteriorDesignPlan with client name and preferences.

        :param client_name: Name of the client
        :param preferences: A dictionary containing client preferences
        """
        self.client_name = client_name
        self.preferences = preferences
        self.plan = {}

    def generate_plan(self) -> Dict[str, Any]:
        """
        Generate a structured interior design plan based on client preferences.

        :return: A dictionary representing the interior design plan
        """
        try:
            self.plan['client_name'] = self.client_name
            self.plan['design_style'] = self.preferences.get('design_style', 'Modern')
            self.plan['color_scheme'] = self.preferences.get('color_scheme', 'Neutral')
            self.plan['room_layout'] = self.preferences.get('room_layout', 'Open Concept')
            self.plan['furniture'] = self.preferences.get('furniture', [])
            self.plan['budget'] = self.preferences.get('budget', 10000)

            # Validate the generated plan
            self.validate_plan()

            return self.plan
        except Exception as e:
            raise RuntimeError(f"Error generating design plan: {str(e)}")

    def validate_plan(self):
        """
        Validate the generated design plan to ensure all required fields are present.

        :raises ValueError: If any required field is missing or invalid
        """
        required_fields = ['client_name', 'design_style', 'color_scheme', 'room_layout', 'budget']
        for field in required_fields:
            if field not in self.plan or not self.plan[field]:
                raise ValueError(f"Missing or invalid field: {field}")

    def save_plan_to_file(self, filename: str) -> None:
        """
        Save the generated design plan to a JSON file.

        :param filename: The name of the file to save the plan
        :raises IOError: If there is an error writing to the file
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.plan, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving design plan to file: {str(e)}")

# Example usage
if __name__ == "__main__":
    client_preferences = {
        'design_style': 'Contemporary',
        'color_scheme': 'Blue and White',
        'room_layout': 'Zoned',
        'furniture': ['Sofa', 'Coffee Table', 'Dining Table'],
        'budget': 15000
    }

    try:
        design_plan = InteriorDesignPlan(client_name='John Doe', preferences=client_preferences)
        generated_plan = design_plan.generate_plan()
        print("Generated Design Plan:", generated_plan)
        design_plan.save_plan_to_file('design_plan.json')
        print("Design plan saved to 'design_plan.json'")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
