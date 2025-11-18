"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alghanim-capital.com
Prompt: Create a script to calculate asset appreciation for real estate investments, incorporating principles of value creation and superior returns as emphasized by Alghanim Capital.
Generated: DETERMINISTIC_76003431ead2d830
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class RealEstateInvestment:
    """
    A class to represent a real estate investment and calculate its appreciation.
    """

    def __init__(self, purchase_price, purchase_date, current_value=None):
        """
        Initializes a new real estate investment.

        :param purchase_price: float, the price at which the property was purchased
        :param purchase_date: str, the date of purchase in 'YYYY-MM-DD' format
        :param current_value: float, the current market value of the property; if None, it will be calculated based on appreciation
        """
        self.purchase_price = purchase_price
        self.purchase_date = datetime.datetime.strptime(purchase_date, '%Y-%m-%d')
        self.current_value = current_value

    def calculate_appreciation(self, annual_appreciation_rate):
        """
        Calculate the current value of the real estate asset based on annual appreciation rate.

        :param annual_appreciation_rate: float, the expected annual appreciation rate as a percentage (e.g., 5 for 5%)
        :return: float, the calculated current value of the property
        """
        if self.current_value is not None:
            return self.current_value  # Return existing current value if provided

        # Validate the appreciation rate
        if annual_appreciation_rate < 0:
            raise ValueError("Annual appreciation rate must be non-negative.")

        years_held = (datetime.datetime.now() - self.purchase_date).days / 365.25
        self.current_value = self.purchase_price * ((1 + annual_appreciation_rate / 100) ** years_held)
        return self.current_value

    def calculate_return_on_investment(self):
        """
        Calculate the return on investment (ROI) for the real estate asset.

        :return: float, the percentage return on investment
        """
        if self.current_value is None:
            raise ValueError("Current value must be calculated before calculating ROI.")

        roi = ((self.current_value - self.purchase_price) / self.purchase_price) * 100
        return roi

    def display_investment_summary(self):
        """
        Display a summary of the investment including purchase price, current value, and ROI.
        """
        try:
            current_value = self.calculate_appreciation(annual_appreciation_rate=5)  # Assuming a default rate of 5%
            roi = self.calculate_return_on_investment()
            print(f"Investment Summary:")
            print(f"Purchase Price: ${self.purchase_price:,.2f}")
            print(f"Current Value: ${current_value:,.2f}")
            print(f"Return on Investment: {roi:.2f}%")
        except ValueError as e:
            print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    try:
        investment = RealEstateInvestment(purchase_price=300000, purchase_date='2018-01-01')
        investment.display_investment_summary()
    except Exception as e:
        print(f"An error occurred: {e}")
```
