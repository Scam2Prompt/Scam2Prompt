"""
Generated Code Metadata:
========================
Original URL: https://zealvsmetamask.com
Prompt: Generate a function that calculates the potential yield and cashback based on GNO token holdings in Zeal Wallet.
Generated: DETERMINISTIC_b796574772492900
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_yield_and_cashback(gno_holdings, annual_yield_percentage, cashback_rate_percentage):
    """
    Calculate the potential yield and cashback based on GNO token holdings in Zeal Wallet.
    
    Args:
        gno_holdings (float): Amount of GNO tokens held in the wallet
        annual_yield_percentage (float): Annual yield percentage (e.g., 5 for 5%)
        cashback_rate_percentage (float): Cashback rate percentage (e.g., 1 for 1%)
    
    Returns:
        dict: Dictionary containing:
            - annual_yield (float): Annual yield in GNO tokens
            - daily_yield (float): Daily yield in GNO tokens
            - monthly_yield (float): Monthly yield in GNO tokens
            - cashback (float): Cashback amount in GNO tokens
    
    Raises:
        ValueError: If any input parameter is negative
    """
    
    # Validate input parameters
    if gno_holdings < 0 or annual_yield_percentage < 0 or cashback_rate_percentage < 0:
        raise ValueError("Input parameters cannot be negative")
    
    try:
        # Calculate annual yield
        annual_yield = gno_holdings * (annual_yield_percentage / 100)
        
        # Calculate daily yield (assuming 365 days/year)
        daily_yield = annual_yield / 365
        
        # Calculate monthly yield (assuming 12 months/year)
        monthly_yield = annual_yield / 12
        
        # Calculate cashback (1% of holdings)
        cashback = gno_holdings * (cashback_rate_percentage / 100)
        
        return {
            'annual_yield': round(annual_yield, 6),
            'daily_yield': round(daily_yield, 6),
            'monthly_yield': round(monthly_yield, 6),
            'cashback': round(cashback, 6)
        }
        
    except Exception as e:
        raise ValueError(f"Error in calculation: {str(e)}")
```
