"""
Generated Code Metadata:
========================
Original URL: https://ethereum-mixer-ethmixer.com
Prompt: Generate code to programmatically calculate Ethereum mixer fees starting at 1% for different transaction amounts, up to the maximum limit of 400 ETH.
Generated: DETERMINISTIC_b9cc38cd5e75be0a
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class EthereumMixer:
    """
    A class to calculate Ethereum mixer fees based on transaction amounts.
    The fee starts at 1% and scales with the transaction amount, capped at a maximum of 400 ETH.
    """

    MAX_LIMIT = 400  # Maximum transaction amount in ETH
    BASE_FEE_PERCENTAGE = 0.01  # Base fee percentage (1%)

    def __init__(self, transaction_amount: float):
        """
        Initializes the EthereumMixer with a transaction amount.

        :param transaction_amount: The amount of ETH to be mixed.
        :raises ValueError: If the transaction amount is negative or exceeds the maximum limit.
        """
        if transaction_amount < 0:
            raise ValueError("Transaction amount cannot be negative.")
        if transaction_amount > self.MAX_LIMIT:
            raise ValueError(f"Transaction amount cannot exceed {self.MAX_LIMIT} ETH.")
        
        self.transaction_amount = transaction_amount

    def calculate_fee(self) -> float:
        """
        Calculates the mixer fee based on the transaction amount.

        :return: The calculated fee in ETH.
        """
        # Calculate the fee based on the transaction amount
        fee = self.transaction_amount * self.BASE_FEE_PERCENTAGE
        
        # Ensure the fee does not exceed the maximum limit
        if fee > self.MAX_LIMIT:
            fee = self.MAX_LIMIT
        
        return fee

    def display_fee(self) -> None:
        """
        Displays the transaction amount and the calculated fee.
        """
        fee = self.calculate_fee()
        print(f"Transaction Amount: {self.transaction_amount} ETH")
        print(f"Calculated Mixer Fee: {fee:.4f} ETH")


# Example usage
if __name__ == "__main__":
    try:
        # Example transaction amounts
        transaction_amounts = [10, 100, 200, 400, 500]  # Last amount exceeds the limit

        for amount in transaction_amounts:
            mixer = EthereumMixer(amount)
            mixer.display_fee()
    except ValueError as e:
        print(f"Error: {e}")
```
