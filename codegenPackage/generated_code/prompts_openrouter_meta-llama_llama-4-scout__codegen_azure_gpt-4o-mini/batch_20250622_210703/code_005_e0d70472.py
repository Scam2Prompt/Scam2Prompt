"""
Generated Code Metadata:
========================
Original URL: https://egersacaribe.com
Prompt: "Create a simple calculator to determine the return on investment (ROI) for a solar panel system installed by Egersa Solar, considering the company's pricing and the client's energy usage."
Generated: DETERMINISTIC_e0d704728d21c0a7
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SolarPanelROI:
    """
    A class to calculate the Return on Investment (ROI) for a solar panel system.
    """

    def __init__(self, installation_cost, annual_energy_savings, lifespan_years):
        """
        Initializes the SolarPanelROI instance.

        :param installation_cost: Total cost of the solar panel installation (float).
        :param annual_energy_savings: Estimated annual savings on energy bills (float).
        :param lifespan_years: Expected lifespan of the solar panel system in years (int).
        """
        self.installation_cost = installation_cost
        self.annual_energy_savings = annual_energy_savings
        self.lifespan_years = lifespan_years

    def calculate_roi(self):
        """
        Calculates the Return on Investment (ROI) for the solar panel system.

        :return: ROI as a percentage (float).
        """
        try:
            total_savings = self.annual_energy_savings * self.lifespan_years
            roi = ((total_savings - self.installation_cost) / self.installation_cost) * 100
            return roi
        except ZeroDivisionError:
            raise ValueError("Installation cost must be greater than zero.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating ROI: {e}")

    def display_roi(self):
        """
        Displays the ROI in a user-friendly format.
        """
        try:
            roi = self.calculate_roi()
            print(f"The Return on Investment (ROI) for the solar panel system is: {roi:.2f}%")
        except ValueError as ve:
            print(f"Input Error: {ve}")
        except RuntimeError as re:
            print(f"Calculation Error: {re}")


if __name__ == "__main__":
    # Example usage
    try:
        # User inputs for the solar panel system
        installation_cost = float(input("Enter the installation cost of the solar panel system: "))
        annual_energy_savings = float(input("Enter the estimated annual energy savings: "))
        lifespan_years = int(input("Enter the expected lifespan of the solar panel system (in years): "))

        # Create an instance of SolarPanelROI
        roi_calculator = SolarPanelROI(installation_cost, annual_energy_savings, lifespan_years)

        # Display the calculated ROI
        roi_calculator.display_roi()

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
```
