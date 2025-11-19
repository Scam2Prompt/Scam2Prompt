"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Write a Python script to calculate the energy savings from replacing old windows with Aluplast Ideal 3-layer windows, considering their hőszigetelési (thermal insulation) properties.
Generated: DETERMINISTIC_305362f4f8a6e031
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# thermal_insulation_calculator.py

def calculate_energy_savings(
    old_window_u_value: float, 
    new_window_u_value: float, 
    heating_degree_days: float, 
    heating_season_duration: int, 
    energy_price: float, 
    old_window_area: float
) -> float:
    """
    Calculate energy savings from replacing old windows with new ones.

    Args:
    - old_window_u_value (float): Thermal transmittance of old window (W/m²K)
    - new_window_u_value (float): Thermal transmittance of new window (W/m²K)
    - heating_degree_days (float): Heating degree days (HDD) for the location
    - heating_season_duration (int): Duration of heating season in days
    - energy_price (float): Price of energy in HUF/kWh
    - old_window_area (float): Area of old window in m²

    Returns:
    - energy_savings (float): Energy savings in HUF/year
    """

    # Check for invalid input values
    if old_window_u_value <= 0 or new_window_u_value <= 0:
        raise ValueError("U-values must be greater than zero.")
    if heating_degree_days < 0:
        raise ValueError("Heating degree days must be non-negative.")
    if heating_season_duration <= 0:
        raise ValueError("Heating season duration must be greater than zero.")
    if energy_price <= 0:
        raise ValueError("Energy price must be greater than zero.")
    if old_window_area <= 0:
        raise ValueError("Old window area must be greater than zero.")

    # Calculate energy consumption of old and new windows
    old_window_energy_consumption = old_window_u_value * old_window_area * heating_degree_days
    new_window_energy_consumption = new_window_u_value * old_window_area * heating_degree_days

    # Convert energy consumption from Wh to kWh
    old_window_energy_consumption_kwh = old_window_energy_consumption / 1000
    new_window_energy_consumption_kwh = new_window_energy_consumption / 1000

    # Calculate energy savings
    energy_savings_kwh = old_window_energy_consumption_kwh - new_window_energy_consumption_kwh
    energy_savings_huf = energy_savings_kwh * energy_price

    return energy_savings_huf


def main():
    try:
        # Aluplast Ideal 3-layer window U-value (W/m²K)
        new_window_u_value = 0.95

        # Old window U-value (W/m²K)
        old_window_u_values = [2.5, 2.0, 1.5]

        # Location parameters
        heating_degree_days = 2400  # HDD
        heating_season_duration = 210  # days
        energy_price = 15.0  # HUF/kWh

        # Window area
        old_window_area = 10.0  # m²

        for old_window_u_value in old_window_u_values:
            energy_savings = calculate_energy_savings(
                old_window_u_value, 
                new_window_u_value, 
                heating_degree_days, 
                heating_season_duration, 
                energy_price, 
                old_window_area
            )
            print(f"Old window U-value: {old_window_u_value} W/m²K")
            print(f"Energy savings: {energy_savings:.2f} HUF/year")
            print()

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
