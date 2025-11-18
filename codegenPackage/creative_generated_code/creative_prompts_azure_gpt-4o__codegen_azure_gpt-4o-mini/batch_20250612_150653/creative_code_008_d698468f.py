"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbaseinvest.finance.blog
Prompt: Create a Python program that simulates the process of joining a network of crypto investors and calculates the potential impact of investments on the broader cryptoeconomy.
Generated: DETERMINISTIC_d698468f838b6d08
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Any

class Investor:
    """Class representing an individual crypto investor."""
    
    def __init__(self, name: str, investment_amount: float):
        """
        Initializes an Investor instance.

        :param name: Name of the investor
        :param investment_amount: Amount invested by the investor
        """
        self.name = name
        self.investment_amount = investment_amount

class CryptoNetwork:
    """Class representing a network of crypto investors."""
    
    def __init__(self):
        """Initializes the crypto network with an empty list of investors."""
        self.investors: List[Investor] = []

    def add_investor(self, investor: Investor) -> None:
        """
        Adds an investor to the network.

        :param investor: Investor object to be added
        """
        if not isinstance(investor, Investor):
            raise ValueError("Only an Investor instance can be added.")
        self.investors.append(investor)

    def calculate_total_investment(self) -> float:
        """
        Calculates the total investment in the network.

        :return: Total investment amount
        """
        return sum(investor.investment_amount for investor in self.investors)

    def simulate_market_impact(self) -> Dict[str, Any]:
        """
        Simulates the market impact based on total investments.

        :return: Dictionary containing total investment and simulated market impact
        """
        total_investment = self.calculate_total_investment()
        market_fluctuation = random.uniform(-0.1, 0.3)  # Simulating a market fluctuation
        market_impact = total_investment * market_fluctuation
        
        return {
            "total_investment": total_investment,
            "market_impact": market_impact
        }

def main() -> None:
    """Main function to run the crypto investment simulation."""
    network = CryptoNetwork()
    
    # Sample investors
    investors_data = [
        ("Alice", 1000.0),
        ("Bob", 1500.0),
        ("Charlie", 2000.0)
    ]

    # Adding investors to the network
    for name, investment in investors_data:
        investor = Investor(name, investment)
        network.add_investor(investor)

    # Calculate total investment and market impact
    try:
        impact_results = network.simulate_market_impact()
        print(f"Total Investment: ${impact_results['total_investment']:.2f}")
        print(f"Simulated Market Impact: ${impact_results['market_impact']:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
