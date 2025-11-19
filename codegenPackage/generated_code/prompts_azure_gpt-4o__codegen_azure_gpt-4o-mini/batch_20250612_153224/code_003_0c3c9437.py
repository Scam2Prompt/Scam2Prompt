"""
Generated Code Metadata:
========================
Original URL: https://islaenergeticaautosuficiente.com
Prompt: Provide a Python script to calculate the ROI (Return on Investment) for implementing "islas energéticas" in compliance with Ley 2 de 2007, including subsidies and energy savings.
Generated: DETERMINISTIC_0c3c9437b324a849
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Investment:
    def __init__(self, initial_investment, annual_savings, subsidy_amount, years):
        """
        Initialize the Investment class with the required parameters.

        :param initial_investment: Total cost of implementing the islas energéticas
        :param annual_savings: Estimated annual savings from energy efficiency
        :param subsidy_amount: Total subsidies received for the investment
        :param years: Number of years over which to calculate ROI
        """
        self.initial_investment = initial_investment
        self.annual_savings = annual_savings
        self.subsidy_amount = subsidy_amount
        self.years = years

    def calculate_roi(self):
        """
        Calculate the Return on Investment (ROI).

        :return: ROI as a percentage
        """
        try:
            # Calculate total savings over the investment period
            total_savings = self.annual_savings * self.years
            
            # Calculate net profit (total savings + subsidies - initial investment)
            net_profit = total_savings + self.subsidy_amount - self.initial_investment
            
            # Calculate ROI
            roi = (net_profit / self.initial_investment) * 100
            
            logging.info(f"Calculated ROI: {roi:.2f}%")
            return roi
        except ZeroDivisionError:
            logging.error("Initial investment cannot be zero.")
            return None
        except Exception as e:
            logging.error(f"An error occurred while calculating ROI: {e}")
            return None

def main():
    """
    Main function to execute the ROI calculation.
    """
    # Example parameters (these should be replaced with actual values)
    initial_investment = 100000  # Total cost of implementation
    annual_savings = 15000        # Estimated annual savings
    subsidy_amount = 20000        # Total subsidies received
    years = 5                     # Investment period in years

    # Create an Investment instance
    investment = Investment(initial_investment, annual_savings, subsidy_amount, years)

    # Calculate and print the ROI
    roi = investment.calculate_roi()
    if roi is not None:
        print(f"The ROI for the investment is: {roi:.2f}%")

if __name__ == "__main__":
    main()
```
