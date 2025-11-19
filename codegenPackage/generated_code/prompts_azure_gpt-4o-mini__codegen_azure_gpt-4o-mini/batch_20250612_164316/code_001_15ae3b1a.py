"""
Generated Code Metadata:
========================
Original URL: https://bafybeihbxjh2jhzkz3ukjjcmui77y7fmp4tvvmhqzhv6csboxxwd7dcndu.ipfs.dweb.link
Prompt: Write a Python function that utilizes the DOP's flexible transparency features to allow users to select specific tokens for sharing.
Generated: DETERMINISTIC_15ae3b1a67e68f90
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class TokenSharingError(Exception):
    """Custom exception for token sharing errors."""
    pass

def share_tokens(data: Dict[str, Any], tokens: List[str]) -> Dict[str, Any]:
    """
    Share specific tokens from the provided data.

    Args:
        data (Dict[str, Any]): The original data containing tokens.
        tokens (List[str]): A list of token keys to be shared.

    Returns:
        Dict[str, Any]: A dictionary containing only the selected tokens.

    Raises:
        TokenSharingError: If any of the specified tokens are not found in the data.
    """
    try:
        # Validate input types
        if not isinstance(data, dict):
            raise TokenSharingError("Data must be a dictionary.")
        if not isinstance(tokens, list):
            raise TokenSharingError("Tokens must be a list of strings.")

        # Create a new dictionary to hold the shared tokens
        shared_data = {}

        # Iterate over the specified tokens and add them to the shared_data
        for token in tokens:
            if token in data:
                shared_data[token] = data[token]
            else:
                raise TokenSharingError(f"Token '{token}' not found in the provided data.")

        return shared_data

    except Exception as e:
        # Log the error (in a real application, consider using logging library)
        print(f"Error occurred: {e}")
        raise TokenSharingError("An error occurred while sharing tokens.") from e

# Example usage
if __name__ == "__main__":
    # Sample data
    original_data = {
        "token1": "value1",
        "token2": "value2",
        "token3": "value3"
    }

    # Tokens to share
    tokens_to_share = ["token1", "token3"]

    try:
        # Share the specified tokens
        shared_tokens = share_tokens(original_data, tokens_to_share)
        print("Shared Tokens:", json.dumps(shared_tokens, indent=2))
    except TokenSharingError as e:
        print(f"Failed to share tokens: {e}")
```
