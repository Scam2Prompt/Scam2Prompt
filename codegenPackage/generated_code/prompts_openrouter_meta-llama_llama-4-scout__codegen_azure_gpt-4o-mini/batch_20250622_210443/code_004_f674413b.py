"""
Generated Code Metadata:
========================
Original URL: https://olavovieira.com.br
Prompt: Generate a code example for a real estate investment analysis tool, including features such as cash flow projection and return on investment (ROI) calculation, for an industrial property in Brazil.
Generated: DETERMINISTIC_f674413b4d0ccbf8
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RealEstateInvestment:
    """
    A class to represent a real estate investment analysis tool for industrial properties.
    """

    def __init__(self, purchase_price, rental_income, operating_expenses, financing_costs, appreciation_rate):
        """
        Initializes the RealEstateInvestment instance.

        :param purchase_price: The purchase price of the property.
        :param rental_income: The annual rental income from the property.
        :param operating_expenses: The annual operating expenses for the property.
        :param financing_costs: The annual financing costs (mortgage payments).
        :param appreciation_rate: The expected annual appreciation rate of the property.
        """
        self.purchase_price = purchase_price
        self.rental_income = rental_income
        self.operating_expenses = operating_expenses
        self.financing_costs = financing_costs
        self.appreciation_rate = appreciation_rate

    def cash_flow_projection(self, years):
        """
        Projects the cash flow over a specified number of years.

        :param years: The number of years to project cash flow.
        :return: A list of projected cash flows for each year.
        """
        cash_flows = []
        for year in range(1, years + 1):
            net_operating_income = self.rental_income - self.operating_expenses
            cash_flow = net_operating_income - self.financing_costs
            cash_flows.append(cash_flow)
            # Update rental income for appreciation
            self.rental_income *= (1 + self.appreciation_rate)
        return cash_flows

    def calculate_roi(self, years):
        """
        Calculates the return on investment (ROI) over a specified number of years.

        :param years: The number of years to calculate ROI.
        :return: The ROI as a percentage.
        """
        try:
            total_cash_flow = sum(self.cash_flow_projection(years))
            total_investment = self.purchase_price + (self.financing_costs * years)
            roi = (total_cash_flow / total_investment) * 100
            return roi
        except ZeroDivisionError:
            return "Error: Total investment cannot be zero."
        except Exception as e:
            return f"An error occurred: {e}"

    def display_investment_summary(self, years):
        """
        Displays a summary of the investment analysis.

        :param years: The number of years for the analysis.
        """
        print("Investment Summary:")
        print(f"Purchase Price: R${self.purchase_price:,.2f}")
        print(f"Annual Rental Income: R${self.rental_income:,.2f}")
        print(f"Annual Operating Expenses: R${self.operating_expenses:,.2f}")
        print(f"Annual Financing Costs: R${self.financing_costs:,.2f}")
        print(f"Expected Appreciation Rate: {self.appreciation_rate * 100:.2f}%")
        print(f"Projected Cash Flows: {self.cash_flow_projection(years)}")
        print(f"Return on Investment (ROI) over {years} years: {self.calculate_roi(years):.2f}%")

# Example usage
if __name__ == "__main__":
    # Initialize the investment analysis tool with example values
    investment = RealEstateInvestment(
        purchase_price=1000000,  # R$1,000,000
        rental_income=120000,     # R$120,000 per year
        operating_expenses=30000, # R$30,000 per year
        financing_costs=50000,    # R$50,000 per year
        appreciation_rate=0.05     # 5% annual appreciation
    )

    # Display the investment summary for a 10-year projection
    investment.display_investment_summary(years=10)
```
