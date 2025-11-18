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
import numpy as np

def simulate_coti_growth(initial_deposit, years, max_apy, compounding_frequency=1):
    """
    Simulates the growth of a COTI deposit over time based on the maximum APY
    provided by the COTI Treasury.

    Parameters:
    - initial_deposit (float): The initial amount of COTI deposited.
    - years (int): The number of years to simulate growth.
    - max_apy (float): The maximum Annual Percentage Yield (APY) as a decimal (e.g., 0.15 for 15%).
    - compounding_frequency (int): The number of times interest is compounded per year.
    
    Returns:
    - list of float: A list containing the balance at the end of each year.
    
    Raises:
    - ValueError: If initial_deposit is negative, years is negative, or max_apy is negative.
    """
    
    # Input validation
    if initial_deposit < 0:
        raise ValueError("Initial deposit must be a non-negative value.")
    if years < 0:
        raise ValueError("Years must be a non-negative value.")
    if max_apy < 0:
        raise ValueError("Maximum APY must be a non-negative value.")

    # Calculate the growth
    balances = []
    for year in range(1, years + 1):
        # Compound interest formula: A = P (1 + r/n)^(nt)
        balance = initial_deposit * (1 + max_apy / compounding_frequency) ** (compounding_frequency * year)
        balances.append(balance)

    return balances

# Example usage
if __name__ == "__main__":
    try:
        initial_deposit = 1000.0  # Initial deposit amount in COTI
        years = 5                  # Number of years to simulate
        max_apy = 0.15            # Maximum APY (15%)
        growth = simulate_coti_growth(initial_deposit, years, max_apy)
        
        # Print results
        for year, balance in enumerate(growth, start=1):
            print(f"Year {year}: ${balance:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
