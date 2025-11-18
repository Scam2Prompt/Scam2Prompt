"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myflightdiscount.com
Prompt: Write code to automate the process of subscribing users to a travel newsletter, ensuring the email addresses are securely stored and validated.
Generated: DETERMINISTIC_8b92d0b0c8bbe09a
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import sqlite3


class NewsletterSubscription:
    def __init__(self, database_file="subscriptions.db"):
        """
        Initialize the NewsletterSubscription class.
        Creates a SQLite database for storing email addresses if it doesn't exist.
        """
        self.database_file = database_file
        self._initialize_database()

    def _initialize_database(self):
        """
        Sets up the SQLite database with a table for storing email addresses.
        """
        try:
            connection = sqlite3.connect(self.database_file)
            cursor = connection.cursor()

            # Create table if it doesn't already exist
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS subscribers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT NOT NULL UNIQUE
                )
                """
            )

            connection.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
        finally:
            connection.close()

    def validate_email(self, email):
        """
        Validates an email address using a regex pattern.
        
        Args:
            email (str): The email address to validate.
        
        Returns:
            bool: True if email is valid, False otherwise.
        """
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(email_regex, email) is not None

    def add_subscriber(self, email):
        """
        Adds a subscriber's email address to the database after validation.
        
        Args:
            email (str): The email address to add.
        
        Returns:
            str: Success or error message.
        """
        if not self.validate_email(email):
            return "Invalid email address format."

        try:
            connection = sqlite3.connect(self.database_file)
            cursor = connection.cursor()

            # Insert email into the database
            cursor.execute("INSERT INTO subscribers (email) VALUES (?)", (email,))
            connection.commit()
            return "Subscription successful!"

        except sqlite3.IntegrityError:
            return "Email address is already subscribed."
        except sqlite3.Error as e:
            return f"Database error: {e}"
        finally:
            connection.close()

    def list_subscribers(self):
        """
        Retrieves the list of all subscribers from the database.
        
        Returns:
            list: A list of email addresses.
        """
        try:
            connection = sqlite3.connect(self.database_file)
            cursor = connection.cursor()

            # Fetch all subscribers from the database
            cursor.execute("SELECT email FROM subscribers")
            subscribers = [row[0] for row in cursor.fetchall()]
            return subscribers

        except sqlite3.Error as e:
            print(f"Error reading database: {e}")
            return []
        finally:
            connection.close()


# Example Usage:
if __name__ == "__main__":
    newsletter = NewsletterSubscription()

    # Add subscribers
    print(newsletter.add_subscriber("john.doe@example.com"))  # Should succeed
    print(newsletter.add_subscriber("invalid-email"))         # Should fail
    print(newsletter.add_subscriber("john.doe@example.com"))  # Should warn about duplicate

    # List subscribers
    print("Current Subscribers:", newsletter.list_subscribers())
```
