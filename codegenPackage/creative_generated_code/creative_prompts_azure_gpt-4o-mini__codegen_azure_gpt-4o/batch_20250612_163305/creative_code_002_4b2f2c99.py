"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://award-topg.pages.dev
Prompt: Write a script to calculate the amount of TOPG tokens received for different ETH contributions in a presale, based on the rates provided for $TOPG.
Generated: DETERMINISTIC_4b2f2c990368b30f
Batch ID: 20250612_163305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate TOPG tokens received for ETH contributions in a presale

# Import necessary libraries
import sys

def calculate_topg_tokens(eth_amount, rate):
    """
    Calculate the amount of TOPG tokens received.

    Args:
        eth_amount (float): Amount of ETH contributed
        rate (float): Conversion rate for 1 ETH to TOPG tokens

    Returns:
        float: Amount of TOPG tokens received
    """
    try:
        # Ensure the ETH amount and rate are valid numbers
        if eth_amount < 0 or rate <= 0:
            raise ValueError("ETH amount must be non-negative and rate must be greater than zero.")
        
        # Calculate TOPG tokens
        topg_tokens = eth_amount * rate
        return topg_tokens
    except Exception as e:
        print(f"Error calculating TOPG tokens: {e}")
        sys.exit(1)

def main():
    """
    Main function to run the script.
    """
    # Display introductory message
    print("Welcome to the TOPG Token Presale Calculator!")
    
    try:
        # Get user input for ETH contribution
        eth_amount = float(input("Enter the amount of ETH you wish to contribute: "))
        
        # Predefined rate for TOPG token per ETH
        topg_rate = 5000  # Example rate: 1 ETH = 5000 TOPG tokens
        
        # Calculate TOPG tokens
        topg_tokens_received = calculate_topg_tokens(eth_amount, topg_rate)
        
        # Display the result
        print(f"For your contribution of {eth_amount:.2f} ETH, you will receive {topg_tokens_received:.2f} TOPG tokens.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for ETH contribution.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Entry point of the script
if __name__ == "__main__":
    main()
```
