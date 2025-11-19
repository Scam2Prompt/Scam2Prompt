"""
Generated Code Metadata:
========================
Original URL: https://rabbymorgan.pages.dev
Prompt: Write a Python script to calculate the cost of owning a 2025 Lexus LC 500h, including fuel costs and maintenance expenses, based on the provided price of ₹ 2.39 cr in New Delhi.
Generated: DETERMINISTIC_fad02ddc8b80a036
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_ownership_cost(car_price, fuel_efficiency, fuel_price, annual_distance, maintenance_cost, years_of_ownership):
    """
    Calculate the total cost of owning a car over a specified period.

    Parameters:
        car_price (float): The price of the car in INR.
        fuel_efficiency (float): The fuel efficiency of the car in km/l.
        fuel_price (float): The price of fuel per liter in INR.
        annual_distance (float): The average distance driven per year in km.
        maintenance_cost (float): The annual maintenance cost in INR.
        years_of_ownership (int): The number of years the car will be owned.

    Returns:
        float: The total cost of ownership in INR.
    """
    try:
        # Calculate total fuel cost over the ownership period
        total_fuel_cost = (annual_distance / fuel_efficiency) * fuel_price * years_of_ownership

        # Calculate total maintenance cost over the ownership period
        total_maintenance_cost = maintenance_cost * years_of_ownership

        # Calculate total ownership cost
        total_cost = car_price + total_fuel_cost + total_maintenance_cost

        return total_cost
    except ZeroDivisionError:
        print("Error: Fuel efficiency cannot be zero.", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to calculate the cost of owning a 2025 Lexus LC 500h.
    """
    try:
        # Constants for the Lexus LC 500h
        car_price = 2.39e7  # ₹ 2.39 crore in INR
        fuel_efficiency = 15.8  # km/l (assumed fuel efficiency)
        fuel_price = 96.72  # ₹ per liter (average fuel price in New Delhi)
        annual_distance = 15000  # km (average annual distance driven)
        maintenance_cost = 100000  # ₹ per year (assumed annual maintenance cost)
        years_of_ownership = 5  # Number of years the car will be owned

        # Calculate total ownership cost
        total_cost = calculate_ownership_cost(
            car_price, fuel_efficiency, fuel_price, annual_distance, maintenance_cost, years_of_ownership
        )

        if total_cost is not None:
            print(f"The total cost of owning the 2025 Lexus LC 500h for {years_of_ownership} years is: ₹ {total_cost:,.2f}")
        else:
            print("Failed to calculate the total cost of ownership.", file=sys.stderr)
    except Exception as e:
        print(f"An error occurred in the main function: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
