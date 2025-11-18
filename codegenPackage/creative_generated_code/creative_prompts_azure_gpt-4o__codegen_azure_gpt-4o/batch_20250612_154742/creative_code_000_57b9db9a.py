"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bestholidaysallindia.com
Prompt: Write a Python script to calculate the cost of a taxi ride based on the rates provided on the "Best Holidays All India" website, including options for different vehicle types like Innova Crysta, Fortuner, and Swift Desire.
Generated: DETERMINISTIC_57b9db9aef1e56ba
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Taxi Fare Calculator

This script calculates the cost of a taxi ride based on predefined rates for different vehicle types.
Vehicle rates are sourced from the 'Best Holidays All India' website.
"""

# Import necessary modules
import sys

# Define taxi rates per kilometer for different vehicle types
TAXI_RATES = {
    "Innova Crysta": 18,  # Rate per km in INR
    "Fortuner": 25,       # Rate per km in INR
    "Swift Desire": 12    # Rate per km in INR
}

def calculate_taxi_fare(vehicle_type, distance_in_km):
    """
    Calculate the cost of a taxi ride.
    
    Parameters:
        vehicle_type (str): The type of vehicle selected (e.g., "Innova Crysta").
        distance_in_km (float): The distance of the ride in kilometers.
    
    Returns:
        float: The total cost of the ride.
    """
    try:
        # Validate the vehicle type
        if vehicle_type not in TAXI_RATES:
            raise ValueError(f"Invalid vehicle type: {vehicle_type}. Choose from {', '.join(TAXI_RATES.keys())}.")
        
        # Validate the distance
        if distance_in_km <= 0:
            raise ValueError("Distance must be a positive number.")
        
        # Calculate the total fare
        rate_per_km = TAXI_RATES[vehicle_type]
        total_fare = rate_per_km * distance_in_km
        return total_fare
    
    except ValueError as ve:
        print(f"Error: {ve}")
        return None

def main():
    """
    Main function to interact with the user and calculate the taxi fare.
    """
    print("Welcome to the Taxi Fare Calculator!")
    print("Available Vehicle Types: Innova Crysta, Fortuner, Swift Desire")
    
    # Get user input for vehicle type
    vehicle_type = input("Enter the vehicle type: ").strip()
    
    # Get user input for distance
    try:
        distance_in_km = float(input("Enter the distance in kilometers: ").strip())
    except ValueError:
        print("Error: Distance must be a numeric value.")
        sys.exit(1)
    
    # Calculate the fare
    total_fare = calculate_taxi_fare(vehicle_type, distance_in_km)
    
    if total_fare is not None:
        print(f"The total fare for a {vehicle_type} ride of {distance_in_km:.2f} km is: ₹{total_fare:.2f}")
    else:
        print("Failed to calculate the fare due to invalid inputs.")

if __name__ == "__main__":
    main()
```
