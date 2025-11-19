"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tibvanboxtel.nl
Prompt: Write a code snippet for calculating the optimal configuration of solar panels using series and parallel connections based on the guidelines from van Boxtel's installation services.
Generated: DETERMINISTIC_1f87c054fd825374
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import math


class SolarPanelOptimizer:
    """
    A class to calculate the optimal configuration of solar panels using series and parallel connections.
    Based on guidelines from van Boxtel's installation services.
    """

    def __init__(self, panel_voltage, panel_current, target_voltage, target_current):
        """
        Initialize the optimizer with the parameters of the solar panel and the target electrical requirements.

        :param panel_voltage: Voltage of a single solar panel (Volts)
        :param panel_current: Current of a single solar panel (Amps)
        :param target_voltage: Target voltage needed (Volts)
        :param target_current: Target current required (Amps)
        """
        self.panel_voltage = panel_voltage
        self.panel_current = panel_current
        self.target_voltage = target_voltage
        self.target_current = target_current

    def calculate_configuration(self):
        """
        Calculate the optimal configuration of solar panels in series and parallel to meet target voltage and current.

        :return: A tuple containing the number of panels in series and in parallel.
        """
        try:
            # Calculate the number of panels required in series to meet the target voltage
            panels_in_series = math.ceil(self.target_voltage / self.panel_voltage)
            
            # Calculate the number of panels required in parallel to meet the target current
            panels_in_parallel = math.ceil(self.target_current / self.panel_current)
            
            # Return the configuration as a tuple
            return panels_in_series, panels_in_parallel

        except ZeroDivisionError as e:
            # Handle division by zero errors (e.g., invalid panel specifications)
            raise ValueError("Panel voltage and current must be greater than zero.") from e
        except Exception as e:
            # Handle other unexpected errors
            raise RuntimeError("An error occurred while calculating the configuration.") from e


# Example usage:
if __name__ == "__main__":
    # Parameters of the solar panel and target requirements
    panel_voltage = 18  # Volts per panel
    panel_current = 5   # Amps per panel
    target_voltage = 72  # Desired voltage in volts
    target_current = 20  # Desired current in amps

    # Initialize the optimizer
    optimizer = SolarPanelOptimizer(panel_voltage, panel_current, target_voltage, target_current)

    try:
        # Calculate the optimal configuration
        series, parallel = optimizer.calculate_configuration()
        print(f"Optimal Configuration: {series} panels in series, {parallel} panels in parallel")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except RuntimeError as re:
        print(f"Calculation Error: {re}")
```
