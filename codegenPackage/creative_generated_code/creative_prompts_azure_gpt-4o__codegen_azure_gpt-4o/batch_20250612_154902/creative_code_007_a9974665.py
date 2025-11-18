"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cotidashboard.com
Prompt: Write a function to simulate $COTI deposit growth over time based on the Max APY (Base + Boost) provided by the COTI Treasury.
Generated: DETERMINISTIC_a9974665721db70d
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math


def simulate_coti_deposit_growth(initial_deposit, annual_percentage_yield, years):
    """
    Simulates COTI deposit growth over time based on the provided APY.
    
    Parameters:
        initial_deposit (float): The initial amount deposited in COTI Treasury.
        annual_percentage_yield (float): The annual percentage yield (APY) in percentage. 
                                         Includes base and boost.
        years (int): The number of years for which the deposit will grow.
    
    Returns:
        list: A list of dictionaries, where each dictionary contains the year and 
              the total balance at the end of that year.
    """
    # Input validation to ensure parameters are correct
    if initial_deposit <= 0:
        raise ValueError("Initial deposit must be greater than zero.")
    if annual_percentage_yield <= 0:
        raise ValueError("APY must be greater than zero.")
    if years <= 0:
        raise ValueError("Years must be greater than zero.")
    
    # Convert APY from percentage to a decimal for calculations
    apy_decimal = annual_percentage_yield / 100
    
    # Initialize results list
    growth_results = []
    
    # Perform yearly compound interest calculation
    for year in range(1, years + 1):
        # Balance calculation using the compound interest formula: A = P * (1 + r)^t
        total_balance = initial_deposit * math.pow((1 + apy_decimal), year)
        growth_results.append({
            'Year': year,
            'Balance': round(total_balance, 2)  # Rounded for readability
        })
    
    return growth_results


# Example usage:
if __name__ == "__main__":
    try:
        initial_deposit = 1000.0  # $1000 initial deposit
        apy = 12.5  # 12.5% APY
        years = 5  # Simulate growth over 5 years
        
        # Run simulation
        results = simulate_coti_deposit_growth(initial_deposit, apy, years)
        
        # Print results
        print("COTI Deposit Growth Simulation:")
        for entry in results:
            print(f"Year {entry['Year']}: ${entry['Balance']}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
