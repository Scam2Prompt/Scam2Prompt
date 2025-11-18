"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neumayaa.com.ar
Prompt: Generate code to calculate the optimal tire pressure for various heavy machinery types, incorporating Neumayaa's guidance on nitrogen inflation and regular pressure checks.
Generated: DETERMINISTIC_eb1285e3ae5e92c7
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Optimal Tire Pressure Calculator for Heavy Machinery

# Import necessary modules
import logging

# Initialize logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Dictionary to store recommended tire pressure ranges for heavy machinery (in PSI)
# These values are illustrative and should be replaced with real-world recommendations
TIRE_PRESSURE_RANGES = {
    "Excavator": (30, 35),
    "Bulldozer": (25, 30),
    "Forklift": (45, 50),
    "Loader": (40, 45),
    "Dump Truck": (50, 55),
}

# Nitrogen inflation adjustment factor (Neumayaa's guidance suggests nitrogen stabilizes pressure)
# Add a small factor to adjust recommended pressure for better nitrogen inflation stability
NITROGEN_ADJUSTMENT_FACTOR = 1.02  # = 2% increase for optimal inflation

def calculate_optimal_tire_pressure(vehicle_type, regular_pressure):
    """
    Calculate the optimal tire pressure for a given heavy machinery type based on regular pressure
    and nitrogen inflation adjustment.

    Args:
        vehicle_type (str): Type of heavy machinery (e.g., "Excavator", "Bulldozer").
        regular_pressure (float): Regular tire pressure as measured in PSI.

    Returns:
        float: Optimal tire pressure after adjustment.
        
    Raises:
        ValueError: If the vehicle type is not recognized or the pressure is out of range.
    """
    if vehicle_type not in TIRE_PRESSURE_RANGES:
        raise ValueError(f"Invalid vehicle type: {vehicle_type}. Supported types are {list(TIRE_PRESSURE_RANGES.keys())}")

    min_pressure, max_pressure = TIRE_PRESSURE_RANGES[vehicle_type]
    if not (min_pressure <= regular_pressure <= max_pressure):
        raise ValueError(
            f"Regular pressure {regular_pressure} PSI is out of range for {vehicle_type}. "
            f"Expected range: {min_pressure}-{max_pressure} PSI."
        )

    # Apply nitrogen adjustment factor to calculate optimal pressure
    optimal_pressure = regular_pressure * NITROGEN_ADJUSTMENT_FACTOR
    return round(optimal_pressure, 2)

def main():
    """
    Main function to interact with the user and perform tire pressure calculations.
    """
    logging.info("Welcome to the Heavy Machinery Tire Pressure Optimizer!")

    try:
        # Get user input for vehicle type and regular pressure
        vehicle_type = input("Enter the type of heavy machinery (e.g., Excavator, Bulldozer): ").strip()
        regular_pressure = float(input("Enter the measured tire pressure in PSI: ").strip())

        # Calculate the optimal tire pressure
        optimal_pressure = calculate_optimal_tire_pressure(vehicle_type, regular_pressure)

        # Display results
        logging.info(f"Optimal tire pressure for {vehicle_type}: {optimal_pressure} PSI")

    except ValueError as ve:
        logging.error(f"Input error: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
