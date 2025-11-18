"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duct-split.com
Prompt: Develop a Python program to calculate the cooling area coverage for Gree duct split systems based on their BTU rating, using models like "Gree GU18T/AK(E)" and "Gree GU60T/AKa" as examples.
Generated: DETERMINISTIC_c53680f74c9c5557
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CoolingAreaCalculator:
    """
    A class to calculate the cooling area coverage for Gree duct split systems
    based on their BTU rating.

    Attributes:
        btu_rating (float): The BTU rating of the system.
    """

    def __init__(self, btu_rating):
        """
        Initializes a new instance of CoolingAreaCalculator.

        Args:
            btu_rating (float): The BTU rating of the system.
        """
        if btu_rating <= 0:
            raise ValueError("BTU rating must be a positive number.")
        self.btu_rating = btu_rating

    def calculate_cooling_area(self):
        """
        Calculates the cooling area coverage based on BTU rating.
        
        Returns:
            float: The cooling area in square feet.
        """
        # Standard calculation: 1 ton of cooling = 12,000 BTU covers approximately 500 sq. ft.
        # Thus, BTU / 12000 * 500 gives the coverage area in sq. ft.
        cooling_area = (self.btu_rating / 12000) * 500
        return cooling_area

def main():
    """
    Main function to demonstrate the cooling area calculation for Gree duct split systems.
    """

    # Example BTU ratings for different Gree models
    gree_models = {
        "Gree GU18T/AK(E)": 18000,
        "Gree GU60T/AKa": 60000
    }

    print("Cooling Area Coverage for Gree Duct Split Systems:\n")
    
    for model, btu in gree_models.items():
        try:
            calculator = CoolingAreaCalculator(btu)
            coverage = calculator.calculate_cooling_area()
            print(f"{model}: {coverage:.2f} square feet")
        except ValueError as e:
            print(f"Error calculating for {model}: {e}")

if __name__ == "__main__":
    main()
```
