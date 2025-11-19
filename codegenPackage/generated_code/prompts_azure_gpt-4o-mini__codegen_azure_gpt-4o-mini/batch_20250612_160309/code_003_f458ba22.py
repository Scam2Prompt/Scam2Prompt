"""
Generated Code Metadata:
========================
Original URL: https://ton-mixer.com
Prompt: Create a code snippet that calculates the amount of TONCOIN to send based on the fee structure provided by the TONCOIN Mixer.
Generated: DETERMINISTIC_f458ba227db71cbe
Batch ID: 20250612_160309
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
    A class to represent the TONCOIN Mixer and calculate the amount of TONCOIN to send
    based on the fee structure.
    """

    def __init__(self, base_fee: float, percentage_fee: float):
        """
        Initializes the ToncoinMixer with a base fee and a percentage fee.

        :param base_fee: The fixed base fee for the transaction.
        :param percentage_fee: The percentage fee applied to the amount being sent.
        """
        if base_fee < 0 or percentage_fee < 0:
            raise ValueError("Fees must be non-negative.")
        
        self.base_fee = base_fee
        self.percentage_fee = percentage_fee / 100  # Convert percentage to decimal

    def calculate_amount_to_send(self, amount_to_receive: float) -> float:
        """
        Calculates the amount of TONCOIN to send based on the desired amount to receive.

        :param amount_to_receive: The amount of TONCOIN the user wants to receive after fees.
        :return: The total amount of TONCOIN to send.
        """
        if amount_to_receive < 0:
            raise ValueError("Amount to receive must be non-negative.")

        # Calculate the total fees
        total_fee = self.base_fee + (self.percentage_fee * amount_to_receive)

        # Calculate the amount to send
        amount_to_send = amount_to_receive + total_fee

        return amount_to_send

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the TONCOIN Mixer with a base fee of 1 TONCOIN and a percentage fee of 2%
        mixer = ToncoinMixer(base_fee=1.0, percentage_fee=2.0)

        # Calculate the amount to send to receive 10 TONCOIN
        amount_to_receive = 10.0
        amount_to_send = mixer.calculate_amount_to_send(amount_to_receive)

        print(f"To receive {amount_to_receive} TONCOIN, you need to send {amount_to_send:.2f} TONCOIN.")
    except ValueError as e:
        print(f"Error: {e}")
```
