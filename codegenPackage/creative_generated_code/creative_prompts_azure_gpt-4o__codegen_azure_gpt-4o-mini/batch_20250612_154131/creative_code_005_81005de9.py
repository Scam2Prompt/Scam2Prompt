"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://risingstarintl.com
Prompt: Develop a script to calculate monthly production capacity for a garment manufacturer with two units capable of producing 50,000 to 100,000 items per month, as described on Rising Star International's website.
Generated: DETERMINISTIC_81005de9a7fc88f7
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GarmentManufacturer:
    def __init__(self, unit_count: int, min_capacity: int, max_capacity: int):
        """
        Initializes the GarmentManufacturer with specified parameters.

        :param unit_count: Number of production units
        :param min_capacity: Minimum production capacity per unit
        :param max_capacity: Maximum production capacity per unit
        """
        self.unit_count = unit_count
        self.min_capacity = min_capacity
        self.max_capacity = max_capacity

    def calculate_monthly_capacity(self) -> dict:
        """
        Calculates the total monthly production capacity range.

        :return: A dictionary containing the minimum and maximum capacity
        """
        try:
            total_min_capacity = self.unit_count * self.min_capacity
            total_max_capacity = self.unit_count * self.max_capacity
            capacity_range = {
                'minimum_capacity': total_min_capacity,
                'maximum_capacity': total_max_capacity
            }
            return capacity_range
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating capacity: {e}")

def main():
    # Configuration for Rising Star International
    unit_count = 2  # Number of production units
    min_capacity = 50000  # Minimum items produced per month per unit
    max_capacity = 100000  # Maximum items produced per month per unit

    # Create an instance of GarmentManufacturer
    garment_manufacturer = GarmentManufacturer(unit_count, min_capacity, max_capacity)

    # Calculate and print monthly production capacity
    try:
        capacity = garment_manufacturer.calculate_monthly_capacity()
        print(f"Monthly Production Capacity: {capacity['minimum_capacity']} to {capacity['maximum_capacity']} items")
    except RuntimeError as e:
        print(e)

if __name__ == "__main__":
    main()
```
