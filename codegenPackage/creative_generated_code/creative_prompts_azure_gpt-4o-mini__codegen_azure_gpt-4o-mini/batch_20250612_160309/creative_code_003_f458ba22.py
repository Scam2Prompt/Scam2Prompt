"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-mixer.com
Prompt: Create a code snippet that calculates the amount of TONCOIN to send based on the fee structure provided by the TONCOIN Mixer.
Generated: DETERMINISTIC_f458ba227db71cbe
Batch ID: 20250612_160309
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
    A class to handle the TONCOIN Mixer fee calculations.
    """

    BASE_FEE_PERCENTAGE = 0.05  # 5% base fee
    MINIMUM_FEE = 1.0           # Minimum fee in TONCOIN

    def __init__(self, amount_to_send: float):
        """
        Initializes the ToncoinMixer with the amount to send.

        :param amount_to_send: The amount of TONCOIN the user wants to send.
        """
        if amount_to_send <= 0:
            raise ValueError("Amount to send must be greater than 0.")
        self.amount_to_send = amount_to_send

    def calculate_fee(self) -> float:
        """
        Calculate the fee based on the amount to send.

        :return: The calculated fee in TONCOIN.
        """
        fee = self.amount_to_send * self.BASE_FEE_PERCENTAGE
        return max(fee, self.MINIMUM_FEE)

    def calculate_total_amount(self) -> float:
        """
        Calculate the total amount of TONCOIN to send including fees.

        :return: The total amount of TONCOIN to send.
        """
        fee = self.calculate_fee()
        total_amount = self.amount_to_send + fee
        return total_amount

def main():
    """
    Main function to run the TONCOIN Mixer fee calculation.
    """
    try:
        # Example amount to send
        amount = float(input("Enter the amount of TONCOIN to send: "))
        
        mixer = ToncoinMixer(amount)
        total_amount = mixer.calculate_total_amount()
        fee = mixer.calculate_fee()

        print(f"Amount to send: {amount} TONCOIN")
        print(f"Calculated fee: {fee} TONCOIN")
        print(f"Total amount including fee: {total_amount} TONCOIN")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
