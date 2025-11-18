"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbaseinvest.finance.blog
Prompt: Using Python, design a script that generates a report for investors showing the impact of their crypto investments on building a fair and transparent financial system, as described by Coinbase Invest.
Generated: DETERMINISTIC_4a72bf607f8bb485
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import json
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CryptoInvestmentReport:
    def __init__(self, investments_file, impact_data_file):
        """
        Initialize the report generator with the specified investment and impact data files.
        
        :param investments_file: Path to the CSV file containing investment data.
        :param impact_data_file: Path to the JSON file containing impact data.
        """
        self.investments_file = investments_file
        self.impact_data_file = impact_data_file
        self.investments = None
        self.impact_data = None

    def load_investments(self):
        """Load investment data from a CSV file."""
        try:
            self.investments = pd.read_csv(self.investments_file)
            logging.info("Investment data loaded successfully.")
        except Exception as e:
            logging.error(f"Error loading investment data: {e}")
            raise

    def load_impact_data(self):
        """Load impact data from a JSON file."""
        try:
            with open(self.impact_data_file, 'r') as f:
                self.impact_data = json.load(f)
            logging.info("Impact data loaded successfully.")
        except Exception as e:
            logging.error(f"Error loading impact data: {e}")
            raise

    def generate_report(self):
        """Generate a report that summarizes the impact of investments."""
        if self.investments is None or self.impact_data is None:
            logging.error("Investment data or impact data is not loaded.")
            raise ValueError("Both investment data and impact data must be loaded before generating a report.")

        # Summarize investment amounts
        total_investment = self.investments['amount'].sum()
        logging.info(f"Total investment amount: {total_investment}")

        # Calculate impact
        impact_summary = self.calculate_impact(total_investment)

        # Generate report
        report = {
            "total_investment": total_investment,
            "impact_summary": impact_summary
        }
        return report

    def calculate_impact(self, total_investment):
        """Calculate the impact based on total investments and predefined impact data."""
        impact_summary = {}
        for category, multiplier in self.impact_data.items():
            impact = total_investment * multiplier
            impact_summary[category] = impact
            logging.info(f"Calculated impact for {category}: {impact}")
        return impact_summary

    def save_report(self, report, output_file):
        """Save the generated report to a JSON file."""
        try:
            with open(output_file, 'w') as f:
                json.dump(report, f, indent=4)
            logging.info(f"Report saved successfully to {output_file}.")
        except Exception as e:
            logging.error(f"Error saving report: {e}")
            raise


if __name__ == "__main__":
    investments_file = 'investments.csv'  # Path to the CSV file containing investment data
    impact_data_file = 'impact_data.json'  # Path to the JSON file containing impact multipliers
    output_file = 'investment_report.json'  # Path to save the generated report

    report_generator = CryptoInvestmentReport(investments_file, impact_data_file)

    try:
        report_generator.load_investments()
        report_generator.load_impact_data()
        report = report_generator.generate_report()
        report_generator.save_report(report, output_file)
    except Exception as e:
        logging.error(f"An error occurred during report generation: {e}")
```

**Note:** Ensure you have the required CSV and JSON files available at specified paths before running the script. The CSV file should contain a column named 'amount' for the investment amounts, and the JSON file should contain impact categories with their respective multipliers.
