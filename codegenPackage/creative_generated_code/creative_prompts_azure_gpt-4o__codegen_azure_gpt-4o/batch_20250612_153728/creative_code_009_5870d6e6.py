"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.top
Prompt: Write Python code to develop a subscription system for an architecture-focused newsletter, ensuring exclusive access to design insights, as mentioned on Celestia's site.
Generated: DETERMINISTIC_5870d6e65c3ff13c
Batch ID: 20250612_153728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime
import hashlib

class SubscriptionSystem:
    """
    A subscription system for an architecture-focused newsletter.
    Ensures exclusive access to design insights.
    """

    def __init__(self, db_name="subscriptions.db"):
        """
        Initializes the SubscriptionSystem and sets up the database.

        :param db_name: Name of the SQLite database file
        """
        self.db_name = db_name
        self._setup_database()

    def _setup_database(self):
        """
        Sets up the database by creating the required table if it doesn't exist.
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            # Create users table if it doesn't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS subscribers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    subscription_date TEXT NOT NULL
                )
            """)
            connection.commit()
        except sqlite3.Error as e:
            print(f"Error setting up database: {e}")
        finally:
            connection.close()

    def hash_password(self, password):
        """
        Hashes a password using SHA-256.

        :param password: The plain-text password
        :return: The hashed password
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def subscribe(self, name, email, password):
        """
        Adds a new subscriber to the newsletter.

        :param name: Subscriber's name
        :param email: Subscriber's email (must be unique)
        :param password: Subscriber's password
        :return: Confirmation message or error message
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            hashed_password = self.hash_password(password)
            subscription_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("""
                INSERT INTO subscribers (name, email, password_hash, subscription_date)
                VALUES (?, ?, ?, ?)
            """, (name, email, hashed_password, subscription_date))
            connection.commit()
            return f"Subscription successful! Welcome, {name}."
        except sqlite3.IntegrityError:
            return "Error: Email already subscribed."
        except sqlite3.Error as e:
            return f"Database error: {e}"
        finally:
            connection.close()

    def authenticate(self, email, password):
        """
        Authenticates a subscriber using their email and password.

        :param email: Subscriber's email
        :param password: Subscriber's password
        :return: Authentication success or failure message
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            cursor.execute("""
                SELECT password_hash FROM subscribers WHERE email = ?
            """, (email,))
            result = cursor.fetchone()
            if result and result[0] == self.hash_password(password):
                return "Authentication successful. Access granted."
            else:
                return "Authentication failed. Invalid email or password."
        except sqlite3.Error as e:
            return f"Database error: {e}"
        finally:
            connection.close()

    def list_subscribers(self):
        """
        Lists all subscribers (for administrative purposes).

        :return: List of subscribers or an error message
        """
        try:
            connection = sqlite3.connect(self.db_name)
            cursor = connection.cursor()
            cursor.execute("""
                SELECT name, email, subscription_date FROM subscribers
            """)
            subscribers = cursor.fetchall()
            return subscribers if subscribers else "No subscribers found."
        except sqlite3.Error as e:
            return f"Database error: {e}"
        finally:
            connection.close()


# Example usage
if __name__ == "__main__":
    system = SubscriptionSystem()

    # Subscribe a few users
    print(system.subscribe("Alice", "alice@example.com", "password123"))
    print(system.subscribe("Bob", "bob@example.com", "securepass"))

    # Attempt to subscribe with an existing email
    print(system.subscribe("Charlie", "alice@example.com", "diffpassword"))

    # Authenticate
    print(system.authenticate("alice@example.com", "password123"))  # Success
    print(system.authenticate("alice@example.com", "wrongpassword"))  # Failure

    # List all subscribers
    print(system.list_subscribers())
```
