"""
Generated Code Metadata:
========================
Original URL: https://grenoble-boxe.fr
Prompt: Generate a Python script to create a simple membership registration system for Team Mhiyaoui.
Generated: DETERMINISTIC_32d7ba533e6f962f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime
from getpass import getpass

class MembershipSystem:
    """A simple membership registration system for Team Mhiyaoui."""
    
    def __init__(self, db_name='membership.db'):
        """Initialize the membership system with database connection."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
        
    def _create_tables(self):
        """Create necessary tables if they don't exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS members (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                full_name TEXT NOT NULL,
                join_date TEXT NOT NULL,
                is_active INTEGER DEFAULT 1
            )
        ''')
        self.conn.commit()
    
    def register_member(self):
        """Register a new member."""
        print("\n--- Member Registration ---")
        username = input("Username: ").strip()
        
        # Check if username exists
        if self._member_exists(username):
            print("Error: Username already exists.")
            return False
        
        password = getpass("Password: ").strip()
        if not password:
            print("Error: Password cannot be empty.")
            return False
            
        email = input("Email: ").strip()
        if not self._validate_email(email):
            print("Error: Invalid email format.")
            return False
            
        full_name = input("Full Name: ").strip()
        if not full_name:
            print("Error: Full name cannot be empty.")
            return False
        
        try:
            join_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.cursor.execute('''
                INSERT INTO members (username, password, email, full_name, join_date)
                VALUES (?, ?, ?, ?, ?)
            ''', (username, password, email, full_name, join_date))
            self.conn.commit()
            print("Registration successful!")
            return True
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False
    
    def _member_exists(self, username):
        """Check if a member exists by username."""
        self.cursor.execute('SELECT id FROM members WHERE username = ?', (username,))
        return self.cursor.fetchone() is not None
    
    def _validate_email(self, email):
        """Basic email validation."""
        return '@' in email and '.' in email.split('@')[-1]
    
    def list_members(self):
        """List all active members."""
        try:
            self.cursor.execute('SELECT id, username, email, full_name, join_date FROM members WHERE is_active = 1')
            members = self.cursor.fetchall()
            
            if not members:
                print("No active members found.")
                return
            
            print("\n--- Active Members ---")
            for member in members:
                print(f"ID: {member[0]}, Username: {member[1]}, Email: {member[2]}, Name: {member[3]}, Joined: {member[4]}")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
    
    def deactivate_member(self):
        """Deactivate a member account."""
        username = input("Enter username to deactivate: ").strip()
        
        if not self._member_exists(username):
            print("Error: Member not found.")
            return False
            
        try:
            self.cursor.execute('UPDATE members SET is_active = 0 WHERE username = ?', (username,))
            self.conn.commit()
            print(f"Member '{username}' deactivated successfully.")
            return True
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False
    
    def close(self):
        """Close the database connection."""
        self.conn.close()

def main():
    """Main function to run the membership system."""
    system = MembershipSystem()
    
    while True:
        print("\nTeam Mhiyaoui Membership System")
        print("1. Register new member")
        print("2. List active members")
        print("3. Deactivate member")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            system.register_member()
        elif choice == '2':
            system.list_members()
        elif choice == '3':
            system.deactivate_member()
        elif choice == '4':
            system.close()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
