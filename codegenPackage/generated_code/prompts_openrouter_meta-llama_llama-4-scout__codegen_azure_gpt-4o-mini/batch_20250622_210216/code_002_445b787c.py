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
# bckr_token_calculator.py

def calculate_bckr_tokens(eth_amount, eth_to_bckr_rate):
    """
    Calculate the number of BCKR tokens received for a given ETH amount.

    Parameters:
    eth_amount (float): The amount of ETH to convert to BCKR tokens.
    eth_to_bckr_rate (float): The conversion rate from ETH to BCKR tokens.

    Returns:
    float: The number of BCKR tokens received.
    """
    if eth_amount < 0:
        raise ValueError("ETH amount must be a non-negative value.")
    
    # Calculate the number of BCKR tokens
    bckr_tokens = eth_amount * eth_to_bckr_rate
    return bckr_tokens

def main():
    """
    Main function to execute the BCKR token calculation based on user input.
    """
    try:
        # Define the conversion rate (0.1 ETH ~ 99,500 BCKR)
        eth_to_bckr_rate = 99500 / 0.1  # Calculate the rate per ETH

        # Get user input for ETH amount
        eth_amount = float(input("Enter the amount of ETH to convert to BCKR tokens: "))

        # Calculate BCKR tokens
        bckr_tokens = calculate_bckr_tokens(eth_amount, eth_to_bckr_rate)

        # Display the result
        print(f"For {eth_amount} ETH, you will receive {bckr_tokens:.2f} BCKR tokens.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
