"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loghouses-woodcraft.com
Prompt: Write a program to simulate the pressure head and flow rate of YQS150 pumps under varying load conditions.
Generated: DETERMINISTIC_99a68ff1c03d8846
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math


class PumpSimulation:
    """
    Class to simulate the pressure head and flow rate of YQS150 pumps
    under varying load conditions.
    """

    def __init__(self, max_flow_rate, max_pressure_head):
        """
        Initialize the pump simulation with max flow rate and pressure head.
        
        :param max_flow_rate: Maximum flow rate of the pump (m³/h)
        :param max_pressure_head: Maximum pressure head of the pump (m)
        """
        self.max_flow_rate = max_flow_rate  # Max flow rate of the pump (m³/h)
        self.max_pressure_head = max_pressure_head  # Max pressure head the pump can produce (m)

    def calculate_performance(self, load_factor):
        """
        Calculate the pressure head and flow rate based on the load factor.
        
        :param load_factor: Load factor as a percentage (0-100)
        :return: A tuple (pressure_head, flow_rate) under the given load condition
        """
        # Input validation for load factor
        if not (0 <= load_factor <= 100):
            raise ValueError("Load factor must be between 0 and 100.")

        # Simulate a quadratic relationship between load factor and performance
        # Pressure head decreases quadratically as flow rate increases linearly
        flow_rate = (load_factor / 100) * self.max_flow_rate
        pressure_head = self.max_pressure_head * (1 - (flow_rate / self.max_flow_rate) ** 2)

        return pressure_head, flow_rate


def main():
    """
    Main function to run the simulation for YQS150 pumps under varying load conditions.
    """
    try:
        # Define the pump parameters
        MAX_FLOW_RATE = 150  # Maximum flow rate in m³/h
        MAX_PRESSURE_HEAD = 50  # Maximum pressure head in meters

        # Create an instance of the PumpSimulation class
        pump_simulator = PumpSimulation(MAX_FLOW_RATE, MAX_PRESSURE_HEAD)

        print("Simulating YQS150 Pump Performance:")
        print("==================================")
        
        # Simulate for load factors from 0% to 100% in increments of 10%
        for load in range(0, 101, 10):
            # Calculate performance metrics
            pressure_head, flow_rate = pump_simulator.calculate_performance(load)

            # Display the results
            print(f"Load Factor: {load}%")
            print(f"Pressure Head: {pressure_head:.2f} m")
            print(f"Flow Rate: {flow_rate:.2f} m³/h")
            print("----------------------------------")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Run the main simulation program
    main()
```
