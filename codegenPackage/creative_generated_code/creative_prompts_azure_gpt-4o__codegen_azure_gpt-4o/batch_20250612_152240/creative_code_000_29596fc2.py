"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neumayaa.com.ar
Prompt: Write Python code to calculate TKPH (Toneladas Kilómetros por Hora) for a specific tire based on its load capacity, distance traveled, and ambient temperature, as described on the Neumayaa website.
Generated: DETERMINISTIC_29596fc20d98303d
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import logging

# Configure logging for error handling and debugging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def calculate_tkph(load_capacity, distance_traveled, ambient_temperature):
    """
    Calculate TKPH (Toneladas Kilómetros por Hora) based on the given parameters.

    TKPH formula (generalized from industry standards):
    TKPH = (Load Capacity * Distance Traveled) / Adjustment Factor

    Adjustment Factor is derived based on ambient temperature.
    This factor reduces TKPH for higher temperatures to account for tire wear.

    Parameters:
        load_capacity (float): The load capacity of the tire in tons.
        distance_traveled (float): The distance traveled by the tire in kilometers.
        ambient_temperature (float): The ambient temperature in degrees Celsius.

    Returns:
        float: Calculated TKPH value.

    Raises:
        ValueError: If any input is not a positive number.
    """
    # Validate input
    if load_capacity <= 0:
        raise ValueError("Load capacity must be a positive number.")
    if distance_traveled <= 0:
        raise ValueError("Distance traveled must be a positive number.")
    if ambient_temperature < -50 or ambient_temperature > 70:
        raise ValueError("Ambient temperature must be within a practical range (-50 to 70°C).")

    # Define adjustment factor based on industry standards
    # Higher temperatures reduce the TKPH rating due to increased tire wear
    if ambient_temperature <= 25:
        adjustment_factor = 1.0  # No reduction for temperatures below or equal to 25°C
    elif ambient_temperature <= 40:
        adjustment_factor = 1.2  # Moderate reduction
    else:
        adjustment_factor = 1.5  # Significant reduction for high temperatures

    # Calculate TKPH
    tkph = (load_capacity * distance_traveled) / adjustment_factor

    return tkph


def main():
    """
    Main function to demonstrate TKPH calculation.
    """
    try:
        # Example inputs
        load_capacity = float(input("Enter tire load capacity in tons: "))
        distance_traveled = float(input("Enter distance traveled in kilometers: "))
        ambient_temperature = float(input("Enter ambient temperature in °C: "))

        # Calculate TKPH
        tkph_result = calculate_tkph(load_capacity, distance_traveled, ambient_temperature)
        logging.info(f"Calculated TKPH: {tkph_result:.2f}")
    except ValueError as e:
        logging.error(f"Input error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
