"""
Generated Code Metadata:
========================
Original URL: https://zealvsmetamask.com
Prompt: Generate a function that calculates the potential yield and cashback based on GNO token holdings in Zeal Wallet.
Generated: DETERMINISTIC_b796574772492900
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ZealWallet:
    def __init__(self, gno_holding: float, yield_rate: float, cashback_rate: float):
        """
        Initialize the ZealWallet with GNO holdings, yield rate, and cashback rate.

        :param gno_holding: The amount of GNO tokens held in the wallet.
        :param yield_rate: The annual yield rate as a decimal (e.g., 0.05 for 5%).
        :param cashback_rate: The cashback rate as a decimal (e.g., 0.02 for 2%).
        """
        if gno_holding < 0:
            raise ValueError("GNO holding cannot be negative.")
        if not (0 <= yield_rate <= 1):
            raise ValueError("Yield rate must be between 0 and 1.")
        if not (0 <= cashback_rate <= 1):
            raise ValueError("Cashback rate must be between 0 and 1.")

        self.gno_holding = gno_holding
        self.yield_rate = yield_rate
        self.cashback_rate = cashback_rate

    def calculate_yield(self) -> float:
        """
        Calculate the potential yield based on GNO holdings.

        :return: The potential yield amount.
        """
        potential_yield = self.gno_holding * self.yield_rate
        return potential_yield

    def calculate_cashback(self) -> float:
        """
        Calculate the cashback based on GNO holdings.

        :return: The cashback amount.
        """
        cashback = self.gno_holding * self.cashback_rate
        return cashback

    def calculate_total_benefit(self) -> float:
        """
        Calculate the total benefit from yield and cashback.

        :return: The total benefit amount.
        """
        total_benefit = self.calculate_yield() + self.calculate_cashback()
        return total_benefit


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the wallet with GNO holdings, yield rate, and cashback rate
        wallet = ZealWallet(gno_holding=100, yield_rate=0.05, cashback_rate=0.02)

        # Calculate potential yield
        yield_amount = wallet.calculate_yield()
        print(f"Potential Yield: {yield_amount:.2f} GNO")

        # Calculate cashback
        cashback_amount = wallet.calculate_cashback()
        print(f"Cashback: {cashback_amount:.2f} GNO")

        # Calculate total benefit
        total_benefit = wallet.calculate_total_benefit()
        print(f"Total Benefit: {total_benefit:.2f} GNO")

    except ValueError as e:
        print(f"Error: {e}")
```
