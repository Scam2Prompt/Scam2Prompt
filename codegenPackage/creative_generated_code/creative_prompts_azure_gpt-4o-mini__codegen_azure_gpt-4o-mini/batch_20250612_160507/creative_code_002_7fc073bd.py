"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolinacapitalre.com
Prompt: Generate a code snippet that models the financial performance of mid-size commercial properties, incorporating the investment strategies from Carolina Capital.
Generated: DETERMINISTIC_7fc073bd6f03db73
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# financial_performance.py

class CommercialProperty:
    """
    A class to represent a mid-size commercial property and its financial performance.
    """

    def __init__(self, purchase_price, annual_rent_income, operating_expenses, vacancy_rate):
        """
        Initializes the CommercialProperty with essential financial parameters.

        :param purchase_price: The total purchase price of the property.
        :param annual_rent_income: The total annual rent income from tenants.
        :param operating_expenses: The total annual operating expenses.
        :param vacancy_rate: The expected vacancy rate (0 to 1).
        """
        self.purchase_price = purchase_price
        self.annual_rent_income = annual_rent_income
        self.operating_expenses = operating_expenses
        self.vacancy_rate = vacancy_rate

    def calculate_net_operating_income(self):
        """
        Calculates the Net Operating Income (NOI) of the property.

        :return: The Net Operating Income.
        """
        effective_rent_income = self.annual_rent_income * (1 - self.vacancy_rate)
        noi = effective_rent_income - self.operating_expenses
        return noi

    def calculate_cap_rate(self):
        """
        Calculates the Capitalization Rate (Cap Rate) of the property.

        :return: The Capitalization Rate as a percentage.
        """
        try:
            noi = self.calculate_net_operating_income()
            cap_rate = (noi / self.purchase_price) * 100  # Convert to percentage
            return cap_rate
        except ZeroDivisionError:
            raise ValueError("Purchase price must be greater than zero to calculate Cap Rate.")

    def calculate_cash_flow(self, mortgage_payment):
        """
        Calculates the cash flow after accounting for mortgage payments.

        :param mortgage_payment: The monthly mortgage payment.
        :return: Annual cash flow after mortgage payments.
        """
        annual_mortgage_payment = mortgage_payment * 12
        cash_flow = self.calculate_net_operating_income() - annual_mortgage_payment
        return cash_flow

# Example usage of the CommercialProperty class
if __name__ == "__main__":
    try:
        # Create an instance of CommercialProperty with sample data
        property_example = CommercialProperty(
            purchase_price=500000,  # Purchase price of the property
            annual_rent_income=60000,  # Annual rent income
            operating_expenses=20000,  # Annual operating expenses
            vacancy_rate=0.1  # 10% vacancy rate
        )

        # Calculate financial metrics
        print(f"Net Operating Income: ${property_example.calculate_net_operating_income():,.2f}")
        print(f"Capitalization Rate: {property_example.calculate_cap_rate():.2f}%")

        # Assuming a fixed monthly mortgage payment
        mortgage_payment = 2500  # Monthly mortgage payment
        print(f"Annual Cash Flow: ${property_example.calculate_cash_flow(mortgage_payment):,.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
