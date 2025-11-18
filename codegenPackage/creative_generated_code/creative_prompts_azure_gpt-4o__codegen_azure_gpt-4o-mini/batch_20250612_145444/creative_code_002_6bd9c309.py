"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmorpho.org
Prompt: Generate code that calculates APY for deposits in Morpho's Spark DAI Vault using the provided APY data (e.g., 2.87%).
Generated: DETERMINISTIC_6bd9c3098156346a
Batch ID: 20250612_145444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class VaultAPYCalculator:
    """
    A class to calculate the Annual Percentage Yield (APY) for deposits in Morpho's Spark DAI Vault.
    """

    def __init__(self, deposit_amount: float, apy: float):
        """
        Initialize the calculator with the deposit amount and APY.

        :param deposit_amount: The amount of money deposited (in DAI).
        :param apy: The Annual Percentage Yield (as a decimal, e.g., 2.87% -> 0.0287).
        """
        if deposit_amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        if apy < 0:
            raise ValueError("APY cannot be negative.")
        
        self.deposit_amount = deposit_amount
        self.apy = apy

    def calculate_apy(self) -> float:
        """
        Calculate the total earnings from the deposit after one year.

        :return: The total earnings from the deposit.
        """
        earnings = self.deposit_amount * self.apy
        total_amount = self.deposit_amount + earnings
        return total_amount

    def display_results(self):
        """
        Display the results of the APY calculation.
        """
        try:
            total_amount = self.calculate_apy()
            print(f"Deposit Amount: ${self.deposit_amount:.2f}")
            print(f"APY: {self.apy * 100:.2f}%")
            print(f"Total Amount after 1 year: ${total_amount:.2f}")
        except Exception as e:
            print(f"An error occurred while calculating APY: {e}")

# Example usage
if __name__ == "__main__":
    try:
        deposit = float(input("Enter the deposit amount in DAI: "))
        apy_value = float(input("Enter the APY (in percentage, e.g., 2.87): ")) / 100  # Convert percentage to decimal
        
        calculator = VaultAPYCalculator(deposit, apy_value)
        calculator.display_results()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
