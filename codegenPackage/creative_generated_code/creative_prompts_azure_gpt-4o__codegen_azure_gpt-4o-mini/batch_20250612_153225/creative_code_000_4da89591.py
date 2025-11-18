"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://efeitoharmonie.com.br
Prompt: Write Python code to calculate the average number of hair follicles per unit based on the FUE technique described on the Efeito Harmonie website, assuming 01 to 06 hairs per follicle with an average of 2.5 hairs per follicle.
Generated: DETERMINISTIC_4da89591ad28fa11
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HairFollicleCalculator:
    """Class to calculate the average number of hair follicles per unit."""

    def __init__(self, min_hairs_per_follicle=1, max_hairs_per_follicle=6, average_hairs=2.5):
        """Initialize the calculator with specified parameters.

        Args:
            min_hairs_per_follicle (int): Minimum hairs per follicle (default is 1).
            max_hairs_per_follicle (int): Maximum hairs per follicle (default is 6).
            average_hairs (float): Average number of hairs per follicle (default is 2.5).
        """
        self.min_hairs_per_follicle = min_hairs_per_follicle
        self.max_hairs_per_follicle = max_hairs_per_follicle
        self.average_hairs = average_hairs

    def calculate_average_follicles(self, units):
        """Calculate the average number of hair follicles per unit.

        Args:
            units (int): The number of units to calculate follicles for.

        Returns:
            float: The average number of hair follicles per unit.

        Raises:
            ValueError: If the number of units is not a positive integer.
        """
        if not isinstance(units, int) or units <= 0:
            raise ValueError("The number of units must be a positive integer.")

        # Calculate the average follicles per unit based on the average hairs per follicle
        average_follicles = self.average_hairs * units
        return average_follicles


def main():
    """Main function to execute the hair follicle calculation."""
    try:
        # Create an instance of the HairFollicleCalculator
        calculator = HairFollicleCalculator()

        # Define the number of units to calculate for (example: 10 units)
        units = 10

        # Calculate and print the average number of hair follicles per unit
        average_follicles = calculator.calculate_average_follicles(units)
        print(f"Average number of hair follicles per unit for {units} units: {average_follicles:.2f}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
