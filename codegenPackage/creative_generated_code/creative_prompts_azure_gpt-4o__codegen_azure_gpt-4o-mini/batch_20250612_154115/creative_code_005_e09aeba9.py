"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orikod.com
Prompt: Generate code to blacklist wallets associated with bot activity or duplicate entries during an airdrop claim process.
Generated: DETERMINISTIC_e09aeba9a64fb9b2
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

class AirdropManager:
    """
    A class to manage airdrop claims and blacklist wallets associated with bot activity or duplicate entries.
    """

    def __init__(self, db_name='airdrop.db'):
        """
        Initializes the AirdropManager with a SQLite database.
        
        Args:
            db_name (str): The name of the SQLite database file.
        """
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """
        Creates the necessary database tables for airdrop claims and blacklisted wallets if they do not exist.
        """
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS claims (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    wallet_address TEXT UNIQUE NOT NULL,
                    claimed_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS blacklist (
                    wallet_address TEXT UNIQUE NOT NULL,
                    reason TEXT NOT NULL,
                    added_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')

    def claim_airdrop(self, wallet_address):
        """
        Processes an airdrop claim for a given wallet address.

        Args:
            wallet_address (str): The wallet address claiming the airdrop.

        Raises:
            ValueError: If the wallet address is blacklisted or a claim already exists.
        """
        if self.is_blacklisted(wallet_address):
            raise ValueError(f"Wallet address {wallet_address} is blacklisted.")

        try:
            with self.connection:
                self.connection.execute('INSERT INTO claims (wallet_address) VALUES (?)', (wallet_address,))
        except sqlite3.IntegrityError:
            raise ValueError(f"Wallet address {wallet_address} has already claimed the airdrop.")

    def is_blacklisted(self, wallet_address):
        """
        Checks if a wallet address is blacklisted.

        Args:
            wallet_address (str): The wallet address to check.

        Returns:
            bool: True if the wallet is blacklisted, False otherwise.
        """
        cursor = self.connection.cursor()
        cursor.execute('SELECT 1 FROM blacklist WHERE wallet_address = ?', (wallet_address,))
        return cursor.fetchone() is not None

    def blacklist_wallet(self, wallet_address, reason):
        """
        Adds a wallet address to the blacklist.

        Args:
            wallet_address (str): The wallet address to blacklist.
            reason (str): The reason for blacklisting the wallet.

        Raises:
            ValueError: If the wallet address is already blacklisted.
        """
        if self.is_blacklisted(wallet_address):
            raise ValueError(f"Wallet address {wallet_address} is already blacklisted.")

        with self.connection:
            self.connection.execute('INSERT INTO blacklist (wallet_address, reason) VALUES (?, ?)', 
                                    (wallet_address, reason))

    def close(self):
        """
        Closes the database connection.
        """
        self.connection.close()


# Example usage of the AirdropManager class:
if __name__ == "__main__":
    manager = AirdropManager()

    # Blacklisting a wallet
    try:
        manager.blacklist_wallet('0x123456789abcdef', 'Detected bot activity')
    except ValueError as e:
        print(e)

    # Trying to claim an airdrop
    try:
        manager.claim_airdrop('0x123456789abcdef')
    except ValueError as e:
        print(e)
    
    # Close the database connection
    manager.close()
```
