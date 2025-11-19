"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coniproasset.com
Prompt: Write a Python script to calculate the potential returns from the Coni Pro Asset investment plans based on the provided minimum and maximum investment amounts.
Generated: DETERMINISTIC_ccc94f2646748d9d
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_returns(min_investment: float, max_investment: float, interest_rate: float, duration_years: int) -> dict:
    """
    Calculate the potential returns from the Coni Pro Asset investment plans.
    
    Parameters:
    min_investment (float): The minimum investment amount.
    max_investment (float): The maximum investment amount.
    interest_rate (float): The annual interest rate (in decimal form).
    duration_years (int): The duration of the investment in years.
    
    Returns:
    dict: A dictionary containing minimum and maximum returns.
    """
    
    # Validate inputs
    if min_investment < 0 or max_investment < 0:
        logging.error("Investment amounts must be non-negative.")
        raise ValueError("Investment amounts must be non-negative.")
    
    if min_investment >= max_investment:
        logging.error("Minimum investment must be less than maximum investment.")
        raise ValueError("Minimum investment must be less than maximum investment.")
    
    if interest_rate < 0:
        logging.error("Interest rate must be non-negative.")
        raise ValueError("Interest rate must be non-negative.")
    
    if duration_years <= 0:
        logging.error("Investment duration must be a positive integer.")
        raise ValueError("Investment duration must be a positive integer.")

    # Calculate potential returns using compound interest formula
    min_return = min_investment * (1 + interest_rate) ** duration_years
    max_return = max_investment * (1 + interest_rate) ** duration_years

    logging.info(f"Calculated returns: min_return={min_return}, max_return={max_return}")
    
    return {
        'min_return': min_return,
        'max_return': max_return
    }

def main():
    """
    Main function to execute the investment return calculation.
    """
    try:
        # Example investment parameters
        min_investment = 1000.0  # Minimum investment amount
        max_investment = 5000.0  # Maximum investment amount
        interest_rate = 0.05      # Annual interest rate (5%)
        duration_years = 10       # Investment duration in years

        # Calculate and display returns
        returns = calculate_returns(min_investment, max_investment, interest_rate, duration_years)
        print(f"Potential Returns:\nMinimum: ${returns['min_return']:.2f}\nMaximum: ${returns['max_return']:.2f}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
```
