"""
Generated Code Metadata:
========================
Original URL: https://generate-digital.com
Prompt: Create a digital sales proposition for a sports business, including a compelling pitch and sales support materials, using insights from fan data and digital inventory management.
Generated: DETERMINISTIC_13a79b75cb7a12f5
Batch ID: 20250622_205436
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

class SportsBusinessSalesProposition:
    def __init__(self, business_name: str, fan_data: List[Dict], digital_inventory: List[Dict]):
        """
        Initializes the SportsBusinessSalesProposition with the business name, fan data, and digital inventory.

        :param business_name: Name of the sports business
        :param fan_data: List of dictionaries containing fan insights
        :param digital_inventory: List of dictionaries containing digital inventory items
        """
        self.business_name = business_name
        self.fan_data = fan_data
        self.digital_inventory = digital_inventory

    def generate_pitch(self) -> str:
        """
        Generates a compelling sales pitch based on fan insights and digital inventory.

        :return: A string containing the sales pitch
        """
        target_audience = self.analyze_fan_data()
        unique_selling_points = self.get_unique_selling_points()

        pitch = (
            f"Welcome to {self.business_name}!\n"
            f"Our fans are our greatest asset. We have identified key insights from our fan data:\n"
            f"- Target Audience: {target_audience}\n"
            f"- Unique Selling Points: {unique_selling_points}\n\n"
            "We invite you to explore our digital inventory that aligns perfectly with our fans' interests.\n"
            "Join us in creating unforgettable experiences for our fans!"
        )
        return pitch

    def analyze_fan_data(self) -> str:
        """
        Analyzes fan data to identify the target audience.

        :return: A string summarizing the target audience
        """
        age_groups = {}
        for fan in self.fan_data:
            age = fan.get('age')
            if age:
                age_groups[age] = age_groups.get(age, 0) + 1

        # Identify the most common age group
        target_age_group = max(age_groups, key=age_groups.get)
        return f"Predominantly aged {target_age_group}"

    def get_unique_selling_points(self) -> List[str]:
        """
        Extracts unique selling points from the digital inventory.

        :return: A list of unique selling points
        """
        return [item['description'] for item in self.digital_inventory if 'description' in item]

    def create_sales_support_materials(self) -> Dict[str, str]:
        """
        Creates sales support materials based on the digital inventory.

        :return: A dictionary containing sales support materials
        """
        materials = {}
        for item in self.digital_inventory:
            materials[item['id']] = (
                f"Item: {item['name']}\n"
                f"Description: {item['description']}\n"
                f"Price: ${item['price']}\n"
                f"Available Stock: {item['stock']}\n"
            )
        return materials

    def save_proposition_to_file(self, filename: str) -> None:
        """
        Saves the sales proposition and support materials to a JSON file.

        :param filename: The name of the file to save the proposition
        """
        try:
            proposition = {
                "pitch": self.generate_pitch(),
                "sales_support_materials": self.create_sales_support_materials()
            }
            with open(filename, 'w') as file:
                json.dump(proposition, file, indent=4)
            print(f"Sales proposition saved to {filename}")
        except IOError as e:
            print(f"Error saving the sales proposition: {e}")

# Example usage
if __name__ == "__main__":
    # Sample fan data
    fan_data = [
        {"age": 25, "name": "Alice"},
        {"age": 30, "name": "Bob"},
        {"age": 25, "name": "Charlie"},
        {"age": 35, "name": "David"},
    ]

    # Sample digital inventory
    digital_inventory = [
        {"id": 1, "name": "VIP Game Pass", "description": "Access to all home games with VIP seating.", "price": 150, "stock": 100},
        {"id": 2, "name": "Team Merchandise", "description": "Official team jersey.", "price": 75, "stock": 200},
        {"id": 3, "name": "Exclusive Content Subscription", "description": "Monthly exclusive content and interviews.", "price": 10, "stock": 500},
    ]

    # Create a sales proposition
    sales_proposition = SportsBusinessSalesProposition("Awesome Sports Co.", fan_data, digital_inventory)
    sales_proposition.save_proposition_to_file("sales_proposition.json")
```
