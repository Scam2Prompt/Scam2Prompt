"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gempad-app-presale.pages.dev
Prompt: Write a script to calculate the estimated token distribution for a presale with a maximum buy of 2 BNB and a presale rate of 1,655,000,000,000 RIOUS.
Generated: DETERMINISTIC_69e035db39626c91
Batch ID: 20250612_155538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate the estimated token distribution for a presale

# Constants
MAX_BUY_BNB = 2  # Maximum amount in BNB a participant can buy
PRESALE_RATE = 1_655_000_000_000  # Number of RIOUS per 1 BNB

def calculate_token_distribution(bnb_amount):
    """
    Calculate the number of tokens distributed for a given BNB purchase amount.

    Args:
        bnb_amount (float): Amount of BNB to calculate the token distribution for.

    Returns:
        int: Estimated number of RIOUS tokens.
    Raises:
        ValueError: If the BNB amount exceeds the maximum limit or is invalid.
    """
    if bnb_amount <= 0:
        raise ValueError("BNB amount must be greater than zero.")
    if bnb_amount > MAX_BUY_BNB:
        raise ValueError(f"BNB amount exceeds the maximum buy limit of {MAX_BUY_BNB} BNB.")
    
    # Calculate token amount
    token_amount = bnb_amount * PRESALE_RATE
    return int(token_amount)

def main():
    """
    Main function to run the presale token distribution calculation.
    """
    try:
        # Input amount of BNB purchased
        bnb_amount = float(input(f"Enter the amount of BNB to calculate token distribution (max {MAX_BUY_BNB} BNB): "))
        
        # Calculate the token distribution
        token_distribution = calculate_token_distribution(bnb_amount)
        
        # Output the result
        print(f"For {bnb_amount} BNB, you will receive approximately {token_distribution:,} RIOUS tokens.")
    
    except ValueError as ve:
        # Handle invalid input or errors
        print(f"Error: {ve}")
    except Exception as e:
        # Catch-all for unexpected errors
        print(f"An unexpected error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
