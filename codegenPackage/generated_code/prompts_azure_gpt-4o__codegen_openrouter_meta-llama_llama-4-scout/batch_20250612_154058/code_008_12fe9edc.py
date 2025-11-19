"""
Generated Code Metadata:
========================
Original URL: https://bonanzavc.com
Prompt: Write a Python function to generate unique referral codes for users upon registration, ensuring the codes are securely stored in a database.
Generated: DETERMINISTIC_12fe9edc2bae3c1c
Batch ID: 20250612_154058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import secrets
import string
from typing import Optional
import sqlite3
from sqlite3 import Error

class ReferralCodeGenerator:
    def __init__(self, db_name: str):
        """
        Initialize the ReferralCodeGenerator with a database name.

        :param db_name: The name of the SQLite database file.
        """
        self.db_name = db_name
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            self.create_table()
        except Error as e:
            print(e)

    def create_table(self):
        """
        Create a table to store referral codes if it doesn't exist.
        """
        query = """
            CREATE TABLE IF NOT EXISTS referral_codes
            (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER UNIQUE, referral_code TEXT UNIQUE)
        """
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except Error as e:
            print(e)

    def generate_referral_code(self, length: int = 8) -> str:
        """
        Generate a unique referral code.

        :param length: The length of the referral code.
        :return: A unique referral code.
        """
        characters = string.ascii_uppercase + string.digits
        while True:
            code = ''.join(secrets.choice(characters) for _ in range(length))
            if not self.check_code_exists(code):
                return code

    def check_code_exists(self, code: str) -> bool:
        """
        Check if a referral code already exists in the database.

        :param code: The referral code to check.
        :return: True if the code exists, False otherwise.
        """
        query = "SELECT 1 FROM referral_codes WHERE referral_code = ?"
        try:
            self.cursor.execute(query, (code,))
            return self.cursor.fetchone() is not None
        except Error as e:
            print(e)
            return True

    def store_referral_code(self, user_id: int, referral_code: str) -> bool:
        """
        Store a referral code in the database.

        :param user_id: The ID of the user.
        :param referral_code: The referral code to store.
        :return: True if the code was stored successfully, False otherwise.
        """
        query = "INSERT INTO referral_codes (user_id, referral_code) VALUES (?, ?)"
        try:
            self.cursor.execute(query, (user_id, referral_code))
            self.conn.commit()
            return True
        except Error as e:
            print(e)
            return False

    def get_referral_code(self, user_id: int) -> Optional[str]:
        """
        Retrieve a referral code for a given user ID.

        :param user_id: The ID of the user.
        :return: The referral code if found, None otherwise.
        """
        query = "SELECT referral_code FROM referral_codes WHERE user_id = ?"
        try:
            self.cursor.execute(query, (user_id,))
            result = self.cursor.fetchone()
            return result[0] if result else None
        except Error as e:
            print(e)
            return None

    def close_connection(self):
        """
        Close the database connection.
        """
        if self.conn:
            self.conn.close()


# Example usage:
if __name__ == "__main__":
    generator = ReferralCodeGenerator("referral_codes.db")
    user_id = 1
    referral_code = generator.generate_referral_code()
    print(f"Generated referral code: {referral_code}")
    stored = generator.store_referral_code(user_id, referral_code)
    print(f"Referral code stored: {stored}")
    retrieved_code = generator.get_referral_code(user_id)
    print(f"Retrieved referral code: {retrieved_code}")
    generator.close_connection()
```
