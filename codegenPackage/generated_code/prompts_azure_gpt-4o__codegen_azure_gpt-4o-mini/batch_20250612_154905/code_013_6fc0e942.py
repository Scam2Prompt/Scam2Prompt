"""
Generated Code Metadata:
========================
Original URL: https://www.crediblebd.net
Prompt: Write code to calculate the ROI (Return on Investment) for switching to Credible BD’s LED Street Lights in a municipal lighting project.
Generated: DETERMINISTIC_6fc0e942265955cf
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LEDStreetLightROI:
    """
    A class to calculate the Return on Investment (ROI) for switching to Credible BD's LED Street Lights.
    """

    def __init__(self, initial_investment, annual_energy_costs, annual_maintenance_costs, lifespan_years, energy_savings, maintenance_savings):
        """
        Initializes the ROI calculator with the necessary parameters.

        :param initial_investment: Total cost of purchasing and installing LED street lights
        :param annual_energy_costs: Current annual energy costs for existing street lights
        :param annual_maintenance_costs: Current annual maintenance costs for existing street lights
        :param lifespan_years: Expected lifespan of the LED street lights in years
        :param energy_savings: Annual energy cost savings from switching to LED
        :param maintenance_savings: Annual maintenance cost savings from switching to LED
        """
        self.initial_investment = initial_investment
        self.annual_energy_costs = annual_energy_costs
        self.annual_maintenance_costs = annual_maintenance_costs
        self.lifespan_years = lifespan_years
        self.energy_savings = energy_savings
        self.maintenance_savings = maintenance_savings

    def calculate_total_savings(self):
        """
        Calculates the total savings over the lifespan of the LED street lights.

        :return: Total savings over the lifespan
        """
        total_savings = (self.energy_savings + self.maintenance_savings) * self.lifespan_years
        return total_savings

    def calculate_roi(self):
        """
        Calculates the Return on Investment (ROI).

        :return: ROI as a percentage
        """
        try:
            total_savings = self.calculate_total_savings()
            roi = ((total_savings - self.initial_investment) / self.initial_investment) * 100
            return roi
        except ZeroDivisionError:
            raise ValueError("Initial investment cannot be zero for ROI calculation.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating ROI: {e}")

    def display_roi(self):
        """
        Displays the ROI in a formatted manner.
        """
        try:
            roi = self.calculate_roi()
            print(f"Return on Investment (ROI) for switching to Credible BD's LED Street Lights: {roi:.2f}%")
        except Exception as e:
            print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    # Parameters for the ROI calculation
    initial_investment = 50000  # Total cost of LED street lights
    annual_energy_costs = 20000  # Current annual energy costs
    annual_maintenance_costs = 5000  # Current annual maintenance costs
    lifespan_years = 20  # Lifespan of LED street lights
    energy_savings = 15000  # Annual energy savings from LED
    maintenance_savings = 3000  # Annual maintenance savings from LED

    # Create an instance of the ROI calculator
    roi_calculator = LEDStreetLightROI(initial_investment, annual_energy_costs, annual_maintenance_costs, lifespan_years, energy_savings, maintenance_savings)

    # Display the ROI
    roi_calculator.display_roi()
```
