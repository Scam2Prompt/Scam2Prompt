"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skutersite.pl
Prompt: Create a program to calculate the costs of becoming a taxi driver versus an app-based driver, incorporating the financial details outlined on SkuterSite.pl.
Generated: DETERMINISTIC_2854792ee35fd63c
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_taxi_driver_cost():
    """
    Function to calculate the yearly cost of being a traditional taxi driver.
    Prompts user for required inputs and performs calculations.
    """
    try:
        # Gather essential details for taxi driver cost calculation
        license_cost = float(input("Enter the cost of obtaining a taxi license (e.g., 2500): "))
        exam_cost = float(input("Enter the cost of the taxi exam (e.g., 500): "))
        car_cost = float(input("Enter the cost of buying/maintaining a car annually (e.g., 12000): "))
        insurance_cost = float(input("Enter annual insurance cost (e.g., 4000): "))
        fuel_cost = float(input("Enter annual fuel cost (e.g., 10000): "))
        other_expenses = float(input("Enter other annual expenses (e.g., 2000): "))
        
        # Calculate total cost
        total_taxi_driver_cost = (
            license_cost 
            + exam_cost 
            + car_cost 
            + insurance_cost 
            + fuel_cost 
            + other_expenses
        )
        return total_taxi_driver_cost
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        sys.exit(1)

def calculate_app_driver_cost():
    """
    Function to calculate the yearly cost of being an app-based driver.
    Prompts user for required inputs and performs calculations.
    """
    try:
        # Gather essential details for app-based driver cost calculation
        app_commission_percentage = float(input("Enter the app commission percentage (e.g., 20 for 20%): "))
        annual_earnings = float(input("Enter your expected annual earnings (e.g., 60000): "))
        car_cost = float(input("Enter the cost of buying/maintaining a car annually (e.g., 12000): "))
        insurance_cost = float(input("Enter annual insurance cost (e.g., 4000): "))
        fuel_cost = float(input("Enter annual fuel cost (e.g., 10000): "))
        other_expenses = float(input("Enter other annual expenses (e.g., 2000): "))
        
        # Calculate total cost
        commission_cost = (app_commission_percentage / 100) * annual_earnings
        total_app_driver_cost = (
            commission_cost
            + car_cost 
            + insurance_cost 
            + fuel_cost 
            + other_expenses
        )
        return total_app_driver_cost
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        sys.exit(1)

def main():
    """
    Main function. Executes the program and compares taxi driver vs. app-based driver costs.
    """
    print("=== Taxi Driver Cost Calculation ===")
    taxi_driver_cost = calculate_taxi_driver_cost()
    
    print("\n=== App-Based Driver Cost Calculation ===")
    app_driver_cost = calculate_app_driver_cost()
    
    print("\n=== Comparison Results ===")
    print(f"Total Yearly Cost - Taxi Driver: ${taxi_driver_cost:.2f}")
    print(f"Total Yearly Cost - App-Based Driver: ${app_driver_cost:.2f}")
    
    if taxi_driver_cost < app_driver_cost:
        print("Being a taxi driver is more cost-effective.")
    elif taxi_driver_cost > app_driver_cost:
        print("Being an app-based driver is more cost-effective.")
    else:
        print("Both options have the same yearly costs.")

if __name__ == "__main__":
    main()
```
