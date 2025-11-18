"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghsttoken.co
Prompt: Using the bonding curve mechanism described, write a Python simulation to model the initial GHST token distribution backed by DAI.
Generated: DETERMINISTIC_dc1c13a2ef6b1b6a
Batch ID: 20250612_154731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

class BondingCurve:
    """
    A class to simulate the bonding curve for the distribution of GHST tokens
    backed by DAI (Dai Stablecoin).
    """

    def __init__(self, reserve_price: float, initial_supply: float):
        """
        Initializes the bonding curve parameters.

        :param reserve_price: The price of each GHST token on the bonding curve.
        :param initial_supply: The initial amount of GHST tokens in circulation.
        """
        self.reserve_price = reserve_price
        self.total_supply = initial_supply
        self.dai_reserve = 0.0

    def buy_tokens(self, dai_amount: float) -> float:
        """
        Buys GHST tokens using DAI.

        :param dai_amount: The amount of DAI to spend for buying GHST tokens.
        :return: The amount of GHST tokens bought.
        """
        if dai_amount <= 0:
            raise ValueError("DAI amount must be greater than zero.")
        
        # Calculate the number of tokens to mint
        tokens_bought = self._calculate_tokens_bought(dai_amount)
        
        # Update reserve and supply
        self.dai_reserve += dai_amount
        self.total_supply += tokens_bought
        
        return tokens_bought

    def _calculate_tokens_bought(self, dai_amount: float) -> float:
        """
        Private method to calculate how many tokens can be bought with a specific amount of DAI.

        :param dai_amount: The amount of DAI being spent.
        :return: The number of tokens that can be bought.
        """
        return dai_amount / self.reserve_price

    def sell_tokens(self, token_amount: float) -> float:
        """
        Sells GHST tokens for DAI.

        :param token_amount: The amount of GHST tokens to sell.
        :return: The amount of DAI received from selling the tokens.
        """
        if token_amount <= 0:
            raise ValueError("Token amount must be greater than zero.")
        if token_amount > self.total_supply:
            raise ValueError("Cannot sell more tokens than available in supply.")

        # Calculate the amount of DAI to return
        dai_returned = self._calculate_dai_return(token_amount)

        # Update reserve and supply
        self.dai_reserve -= dai_returned
        self.total_supply -= token_amount
        
        return dai_returned

    def _calculate_dai_return(self, token_amount: float) -> float:
        """
        Private method to calculate how much DAI can be received for a specific amount of tokens.

        :param token_amount: The amount of tokens being sold.
        :return: The amount of DAI that can be received.
        """
        return token_amount * self.reserve_price

    def simulate_distribution(self, dai_investments: list) -> tuple:
        """
        Simulates the token distribution over a series of DAI investments.

        :param dai_investments: A list of DAI amounts to invest.
        :return: A tuple of total GHST tokens bought and total DAI in reserve after simulation.
        """
        total_tokens_bought = 0.0
        
        for dai_amount in dai_investments:
            tokens_bought = self.buy_tokens(dai_amount)
            total_tokens_bought += tokens_bought
        
        return total_tokens_bought, self.dai_reserve

# Example simulation
if __name__ == "__main__":
    # Initialize the bonding curve with a reserve price and initial supply
    bonding_curve = BondingCurve(reserve_price=1.0, initial_supply=0.0)
    
    # List of DAI investments to simulate
    dai_investments = [10, 20, 30, 40, 50]  # Example investments
    
    # Simulate the distribution
    total_tokens, total_dai_reserve = bonding_curve.simulate_distribution(dai_investments)
    
    print(f"Total GHST Tokens Bought: {total_tokens:.2f}")
    print(f"Total DAI Reserve: {total_dai_reserve:.2f}")
    
    # Optionally, visualize the results
    plt.plot(dai_investments, np.cumsum(dai_investments), marker='o', label='DAI Investments')
    plt.title('DAI Investments vs GHST Tokens Bought')
    plt.xlabel('DAI Investment Amount')
    plt.ylabel('Cumulative GHST Tokens Bought')
    plt.legend()
    plt.grid()
    plt.show()
```
