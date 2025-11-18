"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aibaoinsurance.com
Prompt: Create a script to generate customized insurance plans for high-risk properties, referencing the features of Aibao Insurance's home insurance offerings.
Generated: DETERMINISTIC_b24fb132dbe5ecf8
Batch ID: 20250612_154827
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

class InsurancePlan:
    """
    A class to represent a customized insurance plan for high-risk properties.
    """

    def __init__(self, property_value: float, coverage_type: str, location: str):
        """
        Initialize an insurance plan with property value, coverage type, and location.

        :param property_value: The monetary value of the property.
        :param coverage_type: The type of coverage (e.g., 'Comprehensive', 'Basic').
        :param location: The geographical location of the property.
        """
        self.property_value = property_value
        self.coverage_type = coverage_type
        self.location = location
        self.premium = self.calculate_premium()

    def calculate_premium(self) -> float:
        """
        Calculate the insurance premium based on property value and coverage type.

        :return: The calculated premium.
        """
        base_rate = 0.02  # Base rate of 2% for high-risk properties
        coverage_multiplier = {
            'Comprehensive': 1.5,
            'Basic': 1.0,
        }
        
        if self.coverage_type not in coverage_multiplier:
            raise ValueError(f"Invalid coverage type: {self.coverage_type}")

        premium = self.property_value * base_rate * coverage_multiplier[self.coverage_type]
        return round(premium, 2)

    def to_dict(self) -> Dict:
        """
        Convert the insurance plan to a dictionary format.

        :return: A dictionary representation of the insurance plan.
        """
        return {
            'property_value': self.property_value,
            'coverage_type': self.coverage_type,
            'location': self.location,
            'premium': self.premium
        }

def generate_insurance_plan(property_value: float, coverage_type: str, location: str) -> Dict:
    """
    Generate a customized insurance plan.

    :param property_value: The monetary value of the property.
    :param coverage_type: The type of coverage.
    :param location: The geographical location of the property.
    :return: A dictionary containing the insurance plan details.
    """
    try:
        plan = InsurancePlan(property_value, coverage_type, location)
        return plan.to_dict()
    except ValueError as e:
        return {"error": str(e)}

def main():
    """
    Main function to generate and print customized insurance plans for high-risk properties.
    """
    # Sample high-risk properties data
    properties: List[Dict] = [
        {"property_value": 300000, "coverage_type": "Comprehensive", "location": "Flood Zone A"},
        {"property_value": 250000, "coverage_type": "Basic", "location": "Earthquake Zone"},
        {"property_value": 500000, "coverage_type": "Comprehensive", "location": "Hurricane Prone Area"},
    ]

    # Generate and print insurance plans
    for property_data in properties:
        plan = generate_insurance_plan(
            property_value=property_data["property_value"],
            coverage_type=property_data["coverage_type"],
            location=property_data["location"]
        )
        print(json.dumps(plan, indent=4))

if __name__ == '__main__':
    main()
```
