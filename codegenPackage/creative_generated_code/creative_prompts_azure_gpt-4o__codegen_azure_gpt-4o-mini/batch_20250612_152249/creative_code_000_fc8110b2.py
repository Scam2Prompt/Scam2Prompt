"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ruxindustrial.com.br
Prompt: Write Python code to calculate the cost of industrial maintenance services based on the types of materials used, referencing the classifications mentioned on the Rux Industrial website.
Generated: DETERMINISTIC_fc8110b2faf3adeb
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MaintenanceService:
    """
    A class to represent the maintenance service costs based on materials used.
    """

    # Define a dictionary for material costs
    MATERIAL_COSTS = {
        "standard": 100,  # Cost in currency units
        "premium": 200,
        "eco_friendly": 150,
        "custom": 300
    }

    def __init__(self, material_type, quantity):
        """
        Initializes the MaintenanceService with material type and quantity.

        :param material_type: str - The type of material used for maintenance
        :param quantity: int - The quantity of materials used
        """
        self.material_type = material_type
        self.quantity = quantity

    def validate_material_type(self):
        """
        Validates the material type against the defined material costs.

        :raises ValueError: if the material type is not recognized
        """
        if self.material_type not in self.MATERIAL_COSTS:
            raise ValueError(f"Invalid material type: {self.material_type}. "
                             f"Must be one of {list(self.MATERIAL_COSTS.keys())}.")

    def calculate_cost(self):
        """
        Calculates the total cost based on material type and quantity.

        :return: float - Total cost of the maintenance service
        :raises ValueError: if the quantity is less than or equal to zero
        """
        # Validate the material type
        self.validate_material_type()

        # Validate quantity
        if self.quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        # Calculate and return total cost
        total_cost = self.MATERIAL_COSTS[self.material_type] * self.quantity
        return total_cost


def main():
    """
    Main function to run the maintenance service cost calculation.
    """
    try:
        # Example input values
        material_type = "premium"  # Change to desired material type
        quantity = 5                # Change to desired quantity

        # Create a MaintenanceService instance
        service = MaintenanceService(material_type, quantity)

        # Calculate the total cost
        total_cost = service.calculate_cost()
        print(f"The total cost for {quantity} units of {material_type} material is: {total_cost} currency units.")

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
