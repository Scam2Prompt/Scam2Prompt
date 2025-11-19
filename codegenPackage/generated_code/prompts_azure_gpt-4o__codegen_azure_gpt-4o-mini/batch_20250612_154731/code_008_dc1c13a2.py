"""
Generated Code Metadata:
========================
Original URL: https://ghsttoken.co
Prompt: Using the bonding curve mechanism described, write a Python simulation to model the initial GHST token distribution backed by DAI.
Generated: DETERMINISTIC_dc1c13a2ef6b1b6a
Batch ID: 20250612_154731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt

class BondingCurve:
    """
    A class to model a bonding curve for token distribution.
    
    Attributes:
        reserve (float): The amount of DAI in reserve.
        token_supply (float): The total supply of GHST tokens.
        curve_slope (float): The slope of the bonding curve.
    """

    def __init__(self, initial_reserve: float, initial_supply: float, curve_slope: float):
        """
        Initializes the bonding curve with given parameters.
        
        Args:
            initial_reserve (float): Initial amount of DAI in reserve.
            initial_supply (float): Initial supply of GHST tokens.
            curve_slope (float): Slope of the bonding curve.
        """
        self.reserve = initial_reserve
        self.token_supply = initial_supply
        self.curve_slope = curve_slope

    def buy_tokens(self, amount: float) -> float:
        """
        Simulates the purchase of GHST tokens with DAI.
        
        Args:
            amount (float): The amount of DAI to spend for purchasing tokens.
        
        Returns:
            float: The number of tokens purchased.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        # Calculate the price of tokens based on the bonding curve formula
        price_per_token = self.curve_slope * (self.token_supply ** 2)
        tokens_purchased = amount / price_per_token
        
        # Update the reserve and token supply
        self.reserve += amount
        self.token_supply += tokens_purchased
        
        return tokens_purchased

    def sell_tokens(self, tokens: float) -> float:
        """
        Simulates the sale of GHST tokens for DAI.
        
        Args:
            tokens (float): The number of GHST tokens to sell.
        
        Returns:
            float: The amount of DAI received from the sale.
        """
        if tokens <= 0:
            raise ValueError("Tokens must be greater than zero.")
        if tokens > self.token_supply:
            raise ValueError("Not enough tokens in supply to sell.")
        
        # Calculate the price of tokens based on the bonding curve formula
        price_per_token = self.curve_slope * (self.token_supply ** 2)
        dai_received = tokens * price_per_token
        
        # Update the reserve and token supply
        self.reserve -= dai_received
        self.token_supply -= tokens
        
        return dai_received

    def simulate_distribution(self, num_transactions: int, max_dai: float):
        """
        Simulates a series of buy and sell transactions.
        
        Args:
            num_transactions (int): The number of transactions to simulate.
            max_dai (float): The maximum amount of DAI to spend in a single transaction.
        
        Returns:
            list: A list of tuples containing (DAI spent, tokens purchased).
        """
        distribution = []
        for _ in range(num_transactions):
            dai_spent = np.random.uniform(1, max_dai)
            tokens = self.buy_tokens(dai_spent)
            distribution.append((dai_spent, tokens))
        
        return distribution

def main():
    """
    Main function to run the bonding curve simulation.
    """
    # Initialize the bonding curve with initial parameters
    initial_reserve = 10000.0  # Initial DAI reserve
    initial_supply = 1000.0     # Initial GHST token supply
    curve_slope = 0.01          # Slope of the bonding curve

    bonding_curve = BondingCurve(initial_reserve, initial_supply, curve_slope)

    # Simulate token distribution
    num_transactions = 100
    max_dai = 500
    distribution = bonding_curve.simulate_distribution(num_transactions, max_dai)

    # Print the results
    for dai_spent, tokens in distribution:
        print(f"DAI Spent: {dai_spent:.2f}, Tokens Purchased: {tokens:.4f}")

    # Plotting the results
    plt.plot([dai for dai, _ in distribution], [tokens for _, tokens in distribution], marker='o')
    plt.title('GHST Token Distribution Simulation')
    plt.xlabel('DAI Spent')
    plt.ylabel('Tokens Purchased')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
```
