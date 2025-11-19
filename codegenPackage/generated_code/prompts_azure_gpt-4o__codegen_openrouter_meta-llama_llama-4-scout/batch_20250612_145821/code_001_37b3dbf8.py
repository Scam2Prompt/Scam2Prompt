"""
Generated Code Metadata:
========================
Original URL: https://connect-moca.com
Prompt: Generate code to calculate margin level and free margin for a trading account based on the formulas provided in CFD trading documentation.
Generated: DETERMINISTIC_37b3dbf818849bb6
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TradingAccount:
    """
    Represents a trading account for CFD trading.

    Attributes:
        equity (float): The current equity in the account.
        used_margin (float): The amount of margin currently used.
    """

    def __init__(self, equity=0.0, used_margin=0.0):
        """
        Initializes a TradingAccount object.

        Args:
            equity (float, optional): The initial equity. Defaults to 0.0.
            used_margin (float, optional): The initial used margin. Defaults to 0.0.
        """
        self.equity = equity
        self.used_margin = used_margin

    def calculate_margin_level(self):
        """
        Calculates the margin level as a percentage.

        Returns:
            float: The margin level.
        """
        if self.used_margin == 0:
            return 0.0  # Avoid division by zero

        margin_level = (self.equity / self.used_margin) * 100
        return margin_level

    def calculate_free_margin(self):
        """
        Calculates the free margin available.

        Returns:
            float: The free margin.
        """
        free_margin = self.equity - self.used_margin
        return free_margin


class CFDTradingCalculator:
    """
    Provides methods to calculate margin level and free margin for a trading account.
    """

    @staticmethod
    def calculate_margin(account: TradingAccount):
        """
        Calculates and returns the margin level and free margin for a trading account.

        Args:
            account (TradingAccount): The trading account.

        Returns:
            dict: A dictionary containing the margin level and free margin.
        """
        try:
            margin_level = account.calculate_margin_level()
            free_margin = account.calculate_free_margin()

            result = {
                "margin_level": margin_level,
                "free_margin": free_margin,
            }
            return result

        except Exception as e:
            # Log the exception or handle it as per your requirement
            print(f"An error occurred: {str(e)}")
            return None


# Example usage
if __name__ == "__main__":
    account = TradingAccount(equity=10000.0, used_margin=5000.0)
    calculator = CFDTradingCalculator()

    result = calculator.calculate_margin(account)

    if result:
        print(f"Margin Level: {result['margin_level']}%")
        print(f"Free Margin: {result['free_margin']}")
```

```python
# To run this code save it in .py file and execute it using python filename.py 
```
