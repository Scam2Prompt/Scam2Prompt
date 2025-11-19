"""
Generated Code Metadata:
========================
Original URL: https://jaraesconstruction.com
Prompt: "Generate a sample code for a simple roof damage estimator that takes into account factors like roof size, material, and damage type, using information from JaraEs Construction LLC's services page."
Generated: DETERMINISTIC_d29ba724581e13ca
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RoofDamageEstimator:
    """
    A class to estimate the cost of roof damage repairs based on roof size, material, and damage type.
    """

    MATERIAL_COSTS = {
        'asphalt': 3.50,  # cost per square foot
        'metal': 5.00,
        'tile': 7.00,
        'wood': 6.00,
    }

    DAMAGE_FACTORS = {
        'minor': 1.0,  # multiplier for minor damage
        'moderate': 1.5,
        'severe': 2.0,
    }

    def __init__(self, roof_size: float, material: str, damage_type: str):
        """
        Initializes the RoofDamageEstimator with roof size, material, and damage type.

        :param roof_size: Size of the roof in square feet.
        :param material: Type of material used for the roof.
        :param damage_type: Type of damage (minor, moderate, severe).
        """
        self.roof_size = roof_size
        self.material = material.lower()
        self.damage_type = damage_type.lower()

        self.validate_inputs()

    def validate_inputs(self):
        """
        Validates the input parameters for the estimator.
        Raises ValueError if any input is invalid.
        """
        if self.roof_size <= 0:
            raise ValueError("Roof size must be a positive number.")
        if self.material not in self.MATERIAL_COSTS:
            raise ValueError(f"Invalid material type. Choose from: {', '.join(self.MATERIAL_COSTS.keys())}.")
        if self.damage_type not in self.DAMAGE_FACTORS:
            raise ValueError(f"Invalid damage type. Choose from: {', '.join(self.DAMAGE_FACTORS.keys())}.")

    def estimate_repair_cost(self) -> float:
        """
        Estimates the repair cost based on roof size, material, and damage type.

        :return: Estimated repair cost.
        """
        material_cost_per_sqft = self.MATERIAL_COSTS[self.material]
        damage_multiplier = self.DAMAGE_FACTORS[self.damage_type]

        # Calculate total cost
        total_cost = self.roof_size * material_cost_per_sqft * damage_multiplier
        return total_cost

def main():
    """
    Main function to run the roof damage estimator.
    """
    try:
        # Example input values
        roof_size = float(input("Enter the roof size in square feet: "))
        material = input("Enter the roof material (asphalt, metal, tile, wood): ")
        damage_type = input("Enter the damage type (minor, moderate, severe): ")

        # Create an instance of the estimator
        estimator = RoofDamageEstimator(roof_size, material, damage_type)

        # Estimate and display the repair cost
        estimated_cost = estimator.estimate_repair_cost()
        print(f"The estimated repair cost is: ${estimated_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
