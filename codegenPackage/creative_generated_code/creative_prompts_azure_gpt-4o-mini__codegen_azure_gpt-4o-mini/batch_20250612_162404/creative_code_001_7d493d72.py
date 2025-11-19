"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imbcg.com
Prompt: Write a Python script to calculate the efficiency of a Solar Pool Pump based on the parameters provided by IMB Cambodia Group.
Generated: DETERMINISTIC_7d493d720176346c
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SolarPumpEfficiencyCalculator:
    """
    A class to calculate the efficiency of a solar pool pump based on relevant parameters.
    """

    def __init__(self, pump_power, solar_panel_output, pump_flow_rate):
        """
        Initializes the SolarPumpEfficiencyCalculator with pump and solar panel parameters.

        :param pump_power: Power of the pump in watts (W)
        :param solar_panel_output: Output power of the solar panels in watts (W)
        :param pump_flow_rate: Flow rate of the pump in liters per minute (L/min)
        """
        self.pump_power = pump_power
        self.solar_panel_output = solar_panel_output
        self.pump_flow_rate = pump_flow_rate

    def calculate_efficiency(self):
        """
        Calculates and returns the efficiency of the solar pool pump.

        :return: Efficiency of the pump as a percentage
        :raises ValueError: If any input parameter is invalid (non-positive)
        """
        # Validate input parameters
        if self.pump_power <= 0:
            raise ValueError("Pump power must be a positive value.")
        if self.solar_panel_output <= 0:
            raise ValueError("Solar panel output must be a positive value.")
        if self.pump_flow_rate <= 0:
            raise ValueError("Pump flow rate must be a positive value.")

        # Calculate efficiency
        efficiency = (self.solar_panel_output / self.pump_power) * 100
        return efficiency

def main():
    """
    Main function to execute the efficiency calculation.
    """
    try:
        # Example parameters, replace with actual values
        pump_power = 1500  # Pump power in watts
        solar_panel_output = 1800  # Solar panel output in watts
        pump_flow_rate = 30  # Pump flow rate in liters per minute

        # Create an instance of the calculator
        calculator = SolarPumpEfficiencyCalculator(pump_power, solar_panel_output, pump_flow_rate)

        # Calculate efficiency
        efficiency = calculator.calculate_efficiency()

        # Output the results
        logging.info(f"The efficiency of the solar pool pump is {efficiency:.2f}%.")

    except ValueError as e:
        logging.error(f"Error in input parameters: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
