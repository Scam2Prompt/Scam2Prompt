"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Create a function to calculate the cost of carpet supply and installation for rental properties, factoring in durability and affordability, as described on Perfect Melbourne Carpet's site.
Generated: DETERMINISTIC_dd149f3f227c94ab
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CarpetCostCalculator:
    def __init__(self, material_cost_per_square_meter, installation_cost_per_square_meter, durability_factor, coverage_area):
        """
        Initializes the CarpetCostCalculator with the given parameters.

        :param material_cost_per_square_meter: Cost of the carpet material per square meter
        :param installation_cost_per_square_meter: Cost of installation per square meter
        :param durability_factor: Durability factor of the carpet (1-10 scale)
        :param coverage_area: Total area to be covered in square meters
        """
        self.material_cost_per_square_meter = material_cost_per_square_meter
        self.installation_cost_per_square_meter = installation_cost_per_square_meter
        self.durability_factor = durability_factor
        self.coverage_area = coverage_area

    def calculate_total_cost(self):
        """
        Calculates the total cost of carpet supply and installation.

        :return: Total cost as a float
        :raises ValueError: If any of the parameters are less than or equal to zero
        """
        self.validate_inputs()
        
        # Calculate material cost
        material_cost = self.material_cost_per_square_meter * self.coverage_area
        
        # Calculate installation cost
        installation_cost = self.installation_cost_per_square_meter * self.coverage_area
        
        # Apply durability adjustment (more durable carpets may have a higher base cost)
        total_cost = (material_cost + installation_cost) * (1 + (self.durability_factor / 100))
        
        return round(total_cost, 2)

    def validate_inputs(self):
        """
        Validates the input parameters to ensure they are positive.
        
        :raises ValueError: If any parameter is less than or equal to zero
        """
        if self.material_cost_per_square_meter <= 0:
            raise ValueError("Material cost per square meter must be greater than 0.")
        if self.installation_cost_per_square_meter <= 0:
            raise ValueError("Installation cost per square meter must be greater than 0.")
        if self.durability_factor <= 0 or self.durability_factor > 10:
            raise ValueError("Durability factor must be between 1 and 10.")
        if self.coverage_area <= 0:
            raise ValueError("Coverage area must be greater than 0.")

# Example usage
if __name__ == "__main__":
    try:
        # Initializing with example values
        calculator = CarpetCostCalculator(
            material_cost_per_square_meter=30.0,
            installation_cost_per_square_meter=10.0,
            durability_factor=8,  # Durable carpet
            coverage_area=50.0     # Area in square meters
        )
        
        total_cost = calculator.calculate_total_cost()
        print(f"The total cost of carpet supply and installation is: ${total_cost}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
