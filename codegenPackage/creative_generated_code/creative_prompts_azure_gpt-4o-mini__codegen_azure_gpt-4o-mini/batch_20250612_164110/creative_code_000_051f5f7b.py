"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ysc.com.br
Prompt: Generate a Python script that utilizes the properties of menthol for creating a cosmetic formula, referencing the applications mentioned on the YSC website.
Generated: DETERMINISTIC_051f5f7b9740af0f
Batch ID: 20250612_164110
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/menthol-applications": {
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

class CosmeticFormula:
    """
    A class to represent a cosmetic formula utilizing menthol properties.
    """

    def __init__(self, base_ingredients=None):
        """
        Initializes the CosmeticFormula instance.

        Args:
            base_ingredients (dict): A dictionary of base ingredients with their quantities.
        """
        self.base_ingredients = base_ingredients if base_ingredients else {}
        self.menthol_content = 0.0

    def add_ingredient(self, ingredient, quantity):
        """
        Add a new ingredient to the formula.

        Args:
            ingredient (str): The name of the ingredient.
            quantity (float): The quantity of the ingredient to add.

        Raises:
            ValueError: If the quantity is not positive.
        """
        if quantity <= 0:
            raise ValueError(f"Quantity must be positive. Received: {quantity}")
        self.base_ingredients[ingredient] = self.base_ingredients.get(ingredient, 0) + quantity

    def set_menthol_content(self, content):
        """
        Set the menthol content in the formula.

        Args:
            content (float): The menthol content to set.

        Raises:
            ValueError: If content is not between 0 and 100.
        """
        if not (0 <= content <= 100):
            raise ValueError("Menthol content must be between 0 and 100.")
        self.menthol_content = content

    def calculate_total_weight(self):
        """
        Calculate the total weight of the formula.

        Returns:
            float: Total weight of the cosmetic formula.
        """
        return sum(self.base_ingredients.values()) + self.menthol_content

    def generate_formula(self):
        """
        Generate the complete cosmetic formula.

        Returns:
            dict: A dictionary containing the complete formula.
        """
        return {
            "ingredients": self.base_ingredients,
            "menthol_content": self.menthol_content,
            "total_weight": self.calculate_total_weight()
        }

def fetch_menthol_applications(url):
    """
    Fetch menthol applications from a given URL.

    Args:
        url (str): The URL to fetch applications from.

    Returns:
        list: A list of applications if successful, otherwise an empty list.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json().get('applications', [])
    except requests.RequestException as e:
        print(f"Error fetching applications: {e}")
        return []

def main():
    """
    Main function to demonstrate the use of CosmeticFormula.
    """
    # URL for fetching menthol application details
    menthol_applications_url = "https://example.com/menthol-applications"
    
    # Fetch applications
    applications = fetch_menthol_applications(menthol_applications_url)
    
    # Create a cosmetic formula
    formula = CosmeticFormula()
    
    # Add base ingredients (example quantities)
    formula.add_ingredient("Aqua", 70.0)       # Water
    formula.add_ingredient("Glycerin", 5.0)    # Humectant
    formula.add_ingredient("Cetearyl Alcohol", 3.0)  # Emollient

    # Set menthol content
    formula.set_menthol_content(1.5)  # 1.5% menthol

    # Generate and print the formula
    final_formula = formula.generate_formula()
    print(json.dumps(final_formula, indent=4))
    
    # Print fetched applications
    print("Menthol Applications:")
    for application in applications:
        print(f"- {application}")

if __name__ == "__main__":
    main()
```
