"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://espinelycia.com
Prompt: Write a Python script to calculate the efficiency of hydraulic systems based on the construction methods described by Espinel y Cia.
Generated: DETERMINISTIC_ac71cebb135a1eb8
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class HydraulicSystemEfficiency:
    """
    A class to calculate the efficiency of hydraulic systems based on construction methods described by Espinel y Cia.
    """

    def __init__(self, flow_rate: float, pressure_drop: float, power_input: float):
        """
        Initializes the HydraulicSystemEfficiency with flow rate, pressure drop, and power input.

        :param flow_rate: Flow rate in cubic meters per second (m³/s).
        :param pressure_drop: Pressure drop in pascals (Pa).
        :param power_input: Input power in watts (W).
        """
        self.flow_rate = flow_rate
        self.pressure_drop = pressure_drop
        self.power_input = power_input

    def calculate_power_output(self) -> float:
        """
        Calculates the hydraulic power output based on flow rate and pressure drop.

        :return: Hydraulic power output in watts (W).
        """
        return self.flow_rate * self.pressure_drop

    def calculate_efficiency(self) -> float:
        """
        Calculates the efficiency of the hydraulic system.

        :return: Efficiency as a percentage (%).
        """
        try:
            power_output = self.calculate_power_output()
            efficiency = (power_output / self.power_input) * 100
            return efficiency
        except ZeroDivisionError:
            print("Error: Power input cannot be zero.")
            return 0.0
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0.0

def main():
    """
    Main function to execute the hydraulic system efficiency calculation.
    """
    try:
        # Example values for flow rate (m³/s), pressure drop (Pa), and power input (W)
        flow_rate = 0.1  # Example flow rate
        pressure_drop = 50000  # Example pressure drop
        power_input = 2000  # Example power input

        # Create an instance of HydraulicSystemEfficiency
        hydraulic_system = HydraulicSystemEfficiency(flow_rate, pressure_drop, power_input)

        # Calculate and display efficiency
        efficiency = hydraulic_system.calculate_efficiency()
        print(f"The efficiency of the hydraulic system is: {efficiency:.2f}%")
    
    except ValueError as e:
        print(f"Value error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
