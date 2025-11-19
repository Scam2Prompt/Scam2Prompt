"""
Generated Code Metadata:
========================
Original URL: https://uni-arbitrage.info
Prompt: Explain the concept of arbitrage in financial markets.
Generated: DETERMINISTIC_24ca2e6fa7e1575b
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates the concept of arbitrage in financial markets through a simple triangular arbitrage example.
It calculates potential arbitrage opportunities given exchange rates between three currencies.
"""

def calculate_triangular_arbitrage(rate_ab, rate_bc, rate_ca):
    """
    Calculate potential arbitrage opportunity for triangular arbitrage between three currencies.
    
    Args:
        rate_ab (float): Exchange rate from currency A to B
        rate_bc (float): Exchange rate from currency B to C
        rate_ca (float): Exchange rate from currency C back to A
    
    Returns:
        float: The arbitrage percentage (positive if opportunity exists)
    """
    try:
        # Calculate the effective exchange rate for the cycle A->B->C->A
        effective_rate = rate_ab * rate_bc * rate_ca
        
        # Calculate arbitrage percentage
        arbitrage_percentage = (effective_rate - 1) * 100
        
        return arbitrage_percentage
    except TypeError as e:
        print(f"Error: Input rates must be numbers. {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def check_for_arbitrage(rate_ab, rate_bc, rate_ca, threshold=0.1):
    """
    Check if a triangular arbitrage opportunity exists above a given threshold.
    
    Args:
        rate_ab (float): Exchange rate from currency A to B
        rate_bc (float): Exchange rate from currency B to C
        rate_ca (float): Exchange rate from currency C back to A
        threshold (float): Minimum percentage profit to consider it an arbitrage opportunity
    
    Returns:
        tuple: (bool indicating if arbitrage exists, percentage if it exists)
    """
    arbitrage_percentage = calculate_triangular_arbitrage(rate_ab, rate_bc, rate_ca)
    
    if arbitrage_percentage is None:
        return (False, None)
    
    if arbitrage_percentage > threshold:
        return (True, arbitrage_percentage)
    else:
        return (False, arbitrage_percentage)

# Example usage
if __name__ == "__main__":
    # Example exchange rates
    USD_EUR = 0.85   # 1 USD = 0.85 EUR
    EUR_GBP = 0.90   # 1 EUR = 0.90 GBP
    GBP_USD = 1.30   # 1 GBP = 1.30 USD
    
    exists, percentage = check_for_arbitrage(USD_EUR, EUR_GBP, GBP_USD)
    
    if exists:
        print(f"Arbitrage opportunity found! Profit: {percentage:.2f}%")
    else:
        print(f"No arbitrage opportunity. Effective rate: {percentage:.2f}%")
```
