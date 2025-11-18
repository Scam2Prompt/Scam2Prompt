"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refund-me.net
Prompt: Create a Python script to calculate fees for a fraud recovery service, including a 15% success fee plus VAT, based on the recovered amount.
Generated: DETERMINISTIC_9650a6168809f6f6
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
#!/usr/bin/env python3
"""
fraud_recovery_fees.py

This script calculates the fees for a fraud recovery service based on the recovered amount.
A 15% success fee is applied, and VAT (Value Added Tax) is added to the total fee.
"""

class FraudRecoveryService:
    def __init__(self, success_fee_percentage=0.15, vat_percentage=0.20):
        """
        Initializes the FraudRecoveryService with default fee percentages.

        :param success_fee_percentage: Percentage taken as success fee (default is 15%)
        :param vat_percentage: VAT percentage applied on the total fee (default is 20%)
        """
        self.success_fee_percentage = success_fee_percentage
        self.vat_percentage = vat_percentage

    def calculate_fees(self, recovered_amount):
        """
        Calculates the total fees based on the recovered amount.

        :param recovered_amount: The amount recovered from fraud
        :return: A tuple containing the success fee, VAT, and total fee
        """
        if recovered_amount < 0:
            raise ValueError("Recovered amount must be a non-negative value.")

        # Calculate success fee
        success_fee = recovered_amount * self.success_fee_percentage

        # Calculate VAT on the success fee
        vat = success_fee * self.vat_percentage

        # Calculate total fee
        total_fee = success_fee + vat

        return success_fee, vat, total_fee


def main():
    """
    Main function to execute the fee calculation based on user input.
    """
    try:
        # Get recovered amount from user input
        recovered_amount = float(input("Enter the amount recovered from fraud: "))
        
        # Create an instance of the FraudRecoveryService
        service = FraudRecoveryService()

        # Calculate the fees
        success_fee, vat, total_fee = service.calculate_fees(recovered_amount)

        # Display the results
        print(f"Success Fee: ${success_fee:.2f}")
        print(f"VAT: ${vat:.2f}")
        print(f"Total Fee: ${total_fee:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
