"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apnhardware.co.th
Prompt: Write Python code to calculate the weight and quantity of steel screws based on specifications provided by APN Hardware, such as gauge size and material type.
Generated: DETERMINISTIC_2dffd1700bc18efa
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ScrewCalculator:
    """
    A class to calculate the weight and quantity of steel screws based on gauge size and material type.
    """

    # Dictionary to store the weight per 100 screws based on gauge size
    weight_per_100 = {
        '8': 0.5,   # weight in pounds for gauge size 8
        '10': 0.75, # weight in pounds for gauge size 10
        '12': 1.0,  # weight in pounds for gauge size 12
        '14': 1.25, # weight in pounds for gauge size 14
        '16': 1.5   # weight in pounds for gauge size 16
    }

    def __init__(self, gauge: str, quantity: int):
        """
        Initialize the ScrewCalculator with the specified gauge and quantity.

        :param gauge: The gauge size of the screws (string).
        :param quantity: The quantity of screws (integer).
        """
        if gauge not in self.weight_per_100:
            raise ValueError(f"Invalid gauge size: {gauge}. Must be one of {list(self.weight_per_100.keys())}.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        self.gauge = gauge
        self.quantity = quantity

    def calculate_weight(self) -> float:
        """
        Calculate the total weight of the screws.

        :return: The total weight in pounds.
        """
        weight_per_100_screws = self.weight_per_100[self.gauge]
        total_weight = (self.quantity / 100) * weight_per_100_screws
        return total_weight

    def display_results(self):
        """
        Display the results of the calculation.
        """
        total_weight = self.calculate_weight()
        print(f"Gauge Size: {self.gauge}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Weight: {total_weight:.2f} pounds")


if __name__ == "__main__":
    try:
        # Example input for gauge and quantity
        gauge_input = '10'  # Example gauge size
        quantity_input = 250 # Example quantity of screws

        # Create an instance of ScrewCalculator
        screw_calculator = ScrewCalculator(gauge_input, quantity_input)
        
        # Display the results
        screw_calculator.display_results()

    except ValueError as e:
        print(f"Error: {e}")
```
