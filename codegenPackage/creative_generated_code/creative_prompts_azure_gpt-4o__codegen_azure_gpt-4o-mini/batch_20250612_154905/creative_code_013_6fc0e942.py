"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.crediblebd.net
Prompt: Write code to calculate the ROI (Return on Investment) for switching to Credible BD’s LED Street Lights in a municipal lighting project.
Generated: DETERMINISTIC_6fc0e942265955cf
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StreetLightROI:
    """
    A class to calculate the Return on Investment (ROI) for switching to LED street lights.
    """

    def __init__(self, initial_investment, annual_savings, lifespan, maintenance_costs=None):
        """
        Initializes the ROI calculator with the necessary parameters.

        :param initial_investment: Total cost to purchase and install the LED street lights.
        :param annual_savings: Estimated annual savings from energy costs.
        :param lifespan: Lifespan of the LED lights in years.
        :param maintenance_costs: Estimated annual maintenance costs (default is None).
        """
        self.initial_investment = initial_investment
        self.annual_savings = annual_savings
        self.lifespan = lifespan
        self.maintenance_costs = maintenance_costs if maintenance_costs is not None else 0

    def calculate_total_savings(self):
        """
        Calculate the total savings over the lifespan of the LED lights.

        :return: Total savings over the lifespan.
        """
        total_savings = (self.annual_savings - self.maintenance_costs) * self.lifespan
        return total_savings

    def calculate_roi(self):
        """
        Calculate the Return on Investment (ROI).

        :return: ROI as a percentage.
        """
        total_savings = self.calculate_total_savings()
        roi = ((total_savings - self.initial_investment) / self.initial_investment) * 100

        # Ensure ROI is calculated correctly
        if self.initial_investment == 0:
            raise ValueError("Initial investment cannot be zero.")

        return roi

    def display_roi(self):
        """
        Displays the ROI in a formatted manner.
        """
        try:
            roi = self.calculate_roi()
            print(f"The Return on Investment (ROI) for switching to LED street lights is: {roi:.2f}%")
        except ValueError as e:
            print(f"Error calculating ROI: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Example Usage
if __name__ == "__main__":
    # Define parameters for the calculation
    initial_investment = 100000  # Initial cost in currency
    annual_savings = 20000        # Annual savings in currency
    lifespan = 10                 # Lifespan in years
    maintenance_costs = 1000      # Annual maintenance costs in currency

    # Create an instance of the ROI calculator
    roi_calculator = StreetLightROI(initial_investment, annual_savings, lifespan, maintenance_costs)

    # Display the calculated ROI
    roi_calculator.display_roi()
```
