"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rehiletes.com
Prompt: Generate a script to calculate the total cost of multi-day excursions offered by "Rehiletes," including options for destinations like San Miguel de Allende and Veracruz.
Generated: DETERMINISTIC_f6e7c8102fa454ed
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the total cost of multi-day excursions offered by Rehiletes.
Destinations include San Miguel de Allende and Veracruz.
"""

# Import necessary modules
import sys

# Define excursion pricing and details
EXCURSIONS = {
    "San Miguel de Allende": {
        "price_per_day": 120,  # USD per day
        "max_days": 7         # Maximum number of days
    },
    "Veracruz": {
        "price_per_day": 100,  # USD per day
        "max_days": 5          # Maximum number of days
    }
}

def calculate_total_cost(destination, days):
    """
    Calculate the total cost of the excursion based on destination and days.
    
    Parameters:
        destination (str): The name of the destination.
        days (int): Number of days for the excursion.

    Returns:
        float: Total cost of the excursion.
    """
    # Validate destination
    if destination not in EXCURSIONS:
        raise ValueError(f"Invalid destination: {destination}. Available options: {', '.join(EXCURSIONS.keys())}")
    
    # Validate days
    if days <= 0 or days > EXCURSIONS[destination]['max_days']:
        raise ValueError(f"Invalid number of days: {days}. Allowed range for {destination}: 1-{EXCURSIONS[destination]['max_days']}")
    
    # Calculate total cost
    price_per_day = EXCURSIONS[destination]['price_per_day']
    total_cost = price_per_day * days
    
    return total_cost


def main():
    """
    Main function to handle user input and calculate excursion cost.
    """
    try:
        # Get user input for destination and number of days
        print("Welcome to Rehiletes Excursion Cost Calculator!")
        print(f"Available destinations: {', '.join(EXCURSIONS.keys())}")
        destination = input("Enter your destination: ").strip()
        days = int(input("Enter the number of days for your excursion: ").strip())
        
        # Calculate total cost
        total_cost = calculate_total_cost(destination, days)
        print(f"The total cost for your {days}-day excursion to {destination} is: ${total_cost:.2f}")
    
    except ValueError as ve:
        # Handle validation errors
        print(f"Error: {ve}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
