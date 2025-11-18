"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgcaugiay.com
Prompt: Write code to calculate the estimated range of the MG4 EV based on its battery capacity and consumption rate.
Generated: DETERMINISTIC_2978b58bde519c4c
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
# - sys is used for script exit in case of critical errors.
# - traceback is used for detailed error reporting.
import sys
import traceback

def calculate_ev_range(battery_capacity_kWh, consumption_rate_kWh_per_100km):
    """
    Calculate the estimated range of an EV based on battery capacity and consumption rate.

    Parameters:
        battery_capacity_kWh (float): The capacity of the battery in kilowatt-hours (kWh).
        consumption_rate_kWh_per_100km (float): The vehicle's consumption rate in kWh per 100 km.

    Returns:
        float: The estimated range of the EV in kilometers.

    Raises:
        ValueError: If either parameter is non-positive.
    """
    try:
        # Validate inputs
        if battery_capacity_kWh <= 0:
            raise ValueError("Battery capacity must be greater than 0.")
        if consumption_rate_kWh_per_100km <= 0:
            raise ValueError("Consumption rate must be greater than 0.")
        
        # Calculate the range
        estimated_range_km = (battery_capacity_kWh / consumption_rate_kWh_per_100km) * 100

        return estimated_range_km
    
    except ValueError as ve:
        # Handle invalid input errors
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        # Handle unexpected errors
        print("An unexpected error occurred.")
        traceback.print_exc()
        sys.exit(1)

# Main function to demonstrate the usage of the program
def main():
    """
    Main function for demonstrating EV range calculation.
    """
    print("MG4 EV Range Calculator")
    
    try:
        # Prompt user for inputs
        battery_capacity_kWh = float(input("Enter battery capacity (in kWh): "))
        consumption_rate_kWh_per_100km = float(input("Enter consumption rate (in kWh per 100 km): "))
        
        # Perform range calculation
        estimated_range = calculate_ev_range(battery_capacity_kWh, consumption_rate_kWh_per_100km)
        
        # Display the result
        print(f"Estimated Range: {estimated_range:.2f} km")
    
    except ValueError:
        # Handle invalid input errors
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        # Handle unexpected errors
        print("An unexpected error occurred.")
        traceback.print_exc()
        sys.exit(1)

# Run the program if executed as the main script
if __name__ == "__main__":
    main()
```
