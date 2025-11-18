"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alexashipping.com
Prompt: Write code to calculate storage costs for warehousing solutions, referencing Alexa Shipping's approach to logistics and supply chain management.
Generated: DETERMINISTIC_a0747a2ed0d15830
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Warehouse:
    """
    A class to represent a warehouse and calculate storage costs.
    """

    def __init__(self, base_rate_per_sqft, area_sqft):
        """
        Initialize the warehouse with a base rate per square foot and total area.

        :param base_rate_per_sqft: float, the cost per square foot for storage
        :param area_sqft: float, the total area of the warehouse in square feet
        """
        self.base_rate_per_sqft = base_rate_per_sqft
        self.area_sqft = area_sqft

    def calculate_storage_cost(self, months):
        """
        Calculate the total storage cost for the given number of months.

        :param months: int, the number of months to calculate storage costs for
        :return: float, total storage cost
        :raises ValueError: if months is less than 1
        """
        if months < 1:
            raise ValueError("Number of months must be at least 1.")

        total_cost = self.base_rate_per_sqft * self.area_sqft * months
        return total_cost


def main():
    """
    Entry point of the storage cost calculation program.
    """
    try:
        # Example parameters for the warehouse
        base_rate = 1.50  # Cost per square foot
        area = 10000      # Total area in square feet
        months = 12       # Calculate for 12 months

        # Create a Warehouse instance
        warehouse = Warehouse(base_rate, area)

        # Calculate and print the storage cost
        storage_cost = warehouse.calculate_storage_cost(months)
        print(f"The total storage cost for {months} months is: ${storage_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
