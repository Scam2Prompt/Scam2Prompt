"""
Generated Code Metadata:
========================
Original URL: https://airdrop1-merlinstarter.pages.dev
Prompt: Write a program to calculate the total token supply across all pools ($BTC, $M-BTC, $VOYA, $HUHU) listed on MerlinSwap using the given token amounts.
Generated: DETERMINISTIC_38e2cac096432112
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TokenPool:
    """
    A class to represent a token pool with its name and amount.
    """

    def __init__(self, name: str, amount: float):
        """
        Initializes a new TokenPool instance.

        :param name: The name of the token pool.
        :param amount: The amount of tokens in the pool.
        """
        self.name = name
        self.amount = amount

    def __str__(self):
        """
        Returns a string representation of the TokenPool instance.
        """
        return f"{self.name}: {self.amount}"


class TokenSupplyCalculator:
    """
    A class to calculate the total token supply across multiple pools.
    """

    def __init__(self, pools: list):
        """
        Initializes the TokenSupplyCalculator with a list of token pools.

        :param pools: A list of TokenPool instances.
        """
        self.pools = pools

    def calculate_total_supply(self) -> float:
        """
        Calculates the total token supply across all pools.

        :return: The total amount of tokens across all pools.
        """
        total_supply = 0.0
        for pool in self.pools:
            total_supply += pool.amount
        return total_supply


def main():
    """
    Main function to execute the token supply calculation.
    """
    try:
        # Define the token pools with their respective amounts
        pools = [
            TokenPool("$BTC", 1000.0),
            TokenPool("$M-BTC", 500.0),
            TokenPool("$VOYA", 250.0),
            TokenPool("$HUHU", 750.0)
        ]

        # Create a TokenSupplyCalculator instance
        calculator = TokenSupplyCalculator(pools)

        # Calculate the total token supply
        total_supply = calculator.calculate_total_supply()

        # Output the total token supply
        print(f"Total Token Supply: {total_supply}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
