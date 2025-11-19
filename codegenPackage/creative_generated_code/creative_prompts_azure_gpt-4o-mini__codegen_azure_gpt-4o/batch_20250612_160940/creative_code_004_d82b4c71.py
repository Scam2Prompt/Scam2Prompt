"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptobotsai.pages.dev
Prompt: Create a function to validate a wallet's structure and contents with ClaimTokens.
Generated: DETERMINISTIC_d82b4c7114613f3d
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_wallet(wallet):
    """
    Validates the structure and contents of a wallet containing ClaimTokens.

    Parameters:
        wallet (dict): The wallet data to validate. 
                       Expected structure: {"wallet_id": str, "tokens": list of dicts}
                       Each token dict should have: {"token_id": str, "value": float}

    Returns:
        dict: Validation result with "is_valid" (bool) and "errors" (list of str).
    """

    validation_result = {"is_valid": True, "errors": []}

    try:
        # Validate wallet structure
        if not isinstance(wallet, dict):
            validation_result["is_valid"] = False
            validation_result["errors"].append("Wallet must be a dictionary.")
            return validation_result

        # Validate wallet_id
        wallet_id = wallet.get("wallet_id")
        if not wallet_id or not isinstance(wallet_id, str):
            validation_result["is_valid"] = False
            validation_result["errors"].append("Wallet ID must be a non-empty string.")
        elif not re.match(r"^[A-Za-z0-9_\-]{8,32}$", wallet_id):  # Example ID format validation
            validation_result["is_valid"] = False
            validation_result["errors"].append(
                "Wallet ID must be alphanumeric and 8-32 characters long."
            )

        # Validate tokens
        tokens = wallet.get("tokens")
        if not isinstance(tokens, list):
            validation_result["is_valid"] = False
            validation_result["errors"].append("Tokens must be a list.")
        else:
            for idx, token in enumerate(tokens):
                if not isinstance(token, dict):
                    validation_result["is_valid"] = False
                    validation_result["errors"].append(f"Token at index {idx} must be a dictionary.")
                    continue

                token_id = token.get("token_id")
                value = token.get("value")

                # Validate token_id
                if not token_id or not isinstance(token_id, str):
                    validation_result["is_valid"] = False
                    validation_result["errors"].append(
                        f"Token at index {idx} must have a non-empty string token_id."
                    )
                elif not re.match(r"^[A-Za-z0-9_\-]{8,32}$", token_id):  # Example format validation
                    validation_result["is_valid"] = False
                    validation_result["errors"].append(
                        f"Token ID at index {idx} must be alphanumeric and 8-32 characters long."
                    )

                # Validate value
                if value is None or not isinstance(value, (int, float)):
                    validation_result["is_valid"] = False
                    validation_result["errors"].append(
                        f"Token at index {idx} must have a numeric value."
                    )
                elif value < 0:
                    validation_result["is_valid"] = False
                    validation_result["errors"].append(
                        f"Token value at index {idx} must be non-negative."
                    )

    except Exception as e:
        validation_result["is_valid"] = False
        validation_result["errors"].append(f"Unexpected error during validation: {str(e)}")

    return validation_result


# Example usage:
wallet_example = {
    "wallet_id": "wallet123_ABC",
    "tokens": [
        {"token_id": "token001", "value": 100.5},
        {"token_id": "token002", "value": -10.0},  # Invalid value
    ],
}
result = validate_wallet(wallet_example)
print(result)
```
