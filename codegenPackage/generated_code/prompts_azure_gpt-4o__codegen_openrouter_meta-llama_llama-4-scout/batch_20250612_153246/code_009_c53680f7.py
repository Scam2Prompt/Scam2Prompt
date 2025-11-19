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
# gree_cooling_area_calculator.py

class GreeDuctSplitSystem:
    """
    Calculates the cooling area coverage for Gree duct split systems based on their BTU rating.
    """

    def __init__(self, model, btu_rating):
        """
        Initializes a Gree duct split system with its model and BTU rating.

        Args:
            model (str): The model of the Gree duct split system (e.g., "Gree GU18T/AK(E)").
            btu_rating (int): The BTU rating of the Gree duct split system.

        Raises:
            ValueError: If the BTU rating is not a positive integer.
        """
        if not isinstance(btu_rating, int) or btu_rating <= 0:
            raise ValueError("BTU rating must be a positive integer.")

        self.model = model
        self.btu_rating = btu_rating

    def calculate_cooling_area(self):
        """
        Calculates the cooling area coverage in square meters based on the BTU rating.

        The general guideline for cooling area coverage is:
        - 1 ton (12,000 BTU) = 100-120 sqft (approximately 9-11 sqm)

        Assuming a moderate climate and average insulation, we'll use:
        - 1 BTU = 0.09290304 sqm (approximately)

        Returns:
            float: The cooling area coverage in square meters.
        """
        # Cooling area coverage calculation formula
        cooling_area_sqm = self.btu_rating * 0.09290304

        return cooling_area_sqm


def main():
    try:
        # Example usage:
        gree_gu18t_ak = GreeDuctSplitSystem("Gree GU18T/AK(E)", 18000)
        gree_gu60t_aka = GreeDuctSplitSystem("Gree GU60T/AKa", 60000)

        print(f"Model: {gree_gu18t_ak.model}, BTU Rating: {gree_gu18t_ak.btu_rating}, Cooling Area: {gree_gu18t_ak.calculate_cooling_area():.2f} sqm")
        print(f"Model: {gree_gu60t_aka.model}, BTU Rating: {gree_gu60t_aka.btu_rating}, Cooling Area: {gree_gu60t_aka.calculate_cooling_area():.2f} sqm")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
