"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beckeerererer.pages.dev
Prompt: Write a Python script to calculate the number of BCKR tokens received for any given ETH amount based on the presale rate of 0.1 ETH = 99,500 BCKR.
Generated: DETERMINISTIC_be83225373987ace
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate the number of BCKR tokens received for a given ETH amount
# Presale rate: 0.1 ETH = 99,500 BCKR

def calculate_bckr_tokens(eth_amount: float) -> float:
    """
    Calculate the number of BCKR tokens for a given ETH amount based on the presale rate.

    Args:
        eth_amount (float): The amount of ETH to convert to BCKR.

    Returns:
        float: The equivalent BCKR tokens for the given ETH amount.
    """
    # Define the presale rate
    presale_rate_eth_to_bckr = 99500 / 0.1  # 99,500 BCKR per 0.1 ETH = 995,000 BCKR per 1 ETH
    
    # Validate input
    if eth_amount <= 0:
        raise ValueError("ETH amount must be greater than 0.")
    
    # Calculate the equivalent BCKR tokens
    bckr_tokens = eth_amount * presale_rate_eth_to_bckr
    
    return bckr_tokens


def main():
    """
    Main function to interact with the user and calculate BCKR tokens.
    """
    print("Welcome to the BCKR Token Calculator!")
    try:
        # Prompt the user for the ETH amount
        eth_amount = float(input("Enter the amount of ETH: "))
        
        # Calculate the number of BCKR tokens
        bckr_tokens = calculate_bckr_tokens(eth_amount)
        
        # Display the result
        print(f"For {eth_amount:.6f} ETH, you will receive approximately {bckr_tokens:,.2f} BCKR tokens.")
    
    except ValueError as ve:
        # Handle invalid input
        print(f"Error: {ve}")
    
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
