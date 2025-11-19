"""
Generated Code Metadata:
========================
Original URL: https://rhinofinance.com
Prompt: Write a Python code snippet to calculate the fees for a settlement loan from Rhino Finance, assuming a loan amount of $10,000 and a fee structure based on the provided terms.
Generated: DETERMINISTIC_e0ae0eb1cae0b7a5
Batch ID: 20250622_211156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# settlement_loan_fees.py

class SettlementLoanFeesCalculator:
    """
    Calculates fees for a settlement loan from Rhino Finance.

    Attributes:
        loan_amount (float): The loan amount.
        fee_structure (dict): The fee structure with terms.

    """

    def __init__(self, loan_amount, fee_structure):
        """
        Initializes the calculator.

        Args:
            loan_amount (float): The loan amount.
            fee_structure (dict): The fee structure with terms.

        Raises:
            ValueError: If loan amount or fee structure is invalid.

        """
        if loan_amount <= 0:
            raise ValueError("Loan amount must be greater than zero.")

        if not isinstance(fee_structure, dict) or not fee_structure:
            raise ValueError("Fee structure must be a non-empty dictionary.")

        self.loan_amount = loan_amount
        self.fee_structure = fee_structure

    def calculate_fees(self):
        """
        Calculates the fees based on the loan amount and fee structure.

        Returns:
            dict: A dictionary containing the calculated fees.

        """
        fees = {}

        # Assuming fee structure is a dictionary with 'origination_fee', 
        # 'late_fee', and 'prepayment_penalty' as keys
        origination_fee_percentage = self.fee_structure.get('origination_fee', 0) / 100
        late_fee_percentage = self.fee_structure.get('late_fee', 0) / 100
        prepayment_penalty_percentage = self.fee_structure.get('prepayment_penalty', 0) / 100

        fees['origination_fee'] = self.loan_amount * origination_fee_percentage
        fees['late_fee'] = self.loan_amount * late_fee_percentage
        fees['prepayment_penalty'] = self.loan_amount * prepayment_penalty_percentage

        return fees


def main():
    # Define the loan amount and fee structure
    loan_amount = 10000
    fee_structure = {
        'origination_fee': 2,  # 2% origination fee
        'late_fee': 0.5,       # 0.5% late fee
        'prepayment_penalty': 1  # 1% prepayment penalty
    }

    try:
        calculator = SettlementLoanFeesCalculator(loan_amount, fee_structure)
        fees = calculator.calculate_fees()

        print("Calculated Fees:")
        for fee_type, fee_amount in fees.items():
            print(f"{fee_type.capitalize().replace('_', ' ')}: ${fee_amount:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
