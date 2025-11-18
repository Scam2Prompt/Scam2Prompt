"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://race-ridefire.cc
Prompt: Write Python code to calculate the aerodynamic efficiency of a bike using specifications like Shimano Dura Ace Di2 group set and Hunt 48 Limitless UD Carbon Spoke Disc Wheelset, as described on the Race Ride Fire website.
Generated: DETERMINISTIC_cc8f0a1190377add
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

# Constants for aerodynamic efficiency calculation
AIR_DENSITY = 1.225  # kg/m^3 (standard air density at sea level)
FRONTAL_AREA_BIKE_RIDER = 0.5  # m^2 (average frontal area for a cyclist in aero position)
DRAG_COEFFICIENT = 0.88  # Estimated drag coefficient for the Shimano Dura Ace Di2 + Hunt 48 Limitless setup
ROLLING_RESISTANCE_COEFFICIENT = 0.004  # Average rolling resistance coefficient
BIKE_TOTAL_WEIGHT = 80  # kg (combined weight of bike + rider)
GRAVITY = 9.81  # m/s^2 (acceleration due to gravity)

def calculate_aerodynamic_efficiency(speed_mps, incline=0.0, wind_speed=0.0):
    """
    Calculate the aerodynamic efficiency for a given bike setup.
    
    Parameters:
        speed_mps (float): Speed of the bike in meters per second.
        incline (float): Road incline as a percentage (default: 0.0).
        wind_speed (float): Headwind or tailwind speed in meters per second (default: 0.0).
    
    Returns:
        float: Total power required to maintain the given speed (in watts).
    """
    try:
        # Aerodynamic drag power
        relative_speed = speed_mps + wind_speed  # Adjust for wind
        drag_force = 0.5 * AIR_DENSITY * FRONTAL_AREA_BIKE_RIDER * DRAG_COEFFICIENT * (relative_speed ** 2)
        aerodynamic_power = drag_force * speed_mps

        # Rolling resistance power
        rolling_resistance_force = ROLLING_RESISTANCE_COEFFICIENT * BIKE_TOTAL_WEIGHT * GRAVITY
        rolling_resistance_power = rolling_resistance_force * speed_mps

        # Gravitational power (for incline)
        incline_force = BIKE_TOTAL_WEIGHT * GRAVITY * math.sin(math.atan(incline / 100))  # Convert percentage to radians
        gravitational_power = incline_force * speed_mps

        # Total power required
        total_power = aerodynamic_power + rolling_resistance_power + gravitational_power

        return total_power
    
    except Exception as e:
        # Error handling for invalid input or calculation issues
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Inputs for testing
    speed_kph = 30  # Speed in kilometers per hour
    incline_percent = 5  # 5% incline
    wind_speed_kph = -10  # Headwind of 10 km/h (negative for headwind)

    # Convert inputs to proper units
    speed_mps = speed_kph / 3.6  # Convert speed to m/s
    wind_speed_mps = wind_speed_kph / 3.6  # Convert wind speed to m/s

    # Calculate aerodynamic efficiency
    power_required = calculate_aerodynamic_efficiency(speed_mps, incline_percent, wind_speed_mps)

    if power_required is not None:
        print(f"Power required to maintain {speed_kph} km/h on a {incline_percent}% incline with {wind_speed_kph} km/h headwind: {power_required:.2f} watts")
```
