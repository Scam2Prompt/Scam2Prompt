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
from typing import List, Dict, Any

class TokenHolderEligibilityError(Exception):
    """Custom exception for token holder eligibility checks."""
    pass

def verify_eligible_holders(token_holders: List[Dict[str, Any]], required_tokens: int) -> List[str]:
    """
    Verifies the eligibility of token holders for free NFT minting based on the 
    specified required number of tokens.
    
    Args:
        token_holders (List[Dict[str, Any]]): A list of dictionaries where each dictionary
                                                represents a token holder with 'address'
                                                and 'token_count'.
        required_tokens (int): The number of tokens required to be eligible for minting.

    Returns:
        List[str]: A list of addresses of eligible token holders.

    Raises:
        TokenHolderEligibilityError: If the input data is malformed or invalid.
    """
    
    eligible_holders = []
    
    # Validate the input data
    if not isinstance(token_holders, list) or not isinstance(required_tokens, int):
        raise TokenHolderEligibilityError("Invalid input: token_holders must be a list and required_tokens must be an integer.")
    
    for holder in token_holders:
        # Check if holder has the required fields
        if not isinstance(holder, dict) or 'address' not in holder or 'token_count' not in holder:
            raise TokenHolderEligibilityError("Invalid holder data: must contain 'address' and 'token_count'.")
        
        address = holder['address']
        token_count = holder['token_count']
        
        # Validate the address format (dummy validation for illustration)
        if not isinstance(address, str) or len(address) == 0:
            raise TokenHolderEligibilityError(f"Invalid address for holder: {holder}.")
        
        # Check eligibility
        if token_count >= required_tokens:
            eligible_holders.append(address)
    
    return eligible_holders

# Example usage
if __name__ == "__main__":
    # List of token holders
    token_holders_data = [
        {"address": "0x12345", "token_count": 10},
        {"address": "0x67890", "token_count": 5},
        {"address": "0xabcde", "token_count": 7}
    ]
    
    # Required tokens for eligibility
    required_tokens_for_minting = 6
    
    try:
        eligible_addresses = verify_eligible_holders(token_holders_data, required_tokens_for_minting)
        print("Eligible Addresses for Free NFT Minting:", eligible_addresses)
    except TokenHolderEligibilityError as e:
        print("Eligibility check failed:", str(e))
```
