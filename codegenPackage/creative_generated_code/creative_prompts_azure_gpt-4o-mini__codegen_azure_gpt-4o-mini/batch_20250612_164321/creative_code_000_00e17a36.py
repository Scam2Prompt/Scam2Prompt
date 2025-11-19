"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.twigacementgroup.com
Prompt: Generate a Python script that utilizes the Twiga Extra cement specifications to calculate the required amount for a construction project based on given dimensions.
Generated: DETERMINISTIC_00e17a3615c3b182
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class CementCalculator:
    """
    A class to calculate the required amount of Twiga Extra cement
    based on given dimensions for a construction project.
    """
    
    def __init__(self, volume_per_bag=0.035):
        """
        Initializes the CementCalculator with the volume per bag of cement.

        :param volume_per_bag: Volume of cement in cubic meters per bag, default is 0.035
        """
        self.volume_per_bag = volume_per_bag

    def calculate_bags_needed(self, length, width, height):
        """
        Calculate the number of cement bags required.

        :param length: Length of the area in meters
        :param width: Width of the area in meters
        :param height: Height of the area in meters
        :return: Number of cement bags required
        """
        try:
            # Validate input dimensions
            if length <= 0 or width <= 0 or height <= 0:
                raise ValueError("Dimensions must be greater than zero.")

            # Calculate volume in cubic meters
            volume = length * width * height

            # Calculate number of bags needed
            bags_needed = volume / self.volume_per_bag
            
            # Round up to ensure enough bags are purchased
            bags_needed = int(bags_needed) + (1 if bags_needed % 1 > 0 else 0)

            return bags_needed
        except ValueError as ve:
            print(f"Input error: {ve}")
            sys.exit(1)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)

def main():
    """
    Main function to execute the cement calculation based on user input.
    """
    # Create an instance of CementCalculator
    calculator = CementCalculator()

    try:
        # User input for dimensions
        length = float(input("Enter the length of the area in meters: "))
        width = float(input("Enter the width of the area in meters: "))
        height = float(input("Enter the height of the area in meters: "))

        # Calculate and display the required bags of cement
        bags_needed = calculator.calculate_bags_needed(length, width, height)
        print(f"You will need {bags_needed} bags of Twiga Extra cement.")
    
    except ValueError as ve:
        print(f"Input error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
