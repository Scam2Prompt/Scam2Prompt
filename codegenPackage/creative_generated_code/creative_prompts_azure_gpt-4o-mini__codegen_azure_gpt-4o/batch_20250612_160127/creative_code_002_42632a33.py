"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mitofi-launchpad.pages.dev
Prompt: Write a code snippet to calculate the potential returns from a hyper staking vault in the Black Panther protocol.
Generated: DETERMINISTIC_42632a333967e686
Batch ID: 20250612_160127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_hyper_staking_returns(principal, annual_interest_rate, staking_period_days, compounding_frequency):
    """
    Calculate potential returns from a hyper staking vault.
    
    :param principal: Initial amount staked (float)
    :param annual_interest_rate: Annual interest rate in decimal form (e.g., 0.15 for 15%) (float)
    :param staking_period_days: Number of days staked (int)
    :param compounding_frequency: Number of times interest is compounded per year (int)
    :return: Total value (float)
    """
    try:
        # Validate inputs
        if principal <= 0:
            raise ValueError("Principal must be greater than 0.")
        if annual_interest_rate <= 0 or annual_interest_rate >= 1:
            raise ValueError("Annual interest rate must be a decimal between 0 and 1.")
        if staking_period_days <= 0:
            raise ValueError("Staking period must be greater than 0.")
        if compounding_frequency <= 0:
            raise ValueError("Compounding frequency must be greater than 0.")
        
        # Convert staking period from days to years
        staking_period_years = staking_period_days / 365
        
        # Calculate effective annual interest rate
        effective_rate = math.pow(1 + annual_interest_rate / compounding_frequency, compounding_frequency)
        
        # Calculate final value using compound interest formula
        total_value = principal * math.pow(effective_rate, staking_period_years)
        
        return total_value
    
    except ValueError as e:
        # Handle value errors with descriptive messages
        print(f"Input error: {e}")
        return None
    except Exception as e:
        # Catch-all for unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    principal = 1000.0  # Initial staked amount
    annual_interest_rate = 0.15  # 15% annual interest rate
    staking_period_days = 90  # Number of days staked
    compounding_frequency = 12  # Monthly compounding
    
    # Calculate potential returns
    returns = calculate_hyper_staking_returns(principal, annual_interest_rate, staking_period_days, compounding_frequency)
    
    if returns is not None:
        print(f"Total value after staking: ${returns:.2f}")
    else:
        print("Failed to calculate returns due to input errors.")
```
