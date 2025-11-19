"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earni-fi.finance
Prompt: Describe the unique use cases of Earni-Fi in managing investments through code.
Generated: DETERMINISTIC_e58b8247ac1b2c8c
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EarniFiInvestmentManager:
    """
    A class to manage investments using the Earni-Fi platform.
    
    Attributes:
        investments (dict): A dictionary to store investment amounts by asset type.
    """

    def __init__(self):
        """Initializes the Earni-Fi investment manager with an empty investment portfolio."""
        self.investments = {}

    def add_investment(self, asset_type: str, amount: float) -> None:
        """
        Adds an investment to the portfolio.

        Args:
            asset_type (str): The type of asset to invest in (e.g., 'stocks', 'bonds').
            amount (float): The amount of money to invest.

        Raises:
            ValueError: If the amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        
        if asset_type in self.investments:
            self.investments[asset_type] += amount
        else:
            self.investments[asset_type] = amount
            
        print(f"Added investment: {amount} in {asset_type}. Total investment in {asset_type}: {self.investments[asset_type]}")

    def remove_investment(self, asset_type: str, amount: float) -> None:
        """
        Removes an investment from the portfolio.

        Args:
            asset_type (str): The type of asset to divest from.
            amount (float): The amount of money to remove.

        Raises:
            ValueError: If the amount is negative or exceeds current investment.
            KeyError: If the asset type does not exist in the portfolio.
        """
        if amount <= 0:
            raise ValueError("Removal amount must be greater than zero.")

        if asset_type not in self.investments:
            raise KeyError(f"No investments found for asset type: {asset_type}")

        if amount > self.investments[asset_type]:
            raise ValueError("Removal amount exceeds current investment.")
        
        self.investments[asset_type] -= amount
        if self.investments[asset_type] == 0:
            del self.investments[asset_type]

        print(f"Removed investment: {amount} from {asset_type}. Remaining investment in {asset_type}: {self.investments.get(asset_type, 0)}")

    def get_portfolio_value(self) -> float:
        """
        Calculates the total value of the investment portfolio.

        Returns:
            float: The total value of all investments.
        """
        total_value = sum(self.investments.values())
        print(f"Total portfolio value: {total_value}")
        return total_value

    def display_portfolio(self) -> None:
        """
        Displays the current investment portfolio.

        Returns:
            None: Prints the investments.
        """
        if not self.investments:
            print("Investment portfolio is empty.")
            return
        
        print("Current Investment Portfolio:")
        for asset_type, amount in self.investments.items():
            print(f"{asset_type}: {amount}")

# Example usage:
if __name__ == "__main__":
    manager = EarniFiInvestmentManager()
    try:
        manager.add_investment('stocks', 1000)
        manager.add_investment('bonds', 500)
        manager.display_portfolio()
        manager.remove_investment('stocks', 200)
        manager.get_portfolio_value()
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
