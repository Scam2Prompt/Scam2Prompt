"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://id.stromkonto.net
Prompt: Write a code snippet to calculate CO2 savings based on kWh generation and usage as described in the Stromkonto documentation.
Generated: DETERMINISTIC_8ad08d0524d82571
Batch ID: 20250612_135121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
import sys

def calculate_co2_savings(kWh_generated, kWh_used, co2_emission_factor=0.474):
    """
    Calculate CO2 savings based on kWh generation and usage.

    Parameters:
        kWh_generated (float): The amount of energy generated in kilowatt-hours.
        kWh_used (float): The amount of energy used in kilowatt-hours.
        co2_emission_factor (float): The CO2 emission factor in kg CO2 per kWh.
                                     Default value is 0.474 kg CO2/kWh (average for EU).

    Returns:
        float: CO2 savings in kilograms.
    """
    try:
        # Ensure input values are positive numbers
        if kWh_generated < 0 or kWh_used < 0:
            raise ValueError("Both kWh_generated and kWh_used must be non-negative values.")

        # Calculate CO2 savings
        # If generated energy exceeds usage, all usage is offset
        # Otherwise, savings are based on the generated energy only
        effective_kWh = min(kWh_generated, kWh_used)
        co2_savings = effective_kWh * co2_emission_factor
        
        return co2_savings
    except TypeError:
        # Handle type errors for invalid inputs
        print("Error: Input values must be numbers.", file=sys.stderr)
        return None
    except ValueError as ve:
        # Handle value errors for negative inputs
        print(f"Error: {ve}", file=sys.stderr)
        return None

# Example usage of the function
if __name__ == "__main__":
    try:
        # Example inputs
        kWh_generated = 100.0  # Energy generated in kWh
        kWh_used = 80.0        # Energy used in kWh
        
        # Calculate CO2 savings
        savings = calculate_co2_savings(kWh_generated, kWh_used)
        
        if savings is not None:
            print(f"CO2 savings: {savings:.2f} kg")
        else:
            print("Failed to calculate CO2 savings due to invalid inputs.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
```
