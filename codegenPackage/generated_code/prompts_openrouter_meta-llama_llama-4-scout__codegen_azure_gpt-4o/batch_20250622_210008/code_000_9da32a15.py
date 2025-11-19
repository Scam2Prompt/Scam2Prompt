"""
Generated Code Metadata:
========================
Original URL: https://funkybunnies.pages.dev
Prompt: What is the purpose of the Funky Bunnies project, and how does it relate to new tokens?
Generated: DETERMINISTIC_9da32a152aa11c82
Batch ID: 20250622_210008
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Funky Bunnies Project

Purpose:
The Funky Bunnies project is designed to manage and interact with a blockchain-based ecosystem
where new tokens are created, distributed, and tracked. The project provides functionality to
mint new tokens, assign them to users, and track ownership and metadata associated with each token.

This code snippet demonstrates the core functionality of the Funky Bunnies project, including
token creation and management.

Language: Python
"""

import uuid

class TokenError(Exception):
    """Custom exception for token-related errors."""
    pass

class FunkyBunnies:
    """
    A class to manage the Funky Bunnies token ecosystem.
    """

    def __init__(self):
        """
        Initializes the Funky Bunnies project with an empty token registry.
        """
        self.token_registry = {}  # Stores token data with token_id as the key

    def mint_token(self, owner, metadata):
        """
        Creates a new token and assigns it to the specified owner.

        Args:
            owner (str): The owner of the new token.
            metadata (dict): Metadata associated with the token (e.g., name, description).

        Returns:
            str: The unique ID of the newly created token.

        Raises:
            TokenError: If the owner or metadata is invalid.
        """
        if not owner or not isinstance(owner, str):
            raise TokenError("Invalid owner. Owner must be a non-empty string.")
        if not metadata or not isinstance(metadata, dict):
            raise TokenError("Invalid metadata. Metadata must be a dictionary.")

        # Generate a unique token ID
        token_id = str(uuid.uuid4())

        # Register the token
        self.token_registry[token_id] = {
            "owner": owner,
            "metadata": metadata
        }

        return token_id

    def get_token(self, token_id):
        """
        Retrieves information about a specific token.

        Args:
            token_id (str): The unique ID of the token.

        Returns:
            dict: The token's data, including owner and metadata.

        Raises:
            TokenError: If the token ID does not exist.
        """
        if token_id not in self.token_registry:
            raise TokenError(f"Token with ID {token_id} does not exist.")

        return self.token_registry[token_id]

    def transfer_token(self, token_id, new_owner):
        """
        Transfers ownership of a token to a new owner.

        Args:
            token_id (str): The unique ID of the token.
            new_owner (str): The new owner of the token.

        Raises:
            TokenError: If the token ID does not exist or the new owner is invalid.
        """
        if token_id not in self.token_registry:
            raise TokenError(f"Token with ID {token_id} does not exist.")
        if not new_owner or not isinstance(new_owner, str):
            raise TokenError("Invalid new owner. Owner must be a non-empty string.")

        # Update the token's owner
        self.token_registry[token_id]["owner"] = new_owner

    def list_tokens(self):
        """
        Lists all tokens in the registry.

        Returns:
            dict: A dictionary of all tokens, keyed by token ID.
        """
        return self.token_registry


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the Funky Bunnies project
        funky_bunnies = FunkyBunnies()

        # Mint a new token
        token_id = funky_bunnies.mint_token(
            owner="Alice",
            metadata={"name": "Funky Bunny #1", "description": "A rare funky bunny token."}
        )
        print(f"Token minted with ID: {token_id}")

        # Retrieve token information
        token_info = funky_bunnies.get_token(token_id)
        print(f"Token info: {token_info}")

        # Transfer the token to a new owner
        funky_bunnies.transfer_token(token_id, new_owner="Bob")
        print(f"Token transferred to new owner: {funky_bunnies.get_token(token_id)['owner']}")

        # List all tokens
        all_tokens = funky_bunnies.list_tokens()
        print(f"All tokens: {all_tokens}")

    except TokenError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
