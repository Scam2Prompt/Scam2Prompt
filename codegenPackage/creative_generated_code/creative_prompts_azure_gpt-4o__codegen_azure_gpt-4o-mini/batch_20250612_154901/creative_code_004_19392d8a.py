"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Create a Python function to calculate the total cost of transferring funds internationally, including fixed fees and percentage-based fees, as outlined in the website's description of Citibank and Moneta Money transfer charges.
Generated: DETERMINISTIC_19392d8acff96a44
Batch ID: 20250612_154901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TransferFeeCalculator:
    def __init__(self, fixed_fee, percentage_fee):
        """
        Initializes the TransferFeeCalculator with fixed and percentage fees.

        :param fixed_fee: Fixed fee for the transfer in the currency of the sender.
        :param percentage_fee: Percentage fee for the transfer as a decimal (e.g., 0.02 for 2%).
        """
        self.fixed_fee = fixed_fee
        self.percentage_fee = percentage_fee

    def calculate_total_cost(self, transfer_amount):
        """
        Calculates the total cost of transferring funds internationally.

        :param transfer_amount: The amount of money to be transferred in the currency of the sender.
        :return: The total cost of the transfer including fixed and percentage-based fees.
        :raises ValueError: If the transfer amount is negative or non-numeric.
        """
        # Validate the transfer amount
        if not isinstance(transfer_amount, (int, float)):
            raise ValueError("Transfer amount must be a number.")
        if transfer_amount < 0:
            raise ValueError("Transfer amount must be non-negative.")

        # Calculate percentage fee
        percentage_fee_amount = transfer_amount * self.percentage_fee

        # Calculate total cost
        total_cost = self.fixed_fee + percentage_fee_amount

        return total_cost


def main():
    """
    Main function to demonstrate the TransferFeeCalculator functionality.
    """
    try:
        # Example fixed fee and percentage fee for Citibank and Moneta
        citibank_fixed_fee = 15.00  # Example fixed fee in USD
        citibank_percentage_fee = 0.03  # 3% fee
        moneta_fixed_fee = 10.00  # Example fixed fee in USD
        moneta_percentage_fee = 0.025  # 2.5% fee

        # Create calculator instances
        citibank_calculator = TransferFeeCalculator(citibank_fixed_fee, citibank_percentage_fee)
        moneta_calculator = TransferFeeCalculator(moneta_fixed_fee, moneta_percentage_fee)

        # Sample transfer amount
        transfer_amount = 200.00  # Amount to be transferred in USD

        # Calculate total costs
        citibank_total = citibank_calculator.calculate_total_cost(transfer_amount)
        moneta_total = moneta_calculator.calculate_total_cost(transfer_amount)

        # Output the results
        print(f"Total cost for Citibank transfer: ${citibank_total:.2f}")
        print(f"Total cost for Moneta transfer: ${moneta_total:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
