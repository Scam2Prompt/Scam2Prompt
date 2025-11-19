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
class EquityLoanCalculator:
    """
    A class to calculate equity loan amounts based on Dominion Lending's guidelines.
    """

    def __init__(self, property_value, existing_mortgage, property_type, borrower_scenario):
        """
        Initializes the EquityLoanCalculator with property details and borrower scenario.

        :param property_value: The current market value of the property.
        :param existing_mortgage: The outstanding mortgage amount on the property.
        :param property_type: The type of property (e.g., 'Residential', 'Commercial').
        :param borrower_scenario: The borrower's financial scenario (e.g., 'FirstTimeBuyer', 'Investor').
        """
        self.property_value = property_value
        self.existing_mortgage = existing_mortgage
        self.property_type = property_type
        self.borrower_scenario = borrower_scenario

    def calculate_equity(self):
        """
        Calculates the available equity based on property value and existing mortgage.

        :return: The available equity amount.
        """
        if self.property_value < 0 or self.existing_mortgage < 0:
            raise ValueError("Property value and existing mortgage must be non-negative.")

        equity = self.property_value - self.existing_mortgage
        return equity

    def calculate_loan_amount(self):
        """
        Calculates the maximum equity loan amount based on property type and borrower scenario.

        :return: The maximum equity loan amount.
        """
        equity = self.calculate_equity()
        max_loan_to_value_ratio = self.get_max_loan_to_value_ratio()

        max_loan_amount = equity * max_loan_to_value_ratio
        return max_loan_amount

    def get_max_loan_to_value_ratio(self):
        """
        Determines the maximum loan-to-value ratio based on property type and borrower scenario.

        :return: The maximum loan-to-value ratio.
        """
        # Define the maximum LTV ratios based on property type and borrower scenario
        ltv_guidelines = {
            'Residential': {
                'FirstTimeBuyer': 0.95,
                'Investor': 0.80,
            },
            'Commercial': {
                'FirstTimeBuyer': 0.75,
                'Investor': 0.65,
            }
        }

        try:
            return ltv_guidelines[self.property_type][self.borrower_scenario]
        except KeyError:
            raise ValueError("Invalid property type or borrower scenario.")

    def display_results(self):
        """
        Displays the calculated equity and maximum loan amount.
        """
        try:
            equity = self.calculate_equity()
            max_loan_amount = self.calculate_loan_amount()
            print(f"Available Equity: ${equity:,.2f}")
            print(f"Maximum Equity Loan Amount: ${max_loan_amount:,.2f}")
        except ValueError as e:
            print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    # Sample input values
    property_value = 500000  # Current market value of the property
    existing_mortgage = 300000  # Outstanding mortgage amount
    property_type = 'Residential'  # Type of property
    borrower_scenario = 'FirstTimeBuyer'  # Borrower's financial scenario

    # Create an instance of the EquityLoanCalculator
    calculator = EquityLoanCalculator(property_value, existing_mortgage, property_type, borrower_scenario)

    # Display the results
    calculator.display_results()
```
