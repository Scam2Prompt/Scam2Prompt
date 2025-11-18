"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brexphil.com
Prompt: Generate code to calculate the expected income from farmland portfolios, including row and permanent crop farms, based on Brexphil Inc.'s agricultural investment strategy.
Generated: DETERMINISTIC_22f4f9898639ee77
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FarmlandPortfolio:
    """
    A class to represent a farmland portfolio and calculate expected income
    from row and permanent crop farms based on investment strategies.
    """

    def __init__(self):
        """
        Initializes a new instance of FarmlandPortfolio with empty crop lists.
        """
        self.row_crops = []
        self.permanent_crops = []

    def add_row_crop(self, crop_name: str, expected_yield: float, price_per_unit: float):
        """
        Add a row crop to the portfolio.

        :param crop_name: Name of the crop
        :param expected_yield: Expected yield in units per acre
        :param price_per_unit: Market price per unit of the crop
        """
        if expected_yield < 0 or price_per_unit < 0:
            raise ValueError("Expected yield and price per unit must be non-negative.")
        
        self.row_crops.append({
            'crop_name': crop_name,
            'expected_yield': expected_yield,
            'price_per_unit': price_per_unit
        })

    def add_permanent_crop(self, crop_name: str, expected_yield: float, price_per_unit: float):
        """
        Add a permanent crop to the portfolio.

        :param crop_name: Name of the permanent crop
        :param expected_yield: Expected yield in units per acre
        :param price_per_unit: Market price per unit of the crop
        """
        if expected_yield < 0 or price_per_unit < 0:
            raise ValueError("Expected yield and price per unit must be non-negative.")
        
        self.permanent_crops.append({
            'crop_name': crop_name,
            'expected_yield': expected_yield,
            'price_per_unit': price_per_unit
        })

    def calculate_expected_income(self, acres: float) -> float:
        """
        Calculate the expected income from all crops in the portfolio.

        :param acres: Total number of acres dedicated to farming
        :return: Total expected income
        """
        total_income = 0.0
        
        # Calculate income from row crops
        for crop in self.row_crops:
            income = crop['expected_yield'] * crop['price_per_unit'] * acres
            total_income += income
        
        # Calculate income from permanent crops
        for crop in self.permanent_crops:
            income = crop['expected_yield'] * crop['price_per_unit'] * acres
            total_income += income
        
        return total_income

    def __str__(self):
        """
        Return a string representation of the farmland portfolio.
        """
        return (f"Row Crops: {self.row_crops}\nPermanent Crops: {self.permanent_crops}")


# Example usage
if __name__ == "__main__":
    try:
        portfolio = FarmlandPortfolio()
        portfolio.add_row_crop("Corn", expected_yield=150, price_per_unit=3.5)
        portfolio.add_permanent_crop("Apple", expected_yield=200, price_per_unit=1.2)

        acres = 50  # Example acres dedicated to farming
        expected_income = portfolio.calculate_expected_income(acres)
        print(f"Expected Income from the farmland portfolio: ${expected_income:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
