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
class TokenExchange:
    """
    A class to represent the exchange between wTAO and rsTAO tokens.
    """

    def __init__(self, wtao_balance: float, rsta_balance: float):
        """
        Initializes the TokenExchange with the balances of wTAO and rsTAO.

        :param wtao_balance: The balance of wTAO tokens.
        :param rsta_balance: The balance of rsTAO tokens.
        """
        self.wtao_balance = wtao_balance
        self.rsta_balance = rsta_balance
        self.exchange_rate = 1.0  # 1 wTAO = 1 rsTAO

    def calculate_exchange(self, token_amount: float, token_type: str) -> float:
        """
        Calculates the equivalent amount of tokens based on the exchange rate.

        :param token_amount: The amount of tokens to convert.
        :param token_type: The type of token ('wTAO' or 'rsTAO').
        :return: The equivalent amount of the other token.
        :raises ValueError: If the token type is invalid or if the amount is negative.
        """
        if token_amount < 0:
            raise ValueError("Token amount cannot be negative.")
        
        if token_type == 'wTAO':
            return token_amount * self.exchange_rate  # wTAO to rsTAO
        elif token_type == 'rsTAO':
            return token_amount / self.exchange_rate  # rsTAO to wTAO
        else:
            raise ValueError("Invalid token type. Must be 'wTAO' or 'rsTAO'.")

    def display_balances(self):
        """Displays the current balances of wTAO and rsTAO."""
        print(f"Current wTAO Balance: {self.wtao_balance:.2f}")
        print(f"Current rsTAO Balance: {self.rsta_balance:.2f}")

    def exchange_tokens(self, token_amount: float, token_type: str):
        """
        Exchanges tokens based on the given amount and type.

        :param token_amount: The amount of tokens to exchange.
        :param token_type: The type of token to be exchanged ('wTAO' or 'rsTAO').
        """
        try:
            equivalent_amount = self.calculate_exchange(token_amount, token_type)

            if token_type == 'wTAO':
                self.wtao_balance -= token_amount
                self.rsta_balance += equivalent_amount
            elif token_type == 'rsTAO':
                self.rsta_balance -= token_amount
                self.wtao_balance += equivalent_amount

            print(f"Exchanged {token_amount:.2f} {token_type} successfully.")
            self.display_balances()

        except ValueError as e:
            print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the TokenExchange with example balances
        exchange = TokenExchange(wtao_balance=100.0, rsta_balance=100.0)

        # Display current balances
        exchange.display_balances()

        # Perform a token exchange
        exchange.exchange_tokens(token_amount=10.0, token_type='wTAO')

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
