"""
Generated Code Metadata:
========================
Original URL: https://bnb-mixer.eth.limo
Prompt: Develop a script to calculate the mixing fees for BNB transactions based on the fee structure provided by BNB Mixer.
Generated: DETERMINISTIC_69f82ac71a13e621
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BNBMixer:
    def __init__(self, base_fee: float, additional_fee_per_bnb: float):
        """
        Initialize the BNBMixer with the base fee and additional fee per BNB.

        :param base_fee: The fixed base fee for the transaction.
        :param additional_fee_per_bnb: The fee charged for each BNB mixed.
        """
        self.base_fee = base_fee
        self.additional_fee_per_bnb = additional_fee_per_bnb

    def calculate_fee(self, bnb_amount: float) -> float:
        """
        Calculate the total mixing fee based on the amount of BNB.

        :param bnb_amount: The amount of BNB to be mixed.
        :return: The total mixing fee.
        :raises ValueError: If the bnb_amount is negative.
        """
        if bnb_amount < 0:
            logging.error("Negative BNB amount provided: %s", bnb_amount)
            raise ValueError("BNB amount must be non-negative.")

        total_fee = self.base_fee + (self.additional_fee_per_bnb * bnb_amount)
        logging.info("Calculated fee for %s BNB: %s", bnb_amount, total_fee)
        return total_fee

def main():
    """
    Main function to execute the BNB mixing fee calculation.
    """
    # Example fee structure
    base_fee = 0.01  # Base fee in BNB
    additional_fee_per_bnb = 0.005  # Additional fee per BNB in BNB

    # Create an instance of BNBMixer
    mixer = BNBMixer(base_fee, additional_fee_per_bnb)

    # Example BNB amounts to calculate fees for
    bnb_amounts = [1, 5, 10, -2]  # The last value is for testing error handling

    for amount in bnb_amounts:
        try:
            fee = mixer.calculate_fee(amount)
            print(f"Mixing fee for {amount} BNB: {fee} BNB")
        except ValueError as e:
            print(f"Error calculating fee for {amount} BNB: {e}")

if __name__ == "__main__":
    main()
```
