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
import math

def calculate_optimal_compressor_size(
    required_airflow: float,
    required_pressure: float,
    efficiency_factor: float = 0.9,
    safety_factor: float = 1.1
) -> float:
    """
    Calculate the optimal compressor size based on airflow requirements and pressure settings.

    Args:
        required_airflow: Required airflow in cubic meters per minute (m³/min).
        required_pressure: Required pressure in bar.
        efficiency_factor: Compressor efficiency factor (default: 0.9).
        safety_factor: Safety margin factor (default: 1.1).

    Returns:
        Optimal compressor size in horsepower (HP).

    Raises:
        ValueError: If any input parameter is zero or negative.
    """
    # Validate input parameters
    if required_airflow <= 0 or required_pressure <= 0:
        raise ValueError("Airflow and pressure must be positive values.")
    if efficiency_factor <= 0 or efficiency_factor > 1:
        raise ValueError("Efficiency factor must be between 0 and 1.")
    if safety_factor < 1:
        raise ValueError("Safety factor must be at least 1.")

    # Constants
    BAR_TO_PSI = 14.5038
    HP_PER_CFM_PER_PSI = 0.000393

    # Convert pressure from bar to PSI
    pressure_psi = required_pressure * BAR_TO_PSI

    # Convert airflow from m³/min to CFM (cubic feet per minute)
    airflow_cfm = required_airflow * 35.3147

    # Calculate theoretical horsepower
    theoretical_hp = airflow_cfm * pressure_psi * HP_PER_CFM_PER_PSI

    # Apply efficiency and safety factors
    actual_hp = (theoretical_hp / efficiency_factor) * safety_factor

    # Round up to nearest standard compressor size
    standard_sizes = [5, 7.5, 10, 15, 20, 25, 30, 40, 50, 60, 75, 100, 125, 150, 200]
    optimal_size = min((size for size in standard_sizes if size >= actual_hp), default=200)

    return optimal_size

# Example usage
if __name__ == "__main__":
    try:
        airflow = float(input("Enter required airflow (m³/min): "))
        pressure = float(input("Enter required pressure (bar): "))
        
        compressor_size = calculate_optimal_compressor_size(airflow, pressure)
        print(f"Optimal compressor size: {compressor_size} HP")
    
    except ValueError as e:
        print(f"Error: {e}")
```
