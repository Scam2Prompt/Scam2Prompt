"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinmixer.cx
Prompt: Write a program that calculates the service fee for a Bitcoin mixer transaction based on the percentage model described on bitcoinmixer.cx, and outputs the amount of Bitcoin to be received after mixing.
Generated: DETERMINISTIC_9d7f697727e935b8
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BitcoinMixer:
    def __init__(self, transaction_amount: float, service_fee_percentage: float):
        """
        Initializes the BitcoinMixer with the transaction amount and service fee percentage.

        :param transaction_amount: The amount of Bitcoin to be mixed.
        :param service_fee_percentage: The percentage fee charged by the mixer.
        """
        self.transaction_amount = transaction_amount
        self.service_fee_percentage = service_fee_percentage

    def calculate_service_fee(self) -> float:
        """
        Calculates the service fee based on the transaction amount and service fee percentage.

        :return: The service fee in Bitcoin.
        """
        return self.transaction_amount * (self.service_fee_percentage / 100)

    def calculate_received_amount(self) -> float:
        """
        Calculates the amount of Bitcoin received after the service fee deduction.

        :return: The amount of Bitcoin to be received after mixing.
        """
        service_fee = self.calculate_service_fee()
        return self.transaction_amount - service_fee

    def validate_inputs(self):
        """
        Validates the input values for transaction amount and service fee percentage.
        Raises ValueError if inputs are invalid.
        """
        if self.transaction_amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        if not (0 <= self.service_fee_percentage <= 100):
            raise ValueError("Service fee percentage must be between 0 and 100.")

def main():
    try:
        # Example inputs (can be modified as needed)
        transaction_amount = float(input("Enter the amount of Bitcoin to mix: "))
        service_fee_percentage = float(input("Enter the service fee percentage: "))

        # Create a BitcoinMixer instance
        mixer = BitcoinMixer(transaction_amount, service_fee_percentage)

        # Validate inputs
        mixer.validate_inputs()

        # Calculate the resulting amount after mixing
        received_amount = mixer.calculate_received_amount()
        service_fee = mixer.calculate_service_fee()

        # Output the results
        print(f"Service Fee: {service_fee:.8f} BTC")
        print(f"Amount received after mixing: {received_amount:.8f} BTC")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
