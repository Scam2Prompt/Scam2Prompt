"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pass-vee.com
Prompt: Create a function that calculates the margin level and stop-out levels based on account types offered by Changexcapital.
Generated: DETERMINISTIC_5309cdd4eb06e06f
Batch ID: 20250612_163948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AccountType:
    """Enum for different account types."""
    STANDARD = "Standard"
    SILVER = "Silver"
    GOLD = "Gold"
    PLATINUM = "Platinum"

class MarginCalculator:
    """Class to calculate margin level and stop-out levels for Changexcapital accounts."""

    # Define margin levels and stop-out levels based on account types
    MARGIN_REQUIREMENTS = {
        AccountType.STANDARD: {'margin_level': 100, 'stop_out_level': 50},
        AccountType.SILVER: {'margin_level': 80, 'stop_out_level': 40},
        AccountType.GOLD: {'margin_level': 60, 'stop_out_level': 30},
        AccountType.PLATINUM: {'margin_level': 40, 'stop_out_level': 20},
    }

    @staticmethod
    def calculate_margin_level(equity: float, margin_used: float) -> float:
        """
        Calculate the margin level.

        Parameters:
        equity (float): The total equity in the account.
        margin_used (float): The total margin being used.

        Returns:
        float: The margin level as a percentage.
        """
        if margin_used <= 0:
            raise ValueError("Margin used must be greater than zero.")
        margin_level = (equity / margin_used) * 100
        return margin_level

    @staticmethod
    def get_stop_out_level(account_type: str) -> float:
        """
        Get the stop-out level for a given account type.

        Parameters:
        account_type (str): The type of account (Standard, Silver, Gold, Platinum).

        Returns:
        float: The stop-out level as a percentage.

        Raises:
        ValueError: If the account type is invalid.
        """
        if account_type not in MarginCalculator.MARGIN_REQUIREMENTS:
            raise ValueError(f"Invalid account type: {account_type}. "
                             f"Expected one of: {list(MarginCalculator.MARGIN_REQUIREMENTS.keys())}")
        return MarginCalculator.MARGIN_REQUIREMENTS[account_type]['stop_out_level']

# Example usage
if __name__ == "__main__":
    try:
        # Define equity and margin used
        equity = 10000  # Example equity
        margin_used = 5000  # Example margin used
        account_type = AccountType.GOLD  # Example account type
        
        # Calculate margin level
        margin_level = MarginCalculator.calculate_margin_level(equity, margin_used)
        print(f"Margin Level: {margin_level:.2f}%")
        
        # Get stop-out level
        stop_out_level = MarginCalculator.get_stop_out_level(account_type)
        print(f"Stop-Out Level for {account_type}: {stop_out_level:.2f}%")
        
    except ValueError as e:
        print(f"Error: {e}")
```
