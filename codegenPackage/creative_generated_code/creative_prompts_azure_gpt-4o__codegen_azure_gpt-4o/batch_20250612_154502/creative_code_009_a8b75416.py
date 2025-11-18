"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loghouses-woodcraft.com
Prompt: Write a Python script to analyze and plot the efficiency curve of 200QS water pumps based on manufacturer specifications.
Generated: DETERMINISTIC_a8b75416e1707c67
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate efficiency based on manufacturer specifications
def calculate_efficiency(flow_rate, head, power_input):
    """
    Calculate pump efficiency using the formula:
    Efficiency (%) = (Flow Rate * Head) / Power Input * 100

    Parameters:
        flow_rate (float): Flow rate in cubic meters per second (m³/s)
        head (float): Head in meters (m)
        power_input (float): Power input in kilowatts (kW)

    Returns:
        float: Efficiency percentage
    """
    try:
        # Avoid division by zero
        if power_input <= 0:
            raise ValueError("Power input must be greater than zero.")
        
        # Efficiency calculation
        efficiency = (flow_rate * head) / power_input * 100
        return efficiency
    except Exception as e:
        print(f"Error calculating efficiency: {e}")
        return None


# Manufacturer specifications (example data for 200QS pumps)
flow_rates = np.linspace(0.05, 0.5, 100)  # Flow rates (m³/s)
heads = np.linspace(10, 30, 100)          # Heads (m)
power_input = 15                          # Constant power input (kW)

# Calculate efficiencies for each flow rate and head
efficiencies = np.array([calculate_efficiency(flow, head, power_input) 
                         for flow, head in zip(flow_rates, heads)])

# Ensure valid efficiencies exist
efficiencies = efficiencies[~np.isnan(efficiencies)]  # Remove invalid values

# Plotting the efficiency curve
plt.figure(figsize=(10, 6))
plt.plot(flow_rates[:len(efficiencies)], efficiencies, label='Efficiency Curve', color='blue')
plt.title('Efficiency Curve for 200QS Water Pumps')
plt.xlabel('Flow Rate (m³/s)')
plt.ylabel('Efficiency (%)')
plt.grid(True)  # Add grid for better readability
plt.legend()
plt.tight_layout()

# Save plot to file or show on screen
plt.savefig('efficiency_curve_200QS.png')
plt.show()
```
