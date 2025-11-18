"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-elevate.com
Prompt: Create a script that connects users to investment education firms after registration on Immediate Elevate, simulating the "Instant Connection" feature described on the website.
Generated: DETERMINISTIC_9f24923693f22146
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InvestmentEducationConnector:
    """A class to handle user registration and connection to investment education firms."""

    def __init__(self, db_name='investment_firms.db'):
        """Initialize the database connection and create tables if they don't exist."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        """Create necessary tables for users and investment firms."""
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE
                )
            ''')
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS investment_firms (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    firm_name TEXT NOT NULL,
                    contact_info TEXT NOT NULL
                )
            ''')
            self.connection.commit()
            logging.info('Tables created successfully or already exist.')
        except sqlite3.Error as e:
            logging.error(f"Error creating tables: {e}")

    def register_user(self, name, email):
        """Register a new user and connect them to an investment education firm."""
        try:
            self.cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
            user_id = self.cursor.lastrowid
            self.connection.commit()
            logging.info(f"User registered with ID: {user_id}")
            self.connect_user_to_firm(user_id)
        except sqlite3.IntegrityError:
            logging.error(f"Email {email} already exists. Registration failed.")
            raise ValueError(f"Email {email} is already registered.")
        except sqlite3.Error as e:
            logging.error(f"Error registering user: {e}")
            raise RuntimeError("An error occurred while registering the user.")

    def connect_user_to_firm(self, user_id):
        """Simulate connecting a user to a randomly selected investment education firm."""
        try:
            # Example firm data (in a real application, this should come from a database or API)
            firms = [
                {"firm_name": "Wealth Builders", "contact_info": "contact@wealthbuilders.com"},
                {"firm_name": "Investment Masters", "contact_info": "info@investmentmasters.com"},
                {"firm_name": "Future Investments", "contact_info": "support@futureinvestments.com"}
            ]
            # Simulating a connection by randomly selecting a firm (for simplicity)
            import random
            firm = random.choice(firms)
            logging.info(f"User ID {user_id} connected to firm: {firm['firm_name']} with contact info: {firm['contact_info']}")
            return firm
        except Exception as e:
            logging.error(f"Error connecting user to firm: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            logging.info('Database connection closed.')

if __name__ == '__main__':
    connector = InvestmentEducationConnector()
    try:
        # Example user registration
        connector.register_user("John Doe", "john@example.com")
    except ValueError as ve:
        logging.error(ve)
    except RuntimeError as re:
        logging.error(re)
    finally:
        connector.close_connection()
```
