"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connect-moca.com
Prompt: Write code to simulate trading scenarios with low amounts and calculate the leverage and margin requirements for CFDs on stocks like Apple and Netflix.
Generated: DETERMINISTIC_73093b40336fbc88
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class CFDTradingSimulator:
    """
    A class to simulate trading scenarios with low amounts and calculate 
    leverage and margin requirements for CFDs (Contracts for Difference) on stocks.
    """
    
    def __init__(self, leverage_ratio, stock_prices):
        """
        Initialize the simulator with leverage ratio and stock prices.

        :param leverage_ratio: Maximum leverage ratio (e.g., 5 for 1:5 leverage)
        :param stock_prices: Dictionary with stock names as keys and current prices as values
        """
        self.leverage_ratio = leverage_ratio
        self.stock_prices = stock_prices  # Example: {"Apple": 150.0, "Netflix": 350.0}

    def calculate_margin(self, trade_amount, leverage):
        """
        Calculate the margin requirement for a given trade amount and leverage.

        :param trade_amount: Total value of the trade
        :param leverage: Leverage being used (e.g., 5 for 1:5 leverage)
        :return: Margin requirement
        """
        if leverage > self.leverage_ratio:
            raise ValueError(f"Leverage exceeds allowed ratio of {self.leverage_ratio}")
        return trade_amount / leverage

    def simulate_trade(self, stock_name, trade_amount, leverage):
        """
        Simulate a trade for a given stock, trade amount, and leverage.

        :param stock_name: Name of the stock being traded (e.g., "Apple")
        :param trade_amount: Total value of the trade
        :param leverage: Leverage being used (e.g., 5 for 1:5 leverage)
        :return: Dictionary containing trade details and margin requirement
        """
        if stock_name not in self.stock_prices:
            raise ValueError(f"Stock {stock_name} not found in price list.")
        
        stock_price = self.stock_prices[stock_name]
        margin_required = self.calculate_margin(trade_amount, leverage)
        units_bought = trade_amount / stock_price
        
        return {
            "stock_name": stock_name,
            "trade_amount": trade_amount,
            "leverage": leverage,
            "margin_required": margin_required,
            "units_bought": units_bought,
            "stock_price": stock_price
        }

def main():
    try:
        # Initialize the simulator with leverage ratio and stock prices
        simulator = CFDTradingSimulator(
            leverage_ratio=5,  # 1:5 leverage
            stock_prices={"Apple": 150.0, "Netflix": 350.0}
        )

        # Simulate trades
        trade_1 = simulator.simulate_trade(stock_name="Apple", trade_amount=750, leverage=5)
        trade_2 = simulator.simulate_trade(stock_name="Netflix", trade_amount=1400, leverage=4)

        # Print trade details
        print("Trade 1 Details:", trade_1)
        print("Trade 2 Details:", trade_2)

    except ValueError as e:
        # Handle invalid input or simulation errors
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        # Handle unexpected errors
        print(f"Unexpected error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
