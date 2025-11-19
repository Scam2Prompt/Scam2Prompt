"""
Generated Code Metadata:
========================
Original URL: https://loghouses-woodcraft.com
Prompt: Write a program to simulate the pressure head and flow rate of YQS150 pumps under varying load conditions.
Generated: DETERMINISTIC_99a68ff1c03d8846
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

class Pump:
    def __init__(self, name, max_flow_rate, max_pressure_head):
        """
        Initialize a Pump object.

        Args:
        - name (str): Name of the pump.
        - max_flow_rate (float): Maximum flow rate of the pump in m^3/h.
        - max_pressure_head (float): Maximum pressure head of the pump in m.
        """
        self.name = name
        self.max_flow_rate = max_flow_rate
        self.max_pressure_head = max_pressure_head

    def calculate_pressure_head(self, flow_rate):
        """
        Calculate the pressure head of the pump under a given flow rate.

        Args:
        - flow_rate (float): Flow rate of the pump in m^3/h.

        Returns:
        - pressure_head (float): Pressure head of the pump in m.
        """
        # Assume a linear relationship between flow rate and pressure head
        # for simplicity. In reality, this relationship may be more complex.
        if flow_rate > self.max_flow_rate:
            raise ValueError("Flow rate exceeds maximum flow rate")

        pressure_head = self.max_pressure_head * (1 - (flow_rate / self.max_flow_rate))
        return pressure_head

    def calculate_flow_rate(self, pressure_head):
        """
        Calculate the flow rate of the pump under a given pressure head.

        Args:
        - pressure_head (float): Pressure head of the pump in m.

        Returns:
        - flow_rate (float): Flow rate of the pump in m^3/h.
        """
        # Assume a linear relationship between flow rate and pressure head
        # for simplicity. In reality, this relationship may be more complex.
        if pressure_head > self.max_pressure_head:
            raise ValueError("Pressure head exceeds maximum pressure head")

        flow_rate = self.max_flow_rate * (1 - (pressure_head / self.max_pressure_head))
        return flow_rate


class YQS150Pump(Pump):
    def __init__(self):
        super().__init__("YQS150", 150, 100)


def simulate_pump_performance(pump, flow_rates):
    """
    Simulate the performance of a pump under varying load conditions.

    Args:
    - pump (Pump): Pump object to simulate.
    - flow_rates (list): List of flow rates to simulate.

    Returns:
    - pressure_heads (list): List of pressure heads corresponding to the given flow rates.
    """
    pressure_heads = []
    for flow_rate in flow_rates:
        try:
            pressure_head = pump.calculate_pressure_head(flow_rate)
            pressure_heads.append(pressure_head)
        except ValueError as e:
            print(f"Error: {e}")

    return pressure_heads


def plot_pump_performance(pump, flow_rates, pressure_heads):
    """
    Plot the performance of a pump under varying load conditions.

    Args:
    - pump (Pump): Pump object to plot.
    - flow_rates (list): List of flow rates to plot.
    - pressure_heads (list): List of pressure heads to plot.
    """
    plt.plot(flow_rates, pressure_heads)
    plt.xlabel("Flow Rate (m^3/h)")
    plt.ylabel("Pressure Head (m)")
    plt.title(f"Performance Curve of {pump.name} Pump")
    plt.grid(True)
    plt.show()


def main():
    pump = YQS150Pump()
    flow_rates = np.linspace(0, pump.max_flow_rate, 10)
    pressure_heads = simulate_pump_performance(pump, flow_rates)
    plot_pump_performance(pump, flow_rates, pressure_heads)


if __name__ == "__main__":
    main()
```
