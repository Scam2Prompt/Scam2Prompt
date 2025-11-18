"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atilumber.com
Prompt: Write a script to calculate the cost of timber products based on dimensions and species, referencing the categories of softwood, hardwood, and sawn timber from Askar Trading International.
Generated: DETERMINISTIC_a9cd3215e972cd59
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TimberCostCalculator:
    """
    A class to calculate the cost of timber products based on dimensions, species, and category.
    """
    
    # Pricing per cubic meter for different categories
    PRICE_LIST = {
        'softwood': 200,  # Example price for softwood
        'hardwood': 350,  # Example price for hardwood
        'sawn_timber': 250  # Example price for sawn timber
    }
    
    def __init__(self, species, length, width, height):
        """
        Initialize the TimberCostCalculator with species and dimensions.

        Args:
            species (str): The species of the timber (softwood, hardwood, sawn_timber).
            length (float): The length of the timber in meters.
            width (float): The width of the timber in meters.
            height (float): The height of the timber in meters.
        """
        self.species = species.lower()
        self.length = length
        self.width = width
        self.height = height

    def validate_input(self):
        """
        Validate the input parameters to ensure they are correct.

        Raises:
            ValueError: If species is not valid or dimensions are not positive.
        """
        if self.species not in TimberCostCalculator.PRICE_LIST:
            raise ValueError(f"Invalid species '{self.species}'. Valid options are {list(TimberCostCalculator.PRICE_LIST.keys())}.")
        
        if self.length <= 0 or self.width <= 0 or self.height <= 0:
            raise ValueError("Dimensions must be positive numbers.")

    def calculate_volume(self):
        """
        Calculate the volume of the timber in cubic meters.

        Returns:
            float: Volume of the timber.
        """
        return self.length * self.width * self.height

    def calculate_cost(self):
        """
        Calculate the total cost of the timber based on volume and species.

        Returns:
            float: Total cost of the timber.

        Raises:
            ValueError: If input validation fails.
        """
        self.validate_input()
        volume = self.calculate_volume()
        price_per_cubic_meter = TimberCostCalculator.PRICE_LIST[self.species]
        total_cost = volume * price_per_cubic_meter
        return total_cost


def main():
    """
    Main function to run the TimberCostCalculator based on user input.
    """
    try:
        # Example input: species, length, width, height
        species = input("Enter the species (softwood, hardwood, sawn_timber): ")
        length = float(input("Enter the length in meters: "))
        width = float(input("Enter the width in meters: "))
        height = float(input("Enter the height in meters: "))
        
        # Create a TimberCostCalculator instance
        calculator = TimberCostCalculator(species, length, width, height)
        
        # Calculate and display the total cost
        total_cost = calculator.calculate_cost()
        print(f"The total cost of the timber is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
