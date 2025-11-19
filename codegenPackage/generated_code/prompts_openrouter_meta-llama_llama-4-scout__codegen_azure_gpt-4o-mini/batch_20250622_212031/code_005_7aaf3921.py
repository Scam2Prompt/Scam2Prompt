"""
Generated Code Metadata:
========================
Original URL: https://claimhenlo.com
Prompt: What are the use cases for exercising $oHENLO tokens, and how does it relate to redeeming $HENLO tokens at a discounted price?
Generated: DETERMINISTIC_7aaf39210f7d4165
Batch ID: 20250622_212031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TokenExchange:
    """
    A class to manage the exchange and redemption of $oHENLO and $HENLO tokens.
    """

    def __init__(self):
        self.oHENLO_balance = 0
        self.HENLO_balance = 0
        self.discount_rate = 0.1  # 10% discount for redeeming $HENLO tokens

    def deposit_oHENLO(self, amount: float):
        """
        Deposit $oHENLO tokens into the user's balance.

        :param amount: The amount of $oHENLO tokens to deposit.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        self.oHENLO_balance += amount
        print(f"Deposited {amount} $oHENLO tokens. New balance: {self.oHENLO_balance}")

    def redeem_HENLO(self, amount: float):
        """
        Redeem $HENLO tokens at a discounted price using $oHENLO tokens.

        :param amount: The amount of $HENLO tokens to redeem.
        :raises ValueError: If the amount is negative or exceeds available $oHENLO balance.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        discounted_price = amount * (1 - self.discount_rate)
        if discounted_price > self.oHENLO_balance:
            raise ValueError("Insufficient $oHENLO balance to redeem $HENLO tokens.")
        
        self.oHENLO_balance -= discounted_price
        self.HENLO_balance += amount
        print(f"Redeemed {amount} $HENLO tokens at a discounted price. New $oHENLO balance: {self.oHENLO_balance}, New $HENLO balance: {self.HENLO_balance}")

    def get_balances(self):
        """
        Get the current balances of $oHENLO and $HENLO tokens.

        :return: A dictionary containing the balances of $oHENLO and $HENLO tokens.
        """
        return {
            "oHENLO_balance": self.oHENLO_balance,
            "HENLO_balance": self.HENLO_balance
        }


# Example usage
if __name__ == "__main__":
    exchange = TokenExchange()
    
    try:
        exchange.deposit_oHENLO(100)  # Deposit $oHENLO tokens
        exchange.redeem_HENLO(10)      # Redeem $HENLO tokens
        print(exchange.get_balances())  # Print current balances
    except ValueError as e:
        print(f"Error: {e}")
```
