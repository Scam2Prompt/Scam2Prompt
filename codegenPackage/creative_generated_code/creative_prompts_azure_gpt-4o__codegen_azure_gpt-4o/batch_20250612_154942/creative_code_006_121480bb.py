"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://libertyaid.co
Prompt: Write a script to calculate auto insurance APR rates as low as $19/month, using sample data provided by Liberty Aid's Auto Shield+ feature.
Generated: DETERMINISTIC_121480bb6967963e
Batch ID: 20250612_154942
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# auto_insurance_apr.py

"""
This script calculates auto insurance APR rates using sample data provided by Liberty Aid's Auto Shield+ feature.
The rates are calculated as low as $19/month based on predefined sample data and factors such as age, 
vehicle type, and driving history.

Author: [Your Name]
Date: [Today's Date]
"""

# Import necessary libraries
import sys

def calculate_apr_rate(age, vehicle_type, driving_history):
    """
    Calculate the APR rate based on age, vehicle type, and driving history.
    
    Args:
        age (int): Age of the driver.
        vehicle_type (str): Type of the vehicle (e.g., "sedan", "SUV", "truck").
        driving_history (str): Driving history (e.g., "clean", "minor violations", "major violations").
    
    Returns:
        float: Monthly APR rate in dollars.
    """
    # Define base rate
    base_rate = 19.0  # Minimum base rate in dollars per month
    
    # Adjust rate based on age
    if age < 25:
        base_rate *= 1.3  # Young drivers typically pay more
    elif age > 60:
        base_rate *= 0.9  # Senior drivers may receive discounts
    
    # Adjust rate based on vehicle type
    if vehicle_type.lower() == "suv":
        base_rate *= 1.2  # SUVs may have higher rates
    elif vehicle_type.lower() == "truck":
        base_rate *= 1.1  # Trucks may have slightly higher rates
    
    # Adjust rate based on driving history
    if driving_history.lower() == "minor violations":
        base_rate *= 1.5  # Penalty for minor violations
    elif driving_history.lower() == "major violations":
        base_rate *= 2.0  # Penalty for major violations
    
    # Ensure the rate doesn't fall below the minimum threshold
    return max(base_rate, 19.0)

def main():
    """
    Main function to calculate APR rates using user input.
    """
    print("Welcome to Liberty Aid's Auto Insurance APR Calculator!")
    
    try:
        # Get user input
        age = int(input("Enter your age: ").strip())
        if age <= 0:
            raise ValueError("Age must be a positive integer.")
        
        vehicle_type = input("Enter your vehicle type (e.g., sedan, SUV, truck): ").strip()
        if not vehicle_type:
            raise ValueError("Vehicle type must not be empty.")
        
        driving_history = input("Enter your driving history (e.g., clean, minor violations, major violations): ").strip()
        if not driving_history:
            raise ValueError("Driving history must not be empty.")
        
        # Calculate APR rate
        apr_rate = calculate_apr_rate(age, vehicle_type, driving_history)
        
        # Display the calculated rate
        print(f"Your estimated monthly APR rate is: ${apr_rate:.2f}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
