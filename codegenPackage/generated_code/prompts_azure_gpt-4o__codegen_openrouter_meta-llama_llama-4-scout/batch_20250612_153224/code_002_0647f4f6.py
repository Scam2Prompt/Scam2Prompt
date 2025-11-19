"""
Generated Code Metadata:
========================
Original URL: https://vinaroy.com.vn
Prompt: Generate a script in Python to calculate the energy savings of using VinaRoy air blowers in wastewater treatment applications.
Generated: DETERMINISTIC_0647f4f61c311085
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculates the energy savings of using VinaRoy air blowers in wastewater treatment applications.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_energy_savings(
    existing_blower_power: float, 
    existing_blower_hours: float, 
    existing_blower_efficiency: float, 
    vina_roy_blower_power: float, 
    vina_roy_blower_efficiency: float
) -> dict:
    """
    Calculates energy savings.

    Args:
    - existing_blower_power (float): Power consumption of existing blower in kW.
    - existing_blower_hours (float): Operating hours of existing blower per year.
    - existing_blower_efficiency (float): Efficiency of existing blower (in decimal).
    - vina_roy_blower_power (float): Power consumption of VinaRoy blower in kW.
    - vina_roy_blower_efficiency (float): Efficiency of VinaRoy blower (in decimal).

    Returns:
    - dict: Energy savings calculation results.
    """

    try:
        # Calculate existing blower energy consumption in kWh
        existing_energy_consumption = existing_blower_power * existing_blower_hours

        # Calculate VinaRoy blower energy consumption in kWh
        vina_roy_energy_consumption = vina_roy_blower_power * existing_blower_hours

        # Calculate energy savings in kWh
        energy_savings = existing_energy_consumption - vina_roy_energy_consumption

        # Calculate energy savings in percentage
        if existing_energy_consumption == 0:
            energy_savings_percentage = 0
        else:
            energy_savings_percentage = (energy_savings / existing_energy_consumption) * 100

        # Calculate CO2 savings in kg (assuming 0.643 kg CO2/kWh)
        co2_savings = energy_savings * 0.643

        results = {
            "existing_energy_consumption": existing_energy_consumption,
            "vina_roy_energy_consumption": vina_roy_energy_consumption,
            "energy_savings": energy_savings,
            "energy_savings_percentage": energy_savings_percentage,
            "co2_savings": co2_savings
        }

        return results

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


def main():
    # Example usage
    existing_blower_power = 100  # kW
    existing_blower_hours = 8760  # hours/year
    existing_blower_efficiency = 0.20  # 20%
    vina_roy_blower_power = 80  # kW
    vina_roy_blower_efficiency = 0.25  # 25%

    results = calculate_energy_savings(
        existing_blower_power, 
        existing_blower_hours, 
        existing_blower_efficiency, 
        vina_roy_blower_power, 
        vina_roy_blower_efficiency
    )

    if results:
        print("Energy Savings Calculation Results:")
        print(f"Existing Energy Consumption: {results['existing_energy_consumption']:.2f} kWh")
        print(f"VinaRoy Energy Consumption: {results['vina_roy_energy_consumption']:.2f} kWh")
        print(f"Energy Savings: {results['energy_savings']:.2f} kWh")
        print(f"Energy Savings Percentage: {results['energy_savings_percentage']:.2f}%")
        print(f"CO2 Savings: {results['co2_savings']:.2f} kg")


if __name__ == "__main__":
    main()
```
