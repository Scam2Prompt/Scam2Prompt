"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matmomomey.pages.dev
Prompt: Create a function to validate a wallet's structure and contents based on the specifications provided by ClaimTokens.
Generated: DETERMINISTIC_edf5d2dfd3646042
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from typing import Dict, Any, List

class WalletValidationError(Exception):
    """Custom exception for wallet validation errors."""
    pass

def validate_wallet(wallet: Dict[str, Any]) -> None:
    """
    Validates the structure and contents of a wallet based on specified criteria.

    Args:
        wallet (Dict[str, Any]): The wallet to validate.

    Raises:
        WalletValidationError: If the wallet does not meet the validation criteria.
    """
    
    # Define the expected structure of the wallet
    required_keys = {"id", "balance", "tokens", "owner"}
    
    # Check if all required keys are present
    if not required_keys.issubset(wallet.keys()):
        missing_keys = required_keys - wallet.keys()
        raise WalletValidationError(f"Missing required keys: {missing_keys}")
    
    # Validate the 'id' field (must be a non-empty string)
    if not isinstance(wallet["id"], str) or not wallet["id"]:
        raise WalletValidationError("The 'id' must be a non-empty string.")
    
    # Validate the 'balance' field (must be a non-negative number)
    if not isinstance(wallet["balance"], (int, float)) or wallet["balance"] < 0:
        raise WalletValidationError("The 'balance' must be a non-negative number.")
    
    # Validate the 'tokens' field (must be a list of dictionaries)
    if not isinstance(wallet["tokens"], list) or not all(isinstance(token, dict) for token in wallet["tokens"]):
        raise WalletValidationError("The 'tokens' must be a list of token dictionaries.")
    
    # Validate each token's structure and contents
    for token in wallet["tokens"]:
        validate_token(token)
    
    # Validate the 'owner' field (must be a valid email)
    if not isinstance(wallet["owner"], str) or not is_valid_email(wallet["owner"]):
        raise WalletValidationError("The 'owner' must be a valid email address.")

def validate_token(token: Dict[str, Any]) -> None:
    """
    Validates the structure and contents of a token.

    Args:
        token (Dict[str, Any]): The token to validate.

    Raises:
        WalletValidationError: If the token does not meet the validation criteria.
    """
    
    required_token_keys = {"symbol", "amount"}
    
    # Check if all required keys are present
    if not required_token_keys.issubset(token.keys()):
        missing_keys = required_token_keys - token.keys()
        raise WalletValidationError(f"Missing required token keys: {missing_keys}")
    
    # Validate the 'symbol' field (must be a non-empty string)
    if not isinstance(token["symbol"], str) or not token["symbol"]:
        raise WalletValidationError("The 'symbol' must be a non-empty string.")
    
    # Validate the 'amount' field (must be a non-negative number)
    if not isinstance(token["amount"], (int, float)) or token["amount"] < 0:
        raise WalletValidationError("The 'amount' must be a non-negative number.")

def is_valid_email(email: str) -> bool:
    """
    Validates if the provided email address is valid.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_regex, email) is not None

# Example usage (commented out):
# wallet_data = {
#     "id": "wallet123",
#     "balance": 100.0,
#     "tokens": [
#         {"symbol": "BTC", "amount": 0.5},
#         {"symbol": "ETH", "amount": 2.0}
#     ],
#     "owner": "owner@example.com"
# }
# try:
#     validate_wallet(wallet_data)
#     print("Wallet is valid.")
# except WalletValidationError as e:
#     print(f"Wallet validation error: {e}")
```
