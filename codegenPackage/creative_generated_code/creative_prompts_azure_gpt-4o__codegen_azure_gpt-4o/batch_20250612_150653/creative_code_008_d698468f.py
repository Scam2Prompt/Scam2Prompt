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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CryptoInvestor:
    """
    Represents a Crypto Investor in the network.
    """

    def __init__(self, name, initial_investment):
        """
        Initialize a new investor with a name and initial investment.

        :param name: str - Name of the investor
        :param initial_investment: float - Initial investment amount
        """
        self.name = name
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        self.investment = initial_investment

    def calculate_investment_impact(self, multiplier):
        """
        Simulates the impact of the investor's investment on the cryptoeconomy.

        :param multiplier: float - Impact multiplier for calculation
        :return: float - Impact result
        """
        return self.investment * multiplier


class CryptoNetwork:
    """
    Represents a network of crypto investors.
    """

    def __init__(self):
        """
        Initialize an empty network of investors.
        """
        self.investors = []

    def join_network(self, investor):
        """
        Adds an investor to the network.

        :param investor: CryptoInvestor - Investor to add
        """
        if not isinstance(investor, CryptoInvestor):
            raise TypeError("Argument must be of type CryptoInvestor.")
        self.investors.append(investor)
        logging.info(f"Investor '{investor.name}' joined the network!")

    def simulate_global_impact(self):
        """
        Simulates the global impact of all investments in the network.

        :return: float - Total impact on the cryptoeconomy
        """
        if not self.investors:
            logging.warning("No investors in the network!")
            return 0.0

        total_impact = 0.0
        for investor in self.investors:
            # Generate a random multiplier to simulate market volatility
            multiplier = random.uniform(0.8, 1.5)
            impact = investor.calculate_investment_impact(multiplier)
            logging.info(f"Investor '{investor.name}' had an impact of {impact:.2f} on the cryptoeconomy.")
            total_impact += impact

        return total_impact


def main():
    """
    Main function to simulate joining a crypto network and calculating investment impacts.
    """
    try:
        network = CryptoNetwork()

        # Simulate adding investors
        investor1 = CryptoInvestor(name="Alice", initial_investment=1000)
        investor2 = CryptoInvestor(name="Bob", initial_investment=5000)
        investor3 = CryptoInvestor(name="Charlie", initial_investment=3000)

        network.join_network(investor1)
        network.join_network(investor2)
        network.join_network(investor3)

        # Calculate and display the global impact
        total_impact = network.simulate_global_impact()
        logging.info(f"Total impact on the cryptoeconomy: {total_impact:.2f}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
