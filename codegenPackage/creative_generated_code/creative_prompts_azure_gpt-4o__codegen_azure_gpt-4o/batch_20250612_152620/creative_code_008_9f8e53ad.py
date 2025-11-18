"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-minetrix.web.app
Prompt: Create a Python script to calculate the amount of BTC cloud mining power a user can earn based on the number of BTCMTX tokens staked and mining credits burned, as described on the Bitcoin Minetrix platform.
Generated: DETERMINISTIC_9f8e53ad73e77520
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_mining_power(btcmtx_tokens_staked, mining_credits_burned):
    """
    Calculate the BTC cloud mining power based on BTCMTX tokens staked and mining credits burned.

    Args:
        btcmtx_tokens_staked (float): The number of BTCMTX tokens staked by the user.
        mining_credits_burned (float): The number of mining credits burned by the user.

    Returns:
        float: The calculated BTC cloud mining power in TH/s.
    """
    # Constants for the calculation
    STAKING_WEIGHT = 0.7  # Weight for BTCMTX tokens staked
    BURN_WEIGHT = 0.3     # Weight for mining credits burned
    
    # Ensure inputs are valid
    if btcmtx_tokens_staked < 0:
        raise ValueError("BTCMTX tokens staked cannot be negative.")
    if mining_credits_burned < 0:
        raise ValueError("Mining credits burned cannot be negative.")
    
    # Calculate mining power
    mining_power = (btcmtx_tokens_staked * STAKING_WEIGHT) + (mining_credits_burned * BURN_WEIGHT)
    return mining_power

def main():
    """
    Main function to calculate BTC cloud mining power based on user inputs.
    """
    try:
        # Prompt user for inputs
        print("Welcome to BTC Cloud Mining Power Calculator")
        btcmtx_tokens_staked = float(input("Enter the number of BTCMTX tokens staked: "))
        mining_credits_burned = float(input("Enter the number of mining credits burned: "))

        # Perform the calculation
        mining_power = calculate_mining_power(btcmtx_tokens_staked, mining_credits_burned)
        
        # Display the result
        print(f"\nYour BTC cloud mining power is: {mining_power:.2f} TH/s")
    
    except ValueError as ve:
        # Handle invalid inputs
        print(f"Input Error: {ve}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
