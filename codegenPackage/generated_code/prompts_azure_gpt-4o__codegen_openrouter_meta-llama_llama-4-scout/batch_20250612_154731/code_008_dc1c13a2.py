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
    A simple bonding curve model for GHST token distribution backed by DAI.
    """

    def __init__(self, initial_token_supply, initial_dai_reserve, 
                 curve_coefficient, fee=0):
        """
        Initializes the bonding curve model.

        Args:
        - initial_token_supply (float): The initial GHST token supply.
        - initial_dai_reserve (float): The initial DAI reserve.
        - curve_coefficient (float): The coefficient of the bonding curve.
        - fee (float, optional): The fee for buying or selling GHST tokens. Defaults to 0.
        """
        self.token_supply = initial_token_supply
        self.dai_reserve = initial_dai_reserve
        self.curve_coefficient = curve_coefficient
        self.fee = fee

    def _bonding_curve(self, x):
        """
        The bonding curve function.

        Args:
        - x (float): The amount of DAI.

        Returns:
        - float: The amount of GHST tokens.
        """
        return (self.curve_coefficient * x**2 + self.token_supply**2) ** 0.5 - self.token_supply

    def buy_tokens(self, dai_amount):
        """
        Buys GHST tokens using DAI.

        Args:
        - dai_amount (float): The amount of DAI to spend.

        Returns:
        - float: The amount of GHST tokens bought.
        """
        if dai_amount <= 0:
            raise ValueError("DAI amount must be greater than zero.")

        # Calculate the new DAI reserve
        new_dai_reserve = self.dai_reserve + dai_amount * (1 + self.fee)

        # Calculate the new token supply using the bonding curve
        new_token_supply = self._bonding_curve(new_dai_reserve)

        # Calculate the amount of tokens bought
        tokens_bought = new_token_supply - self.token_supply

        # Update the state
        self.dai_reserve = new_dai_reserve
        self.token_supply = new_token_supply

        return tokens_bought

    def sell_tokens(self, token_amount):
        """
        Sells GHST tokens for DAI.

        Args:
        - token_amount (float): The amount of GHST tokens to sell.

        Returns:
        - float: The amount of DAI received.
        """
        if token_amount <= 0:
            raise ValueError("Token amount must be greater than zero.")
        if token_amount > self.token_supply:
            raise ValueError("Insufficient token supply.")

        # Calculate the new token supply
        new_token_supply = self.token_supply - token_amount

        # Calculate the new DAI reserve using the bonding curve
        new_dai_reserve = ((new_token_supply + self.token_supply) / self.curve_coefficient) ** 2

        # Calculate the amount of DAI received
        dai_received = self.dai_reserve - new_dai_reserve
        dai_received *= (1 - self.fee)

        # Update the state
        self.dai_reserve = new_dai_reserve
        self.token_supply = new_token_supply

        return dai_received


def main():
    # Initial conditions
    initial_token_supply = 10000
    initial_dai_reserve = 10000
    curve_coefficient = 0.001

    # Create a bonding curve model
    model = BondingCurve(initial_token_supply, initial_dai_reserve, curve_coefficient, fee=0.01)

    # Simulate buying and selling GHST tokens
    dai_amounts = [100, 200, 500, 1000]
    token_amounts = [10, 20, 50, 100]

    token_supplies = []
    dai_reserves = []

    for dai_amount in dai_amounts:
        tokens_bought = model.buy_tokens(dai_amount)
        print(f"Bought {tokens_bought:.2f} GHST tokens for {dai_amount:.2f} DAI.")

        token_supplies.append(model.token_supply)
        dai_reserves.append(model.dai_reserve)

    for token_amount in token_amounts:
        dai_received = model.sell_tokens(token_amount)
        print(f"Sold {token_amount:.2f} GHST tokens for {dai_received:.2f} DAI.")

        token_supplies.append(model.token_supply)
        dai_reserves.append(model.dai_reserve)

    # Plot the results
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(token_supplies)
    plt.title("GHST Token Supply Over Time")
    plt.xlabel("Time")
    plt.ylabel("Token Supply")

    plt.subplot(1, 2, 2)
    plt.plot(dai_reserves)
    plt.title("DAI Reserve Over Time")
    plt.xlabel("Time")
    plt.ylabel("DAI Reserve")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
```
