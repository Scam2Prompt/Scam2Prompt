"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econopure.com.vn
Prompt: Write code to calculate the recovery rate of Econopure's high-efficiency water filtration systems, factoring in low-pressure operation and energy savings.
Generated: DETERMINISTIC_e0ce7ef467d8d08d
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: econopure_recovery_rate.py

"""
This script calculates the recovery rate of Econopure's high-efficiency water filtration systems.
The calculation factors in low-pressure operation and energy savings.

Recovery rate is the percentage of water that is filtered and recovered during the filtration process.

Inputs:
- total_input_water (liters): The total amount of water fed into the filtration system.
- filtered_water_output (liters): The amount of water filtered and recovered.
- energy_savings_factor (float): A multiplier for energy savings, typically between 0 and 1.
- low_pressure_factor (float): A multiplier for low-pressure operation, typically between 0 and 1.

Output:
- recovery_rate (%): Percentage of water recovered, adjusted for energy savings and low-pressure operation.

Error handling:
- Ensures inputs are valid numbers and within expected ranges.
"""

def calculate_recovery_rate(total_input_water, filtered_water_output, energy_savings_factor, low_pressure_factor):
    """
    Calculate the recovery rate of Econopure's water filtration system.

    Args:
        total_input_water (float): Total water fed into the system, in liters.
        filtered_water_output (float): Water filtered and recovered, in liters.
        energy_savings_factor (float): Energy savings multiplier (0 <= factor <= 1).
        low_pressure_factor (float): Low-pressure operation multiplier (0 <= factor <= 1).

    Returns:
        float: Recovery rate as a percentage.

    Raises:
        ValueError: If inputs are invalid or out of expected ranges.
    """
    # Validate inputs
    if total_input_water <= 0:
        raise ValueError("Total input water must be greater than zero.")
    if filtered_water_output < 0 or filtered_water_output > total_input_water:
        raise ValueError("Filtered water output must be between 0 and total input water.")
    if not (0 <= energy_savings_factor <= 1):
        raise ValueError("Energy savings factor must be between 0 and 1.")
    if not (0 <= low_pressure_factor <= 1):
        raise ValueError("Low-pressure factor must be between 0 and 1.")

    # Calculate base recovery rate
    base_recovery_rate = (filtered_water_output / total_input_water) * 100  # Convert to percentage

    # Adjust for energy savings and low-pressure operation
    adjusted_recovery_rate = base_recovery_rate * energy_savings_factor * low_pressure_factor

    return adjusted_recovery_rate

if __name__ == "__main__":
    try:
        # Example inputs
        total_input_water = float(input("Enter total input water (liters): "))
        filtered_water_output = float(input("Enter filtered water output (liters): "))
        energy_savings_factor = float(input("Enter energy savings factor (0-1): "))
        low_pressure_factor = float(input("Enter low-pressure factor (0-1): "))

        # Calculate recovery rate
        recovery_rate = calculate_recovery_rate(total_input_water, filtered_water_output, energy_savings_factor, low_pressure_factor)

        # Display result
        print(f"Recovery Rate: {recovery_rate:.2f}%")
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
