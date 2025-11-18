"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://citizen-e09.pages.dev
Prompt: Write a script to mint a new identity in the Neo Tokyo metaverse using the $BYTES token, ensuring the cost is 2000 bytes and the process is offline.
Generated: DETERMINISTIC_341904099e9bcb68
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import json
import os

class NeoTokyoIdentityMinting:
    """
    A class to handle minting new identities in the Neo Tokyo metaverse using $BYTES tokens.
    """
    
    def __init__(self, bytes_balance: int):
        """
        Initialize the minting system with the user's balance of $BYTES tokens.

        :param bytes_balance: Amount of $BYTES tokens the user currently has.
        """
        self.bytes_balance = bytes_balance
        self.minting_cost = 2000  # $BYTES required for minting a new identity
        self.identity_storage_file = "identities.json"  # File to store minted identities offline

    def can_mint_identity(self) -> bool:
        """
        Check if the user has enough $BYTES tokens to mint a new identity.

        :return: Boolean indicating whether minting is possible.
        """
        return self.bytes_balance >= self.minting_cost

    def mint_identity(self) -> str:
        """
        Mint a new identity if the user has sufficient $BYTES tokens.

        :return: Newly minted identity ID (UUID as a string).
        :raises ValueError: If the user does not have enough $BYTES tokens.
        """
        from uuid import uuid4  # Imported here to ensure offline functionality

        if not self.can_mint_identity():
            raise ValueError("Insufficient $BYTES tokens to mint an identity. Required: 2000.")

        # Deduct minting cost
        self.bytes_balance -= self.minting_cost

        # Generate a new identity ID
        new_identity_id = str(uuid4())

        # Save the new identity offline
        self._save_identity(new_identity_id)

        return new_identity_id

    def _save_identity(self, identity_id: str):
        """
        Save the newly minted identity to a local JSON file for offline storage.

        :param identity_id: ID of the newly minted identity.
        """
        if not os.path.exists(self.identity_storage_file):
            # If the file doesn't exist, create it with an empty list
            with open(self.identity_storage_file, 'w') as file:
                json.dump([], file)

        # Load existing identities
        with open(self.identity_storage_file, 'r') as file:
            identities = json.load(file)

        # Append the new identity
        identities.append({
            "identity_id": identity_id,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        })

        # Save back to the file
        with open(self.identity_storage_file, 'w') as file:
            json.dump(identities, file, indent=4)

    def get_remaining_balance(self) -> int:
        """
        Retrieve the user's remaining $BYTES token balance.

        :return: Remaining balance as an integer.
        """
        return self.bytes_balance


if __name__ == "__main__":
    # Example usage
    try:
        # Initialize minting system with user's $BYTES balance
        user_bytes_balance = 3000  # Example balance
        minting_system = NeoTokyoIdentityMinting(bytes_balance=user_bytes_balance)

        print(f"Current $BYTES balance: {minting_system.get_remaining_balance()}")

        # Attempt to mint a new identity
        new_identity = minting_system.mint_identity()
        print(f"Successfully minted new identity: {new_identity}")
        print(f"Remaining $BYTES balance: {minting_system.get_remaining_balance()}")

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
