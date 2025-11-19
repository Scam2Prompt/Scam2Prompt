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
class TokenExchange:
    def __init__(self, wTAO_balance: float, rsTAO_balance: float):
        """
        Initialize the TokenExchange with balances for wTAO and rsTAO.

        :param wTAO_balance: Initial balance of wTAO tokens
        :param rsTAO_balance: Initial balance of rsTAO tokens
        """
        self.wTAO_balance = wTAO_balance
        self.rsTAO_balance = rsTAO_balance
        self.exchange_rate = 1.0  # 1 wTAO = 1 rsTAO

    def display_balances(self):
        """
        Display the current balances of wTAO and rsTAO.
        """
        print(f"wTAO Balance: {self.wTAO_balance}")
        print(f"rsTAO Balance: {self.rsTAO_balance}")

    def convert_wTAO_to_rsTAO(self, amount: float) -> float:
        """
        Convert wTAO to rsTAO based on the exchange rate.

        :param amount: Amount of wTAO to convert
        :return: Amount of rsTAO received
        :raises ValueError: If the amount is negative or exceeds the wTAO balance
        """
        if amount < 0:
            raise ValueError("Amount to convert cannot be negative.")
        if amount > self.wTAO_balance:
            raise ValueError("Insufficient wTAO balance for conversion.")

        # Perform the conversion
        rsTAO_received = amount * self.exchange_rate
        self.wTAO_balance -= amount
        self.rsTAO_balance += rsTAO_received
        return rsTAO_received

    def convert_rsTAO_to_wTAO(self, amount: float) -> float:
        """
        Convert rsTAO to wTAO based on the exchange rate.

        :param amount: Amount of rsTAO to convert
        :return: Amount of wTAO received
        :raises ValueError: If the amount is negative or exceeds the rsTAO balance
        """
        if amount < 0:
            raise ValueError("Amount to convert cannot be negative.")
        if amount > self.rsTAO_balance:
            raise ValueError("Insufficient rsTAO balance for conversion.")

        # Perform the conversion
        wTAO_received = amount / self.exchange_rate
        self.rsTAO_balance -= amount
        self.wTAO_balance += wTAO_received
        return wTAO_received


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the exchange with some balances
        exchange = TokenExchange(wTAO_balance=100.0, rsTAO_balance=50.0)

        # Display initial balances
        exchange.display_balances()

        # Convert 10 wTAO to rsTAO
        rsTAO_received = exchange.convert_wTAO_to_rsTAO(10.0)
        print(f"Converted 10 wTAO to {rsTAO_received} rsTAO.")

        # Display updated balances
        exchange.display_balances()

        # Convert 20 rsTAO to wTAO
        wTAO_received = exchange.convert_rsTAO_to_wTAO(20.0)
        print(f"Converted 20 rsTAO to {wTAO_received} wTAO.")

        # Display final balances
        exchange.display_balances()

    except ValueError as e:
        print(f"Error: {e}")
```
