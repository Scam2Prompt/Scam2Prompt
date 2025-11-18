"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suzuki-capital.com
Prompt: Write a Python script to calculate the cost of exchanging an old Suzuki car for a new one, incorporating features from Suzuki Capital Motors' Certified Used Car Program, such as free evaluation and up to one-year warranty.
Generated: DETERMINISTIC_c55ba55f4a4638c5
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def evaluate_car_value(make, model, year, mileage):
    """
    Evaluate the value of an old car based on its make, model, year, and mileage. 
    For simplicity, this is a mock evaluation.
    
    Args:
        make (str): Car manufacturer name (e.g., "Suzuki").
        model (str): Car model name.
        year (int): Manufacturing year of the car.
        mileage (int): Mileage of the car in kilometers.

    Returns:
        float: Estimated value of the car in USD.
    """
    try:
        base_value = 10000  # Base value of the car in USD
        depreciation_rate = 0.15  # Annual depreciation rate (15%)
        mileage_deduction_per_km = 0.02  # Deduction per km driven in USD
        
        # Calculate depreciation based on the car's age
        current_year = 2023
        age = current_year - year
        if age < 0:
            raise ValueError("Invalid year provided. Year cannot be in the future.")
        
        depreciated_value = base_value * ((1 - depreciation_rate) ** age)
        
        # Calculate deduction based on mileage
        mileage_deduction = mileage * mileage_deduction_per_km
        estimated_value = max(depreciated_value - mileage_deduction, 0)  # Ensure value is non-negative
        
        return estimated_value
    except Exception as e:
        print(f"An error occurred during car evaluation: {e}")
        sys.exit(1)


def calculate_exchange_cost(new_car_price, old_car_value, warranty_cost=500):
    """
    Calculate the cost of exchanging an old car for a new one.

    Args:
        new_car_price (float): Price of the new car in USD.
        old_car_value (float): Value of the old car in USD (as evaluated).
        warranty_cost (float): Cost of the up-to-one-year warranty (default is $500).

    Returns:
        float: Total exchange cost in USD.
    """
    try:
        if new_car_price < 0 or old_car_value < 0 or warranty_cost < 0:
            raise ValueError("Prices and costs must be non-negative.")
        
        # Subtract old car value and add warranty cost
        exchange_cost = new_car_price - old_car_value + warranty_cost
        
        return exchange_cost
    except Exception as e:
        print(f"An error occurred during cost calculation: {e}")
        sys.exit(1)


def main():
    """
    Main function to execute the car exchange cost calculation.
    """
    print("Welcome to Suzuki Capital Motors' Certified Used Car Program!")
    
    try:
        # Get user input for old car details
        make = input("Enter the make of your old car (e.g., 'Suzuki'): ").strip()
        model = input("Enter the model of your old car: ").strip()
        year = int(input("Enter the manufacturing year of your old car: ").strip())
        mileage = int(input("Enter the mileage of your old car (in kilometers): ").strip())

        # Evaluate the old car's value
        old_car_value = evaluate_car_value(make, model, year, mileage)
        print(f"Estimated value of your old car: ${old_car_value:.2f}")
        
        # Get user input for new car price
        new_car_price = float(input("Enter the price of the new Suzuki car you want to purchase: ").strip())
        
        # Calculate exchange cost
        exchange_cost = calculate_exchange_cost(new_car_price, old_car_value)
        print(f"The total cost of exchanging your old car for the new one is: ${exchange_cost:.2f}")
        
        print("Note: This includes an up-to-one-year warranty.")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
