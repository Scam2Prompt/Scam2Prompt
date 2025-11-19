"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zealvsmetamask.com
Prompt: Generate a function that calculates the potential yield and cashback based on GNO token holdings in Zeal Wallet.
Generated: DETERMINISTIC_b796574772492900
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ZealWallet:
    def __init__(self, gno_balance: float, annual_yield_rate: float, cashback_rate: float):
        """
        Initializes the ZealWallet with GNO token holdings and rates.

        :param gno_balance: The amount of GNO tokens held in the wallet.
        :param annual_yield_rate: The annual yield rate as a decimal (e.g., 0.05 for 5%).
        :param cashback_rate: The cashback rate as a decimal (e.g., 0.02 for 2%).
        """
        if gno_balance < 0:
            raise ValueError("GNO balance cannot be negative.")
        if not (0 <= annual_yield_rate <= 1):
            raise ValueError("Annual yield rate must be between 0 and 1.")
        if not (0 <= cashback_rate <= 1):
            raise ValueError("Cashback rate must be between 0 and 1.")

        self.gno_balance = gno_balance
        self.annual_yield_rate = annual_yield_rate
        self.cashback_rate = cashback_rate

    def calculate_yield(self) -> float:
        """
        Calculates the potential yield based on GNO holdings and annual yield rate.

        :return: The potential yield from GNO holdings.
        """
        yield_amount = self.gno_balance * self.annual_yield_rate
        return yield_amount

    def calculate_cashback(self) -> float:
        """
        Calculates the cashback based on GNO holdings and cashback rate.

        :return: The cashback amount from GNO holdings.
        """
        cashback_amount = self.gno_balance * self.cashback_rate
        return cashback_amount

    def calculate_total_potential(self) -> dict:
        """
        Calculates the total potential yield and cashback.

        :return: A dictionary containing yield and cashback amounts.
        """
        yield_amount = self.calculate_yield()
        cashback_amount = self.calculate_cashback()
        
        return {
            "yield": yield_amount,
            "cashback": cashback_amount,
            "total_potential": yield_amount + cashback_amount
        }


# Example usage:
if __name__ == "__main__":
    try:
        wallet = ZealWallet(gno_balance=100, annual_yield_rate=0.05, cashback_rate=0.02)
        potential = wallet.calculate_total_potential()
        print(f"Potential Yield: {potential['yield']}")
        print(f"Cashback: {potential['cashback']}")
        print(f"Total Potential: {potential['total_potential']}")
    except ValueError as e:
        print(f"Error: {e}")
```
