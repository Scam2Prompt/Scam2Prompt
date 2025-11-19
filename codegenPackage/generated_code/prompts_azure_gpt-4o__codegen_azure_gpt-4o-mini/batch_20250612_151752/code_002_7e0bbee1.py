"""
Generated Code Metadata:
========================
Original URL: https://zealvsmetamask.com
Prompt: Create a script to calculate cashback rewards for purchases using Zeal Wallet, factoring in the user's GNO token holdings to determine the rate (0-4%).
Generated: DETERMINISTIC_7e0bbee18c85b542
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ZealWallet:
    def __init__(self, gno_tokens: float):
        """
        Initialize the ZealWallet with the user's GNO token holdings.

        :param gno_tokens: The amount of GNO tokens the user holds.
        """
        if gno_tokens < 0:
            raise ValueError("GNO tokens cannot be negative.")
        self.gno_tokens = gno_tokens
        self.cashback_rate = self.calculate_cashback_rate()

    def calculate_cashback_rate(self) -> float:
        """
        Calculate the cashback rate based on GNO token holdings.

        :return: Cashback rate as a percentage (0-4%).
        """
        if self.gno_tokens < 100:
            return 0.0
        elif self.gno_tokens < 500:
            return 1.0
        elif self.gno_tokens < 1000:
            return 2.0
        elif self.gno_tokens < 5000:
            return 3.0
        else:
            return 4.0

    def calculate_cashback(self, purchase_amount: float) -> float:
        """
        Calculate the cashback amount for a given purchase.

        :param purchase_amount: The total amount of the purchase.
        :return: The cashback amount.
        """
        if purchase_amount < 0:
            raise ValueError("Purchase amount cannot be negative.")
        
        cashback = (self.cashback_rate / 100) * purchase_amount
        return cashback

def main():
    """
    Main function to demonstrate cashback calculation.
    """
    try:
        # Example user GNO token holdings
        user_gno_tokens = float(input("Enter your GNO token holdings: "))
        wallet = ZealWallet(user_gno_tokens)

        # Example purchase amount
        purchase_amount = float(input("Enter the purchase amount: "))
        cashback = wallet.calculate_cashback(purchase_amount)

        print(f"Your cashback for a purchase of ${purchase_amount:.2f} is: ${cashback:.2f} at a rate of {wallet.cashback_rate}%.")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
