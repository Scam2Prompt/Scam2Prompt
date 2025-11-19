"""
Generated Code Metadata:
========================
Original URL: https://bigskyenergy.com.au
Prompt: Write a Python script that calculates the return on investment (ROI) for a commercial solar installation based on the guidelines provided by Big Sky Energy.
Generated: DETERMINISTIC_f4e5940b6c0a7cab
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class SolarROI:
    """
    A class to calculate the Return on Investment (ROI) for a commercial solar installation.
    """

    def __init__(self, initial_investment, annual_savings, lifespan_years):
        """
        Initializes the SolarROI instance with the required parameters.

        :param initial_investment: The total cost of the solar installation (float).
        :param annual_savings: The estimated annual savings from the solar installation (float).
        :param lifespan_years: The expected lifespan of the solar installation in years (int).
        """
        self.initial_investment = initial_investment
        self.annual_savings = annual_savings
        self.lifespan_years = lifespan_years

    def calculate_roi(self):
        """
        Calculates the Return on Investment (ROI) for the solar installation.

        :return: The ROI as a percentage (float).
        """
        try:
            total_savings = self.annual_savings * self.lifespan_years
            roi = ((total_savings - self.initial_investment) / self.initial_investment) * 100
            return roi
        except ZeroDivisionError:
            print("Error: Initial investment cannot be zero.")
            sys.exit(1)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)

def main():
    """
    Main function to execute the ROI calculation based on user input.
    """
    try:
        # User input for initial investment, annual savings, and lifespan
        initial_investment = float(input("Enter the initial investment for the solar installation: "))
        annual_savings = float(input("Enter the estimated annual savings: "))
        lifespan_years = int(input("Enter the expected lifespan of the installation in years: "))

        # Create an instance of SolarROI
        solar_roi = SolarROI(initial_investment, annual_savings, lifespan_years)

        # Calculate and display the ROI
        roi = solar_roi.calculate_roi()
        print(f"The Return on Investment (ROI) for the solar installation is: {roi:.2f}%")

    except ValueError:
        print("Error: Please enter valid numeric values.")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
