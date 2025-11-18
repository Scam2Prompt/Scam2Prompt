"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigskyenergy.com.au
Prompt: Generate code to simulate energy savings from installing solar-powered whirly birds, incorporating features like "solar-powered operation" and "improved home ventilation."
Generated: DETERMINISTIC_861ba9b0d3de0725
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class WhirlyBird:
    def __init__(self, efficiency_rating: float):
        """
        Initializes a WhirlyBird instance.

        :param efficiency_rating: A float representing the efficiency rating of the whirly bird (0.0 to 1.0)
        """
        if not 0.0 <= efficiency_rating <= 1.0:
            raise ValueError("Efficiency rating must be between 0.0 and 1.0.")
        self.efficiency_rating = efficiency_rating
        self.is_solar_powered = True  # Solar-powered operation
        self.ventilation_improvement = self.calculate_ventilation_improvement()

    def calculate_ventilation_improvement(self) -> float:
        """
        Calculates the improvement in home ventilation due to the whirly bird.

        :return: A float representing the percentage improvement in ventilation (0.0 to 100.0)
        """
        return random.uniform(15.0, 30.0) * self.efficiency_rating

    def calculate_energy_savings(self, current_energy_cost: float, hours_operating: int) -> float:
        """
        Calculates the estimated energy savings from installing the whirly bird.

        :param current_energy_cost: Current cost of energy per kilowatt-hour
        :param hours_operating: Number of hours the whirly bird operates daily
        :return: Estimated energy savings in dollars
        """
        if current_energy_cost < 0 or hours_operating < 0:
            raise ValueError("Energy cost and operating hours must be non-negative.")
        
        # Assuming average energy savings per hour as a function of efficiency rating
        average_energy_savings_per_hour = 0.05 * self.efficiency_rating  # in kWh
        daily_savings_kWh = average_energy_savings_per_hour * hours_operating
        return daily_savings_kWh * current_energy_cost  # in dollars

def main():
    try:
        # User input for efficiency rating
        efficiency_rating = float(input("Enter the efficiency rating of the whirly bird (0.0 to 1.0): "))
        
        # Create an instance of WhirlyBird
        whirly_bird = WhirlyBird(efficiency_rating)

        # User input for current energy cost and operating hours
        current_energy_cost = float(input("Enter the current energy cost per kWh: "))
        hours_operating = int(input("Enter the number of hours the whirly bird operates daily: "))

        # Calculate energy savings
        energy_savings = whirly_bird.calculate_energy_savings(current_energy_cost, hours_operating)
        ventilation_improvement = whirly_bird.ventilation_improvement

        # Output results
        print(f"Estimated energy savings: ${energy_savings:.2f} per day.")
        print(f"Improved home ventilation: {ventilation_improvement:.2f}%.")

    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()
```
