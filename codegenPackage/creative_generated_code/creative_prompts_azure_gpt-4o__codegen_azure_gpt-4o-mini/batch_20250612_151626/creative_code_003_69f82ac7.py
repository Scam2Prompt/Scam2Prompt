"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bnb-mixer.eth.limo
Prompt: Develop a script to calculate the mixing fees for BNB transactions based on the fee structure provided by BNB Mixer.
Generated: DETERMINISTIC_69f82ac71a13e621
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# bnb_mixer.py

class BnbMixer:
    """
    A class to calculate mixing fees for BNB transactions based on the BNB Mixer fee structure.
    """

    def __init__(self, mixing_fee_rate=0.02, min_fee=0.0001):
        """
        Initialize the BnbMixer with specified fee parameters.

        :param mixing_fee_rate: The percentage fee applied to the transaction (default is 2%)
        :param min_fee: The minimum fee that can be charged (default is 0.0001 BNB)
        """
        self.mixing_fee_rate = mixing_fee_rate
        self.min_fee = min_fee

    def calculate_fee(self, transaction_amount):
        """
        Calculate the mixing fee for a given transaction amount.

        :param transaction_amount: The amount of BNB to be mixed
        :return: The calculated mixing fee
        :raises ValueError: If the transaction amount is negative or zero
        """
        if transaction_amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")

        # Calculate the fee based on the mixing fee rate
        fee = transaction_amount * self.mixing_fee_rate

        # Ensure the fee meets the minimum fee requirement
        if fee < self.min_fee:
            fee = self.min_fee

        return fee

    def display_fee(self, transaction_amount):
        """
        Display the mixing fee for a given transaction amount.

        :param transaction_amount: The amount of BNB to be mixed
        """
        try:
            fee = self.calculate_fee(transaction_amount)
            print(f"Mixing fee for {transaction_amount} BNB: {fee:.8f} BNB")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Create an instance of the BnbMixer
    mixer = BnbMixer()

    # Example transaction amounts
    transaction_amounts = [0.1, 0.5, 1, 0, -0.1]

    # Calculate and display fees for the example transaction amounts
    for amount in transaction_amounts:
        mixer.display_fee(amount)
```
