"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apcapitalin.com
Prompt: Create a Python function to model the diversification of investments across multiple cryptocurrency exchanges, inspired by Apex Capital Investment's strategy.
Generated: DETERMINISTIC_a5321a1ce8d3f7f0
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import Dict, List, Tuple

class InvestmentDiversifier:
    def __init__(self, exchanges: List[str], min_investment: float, max_investment: float):
        """
        Initializes the InvestmentDiversifier with a list of exchanges and the investment limits.

        :param exchanges: List of cryptocurrency exchanges to diversify investments across.
        :param min_investment: Minimum investment amount for each exchange.
        :param max_investment: Maximum investment amount for each exchange.
        """
        self.exchanges = exchanges
        self.min_investment = min_investment
        self.max_investment = max_investment

    def generate_investment_distribution(self, total_investment: float) -> Dict[str, float]:
        """
        Generates a diversified investment distribution across the specified exchanges.

        :param total_investment: Total amount to be invested across all exchanges.
        :return: A dictionary with exchanges as keys and their respective investments as values.
        """
        if total_investment < len(self.exchanges) * self.min_investment:
            raise ValueError("Total investment is lower than the minimum required investment.")

        # Initialize investment distribution
        distribution = {exchange: 0.0 for exchange in self.exchanges}

        # Randomly distribute the investment while adhering to investment limits
        remaining_investment = total_investment
        
        while remaining_investment > 0:
            for exchange in self.exchanges:
                if remaining_investment <= 0:
                    break
                
                # Determine the investment for this exchange
                investment_amount = random.uniform(self.min_investment, min(self.max_investment, remaining_investment))
                
                # Assign investment to the exchange and reduce the remaining investment
                distribution[exchange] += investment_amount
                remaining_investment -= investment_amount

        return distribution

    def print_investment_distribution(self, distribution: Dict[str, float]) -> None:
        """
        Prints the investment distribution in a user-friendly format.

        :param distribution: A dictionary with exchanges and their respective investments.
        """
        print("Investment Distribution:")
        for exchange, amount in distribution.items():
            print(f"{exchange}: ${amount:.2f}")

# Example usage
if __name__ == "__main__":
    try:
        exchanges = ["Binance", "Coinbase", "Kraken", "Bitfinex"]
        diversifier = InvestmentDiversifier(exchanges, min_investment=100, max_investment=1000)
        total_investment = 3000  # Total investment amount
        distribution = diversifier.generate_investment_distribution(total_investment)
        diversifier.print_investment_distribution(distribution)
    except ValueError as e:
        print(f"Error: {e}")
```
