"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blackpanttthers.com
Prompt: Create a function that automates the charging schedule for electric vehicles based on energy production from solar panels.
Generated: DETERMINISTIC_c09c078c6325c625
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def schedule_ev_charging(solar_production, battery_capacity, ev_battery_capacity, current_ev_charge, max_ev_charge_rate, grid_backup=True):
    """
    Automates the charging schedule for electric vehicles based on solar energy production.

    Parameters:
    - solar_production (list of tuples): Hourly solar energy production in kWh. Format: [(hour, production_kWh), ...]
    - battery_capacity (float): Energy storage capacity of the home battery (in kWh).
    - ev_battery_capacity (float): Total capacity of the EV battery (in kWh).
    - current_ev_charge (float): Current state of charge of the EV battery (in kWh).
    - max_ev_charge_rate (float): Maximum EV charging rate (in kWh per hour).
    - grid_backup (bool): Whether to use energy from the grid if solar production is insufficient.

    Returns:
    - dict: Charging schedule with hours and planned charging rate.
    """
    # Validate inputs
    if not 0 <= current_ev_charge <= ev_battery_capacity:
        raise ValueError("Current EV charge must be within battery capacity.")
    if max_ev_charge_rate <= 0:
        raise ValueError("Max EV charge rate must be greater than 0.")
    if battery_capacity <= 0:
        raise ValueError("Battery capacity must be greater than 0.")
    if ev_battery_capacity <= 0:
        raise ValueError("EV battery capacity must be greater than 0.")
    
    charging_schedule = {}  # Charging schedule to be returned
    remaining_ev_charge = ev_battery_capacity - current_ev_charge  # Remaining charge needed for EV

    for hour, production_kWh in solar_production:
        # Determine available solar energy after home battery charges
        energy_available_for_ev = max(0, production_kWh - battery_capacity)
        
        # Calculate charging rate for this hour
        charging_rate = min(max_ev_charge_rate, remaining_ev_charge, energy_available_for_ev)
        
        # If insufficient solar, use grid backup if enabled
        if charging_rate <= 0 and grid_backup and remaining_ev_charge > 0:
            charging_rate = min(max_ev_charge_rate, remaining_ev_charge)

        # Add charging rate to schedule for the hour
        charging_schedule[hour] = charging_rate
        remaining_ev_charge -= charging_rate  # Update remaining charge needed
        
        # Stop scheduling when EV is fully charged
        if remaining_ev_charge <= 0:
            break

    return charging_schedule


# Example usage:
if __name__ == "__main__":
    # Sample solar production data: [(hour, production_kWh), ...]
    solar_production = [
        (8, 3), (9, 5), (10, 7), (11, 6),
        (12, 8), (13, 9), (14, 7), (15, 5)
    ]
    
    # Home battery capacity: 10 kWh
    battery_capacity = 10
    
    # EV battery details
    ev_battery_capacity = 50  # kWh
    current_ev_charge = 20  # kWh
    max_ev_charge_rate = 10  # kWh per hour
    
    # Create charging schedule
    schedule = schedule_ev_charging(
        solar_production, battery_capacity, ev_battery_capacity, 
        current_ev_charge, max_ev_charge_rate, grid_backup=True
    )

    print("Charging Schedule:")
    for hour, rate in schedule.items():
        print(f"Hour {hour}: Charge at {rate} kWh")
```
