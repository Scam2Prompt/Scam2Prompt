"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bankai-app.pages.dev
Prompt: Write a function to check the migratable balance of a user based on the BankPad migration details.
Generated: DETERMINISTIC_0df95a863af0e040
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BankPadMigration:
    def __init__(self, user_balance, migration_limit):
        """
        Initialize the BankPadMigration instance.

        :param user_balance: Current balance of the user.
        :param migration_limit: Maximum balance that can be migrated.
        """
        self.user_balance = user_balance
        self.migration_limit = migration_limit

    def check_migratable_balance(self):
        """
        Check the migratable balance of the user.

        :return: A tuple containing the migratable balance and a message.
        """
        try:
            if self.user_balance < 0:
                raise ValueError("User balance cannot be negative.")

            # Determine the migratable balance
            migratable_balance = min(self.user_balance, self.migration_limit)
            
            return migratable_balance, "Migratable balance calculated successfully."
        
        except ValueError as ve:
            return 0, str(ve)  # Return 0 and the error message for negative balance
        except Exception as e:
            return 0, "An unexpected error occurred: " + str(e)  # General error handling

# Example usage
if __name__ == "__main__":
    user_balance = 1000  # Example user balance
    migration_limit = 800  # Example migration limit
    migration = BankPadMigration(user_balance, migration_limit)
    
    migratable_balance, message = migration.check_migratable_balance()
    print(f"Migratable Balance: {migratable_balance}, Message: {message}")
```
