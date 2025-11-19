"""
Generated Code Metadata:
========================
Original URL: https://duct-split.com
Prompt: Develop a Python program to calculate the cooling area coverage for Gree duct split systems based on their BTU rating, using models like "Gree GU18T/AK(E)" and "Gree GU60T/AKa" as examples.
Generated: DETERMINISTIC_c53680f74c9c5557
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CoolingAreaCalculator:
    """
    A class to calculate the cooling area coverage for Gree duct split systems
    based on their BTU rating.
    """

    def __init__(self, btu_rating):
        """
        Initializes the CoolingAreaCalculator with a given BTU rating.

        :param btu_rating: The BTU rating of the cooling system.
        """
        if btu_rating <= 0:
            raise ValueError("BTU rating must be a positive number.")
        self.btu_rating = btu_rating

    def calculate_cooling_area(self):
        """
        Calculates the cooling area coverage based on the BTU rating.

        The general rule of thumb is that 1 ton of cooling (12,000 BTU) can cool
        approximately 400-600 square feet of space, depending on various factors.

        :return: The estimated cooling area in square feet.
        """
        # Constants for cooling area estimation
        BTU_PER_TON = 12000
        AREA_PER_TON_MIN = 400  # Minimum area coverage per ton
        AREA_PER_TON_MAX = 600  # Maximum area coverage per ton

        # Calculate the number of tons based on BTU rating
        tons = self.btu_rating / BTU_PER_TON

        # Calculate the cooling area coverage
        min_area = tons * AREA_PER_TON_MIN
        max_area = tons * AREA_PER_TON_MAX

        return min_area, max_area

def main():
    """
    Main function to execute the cooling area calculation for Gree duct split systems.
    """
    try:
        # Example BTU ratings for Gree models
        models_btu = {
            "Gree GU18T/AK(E)": 18000,
            "Gree GU60T/AKa": 60000
        }

        for model, btu in models_btu.items():
            print(f"Calculating cooling area for {model} with BTU rating: {btu}")
            calculator = CoolingAreaCalculator(btu)
            min_area, max_area = calculator.calculate_cooling_area()
            print(f"Estimated cooling area coverage: {min_area:.2f} - {max_area:.2f} square feet\n")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
