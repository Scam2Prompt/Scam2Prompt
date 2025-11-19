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
import numpy as np
import matplotlib.pyplot as plt

class YQS150Pump:
    """
    A class to represent the YQS150 pump and simulate its performance
    under varying load conditions.
    """

    def __init__(self, max_flow_rate, max_head):
        """
        Initializes the YQS150 pump with specified maximum flow rate and head.

        Parameters:
        max_flow_rate (float): The maximum flow rate of the pump in m³/h.
        max_head (float): The maximum pressure head of the pump in meters.
        """
        self.max_flow_rate = max_flow_rate  # Maximum flow rate in m³/h
        self.max_head = max_head              # Maximum head in meters

    def calculate_performance(self, load_conditions):
        """
        Calculate the pressure head and flow rate for given load conditions.

        Parameters:
        load_conditions (list): A list of load conditions (in percentage).

        Returns:
        tuple: A tuple containing two lists - pressure heads and flow rates.
        """
        pressure_heads = []
        flow_rates = []

        for load in load_conditions:
            if load < 0 or load > 100:
                raise ValueError("Load conditions must be between 0 and 100 percent.")

            # Calculate flow rate and pressure head based on load condition
            flow_rate = (load / 100) * self.max_flow_rate
            head = self.max_head * (1 - (load / 100))  # Simplified linear relationship

            flow_rates.append(flow_rate)
            pressure_heads.append(head)

        return pressure_heads, flow_rates

def plot_performance(load_conditions, pressure_heads, flow_rates):
    """
    Plot the performance of the YQS150 pump.

    Parameters:
    load_conditions (list): A list of load conditions (in percentage).
    pressure_heads (list): A list of calculated pressure heads.
    flow_rates (list): A list of calculated flow rates.
    """
    plt.figure(figsize=(10, 5))

    # Plot Pressure Head
    plt.subplot(1, 2, 1)
    plt.plot(load_conditions, pressure_heads, marker='o', color='b')
    plt.title('Pressure Head vs Load Condition')
    plt.xlabel('Load Condition (%)')
    plt.ylabel('Pressure Head (m)')
    plt.grid()

    # Plot Flow Rate
    plt.subplot(1, 2, 2)
    plt.plot(load_conditions, flow_rates, marker='o', color='r')
    plt.title('Flow Rate vs Load Condition')
    plt.xlabel('Load Condition (%)')
    plt.ylabel('Flow Rate (m³/h)')
    plt.grid()

    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to simulate the YQS150 pump performance.
    """
    # Define the maximum specifications for the YQS150 pump
    max_flow_rate = 150  # m³/h
    max_head = 30        # meters

    # Create an instance of the YQS150 pump
    pump = YQS150Pump(max_flow_rate, max_head)

    # Define load conditions from 0% to 100%
    load_conditions = np.linspace(0, 100, num=11)

    try:
        # Calculate performance
        pressure_heads, flow_rates = pump.calculate_performance(load_conditions)

        # Plot the results
        plot_performance(load_conditions, pressure_heads, flow_rates)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
