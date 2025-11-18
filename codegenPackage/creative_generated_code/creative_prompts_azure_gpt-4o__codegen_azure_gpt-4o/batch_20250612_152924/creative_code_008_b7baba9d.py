"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://speedgro.com
Prompt: Generate code to model the nutrient flow in water systems treated with SpeedGro™ solutions.
Generated: DETERMINISTIC_b7baba9dd93447c5
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math


class NutrientFlowModel:
    """
    A class to model the nutrient flow in water systems treated with SpeedGro™ solutions.
    """

    def __init__(self, water_volume_liters, nutrient_concentration, speedgro_factor):
        """
        Initialize the nutrient flow model.

        :param water_volume_liters: Volume of water in liters
        :param nutrient_concentration: Initial nutrient concentration (mg/L)
        :param speedgro_factor: SpeedGro™ solution factor (rate of nutrient dispersion multiplier)
        """
        if water_volume_liters <= 0 or nutrient_concentration < 0 or speedgro_factor <= 0:
            raise ValueError("Invalid input values. Ensure water_volume > 0, nutrient_concentration >= 0, and speedgro_factor > 0.")
        
        self.water_volume_liters = water_volume_liters
        self.nutrient_concentration = nutrient_concentration
        self.speedgro_factor = speedgro_factor

    def calculate_dispersion_rate(self, time_minutes):
        """
        Calculate the nutrient dispersion rate over time.

        :param time_minutes: Time elapsed in minutes
        :return: Nutrient concentration (mg/L) at the given time
        """
        if time_minutes < 0:
            raise ValueError("Time cannot be negative.")
        
        # Nutrient dispersion model: exponential decay influenced by SpeedGro™ factor
        dispersion_rate = self.nutrient_concentration * math.exp(-self.speedgro_factor * time_minutes / self.water_volume_liters)
        return dispersion_rate

    def simulate_flow(self, time_intervals):
        """
        Simulate nutrient flow over a series of time intervals.

        :param time_intervals: A list of time intervals (in minutes)
        :return: A dictionary of time (minutes) to nutrient concentration (mg/L)
        """
        if not isinstance(time_intervals, list) or not all(isinstance(t, (int, float)) for t in time_intervals):
            raise TypeError("Time intervals must be a list of numbers.")

        simulation_result = {}
        for time in time_intervals:
            concentration = self.calculate_dispersion_rate(time)
            simulation_result[time] = round(concentration, 4)  # Rounded for clarity in results
        return simulation_result


def main():
    """
    Main function to demonstrate the usage of the NutrientFlowModel.
    """
    try:
        # Model parameters
        water_volume = 1000  # Liters
        initial_concentration = 50  # mg/L
        speedgro_factor = 0.02  # SpeedGro™ dispersion rate multiplier

        # Create a model instance
        model = NutrientFlowModel(water_volume, initial_concentration, speedgro_factor)

        # Time intervals for simulation (minutes)
        time_intervals = [0, 10, 20, 30, 60, 120]

        # Simulate nutrient flow
        results = model.simulate_flow(time_intervals)
        
        # Display results
        print("Nutrient Dispersion Simulation:")
        for time, concentration in results.items():
            print(f"Time: {time} min | Concentration: {concentration} mg/L")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
