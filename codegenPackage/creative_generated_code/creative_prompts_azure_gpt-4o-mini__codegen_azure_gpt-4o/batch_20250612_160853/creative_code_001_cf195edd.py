"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cvex.pages.dev
Prompt: Write a function that calculates the effective leverage for a given portfolio on the CVEX platform, considering both long and short positions.
Generated: DETERMINISTIC_cf195edd06e45905
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_effective_leverage(portfolio):
    """
    Calculates the effective leverage for a given portfolio on the CVEX platform.
    
    Effective leverage is calculated as:
        (Total Absolute Exposure) / (Net Portfolio Value)
    
    Args:
        portfolio (dict): A dictionary representing the portfolio with the following keys:
            - 'long_positions': List of dicts, each containing 'asset' and 'value' for long positions.
            - 'short_positions': List of dicts, each containing 'asset' and 'value' for short positions.
            - 'cash': Float, the amount of cash in the portfolio.
    
    Returns:
        float: The effective leverage of the portfolio.
    
    Raises:
        ValueError: If Net Portfolio Value is zero or negative, leverage calculation is invalid.
    """
    try:
        # Calculate total long exposure
        total_long_exposure = sum(position['value'] for position in portfolio.get('long_positions', []))
        
        # Calculate total short exposure
        total_short_exposure = sum(position['value'] for position in portfolio.get('short_positions', []))
        
        # Calculate net portfolio value (cash + long positions - short positions)
        net_portfolio_value = portfolio.get('cash', 0) + total_long_exposure - total_short_exposure
        
        # Ensure net portfolio value is positive for valid leverage calculation
        if net_portfolio_value <= 0:
            raise ValueError("Net Portfolio Value must be positive to calculate effective leverage.")

        # Calculate total absolute exposure (long positions + short positions)
        total_absolute_exposure = total_long_exposure + total_short_exposure
        
        # Calculate effective leverage
        effective_leverage = total_absolute_exposure / net_portfolio_value

        return effective_leverage

    except KeyError as e:
        raise ValueError(f"Portfolio data is missing required key: {e}")
    except TypeError as e:
        raise ValueError(f"Invalid data type encountered in portfolio: {e}")
    except ZeroDivisionError:
        raise ValueError("Net Portfolio Value cannot be zero.")
```
