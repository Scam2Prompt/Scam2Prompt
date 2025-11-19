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
# industrial_water_pumps.py

class IndustrialWaterPump:
    """Represents an industrial water pump with its characteristics."""

    def __init__(self, model, flow_rate, power_consumption, head):
        """
        Initializes an IndustrialWaterPump object.

        Args:
            model (str): The model of the pump (e.g., QS series).
            flow_rate (float): The flow rate of the pump in m³/h.
            power_consumption (float): The power consumption of the pump in kW.
            head (float): The head of the pump in meters.
        """
        self.model = model
        self.flow_rate = flow_rate
        self.power_consumption = power_consumption
        self.head = head

    def __repr__(self):
        return f"IndustrialWaterPump(model='{self.model}', flow_rate={self.flow_rate}, power_consumption={self.power_consumption}, head={self.head})"


class PumpSelector:
    """Selects the optimal industrial water pump based on input parameters."""

    def __init__(self, pumps):
        """
        Initializes a PumpSelector object.

        Args:
            pumps (list[IndustrialWaterPump]): A list of available industrial water pumps.
        """
        self.pumps = pumps

    def select_pump(self, required_flow_rate, max_power_consumption):
        """
        Selects the optimal pump that meets the required flow rate and power consumption constraints.

        Args:
            required_flow_rate (float): The required flow rate in m³/h.
            max_power_consumption (float): The maximum allowed power consumption in kW.

        Returns:
            IndustrialWaterPump: The selected pump, or None if no pump meets the requirements.

        Raises:
            ValueError: If the required flow rate or max power consumption is invalid.
        """
        if required_flow_rate <= 0:
            raise ValueError("Required flow rate must be greater than zero.")
        if max_power_consumption <= 0:
            raise ValueError("Max power consumption must be greater than zero.")

        # Filter pumps that meet the requirements
        suitable_pumps = [
            pump for pump in self.pumps
            if pump.flow_rate >= required_flow_rate and pump.power_consumption <= max_power_consumption
        ]

        # Select the pump with the lowest power consumption
        if suitable_pumps:
            return min(suitable_pumps, key=lambda pump: pump.power_consumption)
        else:
            return None


def main():
    # Define available pumps
    pumps = [
        IndustrialWaterPump("QS-20", 20, 2.5, 10),
        IndustrialWaterPump("QS-30", 30, 3.5, 15),
        IndustrialWaterPump("QS-40", 40, 4.5, 20),
        IndustrialWaterPump("QS-50", 50, 5.5, 25),
    ]

    # Create a pump selector
    selector = PumpSelector(pumps)

    try:
        # Input parameters
        required_flow_rate = 35  # m³/h
        max_power_consumption = 4.0  # kW

        # Select the optimal pump
        selected_pump = selector.select_pump(required_flow_rate, max_power_consumption)

        if selected_pump:
            print(f"Selected pump: {selected_pump.model}")
            print(f"Flow rate: {selected_pump.flow_rate} m³/h")
            print(f"Power consumption: {selected_pump.power_consumption} kW")
            print(f"Head: {selected_pump.head} meters")
        else:
            print("No pump meets the requirements.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
