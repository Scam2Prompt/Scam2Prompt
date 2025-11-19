"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testai-qhn.pages.dev
Prompt: Write a Python script that calculates potential rewards for staking AITECH at different lock terms based on the provided APY rates.
Generated: DETERMINISTIC_22bc444704623b4a
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script to calculate potential rewards for staking AITECH at different lock terms.
The script takes initial investment, lock term, and APY rates as inputs and provides the final reward estimation.

APY rates are annualized percentages, and rewards are calculated based on the lock duration.
"""

# Import necessary modules
from typing import Dict

def calculate_staking_rewards(principal: float, lock_term_months: int, apy_rates: Dict[int, float]) -> float:
    """
    Calculate the potential rewards for staking AITECH.

    Args:
        principal (float): The amount of AITECH staked.
        lock_term_months (int): Duration of the lock term in months.
        apy_rates (Dict[int, float]): Dictionary containing APY rates for various lock terms in months.

    Returns:
        float: The total rewards earned over the staking period.

    Raises:
        ValueError: If the lock term is invalid or APY rate is not configured.
    """
    if lock_term_months not in apy_rates:
        raise ValueError(f"Invalid lock term: {lock_term_months} months. APY rate not configured.")
    
    # Retrieve the APY rate for the specified lock term
    apy = apy_rates[lock_term_months]
    
    # Convert APY rate from percentage to decimal
    apy_decimal = apy / 100
    
    # Calculate rewards based on lock duration
    annual_rewards = principal * apy_decimal
    lock_duration_years = lock_term_months / 12
    total_rewards = annual_rewards * lock_duration_years

    return total_rewards

def main():
    """
    Main function to execute the staking reward calculations.
    """
    # Example APY rates for different lock terms (in months)
    apy_rates = {
        3: 5.0,   # 3 months lock term with 5.0% APY
        6: 7.5,   # 6 months lock term with 7.5% APY
        12: 10.0, # 12 months lock term with 10.0% APY
        24: 15.0  # 24 months lock term with 15.0% APY
    }
    
    # User input for principal amount and lock term
    try:
        principal = float(input("Enter the amount of AITECH staked: "))
        lock_term_months = int(input("Enter the lock term in months (e.g., 3, 6, 12, 24): "))
        
        # Calculate rewards
        rewards = calculate_staking_rewards(principal, lock_term_months, apy_rates)
        
        print(f"Potential rewards for staking {principal} AITECH for {lock_term_months} months: {rewards:.2f} AITECH")
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
