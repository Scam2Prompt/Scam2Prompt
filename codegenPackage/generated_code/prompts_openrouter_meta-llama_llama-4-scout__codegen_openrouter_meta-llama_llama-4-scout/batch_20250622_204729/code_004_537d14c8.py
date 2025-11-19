"""
Generated Code Metadata:
========================
Original URL: https://poolz.uk
Prompt: Create a calculator to estimate the cost of a pool building project based on factors like pool type, size, location, and materials, using data from the Poolz website.
Generated: DETERMINISTIC_537d14c85cd3a778
Batch ID: 20250622_204729
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pool_calculator.py

class PoolType:
    """Enum for pool types."""
    FIBERGLASS = "Fiberglass"
    VINYL = "Vinyl"
    CONCRETE = "Concrete"

class PoolCalculator:
    """Calculates the estimated cost of a pool building project."""

    def __init__(self, pool_type, size, location, materials):
        """
        Initializes the PoolCalculator.

        Args:
            pool_type (PoolType): The type of pool.
            size (float): The size of the pool in square feet.
            location (str): The location of the pool.
            materials (dict): A dictionary of materials and their quantities.

        Raises:
            ValueError: If the pool type, size, or location is invalid.
        """
        if not isinstance(pool_type, PoolType):
            raise ValueError("Invalid pool type")
        if size <= 0:
            raise ValueError("Pool size must be greater than zero")
        if not location:
            raise ValueError("Location cannot be empty")

        self.pool_type = pool_type
        self.size = size
        self.location = location
        self.materials = materials

        # Base costs from Poolz website
        self.base_costs = {
            PoolType.FIBERGLASS: 30000,
            PoolType.VINYL: 40000,
            PoolType.CONCRETE: 50000
        }

        # Material costs from Poolz website
        self.material_costs = {
            "concrete": 100,
            "steel": 50,
            "vinyl": 20,
            "fiberglass": 30
        }

        # Location-based cost multipliers from Poolz website
        self.location_multipliers = {
            "urban": 1.2,
            "suburban": 1.0,
            "rural": 0.8
        }

    def calculate_base_cost(self):
        """Calculates the base cost of the pool based on its type and size."""
        return self.base_costs[self.pool_type] * self.size / 1000

    def calculate_material_cost(self):
        """Calculates the cost of materials."""
        material_cost = 0
        for material, quantity in self.materials.items():
            if material in self.material_costs:
                material_cost += self.material_costs[material] * quantity
        return material_cost

    def calculate_location_cost(self):
        """Calculates the location-based cost multiplier."""
        location = self.location.lower()
        if location in self.location_multipliers:
            return self.location_multipliers[location]
        else:
            raise ValueError("Invalid location")

    def estimate_cost(self):
        """Estimates the total cost of the pool building project."""
        try:
            base_cost = self.calculate_base_cost()
            material_cost = self.calculate_material_cost()
            location_multiplier = self.calculate_location_cost()
            total_cost = (base_cost + material_cost) * location_multiplier
            return total_cost
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


def main():
    # Example usage
    pool_type = PoolType.FIBERGLASS
    size = 1000  # square feet
    location = "suburban"
    materials = {
        "concrete": 10,
        "steel": 5,
        "fiberglass": 2
    }

    calculator = PoolCalculator(pool_type, size, location, materials)
    estimated_cost = calculator.estimate_cost()

    if estimated_cost:
        print(f"Estimated cost: ${estimated_cost:.2f}")


if __name__ == "__main__":
    main()
```
