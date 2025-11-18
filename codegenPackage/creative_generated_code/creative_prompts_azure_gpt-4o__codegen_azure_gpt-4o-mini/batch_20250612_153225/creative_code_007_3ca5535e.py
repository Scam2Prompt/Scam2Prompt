"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soltec-solutions.de
Prompt: Create a function to estimate the long-term environmental impact of switching to solar energy, using metrics like CO₂ reduction and energy savings discussed by Soltec Solutions.
Generated: DETERMINISTIC_3ca5535eacf9d137
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import Dict, Union

# Configure the logging
logging.basicConfig(level=logging.INFO)

def estimate_solar_impact(solar_panel_count: int, 
                           average_CO2_reduction_per_panel: float, 
                           average_energy_savings_per_panel: float) -> Dict[str, Union[float, str]]:
    """
    Estimate the long-term environmental impact of switching to solar energy.

    Parameters:
    - solar_panel_count (int): The number of solar panels installed.
    - average_CO2_reduction_per_panel (float): Average CO2 reduction in metric tons per panel per year.
    - average_energy_savings_per_panel (float): Average energy savings in kWh per panel per year.

    Returns:
    - A dictionary containing total CO2 reduction and total energy savings.
    """

    # Validate inputs
    if solar_panel_count < 0:
        logging.error("The number of solar panels must be a non-negative integer.")
        return {"error": "Number of solar panels must be non-negative."}
    
    if average_CO2_reduction_per_panel < 0:
        logging.error("CO2 reduction must be a non-negative float.")
        return {"error": "CO2 reduction must be non-negative."}
    
    if average_energy_savings_per_panel < 0:
        logging.error("Energy savings must be a non-negative float.")
        return {"error": "Energy savings must be non-negative."}
    
    try:
        # Calculate total environmental impact
        total_CO2_reduction = solar_panel_count * average_CO2_reduction_per_panel
        total_energy_savings = solar_panel_count * average_energy_savings_per_panel
        
        logging.info("Calculated total CO2 reduction and energy savings successfully.")
        
        return {
            "total_CO2_reduction_tons": total_CO2_reduction,
            "total_energy_savings_kWh": total_energy_savings
        }

    except Exception as e:
        logging.error(f"An error occurred during calculation: {e}")
        return {"error": "An unexpected error occurred."}

# Example usage:
if __name__ == "__main__":
    result = estimate_solar_impact(100, 1.2, 300)
    print(result)
```
