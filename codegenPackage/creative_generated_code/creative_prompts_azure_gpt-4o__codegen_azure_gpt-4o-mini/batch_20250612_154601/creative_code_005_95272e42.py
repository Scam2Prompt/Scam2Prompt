"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okx-web3-tron-usdt-trc20-000000716.pages.dev
Prompt: Write a function to validate user input for USDT transactions on OKX, ensuring it adheres to TRC-20 standards.
Generated: DETERMINISTIC_95272e42704b242c
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class InvalidInputError(Exception):
    """Custom exception for invalid input."""
    pass

def validate_usdt_transaction(address: str, amount: float) -> None:
    """
    Validates the user input for USDT transactions on OKX adhering to TRC-20 standards.
    
    Parameters:
    address (str): The TRC-20 address to validate.
    amount (float): The amount of USDT to validate.

    Raises:
    InvalidInputError: If the address or amount is invalid.
    """
    
    # Define the TRC-20 address regex pattern (starts with T and is 34 characters long)
    trc20_address_pattern = r'^T[a-zA-Z0-9]{33}$'
    
    # Validate the address format
    if not re.match(trc20_address_pattern, address):
        raise InvalidInputError("Invalid TRC-20 address. It must start with 'T' and be 34 characters long.")

    # Validate the amount (must be a positive number)
    if amount <= 0:
        raise InvalidInputError("Invalid amount. It must be a positive number.")
    
    # If both validations pass, the input is considered valid
    print("Validation successful: Address and amount are valid.")

# Example usage:
if __name__ == "__main__":
    try:
        validate_usdt_transaction("T1234567890123456789012345678901234", 50.0)
    except InvalidInputError as e:
        print(f"Error: {e}")
```
