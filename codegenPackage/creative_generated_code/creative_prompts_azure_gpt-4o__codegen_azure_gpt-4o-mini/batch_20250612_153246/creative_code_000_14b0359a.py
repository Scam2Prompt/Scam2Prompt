"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.ablakvaros.hu
Prompt: Write a Python script to calculate the energy savings after replacing old windows with Aluplast Ideal 5000 profiles, considering their hőszigetelési (thermal insulation) properties.
Generated: DETERMINISTIC_14b0359a2a2245c1
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Window:
    """Class to represent a window and calculate energy savings."""
    
    def __init__(self, area: float, old_u_value: float, new_u_value: float, heating_cost_per_kwh: float):
        """
        Initialize the window properties.
        
        :param area: Area of the window in square meters.
        :param old_u_value: U-value of the old window (W/m²K).
        :param new_u_value: U-value of the new window (W/m²K).
        :param heating_cost_per_kwh: Cost of heating per kWh.
        """
        self.area = area
        self.old_u_value = old_u_value
        self.new_u_value = new_u_value
        self.heating_cost_per_kwh = heating_cost_per_kwh

    def calculate_energy_savings(self, temperature_difference: float, heating_season_days: int) -> float:
        """
        Calculate the energy savings from replacing old windows with new ones.
        
        :param temperature_difference: Average temperature difference between indoor and outdoor (°C).
        :param heating_season_days: Number of days in the heating season.
        :return: Estimated energy savings in currency (e.g., Euros).
        """
        try:
            # Calculate heat loss for old and new windows
            heat_loss_old = self.area * self.old_u_value * temperature_difference * heating_season_days * 24  # kWh
            heat_loss_new = self.area * self.new_u_value * temperature_difference * heating_season_days * 24  # kWh
            
            # Calculate energy savings in kWh
            energy_savings_kwh = heat_loss_old - heat_loss_new

            # Calculate cost savings
            cost_savings = energy_savings_kwh * self.heating_cost_per_kwh
            
            logging.info(f"Energy savings: {energy_savings_kwh:.2f} kWh, Cost savings: {cost_savings:.2f} currency units")
            return cost_savings
        
        except Exception as e:
            logging.error("Error calculating energy savings: %s", e)
            return 0.0

def main():
    """Main function to execute the energy savings calculation."""
    # Example parameters (customize these values as needed)
    window_area = 2.0  # Area of the window in m²
    old_window_u_value = 2.5  # U-value for old window (W/m²K)
    new_window_u_value = 0.9   # U-value for Aluplast Ideal 5000 (W/m²K)
    heating_cost_per_kwh = 0.15  # Cost of heating per kWh in currency units
    temperature_difference = 20   # Average indoor to outdoor temperature difference (°C)
    heating_season_days = 120     # Days in the heating season

    # Create a Window object
    window = Window(window_area, old_window_u_value, new_window_u_value, heating_cost_per_kwh)

    # Calculate and print energy savings
    savings = window.calculate_energy_savings(temperature_difference, heating_season_days)
    print(f"Estimated energy savings: {savings:.2f} currency units")

if __name__ == "__main__":
    main()
```
