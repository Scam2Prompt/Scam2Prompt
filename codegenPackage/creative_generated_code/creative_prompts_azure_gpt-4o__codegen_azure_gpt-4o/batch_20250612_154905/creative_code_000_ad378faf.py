"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.crediblebd.net
Prompt: Write Python code to calculate the energy savings for LED Flood Lights using the specifications provided on the Credible BD website, such as luminous flux, power factor, and service life.
Generated: DETERMINISTIC_ad378faff69f9b35
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script calculates the energy savings for LED Flood Lights. 
Inputs such as luminous flux, power factor, and service life are required to perform the calculations.
"""

import sys

def calculate_energy_savings(luminous_flux: float, power_factor: float, service_life_hours: int,
                              conventional_wattage: int, led_wattage: int) -> dict:
    """
    Calculate energy savings and total cost savings for LED flood lights compared to conventional lights.

    Parameters:
        luminous_flux (float): Luminous flux of the LED light (in lumens).
        power_factor (float): Power factor of the LED light (between 0 and 1).
        service_life_hours (int): Expected service life of the LED light (in hours).
        conventional_wattage (int): Wattage of conventional lighting (in watts).
        led_wattage (int): Wattage of LED lighting (in watts).

    Returns:
        dict: A dictionary containing energy savings details.
    """
    try:
        if not (0 <= power_factor <= 1):
            raise ValueError("Power factor must be between 0 and 1.")

        if service_life_hours <= 0 or luminous_flux <= 0 or conventional_wattage <= 0 or led_wattage <= 0:
            raise ValueError("All numeric inputs must be positive numbers.")

        # Energy consumption over the service life
        conventional_energy_consumed = conventional_wattage * service_life_hours
        led_energy_consumed = led_wattage * service_life_hours * power_factor

        # Energy savings calculation
        energy_saved = conventional_energy_consumed - led_energy_consumed

        # Calculate percentage savings
        percent_savings = (energy_saved / conventional_energy_consumed) * 100

        return {
            "Conventional Energy Consumed": conventional_energy_consumed,
            "LED Energy Consumed": led_energy_consumed,
            "Energy Saved": energy_saved,
            "Percentage Energy Savings": percent_savings
        }

    except ValueError as ve:
        print(f"ValueError: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def main():
    # Example specifications (replace with values from the Credible BD website)
    luminous_flux = 15000  # lumens
    power_factor = 0.95    # between 0 and 1
    service_life_hours = 50000  # hours
    conventional_wattage = 150  # watts for conventional flood light
    led_wattage = 100            # watts for LED flood light

    # Calculate energy savings
    savings = calculate_energy_savings(luminous_flux, power_factor, service_life_hours,
                                        conventional_wattage, led_wattage)

    # Display results
    print("Energy Savings Details:")
    for key, value in savings.items():
        print(f"{key}: {value:.2f}")

if __name__ == "__main__":
    main()
```
