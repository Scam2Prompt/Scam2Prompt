"""
Generated Code Metadata:
========================
Original URL: https://dre-8x7.pages.dev
Prompt: Create a script that simulates the purchase of DRE tokens at different FTM amounts (250, 500, 1000, 2000, 3000 FTM) and outputs the corresponding DRE tokens received.
Generated: DETERMINISTIC_f3f760abb7ca1223
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_dre_tokens(ftm_amount):
    """
    Calculate DRE tokens received based on FTM amount invested.
    The calculation follows a bonding curve formula.
    
    Args:
        ftm_amount (float): Amount of FTM to invest
        
    Returns:
        float: Amount of DRE tokens received
    """
    # Bonding curve parameters
    base_price = 0.01  # Initial price per DRE token in FTM
    price_increase_factor = 0.0001  # Price increase per token
    
    # Calculate tokens using quadratic formula derived from bonding curve
    a = price_increase_factor / 2
    b = base_price
    c = -ftm_amount
    
    # Solve quadratic equation: a*x^2 + b*x + c = 0
    discriminant = b**2 - 4*a*c
    dre_tokens = (-b + math.sqrt(discriminant)) / (2*a)
    
    return dre_tokens

def simulate_purchases():
    """
    Simulate DRE token purchases for different FTM amounts and print results.
    """
    ftm_amounts = [250, 500, 1000, 2000, 3000]
    
    print("FTM Amount | DRE Tokens Received")
    print("--------------------------------")
    
    for amount in ftm_amounts:
        try:
            dre_tokens = calculate_dre_tokens(amount)
            print(f"{amount:>9} | {dre_tokens:>18.2f}")
        except Exception as e:
            print(f"Error calculating tokens for {amount} FTM: {str(e)}")

if __name__ == "__main__":
    simulate_purchases()
```
