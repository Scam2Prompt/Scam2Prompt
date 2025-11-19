"""
Generated Code Metadata:
========================
Original URL: https://socompressoresebombas.com.br
Prompt: Write a code snippet to calculate the optimal compressor size for a specific application using parameters like airflow requirements and pressure settings, similar to those discussed on the Só Compressores e Bombas website.
Generated: DETERMINISTIC_41b63d6bcf72a11c
Batch ID: 20250612_164245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import math

def calculate_compressor_size(airflow, pressure, safety_factor=1.25):
    """
    Calculate the optimal compressor size based on airflow requirements and pressure settings.

    Parameters:
        airflow (float): Airflow requirement in cubic feet per minute (CFM).
        pressure (float): Pressure requirement in pounds per square inch (PSI).
        safety_factor (float): Safety factor to account for inefficiencies (default is 1.25).

    Returns:
        float: Optimal compressor size in horsepower (HP).
    """
    try:
        # Validate inputs
        if airflow <= 0 or pressure <= 0 or safety_factor <= 0:
            raise ValueError("Airflow, pressure, and safety factor must be positive values.")

        # Constants
        # Conversion factor: 1 HP = 4.714 CFM * PSI
        conversion_factor = 4.714

        # Calculate compressor size
        compressor_size = (airflow * pressure * safety_factor) / conversion_factor

        return round(compressor_size, 2)  # Return the result rounded to 2 decimal places

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Input parameters
        airflow = float(input("Enter airflow requirement (CFM): "))
        pressure = float(input("Enter pressure requirement (PSI): "))
        safety_factor = float(input("Enter safety factor (default is 1.25): ") or 1.25)

        # Calculate and display the result
        optimal_size = calculate_compressor_size(airflow, pressure, safety_factor)
        if optimal_size:
            print(f"The optimal compressor size is: {optimal_size} HP")
    except ValueError:
        print("Please enter valid numeric values for the inputs.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
