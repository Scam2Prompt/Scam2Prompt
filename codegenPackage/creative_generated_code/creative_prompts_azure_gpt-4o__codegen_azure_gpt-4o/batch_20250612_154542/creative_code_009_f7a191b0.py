"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mcoinners.com
Prompt: Write a Python script to calculate the total earnings from multiple deposits, treating each deposit as a separate investment, as described on mcoinners.com.
Generated: DETERMINISTIC_f7a191b0d92aea1e
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to display error messages and application flow
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_total_earnings(deposits, interest_rates, durations):
    """
    Calculate the total earnings from multiple deposits, treating each deposit as a separate investment.
    
    Args:
        deposits (list of float): List containing deposit amounts.
        interest_rates (list of float): List containing annual interest rates (in percentage) for each deposit.
        durations (list of float): List containing investment durations (in years) for each deposit.
        
    Returns:
        float: Total earnings from all deposits.
    
    Raises:
        ValueError: If the length of deposits, interest_rates, and durations do not match.
    """
    if not (len(deposits) == len(interest_rates) == len(durations)):
        raise ValueError("The lists `deposits`, `interest_rates`, and `durations` must have the same length.")
    
    total_earnings = 0.0
    
    for i, (deposit, rate, duration) in enumerate(zip(deposits, interest_rates, durations)):
        if deposit <= 0 or rate <= 0 or duration <= 0:
            logging.error(f"Invalid values for deposit, rate, or duration at index {i}. All values must be positive.")
            raise ValueError("Deposit, interest rate, and duration must be positive numbers.")
        
        # Calculate earnings for the current deposit
        earnings = deposit * (rate / 100) * duration
        logging.info(f"Deposit #{i + 1}: Amount={deposit}, Rate={rate}%, Duration={duration} years, Earnings={earnings:.2f}")
        
        total_earnings += earnings
    
    return total_earnings

if __name__ == "__main__":
    try:
        # Example input data
        deposits = [1000, 1500, 2000]
        interest_rates = [5, 4.5, 6]
        durations = [2, 3, 1.5]

        # Calculate total earnings
        total_earnings = calculate_total_earnings(deposits, interest_rates, durations)

        # Display the result
        print(f"Total Earnings from all deposits: ${total_earnings:.2f}")
    except ValueError as e:
        logging.error(f"ValueError: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
