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
import numpy as np
import matplotlib.pyplot as plt

class YQS150Pump:
    """
    A class to represent a YQS150 pump and its characteristics.

    Attributes:
        max_flow_rate (float): Maximum flow rate of the pump in m³/h.
        max_pressure_head (float): Maximum pressure head of the pump in meters.
    """
    
    def __init__(self, max_flow_rate: float, max_pressure_head: float):
        """
        Initializes a YQS150 pump with specified maximum flow rate and pressure head.

        Parameters:
            max_flow_rate (float): Maximum flow rate of the pump in m³/h.
            max_pressure_head (float): Maximum pressure head of the pump in meters.
        """
        self.max_flow_rate = max_flow_rate
        self.max_pressure_head = max_pressure_head

    def calculate_pressure_head(self, flow_rate: float) -> float:
        """
        Calculates the pressure head for a given flow rate.

        Parameters:
            flow_rate (float): The flow rate in m³/h.

        Returns:
            float: The calculated pressure head in meters.
        """
        if flow_rate < 0:
            raise ValueError("Flow rate cannot be negative.")
        if flow_rate > self.max_flow_rate:
            raise ValueError("Flow rate exceeds maximum flow rate of the pump.")

        # Simplified linear relationship for demonstration purposes
        pressure_head = self.max_pressure_head * (1 - (flow_rate / self.max_flow_rate))

        return pressure_head

    def simulate(self, flow_rates: np.ndarray) -> np.ndarray:
        """
        Simulates the pressure head over a range of flow rates.

        Parameters:
            flow_rates (np.ndarray): An array of flow rates in m³/h.

        Returns:
            np.ndarray: An array of corresponding pressure heads in meters.
        """
        pressure_heads = []

        for rate in flow_rates:
            try:
                head = self.calculate_pressure_head(rate)
                pressure_heads.append(head)
            except ValueError as e:
                print(f"Error calculating pressure head for flow rate {rate}: {e}")
                pressure_heads.append(None)  # Append None for error cases

        return np.array(pressure_heads)


def main():
    # Define the maximum flow rate and pressure head for YQS150 pumps
    max_flow_rate = 150  # in m³/h
    max_pressure_head = 30  # in meters

    # Create a YQS150 pump instance
    pump = YQS150Pump(max_flow_rate, max_pressure_head)

    # Define a range of flow rates to simulate
    flow_rates = np.linspace(0, 160, 100)  # Flow rates from 0 to 160 m³/h

    # Simulate the pressure heads for the defined range of flow rates
    pressure_heads = pump.simulate(flow_rates)

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(flow_rates, pressure_heads, label='Pressure Head vs. Flow Rate', color='blue')
    plt.axhline(y=max_pressure_head, color='r', linestyle='--', label='Max Pressure Head')
    plt.title('Pressure Head vs. Flow Rate for YQS150 Pump')
    plt.xlabel('Flow Rate (m³/h)')
    plt.ylabel('Pressure Head (m)')
    plt.grid()
    plt.ylim(-5, max_pressure_head + 5)  # Set limits for y-axis
    plt.xlim(0, max_flow_rate + 10)  # Set limits for x-axis
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
```
