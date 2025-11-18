"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelinjectorservices.com.au
Prompt: Develop a program that categorizes fuel injectors by type (mechanical, electronic, petrol, diesel) and generates a maintenance schedule based on the cleaning process outlined on the Fuel Injector Services website.
Generated: DETERMINISTIC_7fa7fb60251b861f
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

# Define constants for fuel injector types and their maintenance intervals
FUEL_INJECTOR_TYPES = {
    "mechanical": {"maintenance_interval_days": 180},
    "electronic": {"maintenance_interval_days": 365},
    "petrol": {"maintenance_interval_days": 120},
    "diesel": {"maintenance_interval_days": 240}
}

# Exception classes for validation errors
class InvalidFuelInjectorTypeError(Exception):
    """Raised when an invalid fuel injector type is provided."""
    pass

# Function to categorize fuel injectors and generate a maintenance schedule
def generate_maintenance_schedule(fuel_injector_type, last_cleaning_date):
    """
    Categorizes the fuel injector and generates a maintenance schedule.
    
    Args:
        fuel_injector_type (str): Type of the fuel injector (mechanical, electronic, petrol, diesel).
        last_cleaning_date (str): Date of last cleaning in YYYY-MM-DD format.
    
    Returns:
        dict: Maintenance schedule with next cleaning date and injector type.
    
    Raises:
        InvalidFuelInjectorTypeError: If the fuel injector type is invalid.
        ValueError: If the last cleaning date is not in the correct format.
    """
    # Validate fuel injector type
    if fuel_injector_type not in FUEL_INJECTOR_TYPES:
        raise InvalidFuelInjectorTypeError(f"Invalid fuel injector type: {fuel_injector_type}. Valid types are: {', '.join(FUEL_INJECTOR_TYPES.keys())}")
    
    # Validate and parse last cleaning date
    try:
        last_cleaning = datetime.datetime.strptime(last_cleaning_date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    
    # Calculate next cleaning date based on maintenance interval
    maintenance_interval = FUEL_INJECTOR_TYPES[fuel_injector_type]["maintenance_interval_days"]
    next_cleaning_date = last_cleaning + datetime.timedelta(days=maintenance_interval)
    
    # Return maintenance schedule
    return {
        "injector_type": fuel_injector_type,
        "last_cleaning_date": str(last_cleaning),
        "next_cleaning_date": str(next_cleaning_date)
    }

# Main function to interact with the program
def main():
    """
    Main function to interact with the program.
    """
    print("Fuel Injector Maintenance Scheduler")
    print("------------------------------------")
    
    try:
        # Get user input
        fuel_injector_type = input("Enter the fuel injector type (mechanical, electronic, petrol, diesel): ").strip().lower()
        last_cleaning_date = input("Enter the last cleaning date (YYYY-MM-DD): ").strip()
        
        # Generate and display the maintenance schedule
        schedule = generate_maintenance_schedule(fuel_injector_type, last_cleaning_date)
        print("\nGenerated Maintenance Schedule:")
        print(f"Injector Type: {schedule['injector_type']}")
        print(f"Last Cleaning Date: {schedule['last_cleaning_date']}")
        print(f"Next Cleaning Date: {schedule['next_cleaning_date']}")
    except (InvalidFuelInjectorTypeError, ValueError) as e:
        # Handle errors gracefully
        print(f"Error: {e}")
    except Exception as e:
        # Catch unexpected errors
        print(f"An unexpected error occurred: {e}")

# Entry point for the program
if __name__ == "__main__":
    main()
```
