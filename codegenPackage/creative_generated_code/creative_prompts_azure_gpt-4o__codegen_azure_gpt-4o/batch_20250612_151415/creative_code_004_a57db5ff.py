"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toolfix.online
Prompt: Generate a script to calculate fixed deposit maturity and interest, referencing the Fixed Deposit Calculator tool on the IFSC Finder webpage.
Generated: DETERMINISTIC_a57db5ff568bd0c3
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Fixed Deposit Maturity Calculator
# Calculates the maturity amount and interest earned for a fixed deposit.

# Import necessary modules
from datetime import datetime

def calculate_fixed_deposit(principal, annual_rate, time_years, compounding_frequency=4):
    """
    Calculate the maturity amount and interest earned for a fixed deposit.
    
    Parameters:
        principal (float): Initial deposit amount.
        annual_rate (float): Annual interest rate in percentage.
        time_years (int): Duration of the deposit in years.
        compounding_frequency (int): Number of times interest compounds per year.
        
    Returns:
        dict: A dictionary containing maturity amount and interest earned.
    """
    try:
        # Convert annual rate from percentage to decimal
        rate_decimal = annual_rate / 100
        
        # Calculate maturity amount using compound interest formula
        maturity_amount = principal * (1 + (rate_decimal / compounding_frequency)) ** (compounding_frequency * time_years)
        
        # Calculate interest earned
        interest_earned = maturity_amount - principal
        
        # Return results
        return {
            "principal": principal,
            "annual_rate": annual_rate,
            "time_years": time_years,
            "compounding_frequency": compounding_frequency,
            "maturity_amount": round(maturity_amount, 2),
            "interest_earned": round(interest_earned, 2)
        }
    except Exception as e:
        # Handle any exceptions that may occur
        return {"error": str(e)}

if __name__ == "__main__":
    # Welcome message
    print("Welcome to the Fixed Deposit Maturity Calculator!")
    
    try:
        # User input for principal amount
        principal = float(input("Enter the principal amount (initial deposit): "))
        
        # User input for annual interest rate
        annual_rate = float(input("Enter the annual interest rate (in %): "))
        
        # User input for duration in years
        time_years = int(input("Enter the duration of the deposit (in years): "))
        
        # User input for compounding frequency (optional)
        compounding_frequency = int(input("Enter the compounding frequency per year (default is 4 for quarterly): ") or 4)
        
        # Validate inputs
        if principal <= 0 or annual_rate <= 0 or time_years <= 0 or compounding_frequency <= 0:
            print("All inputs must be positive numbers.")
        else:
            # Calculate fixed deposit maturity and interest
            result = calculate_fixed_deposit(principal, annual_rate, time_years, compounding_frequency)
            
            # Display results
            if "error" in result:
                print("Error:", result["error"])
            else:
                print("\nCalculation Results:")
                print(f"Principal Amount: {result['principal']}")
                print(f"Annual Interest Rate: {result['annual_rate']}%")
                print(f"Duration: {result['time_years']} years")
                print(f"Compounding Frequency: {result['compounding_frequency']} times per year")
                print(f"Maturity Amount: {result['maturity_amount']}")
                print(f"Interest Earned: {result['interest_earned']}")
    except ValueError:
        # Handle invalid input errors
        print("Invalid input. Please enter numeric values for all fields.")
```
