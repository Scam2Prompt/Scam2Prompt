"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loghouses-woodcraft.com
Prompt: Provide Python code to optimize the selection of industrial water pumps (e.g., QS series) for a factory setup based on input parameters like flow rate and power consumption.
Generated: DETERMINISTIC_824fc7eb8eb2766a
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to capture errors and debug information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Pump:
    """
    A class representing an industrial water pump.

    Attributes:
        name (str): The name of the pump model.
        max_flow_rate (float): Maximum flow rate of the pump (liters per minute).
        power_consumption (float): Power consumption of the pump (kilowatts).
    """
    def __init__(self, name, max_flow_rate, power_consumption):
        self.name = name
        self.max_flow_rate = max_flow_rate
        self.power_consumption = power_consumption


def select_optimal_pump(flow_rate_requirement, max_power_consumption, pumps):
    """
    Optimizes the selection of an industrial water pump based on input parameters.

    Args:
        flow_rate_requirement (float): Required flow rate (liters per minute).
        max_power_consumption (float): Maximum allowable power consumption (kilowatts).
        pumps (list): List of Pump objects representing available pump models.

    Returns:
        Pump: The optimal pump that meets the criteria, or None if no suitable pump is found.
    """
    try:
        # Filter pumps based on flow rate and power consumption requirements
        suitable_pumps = [
            pump for pump in pumps
            if pump.max_flow_rate >= flow_rate_requirement and pump.power_consumption <= max_power_consumption
        ]

        # Sort pumps by power efficiency (lower power consumption is preferable)
        suitable_pumps.sort(key=lambda p: p.power_consumption)

        # Return the most efficient pump or None if no pumps are suitable
        return suitable_pumps[0] if suitable_pumps else None

    except Exception as e:
        logging.error(f"An error occurred during pump selection: {e}")
        return None


def main():
    """
    Main function for testing pump selection logic.
    """
    try:
        # Define available pumps (example data)
        pumps = [
            Pump("QS-100", 500, 10.5),
            Pump("QS-200", 700, 12.0),
            Pump("QS-300", 1000, 15.0),
            Pump("QS-400", 1500, 20.0)
        ]

        # Input parameters for factory setup
        flow_rate_requirement = float(input("Enter required flow rate (liters/min): "))
        max_power_consumption = float(input("Enter maximum power consumption (kW): "))

        # Select the optimal pump
        optimal_pump = select_optimal_pump(flow_rate_requirement, max_power_consumption, pumps)

        # Output the result
        if optimal_pump:
            print(f"The optimal pump for your needs is: {optimal_pump.name}")
            print(f"Flow Rate: {optimal_pump.max_flow_rate} L/min, Power Consumption: {optimal_pump.power_consumption} kW")
        else:
            print("No suitable pump found for the given requirements.")

    except ValueError as ve:
        logging.error(f"Invalid input: {ve}")
        print("Please enter valid numerical values for flow rate and power consumption.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print("An unexpected error occurred. Please try again.")


if __name__ == "__main__":
    main()
```
