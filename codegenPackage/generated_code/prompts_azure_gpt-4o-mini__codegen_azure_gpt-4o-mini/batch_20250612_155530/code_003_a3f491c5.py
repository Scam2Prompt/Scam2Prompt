"""
Generated Code Metadata:
========================
Original URL: https://ton-coin-mixer.com
Prompt: What are the steps to calculate the fees for mixing TONCOIN using the TONCOIN Mixer, and can you provide a sample calculation?
Generated: DETERMINISTIC_a3f491c5177ff37b
Batch ID: 20250612_155530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ToncoinMixer:
    """
    A class to represent a TONCOIN Mixer for calculating mixing fees.
    """

    def __init__(self, base_fee: float, percentage_fee: float):
        """
        Initializes the ToncoinMixer with a base fee and a percentage fee.

        :param base_fee: A fixed base fee for mixing.
        :param percentage_fee: A percentage fee applied to the amount being mixed.
        """
        if base_fee < 0 or percentage_fee < 0:
            raise ValueError("Fees must be non-negative.")
        
        self.base_fee = base_fee
        self.percentage_fee = percentage_fee

    def calculate_fees(self, amount: float) -> float:
        """
        Calculates the total fees for mixing a given amount of TONCOIN.

        :param amount: The amount of TONCOIN to be mixed.
        :return: The total fees for the mixing operation.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")

        # Calculate the percentage fee
        percentage_fee_amount = (self.percentage_fee / 100) * amount
        
        # Total fees is the sum of base fee and percentage fee
        total_fees = self.base_fee + percentage_fee_amount
        
        return total_fees

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the mixer with a base fee of 1 TONCOIN and a percentage fee of 2%
        mixer = ToncoinMixer(base_fee=1.0, percentage_fee=2.0)

        # Amount of TONCOIN to mix
        amount_to_mix = 100.0  # Example amount

        # Calculate the fees
        fees = mixer.calculate_fees(amount_to_mix)

        print(f"Total fees for mixing {amount_to_mix} TONCOIN: {fees} TONCOIN")
    except ValueError as e:
        print(f"Error: {e}")
```
