"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trialsonicsolutions.com
Prompt: Provide an example of a case study where ultrasonic cleaning significantly reduced downtime and costs for a manufacturing company.
Generated: DETERMINISTIC_a5003f9bb4927a90
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Case Study: Ultrasonic Cleaning Process Analysis
This script simulates an example case study where ultrasonic cleaning is implemented in a manufacturing company.
The company experiences reduced downtime and costs due to the efficiency of ultrasonic cleaning technology.
"""

import logging
from datetime import datetime

# Configure logging to track events and errors
logging.basicConfig(
    filename="ultrasonic_cleaning_case_study.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class ManufacturingCompany:
    """
    Represents a manufacturing company analyzing its cleaning processes.
    """

    def __init__(self, name, downtime_hours, cleaning_costs):
        """
        Initialize company details.
        :param name: Name of the company.
        :param downtime_hours: Current yearly downtime hours due to cleaning.
        :param cleaning_costs: Current yearly cleaning costs incurred.
        """
        self.name = name
        self.downtime_hours = downtime_hours
        self.cleaning_costs = cleaning_costs
        self.ultrasonic_cleaning_implemented = False
        self.reduced_downtime = 0
        self.reduced_costs = 0

    def implement_ultrasonic_cleaning(self, efficiency_factor=0.5):
        """
        Implement ultrasonic cleaning and calculate reductions.
        :param efficiency_factor: Factor by which ultrasonic cleaning reduces downtime and costs (default: 50%).
        :return: None
        """
        if not (0 < efficiency_factor <= 1):
            raise ValueError("Efficiency factor must be between 0 and 1.")

        self.ultrasonic_cleaning_implemented = True
        self.reduced_downtime = self.downtime_hours * efficiency_factor
        self.reduced_costs = self.cleaning_costs * efficiency_factor

        # Log the implementation details
        logging.info(f"Ultrasonic cleaning implemented at {self.name}.")
        logging.info(f"Downtime hours reduced by {self.reduced_downtime:.2f}.")
        logging.info(f"Cleaning costs reduced by ${self.reduced_costs:.2f}.")

    def generate_report(self):
        """
        Generate a report summarizing the impact of ultrasonic cleaning.
        :return: A string containing the report summary.
        """
        if not self.ultrasonic_cleaning_implemented:
            return f"Ultrasonic cleaning has not been implemented for {self.name}."

        report = (
            f"--- Case Study Report for {self.name} ---\n"
            f"Original Downtime Hours: {self.downtime_hours:.2f} hours\n"
            f"Original Cleaning Costs: ${self.cleaning_costs:.2f}\n"
            f"Reduced Downtime Hours: {self.reduced_downtime:.2f} hours\n"
            f"Reduced Cleaning Costs: ${self.reduced_costs:.2f}\n"
            f"Efficiency Factor: 50%\n"
            f"Conclusion: Implementation of ultrasonic cleaning significantly reduced downtime and costs."
        )
        return report


def main():
    """
    Main function to demonstrate the case study.
    :return: None
    """
    try:
        # Example manufacturing company data
        company_name = "Precision Tools Manufacturing"
        initial_downtime_hours = 1000  # Yearly downtime in hours
        initial_cleaning_costs = 50000  # Yearly cleaning costs in dollars

        # Create a ManufacturingCompany object
        company = ManufacturingCompany(
            name=company_name,
            downtime_hours=initial_downtime_hours,
            cleaning_costs=initial_cleaning_costs
        )

        # Simulate implementation of ultrasonic cleaning
        company.implement_ultrasonic_cleaning()

        # Generate and print the report
        report = company.generate_report()
        print(report)

    except ValueError as ve:
        logging.error(f"ValueError encountered: {ve}")
    except Exception as e:
        logging.error(f"Unexpected error encountered: {e}")


if __name__ == "__main__":
    main()
```
