"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramjiacro.com
Prompt: Write a program that calculates the production output of acrylic yarns based on machine efficiency and operating hours, using data inputs like yarn type and machinery specifications.
Generated: DETERMINISTIC_12b2e746741475e4
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to calculate the production output of acrylic yarns based on machine efficiency and operating hours
# Written in Python

# Import required modules
import sys

def calculate_production(yarn_type, machine_efficiency, operating_hours):
    """
    Calculates production output based on the yarn type, machine efficiency, and operating hours.

    Args:
        yarn_type (str): Type of acrylic yarn (e.g., "Type A", "Type B", "Type C").
        machine_efficiency (float): Efficiency of the machine as a percentage (e.g., 85.5 for 85.5%).
        operating_hours (float): Number of hours the machine operates.

    Returns:
        float: Production output in kilograms (kg).
    """

    # Yarn production rate per hour based on yarn type (in kg/hour)
    yarn_production_rates = {
        "Type A": 50.0,  # Example: Type A produces 50 kg/hour
        "Type B": 45.0,  # Example: Type B produces 45 kg/hour
        "Type C": 40.0   # Example: Type C produces 40 kg/hour
    }

    # Validate yarn type
    if yarn_type not in yarn_production_rates:
        raise ValueError(f"Invalid yarn type: {yarn_type}. Valid options are {list(yarn_production_rates.keys())}.")

    # Validate machine efficiency
    if not (0 <= machine_efficiency <= 100):
        raise ValueError("Machine efficiency must be between 0 and 100 (inclusive).")

    # Validate operating hours
    if operating_hours < 0:
        raise ValueError("Operating hours must be non-negative.")

    # Get the production rate for the given yarn type
    production_rate = yarn_production_rates[yarn_type]

    # Calculate production output
    production_output = (production_rate * machine_efficiency / 100) * operating_hours

    return production_output


def main():
    """
    Main function to handle user input and calculate production output.
    """
    try:
        # Input from the user
        print("=== Acrylic Yarn Production Calculator ===")
        yarn_type = input("Enter yarn type (Type A, Type B, Type C): ").strip()
        machine_efficiency = float(input("Enter machine efficiency (as a percentage, e.g., 85.5): "))
        operating_hours = float(input("Enter operating hours: "))

        # Calculate production output
        production_output = calculate_production(yarn_type, machine_efficiency, operating_hours)

        # Display the result
        print(f"\nProduction Output:")
        print(f"Yarn Type: {yarn_type}")
        print(f"Machine Efficiency: {machine_efficiency}%")
        print(f"Operating Hours: {operating_hours} hours")
        print(f"Calculated Production Output: {production_output:.2f} kg")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


# Entry point of the program
if __name__ == "__main__":
    main()
```
