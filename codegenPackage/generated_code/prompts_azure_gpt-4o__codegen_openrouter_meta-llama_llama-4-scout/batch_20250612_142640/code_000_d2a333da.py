"""
Generated Code Metadata:
========================
Original URL: https://rhinoassetfinance.com
Prompt: Write a Python script to simulate an asset finance calculator that includes seasonal payment options for industries like construction, manufacturing, or agriculture, as described on Rhino Asset Finance's website.
Generated: DETERMINISTIC_d2a333da6d8acce8
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# asset_finance_calculator.py

class AssetFinanceCalculator:
    """
    Simulates an asset finance calculator with seasonal payment options.
    """

    def __init__(self, asset_value, finance_term, interest_rate, payment_frequency):
        """
        Initializes the calculator with asset details.

        Args:
            asset_value (float): The value of the asset being financed.
            finance_term (int): The term of the finance in years.
            interest_rate (float): The annual interest rate as a decimal.
            payment_frequency (str): The frequency of payments (e.g., 'monthly', 'quarterly', 'annually').
        """
        self.asset_value = asset_value
        self.finance_term = finance_term
        self.interest_rate = interest_rate
        self.payment_frequency = payment_frequency

    def calculate_seasonal_payment(self, industry):
        """
        Calculates the seasonal payment based on the industry.

        Args:
            industry (str): The industry (e.g., 'construction', 'manufacturing', 'agriculture').

        Returns:
            float: The seasonal payment amount.
        """
        seasonal_payment_factors = {
            'construction': 0.3,  # 30% of annual payment
            'manufacturing': 0.25,  # 25% of annual payment
            'agriculture': 0.2  # 20% of annual payment
        }

        if industry not in seasonal_payment_factors:
            raise ValueError(f"Unsupported industry: {industry}")

        annual_payment = self.calculate_annual_payment()
        seasonal_payment = annual_payment * seasonal_payment_factors[industry]
        return seasonal_payment

    def calculate_annual_payment(self):
        """
        Calculates the annual payment using the formula for monthly payments.

        Returns:
            float: The annual payment amount.
        """
        monthly_interest_rate = self.interest_rate / 12
        number_of_payments = self.finance_term * 12

        monthly_payment = self.asset_value * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments / (
                (1 + monthly_interest_rate) ** number_of_payments - 1)

        annual_payment = monthly_payment * 12
        return annual_payment

    def calculate_payment_schedule(self, industry):
        """
        Calculates the payment schedule with seasonal payments.

        Args:
            industry (str): The industry (e.g., 'construction', 'manufacturing', 'agriculture').

        Returns:
            list: A list of dictionaries representing the payment schedule.
        """
        seasonal_payment = self.calculate_seasonal_payment(industry)
        payment_schedule = []

        for i in range(self.finance_term):
            for _ in range(4):  # Quarterly payments
                payment_schedule.append({
                    'payment_date': f"Year {i+1}, Quarter {_+1}",
                    'payment_amount': seasonal_payment
                })

        return payment_schedule


def main():
    try:
        asset_value = 100000  # Example asset value
        finance_term = 5  # Example finance term in years
        interest_rate = 0.06  # Example interest rate (6%)
        payment_frequency = 'quarterly'  # Example payment frequency
        industry = 'construction'  # Example industry

        calculator = AssetFinanceCalculator(asset_value, finance_term, interest_rate, payment_frequency)
        seasonal_payment = calculator.calculate_seasonal_payment(industry)
        payment_schedule = calculator.calculate_payment_schedule(industry)

        print(f"Seasonal Payment: ${seasonal_payment:.2f}")
        print("Payment Schedule:")
        for payment in payment_schedule:
            print(f"{payment['payment_date']}: ${payment['payment_amount']:.2f}")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
