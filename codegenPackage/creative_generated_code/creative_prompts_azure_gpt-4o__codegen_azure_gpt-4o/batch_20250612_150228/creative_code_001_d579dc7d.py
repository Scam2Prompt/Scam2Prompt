"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeicstr6f6nebuy7tjlpjgzecshw3segkzgnu4rzkkzrr6hrawmofg4.ipfs.dweb.link
Prompt: Create a code snippet to calculate the exchange rate between `wTAO` and `rsTAO` (1 wTAO = 1 rsTAO) and display the balances for both tokens.
Generated: DETERMINISTIC_d579dc7d7967d848
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate and display exchange rates and balances for tokens wTAO and rsTAO
# Assumption: 1 wTAO = 1 rsTAO

class Token:
    """
    A class representing a token with a balance.
    """
    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance

    def update_balance(self, amount: float):
        """
        Updates the balance of the token.
        :param amount: Float amount to add to the balance. Can be negative for deduction.
        """
        if self.balance + amount < 0:
            raise ValueError(f"Insufficient balance in {self.name} to perform this operation.")
        self.balance += amount

    def display_balance(self):
        """
        Displays the current balance of the token.
        """
        print(f"{self.name} Balance: {self.balance:.2f}")


class Exchange:
    """
    A class representing the exchange logic between two tokens.
    """
    def __init__(self, token_a: Token, token_b: Token, exchange_rate: float = 1.0):
        """
        Initializes the exchange.
        :param token_a: First token (wTAO).
        :param token_b: Second token (rsTAO).
        :param exchange_rate: Exchange rate between the two tokens.
        """
        self.token_a = token_a
        self.token_b = token_b
        self.exchange_rate = exchange_rate

    def perform_exchange(self, amount: float, from_token: str):
        """
        Performs the exchange between tokens.
        :param amount: The amount of tokens to exchange.
        :param from_token: The token being exchanged from ('wTAO' or 'rsTAO').
        """
        if from_token == self.token_a.name:
            self.token_a.update_balance(-amount)
            self.token_b.update_balance(amount * self.exchange_rate)
        elif from_token == self.token_b.name:
            self.token_b.update_balance(-amount)
            self.token_a.update_balance(amount / self.exchange_rate)
        else:
            raise ValueError(f"Invalid token name: {from_token}. Must be '{self.token_a.name}' or '{self.token_b.name}'.")

    def display_balances(self):
        """
        Displays the balances of both tokens.
        """
        self.token_a.display_balance()
        self.token_b.display_balance()


# Main execution script
if __name__ == "__main__":
    try:
        # Initialize tokens
        wTAO = Token("wTAO", 100.0)  # Initialize wTAO with a balance of 100
        rsTAO = Token("rsTAO", 50.0)  # Initialize rsTAO with a balance of 50

        # Initialize exchange with a 1:1 exchange rate
        exchange = Exchange(wTAO, rsTAO)

        # Display initial balances
        print("Initial Balances:")
        exchange.display_balances()

        # Perform an exchange: 10 wTAO to rsTAO
        print("\nPerforming exchange: 10 wTAO to rsTAO")
        exchange.perform_exchange(10, "wTAO")
        exchange.display_balances()

        # Perform an exchange: 5 rsTAO to wTAO
        print("\nPerforming exchange: 5 rsTAO to wTAO")
        exchange.perform_exchange(5, "rsTAO")
        exchange.display_balances()

    except Exception as e:
        # Handle errors gracefully
        print(f"An error occurred: {e}")
```
