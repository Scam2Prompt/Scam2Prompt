"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-bitcoinrevolution.com
Prompt: Write code to calculate potential profits based on price predictions for financial assets, including scenarios where asset prices are moving down, as explained in the Bitcoin Revolution app.
Generated: DETERMINISTIC_fc6ac5b869e23e34
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ProfitCalculator:
    """
    A class to calculate potential profits based on price predictions for financial assets.

    Attributes:
        initial_investment (float): The amount of money invested in the asset.
        predicted_prices (list): A list of predicted future prices for the asset.
    """

    def __init__(self, initial_investment, predicted_prices):
        """
        Initializes the ProfitCalculator with an initial investment and predicted prices.

        Parameters:
            initial_investment (float): The initial amount invested.
            predicted_prices (list): A list of predicted prices (float).
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if not all(isinstance(price, (int, float)) for price in predicted_prices):
            raise ValueError("All predicted prices must be numerical values.")
        
        self.initial_investment = initial_investment
        self.predicted_prices = predicted_prices

    def calculate_profit(self):
        """
        Calculate potential profits for all predicted prices.

        Returns:
            dict: A dictionary with each predicted price and the corresponding profit or loss.
        """
        potential_profits = {}
        for price in self.predicted_prices:
            # Calculate the number of assets purchased
            assets = self.initial_investment / self.predicted_prices[0]
            # Calculate the potential profit or loss
            profit = (price * assets) - self.initial_investment
            potential_profits[price] = profit
        
        return potential_profits

    def calculate_scenarios(self):
        """
        Calculate and display scenarios including price increases and decreases.

        Returns:
            None
        """
        profits = self.calculate_profit()
        for price, profit in profits.items():
            if profit > 0:
                print(f"Predicted Price: ${price:.2f} - Potential Profit: ${profit:.2f} (Profit)")
            elif profit < 0:
                print(f"Predicted Price: ${price:.2f} - Potential Loss: ${abs(profit):.2f} (Loss)")
            else:
                print(f"Predicted Price: ${price:.2f} - No profit, no loss.")

# Example usage
if __name__ == "__main__":
    try:
        initial_investment = 1000.00  # Example initial investment
        predicted_prices = [900.00, 950.00, 1050.00, 1100.00, 800.00]  # Example predicted prices
        
        calculator = ProfitCalculator(initial_investment, predicted_prices)
        calculator.calculate_scenarios()
        
    except ValueError as e:
        print(f"Error: {e}")
```
