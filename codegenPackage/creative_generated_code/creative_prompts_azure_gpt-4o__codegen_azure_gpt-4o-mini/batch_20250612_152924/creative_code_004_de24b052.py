"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularity-dao.pages.dev
Prompt: Create a function that calculates the amount of RJV NEW tokens to be received based on the balance of RJV OLD tokens, referencing the SingularityDAO migration process.
Generated: DETERMINISTIC_de24b052f8842063
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenMigrationError(Exception):
    """Custom exception for handling token migration errors."""
    pass


def calculate_new_tokens(old_tokens: float, migration_rate: float) -> float:
    """
    Calculate the amount of RJV NEW tokens to be received based on the balance of RJV OLD tokens.

    Parameters:
    old_tokens (float): The amount of RJV OLD tokens to be migrated.
    migration_rate (float): The rate at which RJV OLD tokens are converted to RJV NEW tokens.

    Returns:
    float: The amount of RJV NEW tokens to be received.

    Raises:
    TokenMigrationError: If the old_tokens or migration_rate are negative or if the migration_rate is zero.
    """
    # Validate inputs
    if old_tokens < 0:
        raise TokenMigrationError("Old tokens amount cannot be negative.")
    if migration_rate <= 0:
        raise TokenMigrationError("Migration rate must be greater than zero.")

    # Calculate the amount of new tokens
    new_tokens = old_tokens * migration_rate
    
    return new_tokens


def main():
    """Main function to execute the token migration calculation."""
    try:
        # Example values; in a real scenario, these would be fetched from user input or a database
        old_tokens = 1000.0  # Amount of RJV OLD tokens
        migration_rate = 1.5  # Migration rate

        # Calculate the new tokens
        new_tokens = calculate_new_tokens(old_tokens, migration_rate)

        print(f"Amount of RJV NEW tokens to be received: {new_tokens}")

    except TokenMigrationError as e:
        print(f"Error during token migration: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
