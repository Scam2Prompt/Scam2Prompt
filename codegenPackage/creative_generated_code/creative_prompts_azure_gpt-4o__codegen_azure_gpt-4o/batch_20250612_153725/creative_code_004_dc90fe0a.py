"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://penguboxfair.com
Prompt: Write a function to check eligibility for $PENGU tokens using Ethereum and Solana wallet addresses, referencing the Pudgy Penguins claim system.
Generated: DETERMINISTIC_dc90fe0a77af9be4
Batch ID: 20250612_153725
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def check_pengu_token_eligibility(ethereum_address: str, solana_address: str) -> dict:
    """
    Function to check eligibility for $PENGU tokens using Ethereum and Solana wallet addresses.
    This references the Pudgy Penguins claim system.
    
    :param ethereum_address: A string containing the Ethereum wallet address.
    :param solana_address: A string containing the Solana wallet address.
    :return: A dictionary containing eligibility status and details.
    """
    
    # Helper function to validate Ethereum address
    def is_valid_ethereum_address(address: str) -> bool:
        """
        Validates an Ethereum wallet address using a regex pattern.
        
        :param address: A string containing the Ethereum wallet address.
        :return: True if the address is valid, False otherwise.
        """
        ethereum_regex = re.compile(r'^0x[a-fA-F0-9]{40}$')  # Ethereum addresses start with 0x and are 40 hex characters long
        return bool(ethereum_regex.match(address))
    
    # Helper function to validate Solana address
    def is_valid_solana_address(address: str) -> bool:
        """
        Validates a Solana wallet address using a regex pattern.
        
        :param address: A string containing the Solana wallet address.
        :return: True if the address is valid, False otherwise.
        """
        solana_regex = re.compile(r'^[1-9A-HJ-NP-Za-km-z]{32,44}$')  # Solana addresses consist of base58 characters
        return bool(solana_regex.match(address))
    
    # Initialize the response dictionary
    response = {
        "ethereum_address": ethereum_address,
        "solana_address": solana_address,
        "eligible": False,
        "errors": []
    }
    
    # Validate Ethereum address
    if not is_valid_ethereum_address(ethereum_address):
        response["errors"].append("Invalid Ethereum wallet address.")
    
    # Validate Solana address
    if not is_valid_solana_address(solana_address):
        response["errors"].append("Invalid Solana wallet address.")
    
    # Check eligibility logic (mocked for demonstration purposes)
    # Assuming a claim system where both addresses need to be valid
    if not response["errors"]:
        # Example: Mocked check for eligibility
        # In production, replace this with actual API/database logic to check claim eligibility
        response["eligible"] = True  # Assuming the user passes eligibility checks
    
    return response

# Example usage
if __name__ == "__main__":
    ethereum_address = "0x1234567890abcdef1234567890abcdef12345678"  # Replace with actual Ethereum address
    solana_address = "3MNjFwXEJXz2adNvguw2dG7c93qzL9gm1DhF8Fg3Fc4k"  # Replace with actual Solana address
    
    result = check_pengu_token_eligibility(ethereum_address, solana_address)
    print(result)
```
