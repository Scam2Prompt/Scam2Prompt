"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asphaltsc.cl
Prompt: Write a Python function that utilizes eco-friendly materials for asphalt recovery and maintenance, as described by Asphalt Solutions Chile.
Generated: DETERMINISTIC_9c1c73c2ca0a051b
Batch ID: 20250612_155845
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EcoFriendlyAsphalt:
    def __init__(self, material_type, quantity):
        """
        Initialize the EcoFriendlyAsphalt class.

        :param material_type: str, type of eco-friendly material used for asphalt recovery
        :param quantity: float, quantity of the material in tons
        """
        self.material_type = material_type
        self.quantity = quantity

    def validate_material(self):
        """
        Validate the type of eco-friendly material.

        :raises ValueError: If the material type is not recognized
        """
        valid_materials = ['recycled asphalt', 'bio-asphalt', 'warm-mix asphalt']
        if self.material_type.lower() not in valid_materials:
            raise ValueError(f"Invalid material type: {self.material_type}. "
                             f"Choose from {valid_materials}.")

    def calculate_cost(self):
        """
        Calculate the estimated cost for using the eco-friendly material.

        :return: float, estimated cost in USD
        """
        cost_per_ton = {
            'recycled asphalt': 50.0,  # Example price per ton
            'bio-asphalt': 70.0,
            'warm-mix asphalt': 60.0
        }
        return cost_per_ton[self.material_type.lower()] * self.quantity

    def prepare_material(self):
        """
        Prepare the eco-friendly material for use.

        :raises ValueError: If the quantity is not a positive number
        :return: str, preparation status
        """
        if self.quantity <= 0:
            raise ValueError("Quantity must be a positive number.")
        return f"{self.quantity} tons of {self.material_type} prepared for asphalt recovery."

    def recover_asphalt(self):
        """
        Perform asphalt recovery using the eco-friendly materials.

        :return: str, recovery status
        """
        try:
            self.validate_material()
            preparation_status = self.prepare_material()
            total_cost = self.calculate_cost()
            return (f"Recovery successful: {preparation_status}\n"
                    f"Total estimated cost: ${total_cost:.2f}")
        except ValueError as e:
            return f"Error during asphalt recovery: {str(e)}"


# Example usage:
if __name__ == "__main__":
    try:
        eco_asphalt = EcoFriendlyAsphalt('recycled asphalt', 25)
        result = eco_asphalt.recover_asphalt()
        print(result)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
