"""
Generated Code Metadata:
========================
Original URL: https://cotidashboard.com
Prompt: Write a function to simulate $COTI deposit growth over time based on the Max APY (Base + Boost) provided by the COTI Treasury.
Generated: DETERMINISTIC_a9974665721db70d
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

def simulate_coti_growth(initial_deposit, years, base_apy, boost_apy, compounding_frequency=1):
    """
    Simulates the growth of a COTI deposit over time based on the provided APY.

    Parameters:
    initial_deposit (float): The initial amount of COTI deposited.
    years (int): The number of years to simulate growth.
    base_apy (float): The base annual percentage yield (APY) as a decimal (e.g., 0.05 for 5%).
    boost_apy (float): The boost annual percentage yield (APY) as a decimal (e.g., 0.02 for 2%).
    compounding_frequency (int): The number of times interest is compounded per year (default is 1 for annually).

    Returns:
    np.ndarray: An array containing the deposit value at the end of each year.
    """
    
    # Validate input parameters
    if initial_deposit < 0:
        raise ValueError("Initial deposit must be a non-negative value.")
    if years < 0:
        raise ValueError("Number of years must be a non-negative integer.")
    if not (0 <= base_apy <= 1):
        raise ValueError("Base APY must be between 0 and 1.")
    if not (0 <= boost_apy <= 1):
        raise ValueError("Boost APY must be between 0 and 1.")
    if compounding_frequency <= 0:
        raise ValueError("Compounding frequency must be a positive integer.")

    # Calculate total APY
    total_apy = base_apy + boost_apy

    # Initialize an array to store the deposit value at the end of each year
    growth_values = np.zeros(years + 1)
    growth_values[0] = initial_deposit

    # Calculate the growth for each year
    for year in range(1, years + 1):
        growth_values[year] = growth_values[year - 1] * (1 + total_apy / compounding_frequency) ** compounding_frequency

    return growth_values

# Example usage
if __name__ == "__main__":
    try:
        initial_deposit = 1000.0  # Initial deposit in COTI
        years = 5                   # Number of years to simulate
        base_apy = 0.05            # Base APY of 5%
        boost_apy = 0.02           # Boost APY of 2%
        
        growth = simulate_coti_growth(initial_deposit, years, base_apy, boost_apy)
        print("COTI Deposit Growth Over Time:")
        for year, value in enumerate(growth):
            print(f"Year {year}: ${value:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
