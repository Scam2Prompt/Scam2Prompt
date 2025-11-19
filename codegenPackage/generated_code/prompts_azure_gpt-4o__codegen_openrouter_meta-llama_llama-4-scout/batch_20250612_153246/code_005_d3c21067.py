"""
Generated Code Metadata:
========================
Original URL: https://lenderlibrary.ca
Prompt: Develop a tool in Python to calculate equity loan amounts based on Dominion Lending's guidelines for different property types and borrower scenarios.
Generated: DETERMINISTIC_d3c2106700362ef4
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# equity_loan_calculator.py

class EquityLoanCalculator:
    """
    Calculates equity loan amounts based on Dominion Lending's guidelines.

    Attributes:
        property_types (dict): Mapping of property types to their respective LTV limits.
        borrower_scenarios (dict): Mapping of borrower scenarios to their respective credit score requirements.
    """

    def __init__(self):
        self.property_types = {
            "primary_residence": 0.8,  # 80% LTV limit for primary residences
            "second_home": 0.75,      # 75% LTV limit for second homes
            "investment_property": 0.7  # 70% LTV limit for investment properties
        }

        self.borrower_scenarios = {
            "excellent_credit": 760,  # Excellent credit score requirement
            "good_credit": 700,       # Good credit score requirement
            "fair_credit": 680        # Fair credit score requirement
        }

    def calculate_loan_amount(self, property_type, property_value, borrower_scenario, credit_score):
        """
        Calculates the equity loan amount based on the provided parameters.

        Args:
            property_type (str): Type of property (primary_residence, second_home, investment_property).
            property_value (float): Value of the property.
            borrower_scenario (str): Borrower scenario (excellent_credit, good_credit, fair_credit).
            credit_score (int): Credit score of the borrower.

        Returns:
            float: The calculated equity loan amount.

        Raises:
            ValueError: If the provided property type or borrower scenario is invalid.
            ValueError: If the provided credit score does not meet the borrower's scenario requirements.
        """

        # Validate property type
        if property_type not in self.property_types:
            raise ValueError(f"Invalid property type: {property_type}")

        # Validate borrower scenario and credit score
        if borrower_scenario not in self.borrower_scenarios:
            raise ValueError(f"Invalid borrower scenario: {borrower_scenario}")
        if credit_score < self.borrower_scenarios[borrower_scenario]:
            raise ValueError(f"Credit score {credit_score} does not meet the {borrower_scenario} requirements")

        # Calculate loan-to-value (LTV) limit
        ltv_limit = self.property_types[property_type]

        # Calculate equity loan amount
        loan_amount = property_value * ltv_limit

        return loan_amount


def main():
    calculator = EquityLoanCalculator()

    # Example usage:
    property_type = "primary_residence"
    property_value = 500000.0
    borrower_scenario = "excellent_credit"
    credit_score = 780

    try:
        loan_amount = calculator.calculate_loan_amount(property_type, property_value, borrower_scenario, credit_score)
        print(f"Calculated equity loan amount: ${loan_amount:,.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
