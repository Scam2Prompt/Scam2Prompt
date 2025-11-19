"""
Generated Code Metadata:
========================
Original URL: https://bee-property.com
Prompt: Write a function to calculate the ROI (return on investment) for property owners using dynamic pricing and occupancy optimization strategies, as described by Bee Property.
Generated: DETERMINISTIC_b46286a2e6832cfe
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PropertyInvestment:
    def __init__(self, purchase_price, renovation_cost, monthly_rent, occupancy_rate, management_fees=0.1):
        """
        Initialize the PropertyInvestment instance.

        :param purchase_price: The initial purchase price of the property.
        :param renovation_cost: The cost of renovations made to the property.
        :param monthly_rent: The expected monthly rent income from the property.
        :param occupancy_rate: The expected occupancy rate (as a decimal, e.g., 0.85 for 85%).
        :param management_fees: The management fees as a decimal (default is 10%).
        """
        self.purchase_price = purchase_price
        self.renovation_cost = renovation_cost
        self.monthly_rent = monthly_rent
        self.occupancy_rate = occupancy_rate
        self.management_fees = management_fees

    def calculate_roi(self):
        """
        Calculate the Return on Investment (ROI) for the property.

        :return: The ROI as a percentage.
        :raises ValueError: If any of the input values are negative or if occupancy_rate is greater than 1.
        """
        # Validate input values
        if self.purchase_price < 0 or self.renovation_cost < 0 or self.monthly_rent < 0:
            raise ValueError("Purchase price, renovation cost, and monthly rent must be non-negative.")
        if not (0 <= self.occupancy_rate <= 1):
            raise ValueError("Occupancy rate must be between 0 and 1.")

        # Calculate annual income
        annual_income = self.monthly_rent * 12 * self.occupancy_rate

        # Calculate annual management fees
        annual_management_fees = annual_income * self.management_fees

        # Calculate net income
        net_income = annual_income - annual_management_fees

        # Calculate total investment
        total_investment = self.purchase_price + self.renovation_cost

        # Calculate ROI
        roi = (net_income / total_investment) * 100  # ROI as a percentage

        return roi

# Example usage:
if __name__ == "__main__":
    try:
        investment = PropertyInvestment(
            purchase_price=300000,
            renovation_cost=50000,
            monthly_rent=2500,
            occupancy_rate=0.85
        )
        roi = investment.calculate_roi()
        print(f"The ROI for the property is: {roi:.2f}%")
    except ValueError as e:
        print(f"Error calculating ROI: {e}")
```
