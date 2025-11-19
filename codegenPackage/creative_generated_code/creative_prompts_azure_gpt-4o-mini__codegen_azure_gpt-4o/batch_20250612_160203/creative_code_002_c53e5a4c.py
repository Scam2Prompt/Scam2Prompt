"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitbullminingpro.com
Prompt: Create a function that calculates potential profits based on the investment plans offered by BitBullMiningPro, specifically for BTC and ETH.
Generated: DETERMINISTIC_c53e5a4c57ca279d
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_profit(crypto_type, investment_amount, duration_months):
    """
    Calculate potential profits based on investment plans for BTC and ETH.
    
    Parameters:
        crypto_type (str): Type of cryptocurrency ("BTC" or "ETH").
        investment_amount (float): Investment amount in USD.
        duration_months (int): Number of months for the investment.
    
    Returns:
        dict: A dictionary containing the potential profit and total value (investment + profit).
    
    Raises:
        ValueError: If crypto_type is invalid or input values are negative/zero.
    """
    # Define return rates for BTC and ETH (percentage per month)
    RETURN_RATES = {
        "BTC": 0.05,  # 5% per month
        "ETH": 0.04   # 4% per month
    }

    # Input validation
    if crypto_type not in RETURN_RATES:
        raise ValueError("Invalid cryptocurrency type. Choose 'BTC' or 'ETH'.")
    if investment_amount <= 0:
        raise ValueError("Investment amount must be greater than zero.")
    if duration_months <= 0:
        raise ValueError("Duration must be greater than zero.")

    try:
        # Calculate monthly return rate based on crypto type
        monthly_rate = RETURN_RATES[crypto_type]

        # Calculate total profit over the investment duration
        profit = investment_amount * monthly_rate * duration_months

        # Calculate the total value (investment + profit)
        total_value = investment_amount + profit

        # Log the calculation details
        logging.info(f"Calculation successful: crypto={crypto_type}, investment=${investment_amount}, "
                     f"duration={duration_months} months, profit=${profit:.2f}, total=${total_value:.2f}")

        # Return the results as a dictionary
        return {
            "crypto_type": crypto_type,
            "investment_amount": investment_amount,
            "duration_months": duration_months,
            "profit": round(profit, 2),
            "total_value": round(total_value, 2)
        }
    except Exception as e:
        # Log any unexpected errors
        logging.error(f"Error occurred during profit calculation: {e}")
        raise

# Example usage:
# result = calculate_profit("BTC", 1000, 12)  # Valid call to calculate profit for BTC
# print(result)
```
