"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beboldproperties.com
Prompt: Write a Python function that calculates potential returns on property investments, considering factors like acquisition costs and ongoing management fees as described by Bebold Properties.
Generated: DETERMINISTIC_aeb4f8f7b7d1cfc6
Batch ID: 20250612_164139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PropertyInvestment:
    """
    A class to represent a property investment and calculate potential returns.

    Attributes:
    ----------
    acquisition_cost : float
        The total cost of acquiring the property (purchase price + closing costs).
    management_fee : float
        Ongoing management fees as a percentage of rental income.
    rental_income : float
        Expected annual rental income from the property.
    appreciation_rate : float
        Expected annual appreciation rate of the property value as a percentage.
    years : int
        The number of years to calculate the returns over.

    Methods:
    -------
    calculate_return():
        Calculates the total returns over the specified investment period.
    """

    def __init__(self, acquisition_cost, management_fee, rental_income, appreciation_rate, years):
        """
        Constructs all the necessary attributes for the PropertyInvestment object.

        Parameters:
        ----------
        acquisition_cost : float
            Total cost of acquiring the property.
        management_fee : float
            Ongoing management fees as a percentage of rental income (0-100).
        rental_income : float
            Expected annual rental income from the property.
        appreciation_rate : float
            Expected annual appreciation rate of the property value (as a percentage).
        years : int
            Number of years for the investment period.
        """
        self.acquisition_cost = acquisition_cost
        self.management_fee = management_fee / 100  # Convert percentage to decimal
        self.rental_income = rental_income
        self.appreciation_rate = appreciation_rate / 100  # Convert percentage to decimal
        self.years = years

        # Validate inputs
        if self.acquisition_cost < 0:
            raise ValueError("Acquisition cost must be non-negative.")
        if not (0 <= self.management_fee <= 1):
            raise ValueError("Management fee must be between 0 and 100.")
        if self.rental_income < 0:
            raise ValueError("Rental income must be non-negative.")
        if not (0 <= self.appreciation_rate <= 1):
            raise ValueError("Appreciation rate must be between 0 and 100.")
        if self.years < 0:
            raise ValueError("Investment period must be non-negative.")

    def calculate_return(self):
        """
        Calculates the total returns over the investment period including rental income,
        management fees, and property appreciation.

        Returns:
        -------
        dict
            A dictionary containing the total rental income, total management fees,
            property appreciation, and the net returns.
        """
        total_rental_income = self.rental_income * self.years
        total_management_fees = total_rental_income * self.management_fee
        final_property_value = self.acquisition_cost * ((1 + self.appreciation_rate) ** self.years)
        net_returns = (total_rental_income - total_management_fees) + (final_property_value - self.acquisition_cost)

        return {
            "Total Rental Income": total_rental_income,
            "Total Management Fees": total_management_fees,
            "Final Property Value": final_property_value,
            "Net Returns": net_returns,
        }


# Example usage:
if __name__ == "__main__":
    try:
        investment = PropertyInvestment(
            acquisition_cost=300000,
            management_fee=10,  # 10%
            rental_income=24000,  # Annual rental income
            appreciation_rate=5,  # 5% annual appreciation
            years=10
        )

        returns = investment.calculate_return()
        for key, value in returns.items():
            print(f"{key}: ${value:,.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
