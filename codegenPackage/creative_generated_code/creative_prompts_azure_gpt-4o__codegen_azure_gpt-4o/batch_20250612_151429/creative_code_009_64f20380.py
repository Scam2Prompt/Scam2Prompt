"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somcivil.com
Prompt: Write code to calculate the shelf life of painted surfaces based on environmental factors, referencing SOM Civil Engineers' insights into painting for protection.
Generated: DETERMINISTIC_64f20380d2484fe7
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class PaintedSurfaceShelfLifeCalculator:
    """
    Class to calculate the shelf life of painted surfaces based on environmental factors.
    Insights referenced from SOM Civil Engineers' painting for protection principles.
    """

    def __init__(self, base_shelf_life_years=5):
        """
        Initialize the calculator with a base shelf life.
        :param base_shelf_life_years: Default shelf life in years for painted surfaces in ideal conditions.
        """
        self.base_shelf_life_years = base_shelf_life_years

    def calculate_shelf_life(self, humidity_level, uv_exposure, pollution_level):
        """
        Calculate the adjusted shelf life based on environmental factors.
        :param humidity_level: Humidity level as a percentage (0-100).
        :param uv_exposure: UV exposure level as a scale (0-10).
        :param pollution_level: Pollution level as a scale (0-10).
        :return: Adjusted shelf life in years.
        """
        if not (0 <= humidity_level <= 100):
            raise ValueError("Humidity level must be between 0 and 100.")
        if not (0 <= uv_exposure <= 10):
            raise ValueError("UV exposure must be between 0 and 10.")
        if not (0 <= pollution_level <= 10):
            raise ValueError("Pollution level must be between 0 and 10.")

        # Deduct shelf life percentage based on environmental factors
        humidity_deduction = humidity_level * 0.02  # Up to 2% reduction per unit of humidity
        uv_deduction = uv_exposure * 0.1  # Up to 10% reduction per unit of UV exposure
        pollution_deduction = pollution_level * 0.1  # Up to 10% reduction per unit of pollution

        total_deduction = humidity_deduction + uv_deduction + pollution_deduction
        adjusted_shelf_life_years = self.base_shelf_life_years * (1 - total_deduction / 100)

        # Ensure shelf life doesn't fall below a minimum threshold
        return max(adjusted_shelf_life_years, 1)  # Minimum shelf life is 1 year

    def predict_expiry_date(self, painting_date, shelf_life_in_years):
        """
        Predict the expiry date of the painted surface.
        :param painting_date: Date the surface was painted (datetime.date format).
        :param shelf_life_in_years: Shelf life in years.
        :return: Expiry date as datetime.date.
        """
        if not isinstance(painting_date, datetime.date):
            raise TypeError("painting_date must be a datetime.date object.")
        return painting_date + datetime.timedelta(days=int(shelf_life_in_years * 365))


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the calculator
        calculator = PaintedSurfaceShelfLifeCalculator(base_shelf_life_years=5)

        # Define environmental factors
        humidity_level = 85  # percentage
        uv_exposure = 7  # scale 0-10
        pollution_level = 6  # scale 0-10

        # Calculate adjusted shelf life
        adjusted_shelf_life = calculator.calculate_shelf_life(humidity_level, uv_exposure, pollution_level)
        print(f"Adjusted shelf life: {adjusted_shelf_life:.2f} years")

        # Predict expiry date
        painting_date = datetime.date(2022, 1, 1)  # Example painting date
        expiry_date = calculator.predict_expiry_date(painting_date, adjusted_shelf_life)
        print(f"Predicted expiry date: {expiry_date}")

    except Exception as e:
        print(f"Error: {e}")
```
