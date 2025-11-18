"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aprisacv.com.mx
Prompt: Generate a Python script to calculate the lifespan of Aprick MgO-C refractory bricks in steel ladles, considering their carbon content and operational temperature.
Generated: DETERMINISTIC_65758dd0c1100209
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the lifespan of Aprick MgO-C refractory bricks in steel ladles.
Factors considered:
1. Carbon content (%)
2. Operational temperature (°C)

The formula used for lifespan calculation is hypothetical for demonstration purposes.
Please replace it with actual scientific or empirical formulae as applicable.

Author: Expert Programmer
"""

def calculate_lifespan(carbon_content_percentage, operational_temperature):
    """
    Calculate the lifespan of MgO-C refractory bricks.

    Parameters:
        carbon_content_percentage (float): Carbon content as a percentage (0 - 100).
        operational_temperature (float): Operational temperature in degrees Celsius.

    Returns:
        float: Estimated lifespan in hours.

    Raises:
        ValueError: If inputs are out of realistic ranges.
    """
    # Validate input ranges
    if not (0 <= carbon_content_percentage <= 100):
        raise ValueError("Carbon content percentage must be between 0 and 100.")
    if operational_temperature <= 0:
        raise ValueError("Operational temperature must be greater than 0°C.")
    
    # Hypothetical formula for calculating lifespan
    # Lifespan decreases with increasing operational temperature and increases with higher carbon content
    lifespan = (carbon_content_percentage * 0.5) / (operational_temperature * 0.01)
    return lifespan


def main():
    """
    Main function to interact with the user and calculate the lifespan of MgO-C bricks.
    """
    print("Aprick MgO-C Refractory Brick Lifespan Calculator")
    print("------------------------------------------------")

    try:
        # Request inputs from the user
        carbon_content_percentage = float(input("Enter the carbon content percentage (0-100): "))
        operational_temperature = float(input("Enter the operational temperature (°C): "))

        # Calculate lifespan
        lifespan = calculate_lifespan(carbon_content_percentage, operational_temperature)

        # Display result
        print(f"Estimated lifespan of refractory bricks: {lifespan:.2f} hours")

    except ValueError as ve:
        # Handle invalid input errors
        print(f"Input error: {ve}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
