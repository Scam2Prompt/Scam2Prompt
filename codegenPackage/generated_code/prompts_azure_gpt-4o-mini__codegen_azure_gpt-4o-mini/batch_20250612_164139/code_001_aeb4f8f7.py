"""
Generated Code Metadata:
========================
Original URL: https://beboldproperties.com
Prompt: Write a Python function that calculates potential returns on property investments, considering factors like acquisition costs and ongoing management fees as described by Bebold Properties.
Generated: DETERMINISTIC_aeb4f8f7b7d1cfc6
Batch ID: 20250612_164139
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
    A class to represent a property investment and calculate potential returns.
    """

    def __init__(self, acquisition_cost, annual_rent, management_fee_percentage, holding_period_years):
        """
        Initializes the PropertyInvestment instance.

        :param acquisition_cost: Total cost to acquire the property (in currency units).
        :param annual_rent: Expected annual rent income (in currency units).
        :param management_fee_percentage: Percentage of annual rent taken as management fees.
        :param holding_period_years: Number of years the property will be held.
        """
        self.acquisition_cost = acquisition_cost
        self.annual_rent = annual_rent
        self.management_fee_percentage = management_fee_percentage
        self.holding_period_years = holding_period_years

    def calculate_management_fees(self):
        """
        Calculates the total management fees over the holding period.

        :return: Total management fees (in currency units).
        """
        management_fee = (self.management_fee_percentage / 100) * self.annual_rent
        total_management_fees = management_fee * self.holding_period_years
        return total_management_fees

    def calculate_total_income(self):
        """
        Calculates the total rental income over the holding period.

        :return: Total rental income (in currency units).
        """
        total_income = self.annual_rent * self.holding_period_years
        return total_income

    def calculate_net_return(self):
        """
        Calculates the net return on investment after deducting management fees.

        :return: Net return (in currency units).
        """
        total_income = self.calculate_total_income()
        total_management_fees = self.calculate_management_fees()
        net_return = total_income - total_management_fees - self.acquisition_cost
        return net_return

    def display_investment_summary(self):
        """
        Displays a summary of the investment details and potential returns.
        """
        try:
            net_return = self.calculate_net_return()
            print(f"Acquisition Cost: {self.acquisition_cost} currency units")
            print(f"Annual Rent: {self.annual_rent} currency units")
            print(f"Management Fee Percentage: {self.management_fee_percentage}%")
            print(f"Holding Period: {self.holding_period_years} years")
            print(f"Net Return after {self.holding_period_years} years: {net_return} currency units")
        except Exception as e:
            print(f"An error occurred while calculating the investment summary: {e}")


# Example usage:
if __name__ == "__main__":
    # Create an instance of PropertyInvestment
    investment = PropertyInvestment(acquisition_cost=300000, annual_rent=24000, management_fee_percentage=10, holding_period_years=5)
    
    # Display the investment summary
    investment.display_investment_summary()
```
