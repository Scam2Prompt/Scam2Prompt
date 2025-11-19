"""
Generated Code Metadata:
========================
Original URL: https://client-website1.pages.dev
Prompt: Provide code examples for implementing a subscription system for publications, similar to the "Subscribe to our publications" feature on the Innodapter ApS website.
Generated: DETERMINISTIC_21685822281fa783
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# subscription_system.py

import sqlite3
from sqlite3 import Error

class SubscriptionSystem:
    def __init__(self, db_file):
        """Initialize the subscription system with a database connection."""
        self.connection = self.create_connection(db_file)
        self.create_subscriptions_table()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"Error '{e}' occurred while connecting to the database")
        return conn

    def create_subscriptions_table(self):
        """Create the subscriptions table if it doesn't exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            self.connection.commit()
        except Error as e:
            print(f"Error '{e}' occurred while creating the table")

    def subscribe(self, email):
        """Subscribe a user to the publication."""
        if self.is_valid_email(email):
            try:
                cursor = self.connection.cursor()
                cursor.execute("INSERT INTO subscriptions (email) VALUES (?)", (email,))
                self.connection.commit()
                print(f"Successfully subscribed {email}")
            except Error as e:
                print(f"Error '{e}' occurred while subscribing the email")
        else:
            print("Invalid email format")

    def is_valid_email(self, email):
        """Validate the email format."""
        import re
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def unsubscribe(self, email):
        """Unsubscribe a user from the publication."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM subscriptions WHERE email = ?", (email,))
            self.connection.commit()
            if cursor.rowcount > 0:
                print(f"Successfully unsubscribed {email}")
            else:
                print(f"No subscription found for {email}")
        except Error as e:
            print(f"Error '{e}' occurred while unsubscribing the email")

    def list_subscriptions(self):
        """List all subscribed emails."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT email FROM subscriptions")
            rows = cursor.fetchall()
            return [row[0] for row in rows]
        except Error as e:
            print(f"Error '{e}' occurred while fetching subscriptions")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed")

# Example usage
if __name__ == "__main__":
    subscription_system = SubscriptionSystem("subscriptions.db")
    subscription_system.subscribe("user@example.com")
    print(subscription_system.list_subscriptions())
    subscription_system.unsubscribe("user@example.com")
    subscription_system.close_connection()
```
