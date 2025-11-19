"""
Generated Code Metadata:
========================
Original URL: https://krosmetal.com
Prompt: "Write a code snippet to automate the process of generating quotes for custom stainless steel fabrication projects, considering factors like material cost, labor, and equipment usage."
Generated: DETERMINISTIC_3c4fe415e69b5118
Batch ID: 20250622_211159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class QuoteGenerator:
    """
    A class to generate quotes for custom stainless steel fabrication projects.
    """

    def __init__(self, material_cost_per_kg, labor_cost_per_hour, equipment_cost_per_hour):
        """
        Initialize the QuoteGenerator with cost parameters.

        :param material_cost_per_kg: Cost of stainless steel per kilogram.
        :param labor_cost_per_hour: Cost of labor per hour.
        :param equipment_cost_per_hour: Cost of equipment usage per hour.
        """
        self.material_cost_per_kg = material_cost_per_kg
        self.labor_cost_per_hour = labor_cost_per_hour
        self.equipment_cost_per_hour = equipment_cost_per_hour

    def calculate_quote(self, material_weight_kg, labor_hours, equipment_hours):
        """
        Calculate the total quote based on material weight, labor hours, and equipment hours.

        :param material_weight_kg: Weight of stainless steel required in kilograms.
        :param labor_hours: Number of labor hours required.
        :param equipment_hours: Number of equipment usage hours required.
        :return: Total quote as a dictionary.
        """
        try:
            # Calculate individual costs
            material_cost = material_weight_kg * self.material_cost_per_kg
            labor_cost = labor_hours * self.labor_cost_per_hour
            equipment_cost = equipment_hours * self.equipment_cost_per_hour

            # Calculate total cost
            total_cost = material_cost + labor_cost + equipment_cost

            # Return the breakdown and total cost
            return {
                "material_cost": round(material_cost, 2),
                "labor_cost": round(labor_cost, 2),
                "equipment_cost": round(equipment_cost, 2),
                "total_cost": round(total_cost, 2)
            }
        except Exception as e:
            # Handle any unexpected errors
            return {"error": str(e)}

    def save_quote_to_file(self, quote, filename="quote.json"):
        """
        Save the quote to a JSON file.

        :param quote: Quote dictionary to save.
        :param filename: Name of the file to save the quote to.
        """
        try:
            with open(filename, "w") as file:
                json.dump(quote, file, indent=4)
        except Exception as e:
            print(f"Error saving quote to file: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize the QuoteGenerator with cost parameters
    generator = QuoteGenerator(material_cost_per_kg=5.0, labor_cost_per_hour=20.0, equipment_cost_per_hour=15.0)

    # Generate a quote
    quote = generator.calculate_quote(material_weight_kg=50, labor_hours=10, equipment_hours=5)

    # Print the quote
    print("Generated Quote:", quote)

    # Save the quote to a file
    generator.save_quote_to_file(quote)
```
