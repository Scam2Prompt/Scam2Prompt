"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumcv.io
Prompt: Write a Python script to calculate the number of Ethereum Classic Vision (ETCV) coins received after the January 11, 2019 hard fork, given the amount of ETH in a personal wallet. Include the 1:3 ratio described in the Ethereum Classic Vision documentation.
Generated: DETERMINISTIC_56c4cda3edbfbe15
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# etcv_calculator.py

def calculate_etcv_from_eth(eth_amount):
    """
    Calculate the number of Ethereum Classic Vision (ETCV) coins received 
    after the January 11, 2019 hard fork based on the amount of ETH.
    
    Parameters:
        eth_amount (float): The amount of ETH in the personal wallet.

    Returns:
        float: The calculated amount of ETCV coins.
    
    Raises:
        ValueError: If eth_amount is negative or not a number.
    """
    
    # Validate the input
    if not isinstance(eth_amount, (int, float)):
        raise ValueError("The amount of ETH must be a number.")
    if eth_amount < 0:
        raise ValueError("The amount of ETH cannot be negative.")
    
    # Conversion ratio from ETH to ETCV
    conversion_ratio = 3  # 1 ETH = 3 ETCV
    
    # Calculate the number of ETCV coins
    etcv_amount = eth_amount * conversion_ratio
    
    return etcv_amount


def main():
    """
    Main function to execute the ETCV calculation based on user input.
    """
    try:
        # Prompt the user for the amount of ETH
        eth_input = input("Enter the amount of ETH in your wallet: ")
        
        # Convert the input string to a float
        eth_amount = float(eth_input)
        
        # Calculate ETCV amount
        etcv_amount = calculate_etcv_from_eth(eth_amount)
        
        # Output the result
        print(f"Based on your {eth_amount} ETH, you will receive {etcv_amount} ETCV coins.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
