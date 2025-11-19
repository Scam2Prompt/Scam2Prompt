"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imbcg.com
Prompt: Provide a code example for calculating CO2 emissions savings when switching from diesel to solar pumps, referencing IMB Cambodia Group's comparison tools.
Generated: DETERMINISTIC_859cca6c7b4800f9
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PumpEmissionCalculator:
    def __init__(self, diesel_consumption_liters_per_day, co2_emission_per_liter, solar_pump_usage_factor):
        """
        Initializes the PumpEmissionCalculator with the given parameters.

        :param diesel_consumption_liters_per_day: Daily diesel consumption in liters
        :param co2_emission_per_liter: CO2 emissions in kg per liter of diesel
        :param solar_pump_usage_factor: Factor representing how much solar can replace diesel usage
        """
        self.diesel_consumption_liters_per_day = diesel_consumption_liters_per_day
        self.co2_emission_per_liter = co2_emission_per_liter
        self.solar_pump_usage_factor = solar_pump_usage_factor

    def calculate_daily_co2_emissions(self):
        """
        Calculates daily CO2 emissions from diesel pumps.

        :return: Daily CO2 emissions in kg
        """
        return self.diesel_consumption_liters_per_day * self.co2_emission_per_liter

    def calculate_savings_with_solar(self):
        """
        Calculates potential CO2 emissions savings when switching from diesel to solar pumps.

        :return: Potential daily CO2 savings in kg
        """
        try:
            # Calculate CO2 emissions if using solar for the given factor
            diesel_emissions = self.calculate_daily_co2_emissions()
            solar_replacement_emissions = diesel_emissions * (1 - self.solar_pump_usage_factor)
            savings = diesel_emissions - solar_replacement_emissions
            return savings
        except Exception as e:
            print(f"Error calculating savings: {e}")
            return None

    def display_savings(self):
        """
        Displays the daily CO2 emission savings when switching to solar pumps.
        """
        savings = self.calculate_savings_with_solar()
        if savings is not None:
            print(f"Daily CO2 emissions savings by switching to solar pumps: {savings:.2f} kg")
        else:
            print("Failed to calculate savings.")


if __name__ == "__main__":
    # Example parameters
    diesel_consumption = 100  # liters per day
    co2_per_liter = 2.68      # kg CO2 per liter of diesel
    solar_usage_factor = 0.75  # 75% of diesel usage replaced by solar

    # Create an instance of the emission calculator
    calculator = PumpEmissionCalculator(diesel_consumption, co2_per_liter, solar_usage_factor)

    # Display the savings
    calculator.display_savings()
```
