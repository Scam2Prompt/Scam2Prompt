"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.chicoelectric.com
Prompt: Develop a program to model grid-positive solar generation for educational institutions, referencing Chico Electric's installation at Butte College.
Generated: DETERMINISTIC_f0f68e5ed45a2f29
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

# Constants for solar generation calculations
SOLAR_CAPACITY_KW = 4500  # Total installed capacity (kW), fictional value based on scale
GRID_POSITIVE_THRESHOLD = 0  # Net surplus threshold for "grid-positive"

class SolarGeneration:
    """
    A class to model solar generation and grid-positive energy production
    for educational institutions, referencing Chico Electric's installation at Butte College.
    """

    def __init__(self, capacity_kw: float, efficiency: float = 0.18):
        """
        Initialize the SolarGeneration model.
        
        :param capacity_kw: Total installed solar capacity in kilowatts.
        :param efficiency: Average solar panel efficiency (default: 18%).
        """
        self.capacity_kw = capacity_kw
        self.efficiency = efficiency

    def estimate_daily_generation(self, sunlight_hours: float) -> float:
        """
        Estimate daily solar generation based on sunlight hours.
        
        :param sunlight_hours: Average hours of sunlight per day.
        :return: Estimated daily solar generation in kWh.
        """
        return self.capacity_kw * self.efficiency * sunlight_hours

    def is_grid_positive(self, daily_generation: float, daily_consumption: float) -> bool:
        """
        Determine if the institution is grid-positive.
        
        :param daily_generation: Daily solar generation (kWh).
        :param daily_consumption: Daily energy consumption (kWh).
        :return: True if institution is grid-positive, False otherwise.
        """
        net_surplus = daily_generation - daily_consumption
        return net_surplus > GRID_POSITIVE_THRESHOLD


def simulate_institution_energy(
    sunlight_hours: List[float],
    daily_consumption: List[float],
    capacity_kw: float
) -> Dict[str, float]:
    """
    Simulate solar generation and grid-positive status for multiple days.

    :param sunlight_hours: List of daily sunlight hours per day.
    :param daily_consumption: List of daily energy consumption per day (kWh).
    :param capacity_kw: Total installed solar capacity in kilowatts.
    :return: Dictionary containing simulation results.
    """
    solar_model = SolarGeneration(capacity_kw)
    results = {
        "days_grid_positive": 0,
        "daily_generations": [],
        "net_surplus_days": []
    }

    for i, (sunlight, consumption) in enumerate(zip(sunlight_hours, daily_consumption)):
        try:
            daily_generation = solar_model.estimate_daily_generation(sunlight)
            results["daily_generations"].append(daily_generation)
            
            net_surplus = daily_generation - consumption
            results["net_surplus_days"].append(net_surplus)

            if solar_model.is_grid_positive(daily_generation, consumption):
                results["days_grid_positive"] += 1

        except Exception as e:
            # Log error and continue simulation
            print(f"Error on day {i + 1}: {e}")

    return results


# Example usage
if __name__ == "__main__":
    try:
        # Simulated sunlight and consumption data for 7 days
        sunlight_hours = [5.5, 6.0, 7.2, 4.8, 5.0, 6.5, 5.8]  # Average sunlight hours per day
        daily_consumption = [3500, 4000, 3200, 3700, 3600, 3300, 3400]  # Energy consumption per day (kWh)

        # Simulate solar generation and grid-positive status
        simulation_results = simulate_institution_energy(sunlight_hours, daily_consumption, SOLAR_CAPACITY_KW)

        # Output results
        print("Simulation Results:")
        print(f"Total Days Grid-Positive: {simulation_results['days_grid_positive']}")
        print(f"Daily Generations (kWh): {simulation_results['daily_generations']}")
        print(f"Net Surplus (kWh): {simulation_results['net_surplus_days']}")

    except Exception as e:
        print(f"An error occurred during the simulation: {e}")
```
