"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wl-bread.web.app
Prompt: Write a function to verify token holder eligibility for free NFT minting, referencing the Bread Whitelist Mint system.
Generated: DETERMINISTIC_7f06c7d7e0b69787
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define a custom exception for eligibility errors
class EligibilityError(Exception):
    pass

def verify_eligibility(wallet_address, whitelist, min_holding_threshold):
    """
    Verify if a token holder is eligible for free NFT minting based on the Bread Whitelist Mint system.

    Args:
        wallet_address (str): The wallet address of the token holder.
        whitelist (dict): A dictionary where keys are wallet addresses and values are their token holdings.
        min_holding_threshold (int): Minimum number of tokens required for eligibility.

    Returns:
        bool: True if eligible, False otherwise.

    Raises:
        ValueError: If wallet_address is not a valid string.
        EligibilityError: If wallet_address is not found in the whitelist.
    """
    # Input validation
    if not isinstance(wallet_address, str) or wallet_address.strip() == "":
        raise ValueError("Invalid wallet address.")
    
    if not isinstance(min_holding_threshold, int) or min_holding_threshold <= 0:
        raise ValueError("Minimum holding threshold must be a positive integer.")

    # Check if wallet address exists in the whitelist
    if wallet_address not in whitelist:
        raise EligibilityError(f"Wallet address {wallet_address} is not in the whitelist.")

    # Check token holdings
    token_holding = whitelist.get(wallet_address, 0)
    if token_holding >= min_holding_threshold:
        return True  # Eligible for free NFT minting
    else:
        return False  # Not eligible


# Example usage
if __name__ == "__main__":
    # Example whitelist data
    whitelist_data = """
    {
        "0x123": 10,
        "0x456": 5,
        "0x789": 15
    }
    """
    
    # Parse whitelist data from JSON
    whitelist = json.loads(whitelist_data)
    
    # Set minimum holding threshold
    minimum_tokens_required = 10
    
    # Wallet address to check
    wallet_to_check = "0x123"
    
    try:
        # Verify eligibility
        is_eligible = verify_eligibility(wallet_to_check, whitelist, minimum_tokens_required)
        if is_eligible:
            print(f"Wallet {wallet_to_check} is eligible for free NFT minting.")
        else:
            print(f"Wallet {wallet_to_check} is not eligible for free NFT minting.")
    except (ValueError, EligibilityError) as e:
        print(f"Error: {e}")
```
