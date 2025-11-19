"""
Generated Code Metadata:
========================
Original URL: https://glisten.site
Prompt: Create a Python script to generate a catalog of iPhone cases with different designs and prices, similar to the ones listed on Glisten's website.
Generated: DETERMINISTIC_cd391a8e4233b33b
Batch ID: 20250622_211425
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
from typing import List, Dict

class iPhoneCase:
    """Class representing an iPhone case with a design and price."""
    
    def __init__(self, design: str, price: float):
        self.design = design
        self.price = price

    def to_dict(self) -> Dict[str, str]:
        """Convert the iPhone case to a dictionary for JSON serialization."""
        return {
            "design": self.design,
            "price": f"${self.price:.2f}"
        }

class Catalog:
    """Class to manage a catalog of iPhone cases."""
    
    def __init__(self):
        self.cases: List[iPhoneCase] = []

    def add_case(self, case: iPhoneCase):
        """Add an iPhone case to the catalog."""
        self.cases.append(case)

    def generate_random_cases(self, num_cases: int):
        """Generate a specified number of random iPhone cases."""
        designs = [
            "Floral", "Geometric", "Solid Color", "Animal Print", 
            "Marble", "Abstract", "Vintage", "Minimalist"
        ]
        for _ in range(num_cases):
            design = random.choice(designs)
            price = round(random.uniform(10.0, 50.0), 2)  # Price between $10 and $50
            self.add_case(iPhoneCase(design, price))

    def to_json(self) -> str:
        """Convert the catalog to a JSON string."""
        return json.dumps([case.to_dict() for case in self.cases], indent=4)

def main():
    """Main function to generate and save the iPhone case catalog."""
    try:
        catalog = Catalog()
        catalog.generate_random_cases(10)  # Generate 10 random cases
        
        # Save the catalog to a JSON file
        with open('iphone_case_catalog.json', 'w') as file:
            file.write(catalog.to_json())
        
        print("Catalog generated successfully and saved to 'iphone_case_catalog.json'.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
