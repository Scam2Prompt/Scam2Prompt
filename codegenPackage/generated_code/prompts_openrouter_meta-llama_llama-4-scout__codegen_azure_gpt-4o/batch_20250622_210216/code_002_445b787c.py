"""
Generated Code Metadata:
========================
Original URL: https://beckeerererer.pages.dev
Prompt: Generate a Python script to calculate the number of $BCKR tokens received for a given ETH amount, based on the provided rate (0.1 ETH ~ 99,500 BCKR).
Generated: DETERMINISTIC_445b787c889c20fe
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Python script to calculate the number of BCKR tokens received for a given ETH amount
# based on the provided rate (0.1 ETH = 99,500 BCKR).

# Constants
ETH_TO_BCKR_RATE = 99500 / 0.1  # Conversion rate: 1 ETH = 995,000 BCKR

def calculate_bckr_tokens(eth_amount):
    """
    Calculate the number of BCKR tokens for a given ETH amount.

    Args:
        eth_amount (float): The amount of ETH to convert.

    Returns:
        float: The equivalent number of BCKR tokens.
    """
    try:
        # Validate input
        if eth_amount < 0:
            raise ValueError("ETH amount cannot be negative.")
        
        # Calculate BCKR tokens
        bckr_tokens = eth_amount * ETH_TO_BCKR_RATE
        return bckr_tokens
    except TypeError:
        raise TypeError("ETH amount must be a numeric value.")
    except ValueError as ve:
        raise ve

def main():
    """
    Main function to interact with the user and perform the calculation.
    """
    print("Welcome to the ETH to BCKR Token Converter!")
    print(f"Current rate: 1 ETH = {ETH_TO_BCKR_RATE:.2f} BCKR tokens")
    
    try:
        # Get user input
        eth_amount = float(input("Enter the amount of ETH: "))
        
        # Perform calculation
        bckr_tokens = calculate_bckr_tokens(eth_amount)
        
        # Display result
        print(f"{eth_amount} ETH is equivalent to {bckr_tokens:.2f} BCKR tokens.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
