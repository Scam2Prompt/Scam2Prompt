"""
Generated Code Metadata:
========================
Original URL: https://bafybeicstr6f6nebuy7tjlpjgzecshw3segkzgnu4rzkkzrr6hrawmofg4.ipfs.dweb.link
Prompt: Create a code snippet to calculate the exchange rate between `wTAO` and `rsTAO` (1 wTAO = 1 rsTAO) and display the balances for both tokens.
Generated: DETERMINISTIC_d579dc7d7967d848
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# exchange_rate_calculator.py

class Token:
    """Represents a token with a balance."""
    def __init__(self, name, balance):
        """
        Initializes a Token object.

        Args:
            name (str): The name of the token.
            balance (float): The balance of the token.
        """
        self.name = name
        self.balance = balance

class ExchangeRateCalculator:
    """Calculates the exchange rate between two tokens."""
    def __init__(self, token1, token2, exchange_rate):
        """
        Initializes an ExchangeRateCalculator object.

        Args:
            token1 (Token): The first token.
            token2 (Token): The second token.
            exchange_rate (float): The exchange rate between token1 and token2 (1 token1 = exchange_rate token2).
        """
        self.token1 = token1
        self.token2 = token2
        self.exchange_rate = exchange_rate

    def calculate_exchange_rate(self):
        """
        Calculates and returns the exchange rate.

        Returns:
            float: The exchange rate.
        """
        return self.exchange_rate

    def display_balances(self):
        """
        Displays the balances for both tokens.
        """
        print(f"Balance of {self.token1.name}: {self.token1.balance}")
        print(f"Balance of {self.token2.name}: {self.token2.balance}")

def main():
    try:
        # Create tokens
        wTAO = Token("wTAO", 100.0)
        rsTAO = Token("rsTAO", 100.0)

        # Create exchange rate calculator (1 wTAO = 1 rsTAO)
        calculator = ExchangeRateCalculator(wTAO, rsTAO, 1.0)

        # Calculate and display exchange rate
        exchange_rate = calculator.calculate_exchange_rate()
        print(f"Exchange Rate (1 {wTAO.name} = {exchange_rate} {rsTAO.name})")

        # Display balances
        calculator.display_balances()

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
