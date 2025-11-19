"""
Generated Code Metadata:
========================
Original URL: https://uni-token.com
Prompt: "Generate a code example for verifying the authenticity of unique items using a tokenization approach, as proposed by Unitoken."
Generated: DETERMINISTIC_13855c244cb699ac
Batch ID: 20250622_212417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
import base64
from typing import Dict, Any, Tuple

class TokenizationError(Exception):
    """Custom exception for tokenization errors."""
    pass

class Unitoken:
    """Class to handle tokenization and verification of unique items."""

    @staticmethod
    def generate_token(item_id: str, metadata: Dict[str, Any]) -> str:
        """
        Generate a unique token for an item using its ID and metadata.

        Args:
            item_id (str): The unique identifier for the item.
            metadata (Dict[str, Any]): Additional metadata associated with the item.

        Returns:
            str: A base64 encoded token representing the item.
        """
        try:
            # Create a unique string by combining item_id and metadata
            unique_string = f"{item_id}:{json.dumps(metadata, sort_keys=True)}"
            # Generate a SHA-256 hash of the unique string
            token = hashlib.sha256(unique_string.encode()).hexdigest()
            # Encode the token in base64 for safe transmission
            encoded_token = base64.urlsafe_b64encode(token.encode()).decode()
            return encoded_token
        except Exception as e:
            raise TokenizationError(f"Error generating token: {str(e)}")

    @staticmethod
    def verify_token(item_id: str, metadata: Dict[str, Any], token: str) -> bool:
        """
        Verify the authenticity of an item using its ID, metadata, and token.

        Args:
            item_id (str): The unique identifier for the item.
            metadata (Dict[str, Any]): Additional metadata associated with the item.
            token (str): The token to verify.

        Returns:
            bool: True if the token is valid, False otherwise.
        """
        try:
            # Decode the token from base64
            decoded_token = base64.urlsafe_b64decode(token).decode()
            # Generate a new token using the provided item_id and metadata
            expected_token = Unitoken.generate_token(item_id, metadata)
            # Compare the decoded token with the expected token
            return decoded_token == expected_token
        except Exception as e:
            raise TokenizationError(f"Error verifying token: {str(e)}")

# Example usage
if __name__ == "__main__":
    item_id = "item123"
    metadata = {"name": "Sample Item", "category": "Example"}
    
    # Generate a token for the item
    token = Unitoken.generate_token(item_id, metadata)
    print(f"Generated Token: {token}")

    # Verify the token
    is_valid = Unitoken.verify_token(item_id, metadata, token)
    print(f"Is the token valid? {is_valid}")
```
