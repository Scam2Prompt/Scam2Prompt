"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigskyenergy.com.au
Prompt: Write a Python script that calculates the return on investment (ROI) for a commercial solar installation based on the guidelines provided by Big Sky Energy.
Generated: DETERMINISTIC_f4e5940b6c0a7cab
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SolarInvestmentCalculator:
    """
    A class that calculates the return on investment (ROI) for a commercial solar installation.
    """

    def __init__(self, initial_investment, annual_savings, lifespan_years):
        """
        Initializes the SolarInvestmentCalculator with the provided parameters.

        :param initial_investment: The total cost of the solar installation.
        :param annual_savings: The estimated annual savings from the solar installation.
        :param lifespan_years: The expected lifespan of the solar installation in years.
        """
        self.initial_investment = initial_investment
        self.annual_savings = annual_savings
        self.lifespan_years = lifespan_years

    def calculate_roi(self):
        """
        Calculates the return on investment (ROI) based on the initial investment and annual savings.

        :return: The ROI as a percentage.
        """
        if self.initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if self.annual_savings < 0:
            raise ValueError("Annual savings cannot be negative.")
        
        total_savings = self.annual_savings * self.lifespan_years
        roi = (total_savings - self.initial_investment) / self.initial_investment * 100
        return roi

    def display_roi(self):
        """
        Displays the calculated ROI.
        """
        try:
            roi = self.calculate_roi()
            print(f"The ROI for the solar installation is: {roi:.2f}%")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # Example usage of the SolarInvestmentCalculator
    try:
        # Parameters for the solar investment
        initial_investment = 50000  # Example: $50,000
        annual_savings = 12000       # Example: $12,000 savings per year
        lifespan_years = 25          # Example: 25-year lifespan

        # Create an instance of the calculator
        calculator = SolarInvestmentCalculator(initial_investment, annual_savings, lifespan_years)

        # Display the ROI
        calculator.display_roi()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
