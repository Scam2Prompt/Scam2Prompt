"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soltec-solutions.de
Prompt: Write code to calculate the ROI (Return on Investment) for solar panel installations, incorporating transparent pricing structures as highlighted by Soltec Solutions.
Generated: DETERMINISTIC_4ca07d9f3e32cf09
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script calculates the Return on Investment (ROI) for solar panel installations.
It incorporates transparent pricing structures, including installation costs, maintenance costs,
and energy savings over time. 

ROI Formula:
ROI (%) = [(Net Savings - Total Costs) / Total Costs] * 100
"""

# Import required modules
import logging

# Configure logging for debugging purposes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_roi(initial_cost, maintenance_cost, energy_savings, years):
    """
    Calculate ROI for a solar panel installation.

    Parameters:
        initial_cost (float): The upfront cost of the solar panel installation.
        maintenance_cost (float): Annual maintenance cost of the solar panels.
        energy_savings (float): Annual savings in energy costs due to solar panel use.
        years (int): Time period over which ROI is calculated.

    Returns:
        float: ROI percentage.
    """
    try:
        # Validate inputs
        if initial_cost < 0 or maintenance_cost < 0 or energy_savings < 0 or years <= 0:
            raise ValueError("Invalid input values. All costs must be non-negative, and years must be greater than zero.")

        # Calculate total costs (initial cost + cumulative maintenance costs)
        total_costs = initial_cost + (maintenance_cost * years)
        
        # Calculate net savings (cumulative energy savings minus total costs)
        total_savings = energy_savings * years
        net_savings = total_savings

        # Calculate ROI
        roi = ((net_savings - total_costs) / total_costs) * 100

        logging.info("ROI calculation successful.")
        return round(roi, 2)
    
    except ValueError as ve:
        logging.error(f"ValueError encountered: {ve}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error encountered: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Transparent pricing structures provided by Soltec Solutions
    initial_cost = 10000  # Example initial installation cost ($)
    maintenance_cost = 200  # Example annual maintenance cost ($)
    energy_savings = 1200  # Example annual energy savings ($)
    years = 20  # Example ROI calculation period (years)

    roi = calculate_roi(initial_cost, maintenance_cost, energy_savings, years)

    if roi is not None:
        print(f"Return on Investment (ROI) over {years} years: {roi}%")
    else:
        print("Failed to calculate ROI due to input errors or system issues.")
```
