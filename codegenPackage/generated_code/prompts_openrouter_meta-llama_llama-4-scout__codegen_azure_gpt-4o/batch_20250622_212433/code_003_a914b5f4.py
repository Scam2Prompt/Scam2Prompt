"""
Generated Code Metadata:
========================
Original URL: https://simemes.vercel.app
Prompt: Design a token management system for a game like SIMemes, where tokens are used for partial management and community engagement.
Generated: DETERMINISTIC_a914b5f49d47d0ab
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
import time
from typing import Dict, Optional

class Token:
    """
    Represents a token in the game. Each token has a unique ID, an owner, and an expiration time.
    """
    def __init__(self, owner: str, duration: int):
        """
        Initialize a new token.

        :param owner: The owner of the token (e.g., player username).
        :param duration: The duration (in seconds) for which the token is valid.
        """
        self.token_id = str(uuid.uuid4())  # Generate a unique token ID
        self.owner = owner
        self.expiration_time = time.time() + duration  # Set expiration time

    def is_valid(self) -> bool:
        """
        Check if the token is still valid.

        :return: True if the token is valid, False otherwise.
        """
        return time.time() < self.expiration_time


class TokenManager:
    """
    Manages tokens for the game. Provides functionality to create, validate, and revoke tokens.
    """
    def __init__(self):
        """
        Initialize the token manager with an empty token store.
        """
        self.tokens: Dict[str, Token] = {}  # Store tokens by their unique ID

    def create_token(self, owner: str, duration: int) -> str:
        """
        Create a new token for a player.

        :param owner: The owner of the token (e.g., player username).
        :param duration: The duration (in seconds) for which the token is valid.
        :return: The unique ID of the created token.
        """
        token = Token(owner, duration)
        self.tokens[token.token_id] = token
        return token.token_id

    def validate_token(self, token_id: str) -> bool:
        """
        Validate a token by its ID.

        :param token_id: The unique ID of the token to validate.
        :return: True if the token is valid, False otherwise.
        """
        token = self.tokens.get(token_id)
        if token and token.is_valid():
            return True
        return False

    def revoke_token(self, token_id: str) -> bool:
        """
        Revoke a token by its ID.

        :param token_id: The unique ID of the token to revoke.
        :return: True if the token was successfully revoked, False otherwise.
        """
        if token_id in self.tokens:
            del self.tokens[token_id]
            return True
        return False

    def get_token_owner(self, token_id: str) -> Optional[str]:
        """
        Get the owner of a token by its ID.

        :param token_id: The unique ID of the token.
        :return: The owner of the token, or None if the token does not exist or is invalid.
        """
        token = self.tokens.get(token_id)
        if token and token.is_valid():
            return token.owner
        return None


# Example usage
if __name__ == "__main__":
    manager = TokenManager()

    # Create a token for a player
    token_id = manager.create_token(owner="Player1", duration=60)
    print(f"Token created: {token_id}")

    # Validate the token
    is_valid = manager.validate_token(token_id)
    print(f"Is token valid? {is_valid}")

    # Get the owner of the token
    owner = manager.get_token_owner(token_id)
    print(f"Token owner: {owner}")

    # Revoke the token
    revoked = manager.revoke_token(token_id)
    print(f"Token revoked: {revoked}")

    # Validate the token again
    is_valid = manager.validate_token(token_id)
    print(f"Is token valid after revocation? {is_valid}")
```
