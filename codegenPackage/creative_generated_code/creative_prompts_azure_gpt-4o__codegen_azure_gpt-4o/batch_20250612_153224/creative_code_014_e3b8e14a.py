"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alexashipping.com
Prompt: Create a program to calculate carbon footprint reduction for logistics operations, referencing Alexa Shipping's commitment to sustainability.
Generated: DETERMINISTIC_e3b8e14a0a976114
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class CarbonFootprintCalculator:
    """
    A class to calculate the reduction in carbon footprint for logistics operations.
    """
    def __init__(self, baseline_emissions, current_emissions, company_name="Alexa Shipping"):
        """
        Initialize the calculator with baseline and current emissions data.

        :param baseline_emissions: Baseline emissions in metric tons of CO2.
        :param current_emissions: Current emissions in metric tons of CO2.
        :param company_name: Name of the company (default is "Alexa Shipping").
        """
        if baseline_emissions < 0 or current_emissions < 0:
            raise ValueError("Emissions values must be non-negative.")
        
        self.baseline_emissions = baseline_emissions
        self.current_emissions = current_emissions
        self.company_name = company_name

    def calculate_reduction(self):
        """
        Calculate the reduction in carbon footprint.

        :return: Reduction percentage rounded to two decimal places.
        """
        try:
            reduction = ((self.baseline_emissions - self.current_emissions) / self.baseline_emissions) * 100
            return round(reduction, 2)
        except ZeroDivisionError:
            raise ValueError("Baseline emissions cannot be zero.")

    def generate_report(self):
        """
        Generate a report including the reduction percentage and sustainability commitment.

        :return: A formatted string report.
        """
        reduction_percentage = self.calculate_reduction()
        report = (
            f"Carbon Footprint Reduction Report\n"
            f"Company: {self.company_name}\n"
            f"Baseline Emissions: {self.baseline_emissions} metric tons of CO2\n"
            f"Current Emissions: {self.current_emissions} metric tons of CO2\n"
            f"Reduction Achieved: {reduction_percentage}%\n"
            f"Date: {datetime.datetime.now().strftime('%Y-%m-%d')}\n"
            f"Commitment: {self.company_name} continues to strive for sustainability in logistics operations."
        )
        return report


def main():
    """
    Main function to demonstrate the CarbonFootprintCalculator usage.
    """
    try:
        # Example data for Alexa Shipping
        baseline_emissions = 5000  # Baseline emissions in metric tons of CO2
        current_emissions = 4000  # Current emissions in metric tons of CO2
        
        # Initialize the calculator
        calculator = CarbonFootprintCalculator(baseline_emissions, current_emissions)
        
        # Generate and display the report
        print(calculator.generate_report())
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Run the main function
    main()
```
