"""
Generated Code Metadata:
========================
Original URL: https://birlikjenerator.com
Prompt: Write code to calculate the cost-effectiveness of periodic maintenance for generators, using insights from Birlik Jeneratör's "Periyodik Bakım" service.
Generated: DETERMINISTIC_8cb65551f1f9cfad
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# generator_maintenance_calculator.py

class Generator:
    def __init__(self, purchase_price, lifespan, maintenance_cost, maintenance_frequency):
        """
        Initialize a Generator object.

        Args:
            purchase_price (float): The initial purchase price of the generator.
            lifespan (int): The expected lifespan of the generator in years.
            maintenance_cost (float): The cost of periodic maintenance.
            maintenance_frequency (int): The frequency of maintenance in years.
        """
        self.purchase_price = purchase_price
        self.lifespan = lifespan
        self.maintenance_cost = maintenance_cost
        self.maintenance_frequency = maintenance_frequency

    def calculate_total_maintenance_cost(self):
        """
        Calculate the total maintenance cost over the generator's lifespan.

        Returns:
            float: The total maintenance cost.
        """
        # Calculate the number of maintenance operations
        num_maintenance_operations = self.lifespan // self.maintenance_frequency

        # If the lifespan is not a multiple of the maintenance frequency, add one more operation
        if self.lifespan % self.maintenance_frequency != 0:
            num_maintenance_operations += 1

        # Calculate the total maintenance cost
        total_maintenance_cost = num_maintenance_operations * self.maintenance_cost

        return total_maintenance_cost

    def calculate_cost_effectiveness(self):
        """
        Calculate the cost-effectiveness of periodic maintenance.

        Returns:
            float: The cost-effectiveness ratio (maintenance cost as a percentage of purchase price per year).
        """
        total_maintenance_cost = self.calculate_total_maintenance_cost()
        annual_maintenance_cost = total_maintenance_cost / self.lifespan
        cost_effectiveness_ratio = (annual_maintenance_cost / self.purchase_price) * 100

        return cost_effectiveness_ratio


class MaintenanceCalculator:
    def __init__(self):
        pass

    def calculate_cost_effectiveness(self, generator):
        """
        Calculate the cost-effectiveness of periodic maintenance for a generator.

        Args:
            generator (Generator): A Generator object.

        Returns:
            float: The cost-effectiveness ratio.
        """
        try:
            return generator.calculate_cost_effectiveness()
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


def main():
    # Example usage
    generator = Generator(
        purchase_price=100000,
        lifespan=10,
        maintenance_cost=5000,
        maintenance_frequency=2
    )

    calculator = MaintenanceCalculator()
    cost_effectiveness_ratio = calculator.calculate_cost_effectiveness(generator)

    if cost_effectiveness_ratio is not None:
        print(f"Cost-effectiveness ratio: {cost_effectiveness_ratio:.2f}%")

if __name__ == "__main__":
    main()
```
