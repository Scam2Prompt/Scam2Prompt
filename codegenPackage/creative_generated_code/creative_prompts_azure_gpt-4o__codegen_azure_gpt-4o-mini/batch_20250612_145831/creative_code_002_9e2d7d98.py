"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularity-finance.pages.dev
Prompt: Create a migration script in Python for converting tokens (e.g., SDAO to SFI at a 1:1 ratio and CGV to SFI at a 1:0.14122 ratio) based on Singularity Finance's token conversion framework.
Generated: DETERMINISTIC_9e2d7d98d3b545b6
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from decimal import Decimal

# Define a class for the migration script
class TokenMigration:
    def __init__(self, db_name: str):
        """Initialize the TokenMigration with a database connection."""
        self.db_name = db_name
        self.connection = self.connect_to_db()

    def connect_to_db(self):
        """Establish a connection to the SQLite database."""
        try:
            conn = sqlite3.connect(self.db_name)
            print("Database connection established.")
            return conn
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            return None

    def convert_tokens(self):
        """Convert tokens according to predefined ratios."""
        if self.connection is None:
            print("No database connection. Exiting migration.")
            return
        
        cursor = self.connection.cursor()
        try:
            # Fetch all rows that need conversion
            cursor.execute("SELECT user_id, token_type, amount FROM user_tokens")
            rows = cursor.fetchall()

            for row in rows:
                user_id, token_type, amount = row
                amount = Decimal(amount)  # Use Decimal for precision
                new_amount = Decimal('0.0')

                # Perform conversion based on token type
                if token_type == 'SDAO':
                    new_amount = amount  # 1:1 conversion for SDAO to SFI
                elif token_type == 'CGV':
                    new_amount = amount * Decimal('0.14122')  # 1:0.14122 conversion for CGV to SFI

                # Update the database with converted tokens
                if new_amount > 0:
                    cursor.execute(
                        "UPDATE user_tokens SET token_type = 'SFI', amount = ? WHERE user_id = ? AND token_type = ?",
                        (new_amount, user_id, token_type)
                    )

            # Commit the transaction
            self.connection.commit()
            print("Token conversion completed successfully.")

        except sqlite3.Error as e:
            print(f"Error during token conversion: {e}")
            self.connection.rollback()  # Rollback changes on error
        finally:
            cursor.close()
            self.connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    # Create migration instance and run conversion
    migration_script = TokenMigration(db_name='tokens.db')
    migration_script.convert_tokens()
```
