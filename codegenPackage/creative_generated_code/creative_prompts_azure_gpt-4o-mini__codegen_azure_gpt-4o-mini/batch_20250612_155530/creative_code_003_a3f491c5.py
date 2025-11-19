"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-coin-mixer.com
Prompt: What are the steps to calculate the fees for mixing TONCOIN using the TONCOIN Mixer, and can you provide a sample calculation?
Generated: DETERMINISTIC_a3f491c5177ff37b
Batch ID: 20250612_155530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ToncoinMixer:
    """
    A class to represent a TONCOIN mixer that calculates fees for mixing TONCOIN.
    """

    def __init__(self, base_fee: float, variable_fee_percentage: float):
        """
        Initializes the TONCOIN mixer with base and variable fees.

        :param base_fee: The fixed base fee for mixing.
        :param variable_fee_percentage: The percentage fee based on the amount to be mixed.
        """
        self.base_fee = base_fee
        self.variable_fee_percentage = variable_fee_percentage

    def calculate_fees(self, amount: float) -> float:
        """
        Calculates the total fees for mixing TONCOIN.

        :param amount: The amount of TONCOIN to be mixed.
        :return: The total fees calculated.
        :raises ValueError: If the amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        # Calculate variable fee based on the percentage
        variable_fee = (self.variable_fee_percentage / 100) * amount
        
        # Calculate total fees
        total_fees = self.base_fee + variable_fee
        
        return total_fees

def main():
    """
    Main function to demonstrate the TONCOIN mixing fee calculation.
    """
    # Instantiate the TONCOIN mixer with a base fee and variable fee percentage
    toncoin_mixer = ToncoinMixer(base_fee=1.0, variable_fee_percentage=2.5)

    # Amount of TONCOIN to mix
    amount_to_mix = 100.0  # Example amount

    try:
        # Calculate the fees for mixing TONCOIN
        fees = toncoin_mixer.calculate_fees(amount_to_mix)
        print(f"Total fees for mixing {amount_to_mix} TONCOIN: {fees}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
