"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spotfutures.vip
Prompt: Create a function that calculates potential earnings from the interest earning plan mentioned on the Spot Futures website.
Generated: DETERMINISTIC_8fba67a41d0ba6df
Batch ID: 20250612_162629
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to capture errors and debug information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_potential_earnings(principal, annual_interest_rate, duration_in_days):
    """
    Calculates potential earnings from an interest earning plan.
    
    Args:
        principal (float): The initial amount of money deposited (in USD).
        annual_interest_rate (float): The yearly interest rate as a percentage (e.g., 5 for 5%).
        duration_in_days (int): The duration of the earning plan in days.
    
    Returns:
        float: The total earnings from the interest plan over the specified duration.
    
    Raises:
        ValueError: If any of the input values are invalid (e.g., negative numbers).
    """
    try:
        # Validate inputs
        if principal < 0:
            raise ValueError("Principal amount must be a non-negative value.")
        if annual_interest_rate < 0:
            raise ValueError("Annual interest rate must be a non-negative value.")
        if duration_in_days < 0:
            raise ValueError("Duration in days must be a non-negative value.")

        # Convert annual interest rate from percentage to decimal
        annual_interest_rate_decimal = annual_interest_rate / 100

        # Calculate daily interest rate
        daily_interest_rate = annual_interest_rate_decimal / 365

        # Calculate earnings
        earnings = principal * daily_interest_rate * duration_in_days
        return round(earnings, 2)  # Round to 2 decimal places for financial calculations

    except ValueError as e:
        logging.error(f"Input validation error: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        # Example parameters
        principal_amount = 1000.0  # USD
        annual_rate = 5.0         # Percent
        duration = 30             # Days
        
        potential_earnings = calculate_potential_earnings(principal_amount, annual_rate, duration)
        print(f"Potential earnings over {duration} days: ${potential_earnings}")
    except Exception as e:
        print(f"Error occurred: {e}")
```
