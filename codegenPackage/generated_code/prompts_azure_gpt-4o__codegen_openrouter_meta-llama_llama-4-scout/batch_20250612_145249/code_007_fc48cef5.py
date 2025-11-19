"""
Generated Code Metadata:
========================
Original URL: https://www.premierpointing.com.au
Prompt: Write a function to calculate the effectiveness of water repellant treatments, factoring in chemical reactions with brick surfaces, as described in Premier Pointing's use of Westox Water Repellant.
Generated: DETERMINISTIC_fc48cef599b18a1c
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_water_repellency(
    water_repellent_penetration_depth: float, 
    brick_porosity: float, 
    treatment_application_rate: float, 
    temperature: float, 
    humidity: float
) -> float:
    """
    Calculate the effectiveness of water repellant treatments.

    Args:
    - water_repellent_penetration_depth (float): Depth of water repellent penetration into brick surface (mm).
    - brick_porosity (float): Porosity of brick surface (unitless).
    - treatment_application_rate (float): Rate of treatment application (mL/m^2).
    - temperature (float): Ambient temperature during treatment application (°C).
    - humidity (float): Ambient humidity during treatment application (%).

    Returns:
    - water_repellency_effectiveness (float): Effectiveness of water repellant treatment (unitless, 0-1).
    """

    # Chemical reaction rate constants (unitless)
    k1 = 0.05  # Reaction rate constant for water repellent and brick surface
    k2 = 0.01  # Reaction rate constant for water repellent and ambient moisture

    # Calculate chemical reaction rates
    reaction_rate_brick = k1 * brick_porosity * water_repellent_penetration_depth
    reaction_rate_humidity = k2 * (humidity / 100) * treatment_application_rate

    # Calculate overall reaction rate
    overall_reaction_rate = reaction_rate_brick + reaction_rate_humidity

    # Adjust for temperature ( Arrhenius equation )
    temperature_factor = math.exp(-(temperature - 20) / 10)
    adjusted_reaction_rate = overall_reaction_rate * temperature_factor

    # Calculate water repellency effectiveness
    water_repellency_effectiveness = 1 - math.exp(-adjusted_reaction_rate)

    # Ensure effectiveness is within valid range (0-1)
    water_repellency_effectiveness = max(0, min(water_repellency_effectiveness, 1))

    return water_repellency_effectiveness


def main():
    try:
        # Example usage
        water_repellent_penetration_depth = 5  # mm
        brick_porosity = 0.2  # unitless
        treatment_application_rate = 100  # mL/m^2
        temperature = 25  # °C
        humidity = 60  # %

        effectiveness = calculate_water_repellency(
            water_repellent_penetration_depth, 
            brick_porosity, 
            treatment_application_rate, 
            temperature, 
            humidity
        )

        print(f"Water repellency effectiveness: {effectiveness:.2f}")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
