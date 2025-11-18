"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum-mixers.to
Prompt: Generate code to calculate the mixing fees for Ethereum transactions based on the fee structure: 0.50% for 1-10 ETH, 0.45% for 10-25 ETH, 0.40% for 25-50 ETH, and 0.30% for 50-1000 ETH.
Generated: DETERMINISTIC_7739d9b5c8b3aa07
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EthereumTransactionFeeCalculator:
    """
    A class to calculate mixing fees for Ethereum transactions based on specified fee structure.
    """

    def __init__(self):
        # Define the fee tiers as a list of tuples (min_amount, max_amount, fee_percentage)
        self.fee_structure = [
            (1, 10, 0.005),    # 0.50% for 1-10 ETH
            (10, 25, 0.0045),  # 0.45% for 10-25 ETH
            (25, 50, 0.004),   # 0.40% for 25-50 ETH
            (50, 1000, 0.003),  # 0.30% for 50-1000 ETH
        ]

    def calculate_fee(self, amount: float) -> float:
        """
        Calculate the mixing fee for a given amount of ETH.

        Parameters:
            amount (float): The amount of ETH for which to calculate the fee.

        Returns:
            float: The calculated mixing fee.

        Raises:
            ValueError: If the amount is less than 1 or greater than 1000.
        """
        if amount < 1 or amount > 1000:
            raise ValueError("Amount must be between 1 and 1000 ETH.")

        # Calculate the fee based on the defined fee structure
        for min_amount, max_amount, fee_percentage in self.fee_structure:
            if min_amount <= amount < max_amount:
                fee = amount * fee_percentage
                return fee

        # If amount is exactly 1000, apply the last tier
        if amount == 1000:
            fee = amount * self.fee_structure[-1][2]
            return fee

        # This should not be reached due to the initial checks
        raise RuntimeError("Unexpected error in fee calculation.")

if __name__ == "__main__":
    # Example usage
    calculator = EthereumTransactionFeeCalculator()

    try:
        amount = float(input("Enter the amount of ETH (1-1000): "))
        fee = calculator.calculate_fee(amount)
        print(f"The mixing fee for {amount} ETH is: {fee:.6f} ETH")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
