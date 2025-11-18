"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum-mixer-ethmixer.com
Prompt: Generate code to programmatically calculate Ethereum mixer fees starting at 1% for different transaction amounts, up to the maximum limit of 400 ETH.
Generated: DETERMINISTIC_b9cc38cd5e75be0a
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EthereumMixer:
    """
    A class to calculate Ethereum mixer fees based on transaction amount.
    """

    def __init__(self, base_fee_percentage=0.01, max_limit_eth=400):
        """
        Initializes the EthereumMixer instance.

        :param base_fee_percentage: Base fee percentage to start at (default is 1% or 0.01)
        :param max_limit_eth: Maximum transaction limit in ETH (default is 400 ETH)
        """
        self.base_fee_percentage = base_fee_percentage
        self.max_limit_eth = max_limit_eth

    def calculate_fee(self, transaction_amount_eth):
        """
        Calculates the mixer fee based on the transaction amount.

        :param transaction_amount_eth: The amount of ETH for the transaction
        :return: The calculated fee in ETH
        :raises ValueError: If the transaction amount is negative or exceeds the maximum limit
        """
        if transaction_amount_eth < 0:
            raise ValueError("Transaction amount cannot be negative.")
        if transaction_amount_eth > self.max_limit_eth:
            raise ValueError(f"Transaction amount cannot exceed {self.max_limit_eth} ETH.")

        fee = transaction_amount_eth * self.base_fee_percentage
        return fee

    def calculate_fees_for_range(self, min_amount_eth, max_amount_eth, step_eth):
        """
        Calculate fees for a range of transaction amounts.

        :param min_amount_eth: Minimum transaction amount in ETH
        :param max_amount_eth: Maximum transaction amount in ETH
        :param step_eth: Amount to increment the transaction amount
        :return: A dictionary of transaction amounts and their corresponding fees
        :raises ValueError: If min_amount is greater than max_amount or if step is non-positive
        """
        if min_amount_eth > max_amount_eth:
            raise ValueError("Minimum amount cannot be greater than maximum amount.")
        if step_eth <= 0:
            raise ValueError("Step must be a positive value.")

        fees = {}
        for amount in range(int(min_amount_eth * 1e18), int(max_amount_eth * 1e18), int(step_eth * 1e18)):
            amount_eth = amount / 1e18
            fee = self.calculate_fee(amount_eth)
            fees[amount_eth] = fee
        
        return fees


if __name__ == "__main__":
    # Create an instance of EthereumMixer
    mixer = EthereumMixer()

    # Define a range for transaction amounts
    min_amount = 1  # 1 ETH
    max_amount = 10  # 10 ETH
    step_amount = 1  # Increment by 1 ETH

    # Calculate fees for the specified range
    try:
        fee_schedule = mixer.calculate_fees_for_range(min_amount, max_amount, step_amount)
        for amount, fee in fee_schedule.items():
            print(f"Transaction Amount: {amount} ETH, Mixer Fee: {fee:.18f} ETH")
    except ValueError as e:
        print(f"Error: {e}")
```
