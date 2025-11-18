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
# Python script to calculate the Return on Investment (ROI)
# for switching to Credible BD's LED Street Lights in a municipal lighting project

class ROI_Calculator:
    """
    A class to calculate Return on Investment (ROI) for LED street lights in a municipal lighting project.
    """

    def __init__(self, current_cost, led_cost, energy_savings, maintenance_savings):
        """
        Initializes the calculator with project details.

        Parameters:
        current_cost (float): Annual operational cost of existing lighting system.
        led_cost (float): Annual operational cost of LED lighting system.
        energy_savings (float): Annual energy savings after switching to LEDs.
        maintenance_savings (float): Annual maintenance savings after switching to LEDs.
        """
        self.current_cost = current_cost
        self.led_cost = led_cost
        self.energy_savings = energy_savings
        self.maintenance_savings = maintenance_savings

    def calculate_roi(self):
        """
        Calculates ROI as a percentage.

        Formula:
        ROI (%) = ((Savings - Investment Cost) / Investment Cost) * 100

        Returns:
        float: ROI percentage
        """
        try:
            # Calculate annual savings
            total_savings = self.energy_savings + self.maintenance_savings
            
            # Calculate net savings after switching to LEDs
            investment_cost = self.current_cost - self.led_cost
            
            if investment_cost <= 0:
                raise ValueError("Investment cost must be greater than zero for ROI calculation.")

            # Calculate ROI percentage
            roi_percentage = (total_savings / investment_cost) * 100
            return roi_percentage

        except ZeroDivisionError:
            raise ValueError("Investment cost cannot be zero.")
        except Exception as e:
            raise RuntimeError(f"An error occurred during ROI calculation: {str(e)}")

    def display_results(self):
        """
        Displays the calculated ROI in a user-friendly format.
        """
        try:
            roi = self.calculate_roi()
            print(f"Calculated ROI: {roi:.2f}%")
        except Exception as e:
            print(f"Error: {str(e)}")


# Main block to run the code
if __name__ == "__main__":
    # Example input for municipality lighting project
    current_annual_cost = 50000.0  # Example: Current lighting system annual cost in USD
    led_annual_cost = 30000.0      # Example: LED lighting system annual cost in USD
    annual_energy_savings = 15000.0 # Example: Annual energy savings in USD
    annual_maintenance_savings = 5000.0  # Example: Annual maintenance savings in USD

    # Instantiate the ROI calculator
    roi_calculator = ROI_Calculator(
        current_cost=current_annual_cost,
        led_cost=led_annual_cost,
        energy_savings=annual_energy_savings,
        maintenance_savings=annual_maintenance_savings
    )

    # Display the results
    roi_calculator.display_results()
```
