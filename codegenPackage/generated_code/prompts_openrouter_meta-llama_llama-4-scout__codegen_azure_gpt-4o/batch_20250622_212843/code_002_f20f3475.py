"""
Generated Code Metadata:
========================
Original URL: https://dimensions-solar.com
Prompt: "Write a Python code snippet to calculate the return on investment (ROI) for a rooftop solar plant installation, considering factors like system cost, energy output, and maintenance expenses."
Generated: DETERMINISTIC_f20f3475b69fce00
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import sys

def calculate_roi(system_cost, annual_energy_output_kwh, energy_rate_per_kwh, annual_maintenance_cost, years):
    """
    Calculate the Return on Investment (ROI) for a rooftop solar plant installation.

    Parameters:
        system_cost (float): Initial cost of the solar system installation.
        annual_energy_output_kwh (float): Annual energy output of the solar system in kilowatt-hours (kWh).
        energy_rate_per_kwh (float): Rate of energy per kWh (savings per kWh).
        annual_maintenance_cost (float): Annual maintenance cost for the solar system.
        years (int): Number of years to calculate ROI over.

    Returns:
        float: ROI percentage.
    """
    try:
        # Validate inputs
        if system_cost <= 0 or annual_energy_output_kwh <= 0 or energy_rate_per_kwh <= 0 or annual_maintenance_cost < 0 or years <= 0:
            raise ValueError("All input values must be positive, except maintenance cost which can be zero.")

        # Calculate total savings from energy production over the given years
        total_energy_savings = annual_energy_output_kwh * energy_rate_per_kwh * years

        # Calculate total maintenance cost over the given years
        total_maintenance_cost = annual_maintenance_cost * years

        # Calculate net profit
        net_profit = total_energy_savings - total_maintenance_cost - system_cost

        # Calculate ROI percentage
        roi_percentage = (net_profit / system_cost) * 100

        return roi_percentage

    except ValueError as ve:
        print(f"Input Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None


# Example usage
if __name__ == "__main__":
    # Example inputs
    system_cost = 15000.0  # Cost of the solar system installation in dollars
    annual_energy_output_kwh = 5000.0  # Annual energy output in kWh
    energy_rate_per_kwh = 0.12  # Energy rate per kWh in dollars
    annual_maintenance_cost = 200.0  # Annual maintenance cost in dollars
    years = 25  # Number of years to calculate ROI over

    # Calculate ROI
    roi = calculate_roi(system_cost, annual_energy_output_kwh, energy_rate_per_kwh, annual_maintenance_cost, years)

    if roi is not None:
        print(f"Return on Investment (ROI) over {years} years: {roi:.2f}%")
    else:
        print("Failed to calculate ROI due to input errors or unexpected issues.")
```
