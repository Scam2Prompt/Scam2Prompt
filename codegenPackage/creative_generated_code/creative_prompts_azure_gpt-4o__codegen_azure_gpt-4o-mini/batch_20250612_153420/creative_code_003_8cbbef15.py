"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dog-68c.pages.dev
Prompt: Write a Python script using the `web3.py` library to calculate the number of DOG tokens received for a given ETH deposit during the presale.
Generated: DETERMINISTIC_8cbbef153ad8bc21
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from web3 import Web3

# Load environment variables for sensitive information
INFURA_URL = os.getenv("INFURA_URL")  # Infura project URL
DOG_CONTRACT_ADDRESS = os.getenv("DOG_CONTRACT_ADDRESS")  # DOG token contract address
ETH_TO_DOG_RATE = float(os.getenv("ETH_TO_DOG_RATE"))  # Rate of DOG tokens per ETH during presale

# Initialize Web3 connection
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

def get_dog_tokens(received_eth: float) -> float:
    """
    Calculate the number of DOG tokens received for a given ETH deposit.

    Parameters:
        received_eth (float): Amount of ETH to convert into DOG tokens.

    Returns:
        float: Number of DOG tokens received.
    
    Raises:
        ValueError: If received_eth is negative or ETH_TO_DOG_RATE is zero.
    """
    if received_eth < 0:
        raise ValueError("Received ETH must be non-negative.")
    
    if ETH_TO_DOG_RATE <= 0:
        raise ValueError("ETH to DOG rate must be greater than zero.")

    # Calculate the number of DOG tokens
    dog_tokens = received_eth * ETH_TO_DOG_RATE
    return dog_tokens

def main():
    """
    Main function to execute the conversion of ETH to DOG tokens.
    """
    try:
        # Sample ETH amount for conversion
        received_eth = float(input("Enter the amount of ETH to deposit: "))
        dog_tokens = get_dog_tokens(received_eth)
        
        print(f"You will receive {dog_tokens} DOG tokens for {received_eth} ETH.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

Make sure to set the environment variables `INFURA_URL`, `DOG_CONTRACT_ADDRESS`, and `ETH_TO_DOG_RATE` before running the script.
