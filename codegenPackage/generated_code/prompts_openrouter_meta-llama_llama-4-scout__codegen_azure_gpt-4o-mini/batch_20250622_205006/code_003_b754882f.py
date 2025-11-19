"""
Generated Code Metadata:
========================
Original URL: https://blockdag-apps.pages.dev
Prompt: "Develop a code snippet to calculate the total coin sales and miner sales in USD for the BlockDAG presale."
Generated: DETERMINISTIC_b754882f5705de6d
Batch ID: 20250622_205006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SalesCalculator:
    """
    A class to calculate total coin sales and miner sales in USD for the BlockDAG presale.
    """

    def __init__(self):
        # Initialize sales data
        self.coin_sales = 0.0
        self.miner_sales = 0.0

    def add_coin_sales(self, amount: float, price_per_coin: float):
        """
        Add coin sales to the total.

        :param amount: The number of coins sold
        :param price_per_coin: The price per coin in USD
        :raises ValueError: If amount or price_per_coin is negative
        """
        if amount < 0 or price_per_coin < 0:
            raise ValueError("Amount and price per coin must be non-negative.")
        
        self.coin_sales += amount * price_per_coin

    def add_miner_sales(self, amount: float, price_per_miner: float):
        """
        Add miner sales to the total.

        :param amount: The number of miners sold
        :param price_per_miner: The price per miner in USD
        :raises ValueError: If amount or price_per_miner is negative
        """
        if amount < 0 or price_per_miner < 0:
            raise ValueError("Amount and price per miner must be non-negative.")
        
        self.miner_sales += amount * price_per_miner

    def total_sales(self) -> float:
        """
        Calculate the total sales in USD.

        :return: Total sales in USD
        """
        return self.coin_sales + self.miner_sales

    def __str__(self):
        """
        String representation of the sales data.

        :return: A formatted string showing total coin and miner sales
        """
        return (f"Total Coin Sales: ${self.coin_sales:.2f}\n"
                f"Total Miner Sales: ${self.miner_sales:.2f}\n"
                f"Total Sales: ${self.total_sales():.2f}")


# Example usage
if __name__ == "__main__":
    try:
        sales_calculator = SalesCalculator()
        
        # Adding coin sales
        sales_calculator.add_coin_sales(amount=100, price_per_coin=5.0)
        
        # Adding miner sales
        sales_calculator.add_miner_sales(amount=50, price_per_miner=10.0)
        
        # Display total sales
        print(sales_calculator)
        
    except ValueError as e:
        print(f"Error: {e}")
```
