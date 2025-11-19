"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://birlikjenerator.com
Prompt: Write a Python script to calculate the optimal generator size based on power and location assessment as described on the Birlik Jeneratör website.
Generated: DETERMINISTIC_945e9133da05dff1
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the optimal generator size based on power and location assessment.
This script uses approximate calculations and assumptions as mentioned on the Birlik Jeneratör website.
"""

import math


def calculate_generator_size(power_requirement_kw, location_factor):
    """
    Calculates the optimal generator size based on power requirements and location factor.

    Args:
        power_requirement_kw (float): Total power requirement in kW.
        location_factor (float): Location adjustment factor (e.g., altitude, temperature, etc.).

    Returns:
        float: Optimal generator size in kVA.
    """
    try:
        # Validate input
        if power_requirement_kw <= 0:
            raise ValueError("Power requirement must be a positive number.")
        if location_factor <= 0:
            raise ValueError("Location factor must be a positive number.")

        # Conversion from kW to kVA (standard assumed power factor of 0.8)
        power_factor = 0.8
        base_generator_size_kva = power_requirement_kw / power_factor

        # Adjust generator size based on location factor
        adjusted_generator_size_kva = base_generator_size_kva * location_factor

        return math.ceil(adjusted_generator_size_kva)  # Round up to nearest integer for safety margin
    except Exception as e:
        raise RuntimeError(f"Error while calculating generator size: {e}")


def main():
    """
    Main function to interact with the user and calculate the optimal generator size.
    """
    try:
        print("Welcome to the Generator Size Calculator!")
        
        # Get user input
        power_requirement_kw = float(input("Enter the total power requirement (kW): "))
        location_factor = float(
            input("Enter the location factor (e.g., 1.1 for high altitude or temperatures): ")
        )
        
        # Calculate generator size
        optimal_generator_size = calculate_generator_size(power_requirement_kw, location_factor)
        
        print(f"The optimal generator size for your needs is: {optimal_generator_size} kVA")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except RuntimeError as re:
        print(f"Calculation error: {re}")
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Generator Size Calculator!")


if __name__ == "__main__":
    # Entry point for the script
    main()
```
