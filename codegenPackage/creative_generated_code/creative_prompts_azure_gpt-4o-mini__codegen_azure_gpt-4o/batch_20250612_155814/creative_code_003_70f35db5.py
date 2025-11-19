"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kelpdigital.xyz
Prompt: Create a function to check the supported tokens for liquid restaking on Kelp Digital, including ETH, stETH, and ETHx.
Generated: DETERMINISTIC_70f35db5197969f6
Batch ID: 20250612_155814
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List

def check_supported_tokens(token: str) -> bool:
    """
    Function to check if a token is supported for liquid restaking on Kelp Digital.
    
    Supported tokens:
    - ETH
    - stETH
    - ETHx

    Args:
        token (str): The token symbol to check for support.

    Returns:
        bool: True if the token is supported, False otherwise.
    """
    # List of supported tokens
    supported_tokens: List[str] = ["ETH", "stETH", "ETHx"]
    
    # Check if the token is supported
    if not isinstance(token, str):
        raise ValueError("Token must be a string.")
    
    return token in supported_tokens


# Example usage:
if __name__ == "__main__":
    try:
        # Token to check
        token_to_check = "ETHx"
        
        # Check if the token is supported
        is_supported = check_supported_tokens(token_to_check)
        print(f"Is {token_to_check} supported for liquid restaking? {is_supported}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
