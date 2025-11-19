"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-dogdog.pages.dev
Prompt: Write a Python script that calculates the number of DOG tokens received for different ETH amounts during the presale, given the conversion rate of 0.1 ETH for 99,500 DOG.
Generated: DETERMINISTIC_3ebaa0e49aa8dbef
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate the number of DOG tokens received for different ETH amounts.

# Constants
CONVERSION_RATE_ETH_TO_DOG = 99500  # Number of DOG tokens for 0.1 ETH
ETH_INCREMENT = 0.1  # Increment step for ETH amounts

def calculate_dog_tokens(eth_amount):
    """
    Calculate the number of DOG tokens received for a given ETH amount.
    
    Args:
        eth_amount (float): Amount of ETH to convert to DOG tokens.
    
    Returns:
        int: Number of DOG tokens received.
    """
    try:
        # Ensure ETH amount is valid
        if eth_amount <= 0:
            raise ValueError("ETH amount must be greater than 0.")
        
        # Calculate DOG tokens based on conversion rate
        dog_tokens = (eth_amount / ETH_INCREMENT) * CONVERSION_RATE_ETH_TO_DOG
        return int(dog_tokens)  # Return as integer (round down to nearest whole number)
    
    except Exception as e:
        # Handle any unexpected errors
        print(f"Error calculating DOG tokens: {e}")
        return 0


def main():
    """
    Main function to display DOG tokens for a range of ETH amounts.
    """
    try:
        print("DOG Token Presale Calculator")
        print(f"Conversion Rate: {ETH_INCREMENT} ETH = {CONVERSION_RATE_ETH_TO_DOG} DOG\n")
        
        # List of ETH amounts for demonstration
        eth_amounts = [0.1, 0.5, 1.0, 2.0, 5.0]  # Example ETH amounts
        
        print(f"{'ETH Amount':<10} | {'DOG Tokens':<10}")
        print("-" * 25)
        
        # Calculate DOG tokens for each ETH amount
        for eth in eth_amounts:
            dog_tokens = calculate_dog_tokens(eth)
            print(f"{eth:<10.2f} | {dog_tokens:<10}")
    
    except Exception as e:
        # Handle any unexpected errors in main execution
        print(f"An error occurred: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
