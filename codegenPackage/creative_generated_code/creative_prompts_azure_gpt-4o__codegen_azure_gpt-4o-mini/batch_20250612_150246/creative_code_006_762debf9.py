"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kings-tradefx.com
Prompt: Develop a program to calculate and track ROI for progressive investment portfolios, ensuring continuous growth as described by KINGSTRADE FX.
Generated: DETERMINISTIC_762debf9f36252fe
Batch ID: 20250612_150246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging

# Set up logging for tracking events and errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InvestmentPortfolio:
    def __init__(self):
        """
        Initialize an empty investment portfolio.
        The portfolio will track investments and their respective returns.
        """
        self.investments = []

    def add_investment(self, amount, expected_return_rate, duration_years):
        """
        Add a new investment to the portfolio.

        :param amount: Initial amount of the investment
        :param expected_return_rate: Expected annual return rate (as a decimal)
        :param duration_years: Duration of the investment in years
        """
        investment = {
            'amount': amount,
            'expected_return_rate': expected_return_rate,
            'duration_years': duration_years,
            'start_date': datetime.datetime.now()
        }
        self.investments.append(investment)
        logging.info(f"Added investment: {investment}")

    def calculate_roi(self, investment):
        """
        Calculate the ROI for a given investment.

        :param investment: A dictionary containing investment details
        :return: The ROI for the investment
        """
        try:
            future_value = investment['amount'] * ((1 + investment['expected_return_rate']) ** investment['duration_years'])
            roi = future_value - investment['amount']
            logging.info(f"Calculated ROI: {roi} for investment: {investment}")
            return roi
        except Exception as e:
            logging.error(f"Error calculating ROI: {e}")
            return None

    def total_roi(self):
        """
        Calculate the total ROI for all investments in the portfolio.

        :return: The total ROI across all investments
        """
        total_roi = 0
        for investment in self.investments:
            roi = self.calculate_roi(investment)
            if roi is not None:
                total_roi += roi
        logging.info(f"Total ROI calculated: {total_roi}")
        return total_roi

    def report(self):
        """
        Generate a report detailing all investments and their respective ROIs.
        """
        logging.info("Generating investment report...")
        report_data = []
        for investment in self.investments:
            roi = self.calculate_roi(investment)
            report_data.append({
                'amount': investment['amount'],
                'expected_return_rate': investment['expected_return_rate'],
                'duration_years': investment['duration_years'],
                'roi': roi,
                'start_date': investment['start_date']
            })
        logging.info("Investment report generated successfully.")
        return report_data

# Example usage
if __name__ == "__main__":
    portfolio = InvestmentPortfolio()
    portfolio.add_investment(10000, 0.05, 10)  # $10,000 at 5% for 10 years
    portfolio.add_investment(5000, 0.07, 5)    # $5,000 at 7% for 5 years
    print("Total ROI:", portfolio.total_roi())
    print("Investment Report:", portfolio.report())
```
