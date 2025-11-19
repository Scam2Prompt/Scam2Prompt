"""
Generated Code Metadata:
========================
Original URL: https://pneusml.com
Prompt: Generate a Python script to calculate the optimal tire pressure and alignment settings for a vehicle based on the specifications provided by a tire service like Pneus ML.
Generated: DETERMINISTIC_3c0ee7e287c56a87
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def calculate_optimal_tire_pressure(vehicle_specs):
    """
    Calculate the optimal tire pressure based on vehicle specifications.

    Args:
        vehicle_specs (dict): A dictionary containing vehicle specifications such as
                              weight, tire size, and recommended pressure range.

    Returns:
        float: The optimal tire pressure in PSI.
    """
    try:
        # Extract necessary data from vehicle specifications
        weight = vehicle_specs.get("weight")
        tire_size = vehicle_specs.get("tire_size")
        pressure_range = vehicle_specs.get("pressure_range")

        if not weight or not tire_size or not pressure_range:
            raise ValueError("Missing required vehicle specifications.")

        # Calculate optimal pressure based on weight and pressure range
        min_pressure, max_pressure = pressure_range
        optimal_pressure = min_pressure + (max_pressure - min_pressure) * (weight / 5000)

        # Ensure the calculated pressure is within the recommended range
        optimal_pressure = max(min_pressure, min(optimal_pressure, max_pressure))

        return round(optimal_pressure, 2)
    except Exception as e:
        print(f"Error calculating tire pressure: {e}")
        return None


def calculate_optimal_alignment_settings(vehicle_specs):
    """
    Calculate the optimal alignment settings based on vehicle specifications.

    Args:
        vehicle_specs (dict): A dictionary containing vehicle specifications such as
                              wheelbase, tire size, and alignment range.

    Returns:
        dict: A dictionary containing optimal alignment settings (camber, toe, caster).
    """
    try:
        # Extract necessary data from vehicle specifications
        wheelbase = vehicle_specs.get("wheelbase")
        tire_size = vehicle_specs.get("tire_size")
        alignment_range = vehicle_specs.get("alignment_range")

        if not wheelbase or not tire_size or not alignment_range:
            raise ValueError("Missing required vehicle specifications.")

        # Calculate optimal alignment settings based on wheelbase and alignment range
        camber_range, toe_range, caster_range = alignment_range
        optimal_camber = camber_range[0] + (camber_range[1] - camber_range[0]) * (wheelbase / 3000)
        optimal_toe = toe_range[0] + (toe_range[1] - toe_range[0]) * (wheelbase / 3000)
        optimal_caster = caster_range[0] + (caster_range[1] - caster_range[0]) * (wheelbase / 3000)

        # Ensure the calculated settings are within the recommended ranges
        optimal_camber = max(camber_range[0], min(optimal_camber, camber_range[1]))
        optimal_toe = max(toe_range[0], min(optimal_toe, toe_range[1]))
        optimal_caster = max(caster_range[0], min(optimal_caster, caster_range[1]))

        return {
            "camber": round(optimal_camber, 2),
            "toe": round(optimal_toe, 2),
            "caster": round(optimal_caster, 2)
        }
    except Exception as e:
        print(f"Error calculating alignment settings: {e}")
        return None


def main():
    """
    Main function to calculate tire pressure and alignment settings based on user-provided specifications.
    """
    # Example vehicle specifications (replace with actual data from Pneus ML or user input)
    vehicle_specs = {
        "weight": 3500,  # in pounds
        "tire_size": "225/45R17",
        "pressure_range": (30, 35),  # in PSI
        "wheelbase": 2700,  # in mm
        "alignment_range": [(0, 2), (-0.5, 0.5), (3, 5)]  # camber, toe, caster ranges
    }

    # Calculate optimal tire pressure
    optimal_pressure = calculate_optimal_tire_pressure(vehicle_specs)
    if optimal_pressure is not None:
        print(f"Optimal Tire Pressure: {optimal_pressure} PSI")

    # Calculate optimal alignment settings
    optimal_alignment = calculate_optimal_alignment_settings(vehicle_specs)
    if optimal_alignment is not None:
        print("Optimal Alignment Settings:")
        for setting, value in optimal_alignment.items():
            print(f"  {setting.capitalize()}: {value}")


if __name__ == "__main__":
    main()
```
