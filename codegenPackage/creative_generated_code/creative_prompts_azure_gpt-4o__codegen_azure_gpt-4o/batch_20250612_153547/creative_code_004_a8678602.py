"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.zkfinance.org
Prompt: Create a script to calculate the Maximum Loan-to-Value (LTV) ratio for zkFinance users based on their specific collateral and debt combination.
Generated: DETERMINISTIC_a86786026aa713eb
Batch ID: 20250612_153547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import logging

# Configure logging for error handling and debug information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_max_ltv(collateral_value, debt_value):
    """
    Calculate the Maximum Loan-to-Value (LTV) ratio.
    
    Parameters:
        collateral_value (float): The value of the user's collateral.
        debt_value (float): The value of the user's debt.

    Returns:
        float: Maximum Loan-to-Value ratio (LTV), expressed as a percentage.
    """
    try:
        # Validate inputs
        if collateral_value <= 0:
            raise ValueError("Collateral value must be greater than zero.")
        if debt_value < 0:
            raise ValueError("Debt value cannot be negative.")
        
        # Calculate LTV
        ltv_ratio = (debt_value / collateral_value) * 100
        return round(ltv_ratio, 2)
    
    except ZeroDivisionError as e:
        logging.error("Error: Collateral value cannot be zero. Division by zero occurred.")
        raise ValueError("Collateral value must be greater than zero.") from e
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
        raise

# Example usage of the function
if __name__ == "__main__":
    try:
        # Example user data
        collateral_value = 10000.0  # Example collateral amount in USD
        debt_value = 5000.0         # Example debt amount in USD
        
        # Calculate Maximum LTV
        max_ltv = calculate_max_ltv(collateral_value, debt_value)
        
        # Print the result
        logging.info(f"Maximum Loan-to-Value (LTV) Ratio: {max_ltv}%")
    
    except ValueError as ve:
        logging.error(f"Input error: {ve}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
```
