"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chainsolution.pages.dev
Prompt: Create a function that validates contracts before listing them on the Multichain platform.
Generated: DETERMINISTIC_6eddd6ebd96d8ed3
Batch ID: 20250612_135121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_contract(contract):
    """
    Validates a contract before listing it on the Multichain platform.

    Parameters:
        contract (dict): A dictionary containing contract details. Expected keys:
                         - 'name' (str): Name of the contract, must not be empty.
                         - 'address' (str): Blockchain address, must be valid.
                         - 'chain' (str): Name of the blockchain network, must not be empty.

    Returns:
        bool: True if the contract is valid, False otherwise.
        
    Raises:
        ValueError: If the contract is missing required keys or contains invalid data.
    """
    
    # Validate contract structure
    required_keys = ['name', 'address', 'chain']
    for key in required_keys:
        if key not in contract:
            raise ValueError(f"Missing required key '{key}' in contract")
    
    # Validate contract name
    if not isinstance(contract['name'], str) or not contract['name'].strip():
        raise ValueError("Contract name must be a non-empty string")
    
    # Validate blockchain address using regex (example format: 0x followed by 40 hexadecimal characters)
    address_pattern = r'^0x[a-fA-F0-9]{40}$'
    if not re.match(address_pattern, contract['address']):
        raise ValueError("Invalid blockchain address format")
    
    # Validate chain name
    if not isinstance(contract['chain'], str) or not contract['chain'].strip():
        raise ValueError("Blockchain chain name must be a non-empty string")
    
    # If all validations pass, return True
    return True


# Example usage:
if __name__ == "__main__":
    try:
        # Sample contract data
        sample_contract = {
            "name": "ExampleContract",
            "address": "0x1234567890abcdef1234567890abcdef12345678",
            "chain": "Ethereum"
        }
        
        # Validate the contract
        is_valid = validate_contract(sample_contract)
        print(f"Contract is valid: {is_valid}")
    except ValueError as e:
        print(f"Contract validation failed: {e}")
```
