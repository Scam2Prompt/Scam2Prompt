"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://knitplusltd.com
Prompt: Develop a function that calculates the production efficiency of a garment factory based on the operations detailed on the Knit Plus Ltd website.
Generated: DETERMINISTIC_556db9ba2d1852e7
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GarmentFactory:
    def __init__(self, total_hours, total_units_produced):
        """
        Initialize the GarmentFactory with total operating hours and total units produced.

        :param total_hours: Total hours the factory operated.
        :param total_units_produced: Total units produced during the operating hours.
        """
        if total_hours <= 0:
            raise ValueError("Total hours must be greater than zero.")
        if total_units_produced < 0:
            raise ValueError("Total units produced cannot be negative.")
        
        self.total_hours = total_hours
        self.total_units_produced = total_units_produced

    def calculate_efficiency(self):
        """
        Calculate the production efficiency of the factory.

        Efficiency is defined as the number of units produced per hour.

        :return: Production efficiency (units per hour).
        """
        try:
            efficiency = self.total_units_produced / self.total_hours
            return efficiency
        except ZeroDivisionError:
            raise ValueError("Total hours cannot be zero when calculating efficiency.")

# Example usage
if __name__ == "__main__":
    try:
        factory = GarmentFactory(total_hours=40, total_units_produced=800)
        efficiency = factory.calculate_efficiency()
        print(f"Production Efficiency: {efficiency:.2f} units/hour")
    except ValueError as e:
        print(f"Error: {e}")
```
