"""
Generated Code Metadata:
========================
Original URL: https://bafybeiexkodjd2izwx6r53x5g4q54yhqmiifywanhuecvkkdn2yyxq3rpu.ipfs.dweb.link
Prompt: Generate code for a simple token sale calculator that takes ETH input and returns the corresponding ALIEN tokens, based on the rates shown for the $ALIEN PRE-SALE.
Generated: DETERMINISTIC_76a7483171f0256b
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Token Sale Calculator for $ALIEN Pre-Sale
# This script calculates the number of ALIEN tokens received for a given ETH input
# based on the pre-sale rates.

# Constants
ALIEN_RATE_PER_ETH = 1000  # Number of ALIEN tokens per 1 ETH
MIN_ETH_INPUT = 0.01       # Minimum ETH input allowed
MAX_ETH_INPUT = 100        # Maximum ETH input allowed

def calculate_alien_tokens(eth_input):
    """
    Calculate the number of ALIEN tokens based on the ETH input.
    
    Args:
        eth_input (float): The amount of ETH provided by the user.
    
    Returns:
        float: The number of ALIEN tokens received.
    
    Raises:
        ValueError: If the ETH input is outside the allowed range.
    """
    if eth_input < MIN_ETH_INPUT:
        raise ValueError(f"ETH input must be at least {MIN_ETH_INPUT} ETH.")
    if eth_input > MAX_ETH_INPUT:
        raise ValueError(f"ETH input must not exceed {MAX_ETH_INPUT} ETH.")
    
    # Calculate the number of ALIEN tokens
    alien_tokens = eth_input * ALIEN_RATE_PER_ETH
    return alien_tokens

def main():
    """
    Main function to interact with the user and calculate ALIEN tokens.
    """
    print("Welcome to the $ALIEN Pre-Sale Token Calculator!")
    print(f"Current rate: {ALIEN_RATE_PER_ETH} ALIEN tokens per 1 ETH")
    print(f"Minimum ETH input: {MIN_ETH_INPUT} ETH")
    print(f"Maximum ETH input: {MAX_ETH_INPUT} ETH")
    
    try:
        # Get user input
        eth_input = float(input("Enter the amount of ETH you want to spend: "))
        
        # Calculate ALIEN tokens
        alien_tokens = calculate_alien_tokens(eth_input)
        
        # Display the result
        print(f"You will receive {alien_tokens:.2f} ALIEN tokens for {eth_input} ETH.")
    except ValueError as ve:
        # Handle invalid ETH input
        print(f"Error: {ve}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
