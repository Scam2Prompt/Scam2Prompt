"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-mixers.to
Prompt: Create a script that validates Bitcoin addresses, accepts user inputs for mixing BTC, and outputs the estimated arrival time of clean coins based on a user-defined transfer delay.
Generated: DETERMINISTIC_32c591a9ba3c5f35
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import time
from datetime import datetime, timedelta

# Function to validate a Bitcoin address
def is_valid_btc_address(address: str) -> bool:
    """
    Validates a Bitcoin address using regex.
    
    Args:
        address (str): The Bitcoin address to validate.
    
    Returns:
        bool: True if the address is valid, False otherwise.
    """
    # Regex pattern for Bitcoin addresses (both P2PKH and P2SH)
    btc_regex = re.compile(r'^(1[1-9A-HJ-NP-Za-km-z]{25,34}|3[1-9A-HJ-NP-Za-km-z]{24,34}|bc1[a-z0-9]{39,59})$')
    return bool(btc_regex.match(address))

# Function to estimate arrival time of clean coins after mixing
def estimate_arrival_time(transfer_delay: int) -> str:
    """
    Estimates the arrival time of clean coins based on the transfer delay.
    
    Args:
        transfer_delay (int): The transfer delay in minutes.
    
    Returns:
        str: The estimated arrival time formatted as a string.
    """
    arrival_time = datetime.now() + timedelta(minutes=transfer_delay)
    return arrival_time.strftime('%Y-%m-%d %H:%M:%S')

def main():
    """
    Main function to execute the Bitcoin address validation and transfer delay estimation.
    """
    try:
        # Input Bitcoin address from the user
        btc_address = input("Enter a Bitcoin address: ")
        
        # Validate the Bitcoin address
        if not is_valid_btc_address(btc_address):
            print("Invalid Bitcoin address. Please try again.")
            return
        
        # Input the amount of BTC to mix
        amount_to_mix = float(input("Enter the amount of BTC to mix: "))
        
        if amount_to_mix <= 0:
            print("The amount to mix must be greater than zero.")
            return
        
        # Input the transfer delay in minutes
        transfer_delay = int(input("Enter the transfer delay in minutes: "))
        
        if transfer_delay < 0:
            print("Transfer delay cannot be negative.")
            return
        
        # Output estimated arrival time
        estimated_time = estimate_arrival_time(transfer_delay)
        print(f"Estimated arrival time of clean coins: {estimated_time}")

    except ValueError as ve:
        print("Error in input. Please enter valid values.", ve)
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()
```
