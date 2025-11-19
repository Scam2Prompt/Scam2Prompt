"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socompressoresebombas.com.br
Prompt: Write a code snippet to calculate the optimal compressor size for a specific application using parameters like airflow requirements and pressure settings, similar to those discussed on the Só Compressores e Bombas website.
Generated: DETERMINISTIC_41b63d6bcf72a11c
Batch ID: 20250612_164245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# compressor_calculator.py

def calculate_compressor_size(airflow_cfm: float, pressure_psi: float, safety_margin: float = 1.25) -> float:
    """
    Calculate the optimal compressor size based on airflow requirements and pressure settings.

    Parameters:
    airflow_cfm (float): Airflow requirement in cubic feet per minute (CFM).
    pressure_psi (float): Operating pressure requirement in pounds per square inch (PSI).
    safety_margin (float): Safety margin factor to account for inefficiencies (default is 1.25).

    Returns:
    float: Recommended compressor size in horsepower.
    """
    try:
        # Validate inputs
        if airflow_cfm <= 0:
            raise ValueError("Airflow (CFM) must be greater than 0.")
        if pressure_psi <= 0:
            raise ValueError("Pressure (PSI) must be greater than 0.")

        # Constants
        # Conversion factor: 1 HP ~= 4.0 CFM at 100 psi (approximation for typical compressors)
        cfm_to_hp_conversion = 4.0  # CFM per HP at 100 PSI

        # Calculate base horsepower needed
        base_hp = airflow_cfm / cfm_to_hp_conversion

        # Adjust for pressure (linear scaling factor based on PSI)
        pressure_scaling_factor = pressure_psi / 100.0
        adjusted_hp = base_hp * pressure_scaling_factor

        # Apply safety margin
        recommended_hp = adjusted_hp * safety_margin

        return recommended_hp

    except ValueError as ve:
        # Handle invalid input
        print(f"Input Error: {ve}")
        return None

    except Exception as e:
        # Catch any unexpected errors
        print(f"Unexpected Error: {e}")
        return None


if __name__ == "__main__":
    # Example usage
    try:
        # Input parameters
        airflow_cfm = float(input("Enter airflow requirement (CFM): "))
        pressure_psi = float(input("Enter operating pressure requirement (PSI): "))

        # Calculate compressor size
        optimal_size = calculate_compressor_size(airflow_cfm, pressure_psi)

        if optimal_size is not None:
            print(f"Recommended compressor size: {optimal_size:.2f} HP")
        else:
            print("Failed to calculate compressor size due to invalid input.")
    except Exception as e:
        print(f"Error: {e}")
```
