"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-triasmigration.web.app
Prompt: Explain the 1:1 migration ratio for TRIAS tokens and how it works during the migration process.
Generated: DETERMINISTIC_fae34a4dc8b35a91
Batch ID: 20250612_155503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script explains the 1:1 migration process for TRIAS tokens using a simple simulation. 
The migration ensures that for every old TRIAS token, the user receives exactly 
one new TRIAS token.

Key Features:
- Token balance validation
- Transparent migration with error handling
"""

class TokenMigrationError(Exception):
    """Custom exception for token migration errors."""
    pass


class TriasTokenMigration:
    """
    A class representing the TRIAS token migration process.
    """

    def __init__(self):
        """
        Initializes the migration system with empty balances for old and new tokens.
        """
        self.old_token_balances = {}  # Stores user balances for old TRIAS tokens
        self.new_token_balances = {}  # Stores user balances for new TRIAS tokens

    def add_old_token_balance(self, user_id, balance):
        """
        Adds a user's balance of old TRIAS tokens to the system.

        Args:
            user_id: A unique identifier for the user.
            balance: The number of old TRIAS tokens the user holds.

        Raises:
            ValueError: If the balance is negative.
        """
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        self.old_token_balances[user_id] = balance

    def migrate_tokens(self, user_id):
        """
        Migrates a user's old TRIAS tokens to new TRIAS tokens at a 1:1 ratio.

        Args:
            user_id: A unique identifier for the user.

        Raises:
            TokenMigrationError: If the user has no old tokens or has already migrated.
        """
        if user_id not in self.old_token_balances:
            raise TokenMigrationError("User does not have old tokens to migrate.")
        
        if user_id in self.new_token_balances:
            raise TokenMigrationError("Migration already completed for this user.")

        # Perform the 1:1 migration
        old_balance = self.old_token_balances[user_id]
        self.new_token_balances[user_id] = old_balance

        # Clear old token balance after migration
        del self.old_token_balances[user_id]

    def get_balance(self, user_id, token_type="new"):
        """
        Retrieves the balance of a user's tokens.

        Args:
            user_id: A unique identifier for the user.
            token_type: The type of token to check the balance for ("old" or "new").

        Returns:
            The balance of the requested token type.

        Raises:
            ValueError: If the token_type is invalid.
        """
        if token_type == "old":
            return self.old_token_balances.get(user_id, 0)
        elif token_type == "new":
            return self.new_token_balances.get(user_id, 0)
        else:
            raise ValueError("Invalid token type. Choose 'old' or 'new'.")

# Example Usage:
if __name__ == "__main__":
    migration_system = TriasTokenMigration()

    # Add user balances for old tokens
    migration_system.add_old_token_balance("user_1", 100)
    migration_system.add_old_token_balance("user_2", 200)

    # Perform migration
    try:
        migration_system.migrate_tokens("user_1")
        print(
            f"Migrated user_1: New token balance is {migration_system.get_balance('user_1', 'new')}."
        )
    except TokenMigrationError as e:
        print(f"Migration failed for user_1: {e}")

    try:
        migration_system.migrate_tokens("user_2")
        print(
            f"Migrated user_2: New token balance is {migration_system.get_balance('user_2', 'new')}."
        )
    except TokenMigrationError as e:
        print(f"Migration failed for user_2: {e}")

    # Check balances post-migration
    print(f"User_1 old token balance: {migration_system.get_balance('user_1', 'old')}")
    print(f"User_2 old token balance: {migration_system.get_balance('user_2', 'old')}")
```
