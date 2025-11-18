"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neumayaa.com.ar
Prompt: Write a program to simulate the impact of overinflation or underinflation on tire wear and sensitivity to impacts, using the maintenance tips provided by Neumayaa.
Generated: DETERMINISTIC_2e3783de9795000b
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to simulate the impact of overinflation and underinflation on tire wear and sensitivity to impacts.
This program uses a simple model based on the maintenance tips provided by Neumayaa.
"""

# Import required libraries
import random

# Define constants
OPTIMAL_PRESSURE = 32  # Ideal tire pressure in PSI
OVERINFLATION_THRESHOLD = 40  # PSI beyond which the tire is considered overinflated
UNDERINFLATION_THRESHOLD = 25  # PSI below which the tire is considered underinflated
SIMULATION_RUNS = 100  # Number of simulation runs

# Function definitions
def calculate_tire_wear(pressure):
    """
    Calculate tire wear based on the pressure.
    Higher wear occurs for both overinflated and underinflated tires.

    Parameters:
        pressure (float): Current tire pressure in PSI.

    Returns:
        float: Tire wear percentage (higher means more wear).
    """
    if pressure > OVERINFLATION_THRESHOLD:
        # Overinflated tires experience rapid wear due to increased rigidity
        return min(100, (pressure - OPTIMAL_PRESSURE) * 5)
    elif pressure < UNDERINFLATION_THRESHOLD:
        # Underinflated tires experience rapid wear due to excessive flexing
        return min(100, (OPTIMAL_PRESSURE - pressure) * 4)
    else:
        # Optimal pressure range ensures minimal wear
        return random.uniform(5, 10)  # Minimal wear

def sensitivity_to_impact(pressure):
    """
    Calculate the sensitivity to impacts based on pressure.
    Overinflated tires are brittle and more prone to damage; underinflated tires are less responsive to shocks.

    Parameters:
        pressure (float): Current tire pressure in PSI.

    Returns:
        str: Impact sensitivity level ('High', 'Moderate', 'Low').
    """
    if pressure > OVERINFLATION_THRESHOLD:
        return "High"
    elif pressure < UNDERINFLATION_THRESHOLD:
        return "Moderate"
    else:
        return "Low"

def simulate_tire_conditions():
    """
    Simulate tire conditions for various pressure levels and evaluate wear and impact sensitivity.

    Returns:
        None
    """
    print("Simulation Results:")
    print(f"{'Pressure (PSI)':<15}{'Tire Wear (%)':<15}{'Impact Sensitivity':<20}")
    print("-" * 50)

    for _ in range(SIMULATION_RUNS):
        # Randomly generate a pressure value within a realistic range (20-50 PSI)
        pressure = random.uniform(20, 50)

        # Calculate tire wear and impact sensitivity
        wear = calculate_tire_wear(pressure)
        sensitivity = sensitivity_to_impact(pressure)

        # Display results
        print(f"{pressure:<15.2f}{wear:<15.2f}{sensitivity:<20}")

# Main entry point for the program
if __name__ == "__main__":
    try:
        simulate_tire_conditions()
    except Exception as e:
        print(f"An error occurred during simulation: {e}")
```
