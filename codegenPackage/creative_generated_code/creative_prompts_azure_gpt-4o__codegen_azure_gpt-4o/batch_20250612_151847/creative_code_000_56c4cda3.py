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
# Python script to calculate the number of Ethereum Classic Vision (ETCV) coins
# received after the January 11, 2019 hard fork based on the user's ETH wallet balance.
# The ratio of distribution is 1:3 (1 ETH gives 3 ETCV).

def calculate_etcv(eth_balance):
    """
    Calculate the number of ETCV coins received after the hard fork.
    
    Parameters:
        eth_balance (float): Amount of ETH in the wallet.
        
    Returns:
        float: Amount of ETCV coins received.
    """
    # Validate input
    if eth_balance < 0:
        raise ValueError("ETH balance cannot be negative.")
    
    # ETCV coins are distributed at a 1:3 ratio (ETH to ETCV)
    etcv_coins = eth_balance * 3
    return etcv_coins

def main():
    """
    Main function to prompt the user for their ETH balance
    and calculate the corresponding ETCV coins received.
    """
    print("Ethereum Classic Vision (ETCV) Hard Fork Calculator")
    print("--------------------------------------------------")
    
    try:
        # Prompt the user to enter their ETH wallet balance
        eth_balance = float(input("Enter the amount of ETH in your wallet: "))
        
        # Calculate ETCV coins
        etcv_coins = calculate_etcv(eth_balance)
        
        # Display the result
        print(f"With {eth_balance} ETH, you received {etcv_coins} ETCV coins in the hard fork.")
    
    except ValueError as e:
        # Handle invalid input gracefully
        print(f"Error: {e}. Please enter a valid number for ETH balance.")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Entry point of the script
    main()
```
