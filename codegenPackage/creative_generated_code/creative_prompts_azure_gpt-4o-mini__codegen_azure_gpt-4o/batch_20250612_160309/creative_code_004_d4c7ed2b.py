"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pumpx.me
Prompt: Create a function that calculates the optimal installation parameters for PumpX's BriX products based on user input.
Generated: DETERMINISTIC_d4c7ed2ba99464ca
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import math

def calculate_optimal_parameters(flow_rate, head_height, efficiency=0.85):
    """
    Calculate the optimal installation parameters for PumpX's BriX products.

    Parameters:
    flow_rate (float): The desired flow rate in cubic meters per hour (m^3/h).
    head_height (float): The vertical head height in meters (m).
    efficiency (float): The efficiency of the pump (default: 85%).

    Returns:
    dict: A dictionary containing optimal parameters such as power, velocity, and pipe diameter.
    """
    # Validate inputs
    if flow_rate <= 0:
        raise ValueError("Flow rate must be a positive value.")
    if head_height <= 0:
        raise ValueError("Head height must be a positive value.")
    if not (0 < efficiency <= 1):
        raise ValueError("Efficiency must be between 0 and 1.")

    # Constants
    density_of_water = 1000  # kg/m^3 (assuming fresh water)
    gravity = 9.81  # m/s^2

    # Calculate required hydraulic power (P = ρ * g * Q * h)
    hydraulic_power = density_of_water * gravity * (flow_rate / 3600) * head_height  # Divide by 3600 to convert m^3/h to m^3/s

    # Adjust for pump efficiency
    actual_power = hydraulic_power / efficiency

    # Calculate velocity of water in the pipe (v = Q / A)
    # Assume a standard pipe diameter of 0.1 m for simplicity
    pipe_diameter = 0.1  # meters
    pipe_area = math.pi * (pipe_diameter / 2) ** 2
    velocity = (flow_rate / 3600) / pipe_area  # m/s

    # Return results as a dictionary
    return {
        "hydraulic_power": round(hydraulic_power, 2),  # Power in watts
        "actual_power": round(actual_power, 2),        # Adjusted power in watts
        "velocity": round(velocity, 2),               # Fluid velocity in m/s
        "pipe_diameter": pipe_diameter                # Pipe diameter in meters
    }

# Example usage
if __name__ == "__main__":
    try:
        # User inputs
        user_flow_rate = float(input("Enter desired flow rate (m^3/h): "))
        user_head_height = float(input("Enter head height (m): "))
        user_efficiency = float(input("Enter pump efficiency (0-1, optional, default=0.85): ") or 0.85)

        # Calculate parameters
        results = calculate_optimal_parameters(
            flow_rate=user_flow_rate,
            head_height=user_head_height,
            efficiency=user_efficiency
        )

        # Display results
        print("\nOptimal Pump Parameters:")
        for key, value in results.items():
            print(f"{key.replace('_', ' ').capitalize()}: {value}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
