"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtimecodes.pages.dev
Prompt: Implement code for crafting and upgrading Hourglasses using the Time Warden's features in Big Time, ensuring integration with the $BIGTIME token economy.
Generated: DETERMINISTIC_fc0e0c89887baa97
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import time
import random

class TimeWarden:
    """
    Time Warden class facilitates crafting and upgrading Hourglasses.
    It integrates with the $BIGTIME token economy.
    """

    def __init__(self):
        """
        Initialize the Time Warden, setting up the token balance and database connection.
        """
        self.token_balance = 0  # Initial $BIGTIME token balance
        self.db_connection = sqlite3.connect('hourglasses.db')
        self._setup_database()

    def _setup_database(self):
        """
        Setup the database schema for storing Hourglass data.
        """
        cursor = self.db_connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS hourglasses (
                id INTEGER PRIMARY KEY,
                level INTEGER,
                durability INTEGER
            )
        ''')
        self.db_connection.commit()

    def add_tokens(self, amount):
        """
        Add $BIGTIME tokens to the Time Warden's balance.

        :param amount: Amount of tokens to add.
        """
        if amount < 0:
            raise ValueError("Amount of tokens to add must be non-negative.")
        self.token_balance += amount

    def craft_hourglass(self):
        """
        Craft a new Hourglass.

        :return: The newly created Hourglass ID.
        """
        token_cost = 10  # Crafting cost in $BIGTIME tokens
        if self.token_balance < token_cost:
            raise ValueError("Insufficient $BIGTIME tokens to craft an Hourglass.")
        
        self.token_balance -= token_cost
        new_hourglass = {
            'level': 1,  # Hourglass starts at level 1
            'durability': 100  # Initial durability
        }

        cursor = self.db_connection.cursor()
        cursor.execute('''
            INSERT INTO hourglasses (level, durability)
            VALUES (:level, :durability)
        ''', new_hourglass)
        self.db_connection.commit()

        return cursor.lastrowid

    def upgrade_hourglass(self, hourglass_id):
        """
        Upgrade an existing Hourglass to the next level.

        :param hourglass_id: ID of the Hourglass to upgrade.
        :return: Updated Hourglass data.
        """
        token_cost_per_level = 15  # Upgrade cost per level in $BIGTIME tokens
        
        cursor = self.db_connection.cursor()
        cursor.execute('SELECT level, durability FROM hourglasses WHERE id = ?', (hourglass_id,))
        result = cursor.fetchone()
        
        if not result:
            raise ValueError(f"No Hourglass found with ID {hourglass_id}.")
        
        current_level, current_durability = result
        upgrade_cost = token_cost_per_level * current_level
        
        if self.token_balance < upgrade_cost:
            raise ValueError("Insufficient $BIGTIME tokens to upgrade the Hourglass.")
        if current_durability <= 0:
            raise ValueError("Cannot upgrade a broken Hourglass (durability 0).")
        
        # Deduct tokens and upgrade hourglass
        self.token_balance -= upgrade_cost
        new_level = current_level + 1
        new_durability = current_durability - random.randint(10, 30)  # Durability decreases randomly on upgrade
        
        cursor.execute('''
            UPDATE hourglasses
            SET level = ?, durability = ?
            WHERE id = ?
        ''', (new_level, new_durability, hourglass_id))
        self.db_connection.commit()

        return {'id': hourglass_id, 'level': new_level, 'durability': new_durability}

    def fetch_hourglass(self, hourglass_id):
        """
        Retrieve data of an Hourglass by ID.

        :param hourglass_id: ID of the Hourglass to fetch.
        :return: Hourglass data.
        """
        cursor = self.db_connection.cursor()
        cursor.execute('SELECT id, level, durability FROM hourglasses WHERE id = ?', (hourglass_id,))
        result = cursor.fetchone()

        if not result:
            return None
        
        return {'id': result[0], 'level': result[1], 'durability': result[2]}

    def close(self):
        """
        Close the database connection.
        """
        self.db_connection.close()


# Example usage
if __name__ == "__main__":
    try:
        warden = TimeWarden()
        
        # Add $BIGTIME tokens
        warden.add_tokens(100)

        # Craft an Hourglass
        hourglass_id = warden.craft_hourglass()
        print(f"Crafted Hourglass ID: {hourglass_id}")

        # Upgrade the Hourglass
        upgraded_hourglass = warden.upgrade_hourglass(hourglass_id)
        print(f"Upgraded Hourglass: {upgraded_hourglass}")

        # Fetch Hourglass data
        fetched_hourglass = warden.fetch_hourglass(hourglass_id)
        print(f"Fetched Hourglass: {fetched_hourglass}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        warden.close()
```
