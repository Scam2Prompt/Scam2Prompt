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
# Import necessary libraries
import sys

# Constants
TOKEN_EXCHANGE_RATE = 1.5  # Example: 1 FTM = 1.5 DRE
FTM_AMOUNTS = [250, 500, 1000, 2000, 3000]  # FTM amounts to simulate purchases

def calculate_dre_tokens(ftm_amount, exchange_rate):
    """
    Calculate the number of DRE tokens received for a given FTM amount.
    
    Args:
        ftm_amount (float): The amount of FTM being spent.
        exchange_rate (float): The exchange rate of FTM to DRE tokens.
    
    Returns:
        float: The number of DRE tokens received.
    """
    try:
        # Ensure the FTM amount is valid
        if ftm_amount <= 0:
            raise ValueError("FTM amount must be greater than zero.")
        
        # Calculate the DRE tokens
        dre_tokens = ftm_amount * exchange_rate
        return dre_tokens
    except Exception as e:
        # Handle any unexpected errors
        print(f"Error calculating DRE tokens: {e}", file=sys.stderr)
        return None

def main():
    """
    Main function to simulate the purchase of DRE tokens for predefined FTM amounts.
    """
    print("Simulating DRE token purchases...\n")
    print(f"Exchange Rate: 1 FTM = {TOKEN_EXCHANGE_RATE} DRE\n")
    
    # Iterate over the predefined FTM amounts
    for ftm in FTM_AMOUNTS:
        # Calculate the DRE tokens for the current FTM amount
        dre_tokens = calculate_dre_tokens(ftm, TOKEN_EXCHANGE_RATE)
        
        # Output the result
        if dre_tokens is not None:
            print(f"FTM Amount: {ftm} -> DRE Tokens Received: {dre_tokens:.2f}")
        else:
            print(f"FTM Amount: {ftm} -> Error in calculation.")

if __name__ == "__main__":
    # Entry point of the script
    main()
```
