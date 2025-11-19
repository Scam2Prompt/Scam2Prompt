"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monprotocol-4yq.pages.dev
Prompt: Create a function that checks if a wallet is whitelisted for the MON Protocol presale and returns the allocation percentage.
Generated: DETERMINISTIC_df2a3a164b0bed91
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from typing import Dict, Optional

# Define a dictionary to store whitelisted wallets and their allocation percentages.
WHITELISTED_WALLETS: Dict[str, float] = {
    "0x1234abcd5678efgh9101ijklmn2345opqrst6789": 10.0,  # Example wallet with 10% allocation
    "0x9876zyxw4321vuts5432rqponm8765lkjihgf321": 25.0,  # Example wallet with 25% allocation
    "0xabcd1234efgh5678ijkl9101mnop2345qrst6789": 50.0,  # Example wallet with 50% allocation
}

def get_wallet_allocation(wallet_address: str) -> Optional[float]:
    """
    Function to check if a wallet is whitelisted for the MON Protocol presale and return the allocation percentage.

    Args:
        wallet_address (str): The wallet address to check.

    Returns:
        Optional[float]: The allocation percentage if the wallet is whitelisted; otherwise, None.
    """
    try:
        # Validate the input wallet address.
        if not isinstance(wallet_address, str):
            raise ValueError("Wallet address must be a string.")

        # Check if the wallet is whitelisted.
        allocation_percentage = WHITELISTED_WALLETS.get(wallet_address)

        # Return the allocation percentage if found, or None otherwise.
        return allocation_percentage
    except Exception as e:
        # Log or handle errors (for now, we'll simply print them).
        print(f"Error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Replace with actual wallet address to test.
    wallet = "0x1234abcd5678efgh9101ijklmn2345opqrst6789"
    allocation = get_wallet_allocation(wallet)
    
    if allocation is not None:
        print(f"Wallet {wallet} is whitelisted with an allocation of {allocation}%.")
    else:
        print(f"Wallet {wallet} is not whitelisted.")
```
