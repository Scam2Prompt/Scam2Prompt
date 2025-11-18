"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonaeac.com
Prompt: Develop a referral code validation system in Python that checks if the referral code provided during registration exists in the database, as described on bonaeac.com.
Generated: DETERMINISTIC_d0e52be2acf9d008
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

class ReferralCodeValidator:
    """
    A class to validate referral codes during user registration.
    Connects to a database to verify the existence of referral codes.
    """

    def __init__(self, db_path):
        """
        Initializes the validator with a connection to the database.

        :param db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self._connect_to_database()

    def _connect_to_database(self):
        """
        Establishes a connection to the SQLite database.
        """
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            raise Exception(f"Database connection error: {e}")

    def validate_referral_code(self, referral_code):
        """
        Validates the provided referral code by checking its existence in the database.

        :param referral_code: The referral code to validate.
        :return: Boolean indicating whether the referral code exists.
        """
        try:
            query = "SELECT COUNT(*) FROM referral_codes WHERE code = ?"
            self.cursor.execute(query, (referral_code,))
            result = self.cursor.fetchone()

            # If the count is greater than 0, the referral code exists
            return result[0] > 0
        except sqlite3.Error as e:
            raise Exception(f"Database query error: {e}")

    def close_connection(self):
        """
        Closes the connection to the database.
        """
        try:
            if self.conn:
                self.conn.close()
        except sqlite3.Error as e:
            print(f"Error while closing the database connection: {e}")


# Example usage:
if __name__ == "__main__":
    # Path to your SQLite database file
    database_path = "referral_codes.db"

    # Create instance of the validator
    validator = ReferralCodeValidator(database_path)

    try:
        # Input referral code for validation
        referral_code = input("Please enter the referral code: ").strip()

        # Validate the referral code
        if validator.validate_referral_code(referral_code):
            print("Referral code is valid!")
        else:
            print("Referral code is invalid!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the database connection is closed
        validator.close_connection()
```

### Notes:
- This code assumes your database has a table named `referral_codes` with a column `code` that stores referral codes.
- Replace `"referral_codes.db"` with the path to your database file.
- Ensure the database and table structure are correctly set up before running the code.
