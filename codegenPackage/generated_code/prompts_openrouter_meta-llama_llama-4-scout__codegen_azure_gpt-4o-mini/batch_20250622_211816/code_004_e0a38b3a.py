"""
Generated Code Metadata:
========================
Original URL: https://beboldproperties.com
Prompt: How can Bebold Properties' tailored investment buying and property management solutions help investors achieve their financial goals, and what are the advantages of their streamlined approach?
Generated: DETERMINISTIC_e0a38b3afb396d3b
Batch ID: 20250622_211816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PropertyInvestment:
    """
    A class to represent a property investment solution.
    """

    def __init__(self, property_value, expected_appreciation_rate, rental_income):
        """
        Initializes the PropertyInvestment instance.

        :param property_value: Initial value of the property
        :param expected_appreciation_rate: Expected annual appreciation rate (as a decimal)
        :param rental_income: Expected annual rental income
        """
        self.property_value = property_value
        self.expected_appreciation_rate = expected_appreciation_rate
        self.rental_income = rental_income

    def calculate_appreciation(self, years):
        """
        Calculate the future value of the property after a number of years.

        :param years: Number of years to project the appreciation
        :return: Future value of the property
        """
        try:
            future_value = self.property_value * ((1 + self.expected_appreciation_rate) ** years)
            return future_value
        except Exception as e:
            print(f"Error calculating appreciation: {e}")
            return None

    def calculate_total_income(self, years):
        """
        Calculate the total income from rental over a number of years.

        :param years: Number of years to project the rental income
        :return: Total rental income over the specified years
        """
        try:
            total_income = self.rental_income * years
            return total_income
        except Exception as e:
            print(f"Error calculating total income: {e}")
            return None

    def investment_summary(self, years):
        """
        Provide a summary of the investment after a number of years.

        :param years: Number of years to project the investment
        :return: Summary of future property value and total rental income
        """
        try:
            future_value = self.calculate_appreciation(years)
            total_income = self.calculate_total_income(years)
            return {
                "Future Property Value": future_value,
                "Total Rental Income": total_income,
                "Total Investment Value": future_value + total_income
            }
        except Exception as e:
            print(f"Error generating investment summary: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Initialize a property investment with a value of $300,000, an appreciation rate of 5%, and rental income of $20,000 per year
    investment = PropertyInvestment(property_value=300000, expected_appreciation_rate=0.05, rental_income=20000)

    # Project the investment over 10 years
    years = 10
    summary = investment.investment_summary(years)

    if summary:
        print("Investment Summary:")
        for key, value in summary.items():
            print(f"{key}: ${value:,.2f}")
```
