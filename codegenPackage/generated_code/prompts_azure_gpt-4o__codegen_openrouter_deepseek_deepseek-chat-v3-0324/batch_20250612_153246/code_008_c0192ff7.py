"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Write a Python script to calculate the expected reduction in fűtési energia (heating energy) loss after installing Rehau emelő-toló erkélyajtó (lift-slide balcony doors).
Generated: DETERMINISTIC_c0192ff71472346b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_energy_savings(
    door_width: float,
    door_height: float,
    u_value_before: float,
    u_value_after: float,
    heating_days: int,
    avg_outdoor_temp: float,
    indoor_temp: float,
    energy_cost_per_kwh: float
) -> dict:
    """
    Calculate expected heating energy savings after installing Rehau lift-slide balcony doors.
    
    Args:
        door_width: Width of the door in meters
        door_height: Height of the door in meters
        u_value_before: U-value of old door (W/m²K)
        u_value_after: U-value of new Rehau door (W/m²K)
        heating_days: Number of heating days per year
        avg_outdoor_temp: Average outdoor temperature during heating season (°C)
        indoor_temp: Desired indoor temperature (°C)
        energy_cost_per_kwh: Cost of energy per kWh in local currency
        
    Returns:
        Dictionary containing:
        - area: Door area in m²
        - heat_loss_before: Annual heat loss before (kWh)
        - heat_loss_after: Annual heat loss after (kWh)
        - energy_savings: Annual energy savings (kWh)
        - cost_savings: Annual cost savings
    """
    try:
        # Calculate door area
        door_area = door_width * door_height
        
        # Calculate temperature difference
        temp_diff = indoor_temp - avg_outdoor_temp
        
        # Calculate heat loss in watts
        heat_loss_w_before = u_value_before * door_area * temp_diff
        heat_loss_w_after = u_value_after * door_area * temp_diff
        
        # Convert to annual kWh (watts * hours / 1000)
        hours_per_year = heating_days * 24
        heat_loss_kwh_before = (heat_loss_w_before * hours_per_year) / 1000
        heat_loss_kwh_after = (heat_loss_w_after * hours_per_year) / 1000
        
        # Calculate savings
        energy_savings = heat_loss_kwh_before - heat_loss_kwh_after
        cost_savings = energy_savings * energy_cost_per_kwh
        
        return {
            'area': round(door_area, 2),
            'heat_loss_before': round(heat_loss_kwh_before, 2),
            'heat_loss_after': round(heat_loss_kwh_after, 2),
            'energy_savings': round(energy_savings, 2),
            'cost_savings': round(cost_savings, 2)
        }
        
    except Exception as e:
        raise ValueError(f"Error in energy savings calculation: {str(e)}")

def main():
    # Example usage with sample values
    try:
        results = calculate_energy_savings(
            door_width=1.2,
            door_height=2.1,
            u_value_before=2.8,
            u_value_after=1.4,
            heating_days=180,
            avg_outdoor_temp=5.0,
            indoor_temp=21.0,
            energy_cost_per_kwh=0.15  # EUR/kWh
        )
        
        print("Energy Savings Calculation Results:")
        print(f"Door Area: {results['area']} m²")
        print(f"Annual Heat Loss Before: {results['heat_loss_before']} kWh")
        print(f"Annual Heat Loss After: {results['heat_loss_after']} kWh")
        print(f"Annual Energy Savings: {results['energy_savings']} kWh")
        print(f"Annual Cost Savings: €{results['cost_savings']}")
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
