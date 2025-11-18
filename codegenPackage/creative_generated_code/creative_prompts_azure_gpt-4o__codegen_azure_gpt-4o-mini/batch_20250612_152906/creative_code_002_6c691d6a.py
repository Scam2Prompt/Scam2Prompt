"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kayen.pages.dev
Prompt: Create a function to calculate bonus points for liquidity supply in the USDT-CHZ pool on KAYEN League, including the +100% bonus multiplier.
Generated: DETERMINISTIC_6c691d6a66ecf9ee
Batch ID: 20250612_152906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LiquidityBonusCalculator:
    """
    A class to calculate bonus points for liquidity supply in the USDT-CHZ pool on KAYEN League.
    The bonus system includes a +100% bonus multiplier.
    """

    def __init__(self, base_points):
        """
        Initializes the calculator with the specified base points.

        :param base_points: float, the base points for liquidity supplied
        :raises ValueError: if base_points is negative
        """
        if base_points < 0:
            raise ValueError("Base points must be non-negative.")
        self.base_points = base_points

    def calculate_bonus_points(self):
        """
        Calculates the total bonus points based on the base points and a +100% bonus multiplier.

        :return: float, total bonus points
        """
        bonus_multiplier = 2.0  # +100% bonus
        total_bonus_points = self.base_points * bonus_multiplier
        return total_bonus_points

    def display_bonus_info(self):
        """
        Displays the base points and the calculated bonus points.

        :return: None
        """
        try:
            bonus_points = self.calculate_bonus_points()
            print(f"Base Points: {self.base_points}")
            print(f"Total Bonus Points (with +100% multiplier): {bonus_points}")
        except Exception as e:
            print(f"An error occurred while calculating bonus points: {e}")


# Example usage:
if __name__ == "__main__":
    try:
        # Instantiate the calculator with the base points supplied by the user.
        base_points = 50.0  # Example base points
        bonus_calculator = LiquidityBonusCalculator(base_points)
        
        # Display the bonus information.
        bonus_calculator.display_bonus_info()
        
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
