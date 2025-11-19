"""
Generated Code Metadata:
========================
Original URL: https://jhpsgaya.com
Prompt: Write a code to create a simple login system for a school website with features like user authentication and authorization.
Generated: DETERMINISTIC_7eca4706b3c7a9a7
Batch ID: 20250622_212312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import sqlite3
from getpass import getpass
from hashlib import sha256

# Define a class for the login system
class LoginSystem:
    def __init__(self, db_name):
        """
        Initialize the login system with a database connection.

        Args:
            db_name (str): The name of the database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Create a table for users if it does not exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users
            (username TEXT PRIMARY KEY, password TEXT, role TEXT)
        ''')
        self.conn.commit()

    def register(self, username, password, role):
        """
        Register a new user.

        Args:
            username (str): The username chosen by the user.
            password (str): The password chosen by the user.
            role (str): The role of the user (e.g., student, teacher, admin).

        Returns:
            bool: True if the registration was successful, False otherwise.
        """
        try:
            hashed_password = sha256(password.encode()).hexdigest()
            self.cursor.execute('INSERT INTO users VALUES (?, ?, ?)', 
                                (username, hashed_password, role))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            print("Username already exists.")
            return False

    def login(self, username, password):
        """
        Login an existing user.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.

        Returns:
            tuple: A tuple containing the username and role of the user if the login was successful, None otherwise.
        """
        try:
            hashed_password = sha256(password.encode()).hexdigest()
            self.cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', 
                                (username, hashed_password))
            user = self.cursor.fetchone()
            if user:
                return user[0], user[2]
            else:
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def authorize(self, username, role):
        """
        Check if a user has a certain role.

        Args:
            username (str): The username of the user.
            role (str): The role to check.

        Returns:
            bool: True if the user has the specified role, False otherwise.
        """
        try:
            self.cursor.execute('SELECT role FROM users WHERE username = ?', 
                                (username,))
            user_role = self.cursor.fetchone()
            if user_role and user_role[0] == role:
                return True
            else:
                return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def close_connection(self):
        """
        Close the database connection.
        """
        self.conn.close()


def main():
    login_system = LoginSystem('school.db')

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter a username: ")
            password = getpass("Enter a password: ")
            role = input("Enter a role (e.g., student, teacher, admin): ")
            if login_system.register(username, password, role):
                print("Registration successful.")
        elif choice == '2':
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")
            user = login_system.login(username, password)
            if user:
                print(f"Login successful. You are a {user[1]}.")
                if login_system.authorize(username, 'admin'):
                    print("You have admin privileges.")
                elif login_system.authorize(username, 'teacher'):
                    print("You have teacher privileges.")
                elif login_system.authorize(username, 'student'):
                    print("You have student privileges.")
            else:
                print("Invalid username or password.")
        elif choice == '3':
            login_system.close_connection()
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
