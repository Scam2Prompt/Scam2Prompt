"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgcaugiay.com
Prompt: Generate code to calculate the fuel consumption of an MG car model (e.g., NSE 1.5L engine with 5.3L/100km) over a given distance in kilometers.
Generated: DETERMINISTIC_b6c9e18abfd8dcaf
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate fuel consumption for an MG car model over a given distance.

def calculate_fuel_consumption(fuel_efficiency, distance):
    """
    Calculate fuel consumption based on fuel efficiency and distance.

    Args:
        fuel_efficiency (float): Fuel efficiency in liters per 100 kilometers (L/100km).
        distance (float): Distance traveled in kilometers.

    Returns:
        float: Fuel consumption in liters.
    """
    try:
        # Ensure valid inputs
        if fuel_efficiency <= 0 or distance < 0:
            raise ValueError("Fuel efficiency must be positive and distance must be non-negative.")

        # Calculate fuel consumption
        fuel_consumed = (fuel_efficiency / 100) * distance
        return fuel_consumed

    except TypeError:
        raise TypeError("Both fuel_efficiency and distance must be numbers.")
    except ValueError as ve:
        raise ve


def main():
    """
    Main function to get user inputs and calculate fuel consumption.
    """
    try:
        # Example car details: MG NSE 1.5L engine with 5.3 liters per 100 km
        fuel_efficiency = 5.3  # L/100km

        # Get distance from user
        distance = float(input("Enter the distance traveled (in kilometers): "))

        # Calculate fuel consumption
        fuel_consumed = calculate_fuel_consumption(fuel_efficiency, distance)

        # Display the result
        print(f"The fuel consumption over {distance} km is approximately {fuel_consumed:.2f} liters.")

    except ValueError:
        print("Invalid input. Please enter a valid number for the distance.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
