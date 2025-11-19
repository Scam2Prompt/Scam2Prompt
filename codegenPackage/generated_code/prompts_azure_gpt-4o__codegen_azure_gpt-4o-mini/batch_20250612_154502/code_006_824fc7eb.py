"""
Generated Code Metadata:
========================
Original URL: https://loghouses-woodcraft.com
Prompt: Provide Python code to optimize the selection of industrial water pumps (e.g., QS series) for a factory setup based on input parameters like flow rate and power consumption.
Generated: DETERMINISTIC_824fc7eb8eb2766a
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class Pump:
    """
    A class to represent an industrial water pump.

    Attributes:
        model (str): The model of the pump.
        flow_rate (float): The flow rate of the pump in liters per minute (L/min).
        power_consumption (float): The power consumption of the pump in kilowatts (kW).
    """

    def __init__(self, model: str, flow_rate: float, power_consumption: float):
        self.model = model
        self.flow_rate = flow_rate
        self.power_consumption = power_consumption

    def __repr__(self):
        return f"Pump(model={self.model}, flow_rate={self.flow_rate}, power_consumption={self.power_consumption})"


class PumpSelector:
    """
    A class to select the optimal pump based on input parameters.

    Attributes:
        pumps (list): A list of available pumps.
    """

    def __init__(self, pumps: list):
        self.pumps = pumps

    def select_optimal_pump(self, required_flow_rate: float, max_power_consumption: float) -> Pump:
        """
        Selects the optimal pump based on required flow rate and maximum power consumption.

        Parameters:
            required_flow_rate (float): The required flow rate in liters per minute (L/min).
            max_power_consumption (float): The maximum allowable power consumption in kilowatts (kW).

        Returns:
            Pump: The optimal pump that meets the criteria.

        Raises:
            ValueError: If no pump meets the criteria.
        """
        # Filter pumps based on the required flow rate and power consumption
        suitable_pumps = [
            pump for pump in self.pumps
            if pump.flow_rate >= required_flow_rate and pump.power_consumption <= max_power_consumption
        ]

        if not suitable_pumps:
            raise ValueError("No suitable pump found for the given criteria.")

        # Select the pump with the minimum power consumption among the suitable pumps
        optimal_pump = min(suitable_pumps, key=lambda p: p.power_consumption)
        return optimal_pump


def main():
    # Sample data for available pumps
    pump_data = [
        {"model": "QS100", "flow_rate": 100, "power_consumption": 5.0},
        {"model": "QS150", "flow_rate": 150, "power_consumption": 7.5},
        {"model": "QS200", "flow_rate": 200, "power_consumption": 10.0},
        {"model": "QS250", "flow_rate": 250, "power_consumption": 12.5},
    ]

    # Create Pump instances from the sample data
    pumps = [Pump(**data) for data in pump_data]

    # Initialize the PumpSelector with available pumps
    pump_selector = PumpSelector(pumps)

    # Define required parameters
    required_flow_rate = 180  # L/min
    max_power_consumption = 10.0  # kW

    try:
        # Select the optimal pump
        optimal_pump = pump_selector.select_optimal_pump(required_flow_rate, max_power_consumption)
        print(f"Optimal Pump Selected: {optimal_pump}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```
