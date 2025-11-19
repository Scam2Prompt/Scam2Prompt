"""
Generated Code Metadata:
========================
Original URL: https://devv.sellpass.io
Prompt: Write a script to integrate a customer login system with error handling, inspired by the services offered by Devv.
Generated: DETERMINISTIC_80003a872d4768c5
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import sqlite3
from getpass import getpass
from typing import Optional, Tuple

class CustomerLoginSystem:
    """
    A secure customer login system with error handling.
    Handles user registration, authentication, and session management.
    """
    
    def __init__(self, db_name: str = "customer_auth.db"):
        """
        Initialize the login system with a SQLite database.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.db_name = db_name
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Create the database tables if they don't exist."""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS customers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password_hash TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS sessions (
                        session_id TEXT PRIMARY KEY,
                        customer_id INTEGER NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        expires_at TIMESTAMP NOT NULL,
                        FOREIGN KEY (customer_id) REFERENCES customers (id)
                    )
                """)
                conn.commit()
        except sqlite3.Error as e:
            raise RuntimeError(f"Database initialization failed: {str(e)}")
    
    def _hash_password(self, password: str) -> str:
        """
        Securely hash a password using SHA-256 with salt.
        
        Args:
            password: Plain text password to hash
            
        Returns:
            Hashed password as hex string
        """
        salt = "devv_secure_salt"
        return hashlib.sha256((password + salt).encode()).hexdigest()
    
    def register_customer(self, username: str, email: str, password: str) -> bool:
        """
        Register a new customer with username, email, and password.
        
        Args:
            username: Unique username
            email: Unique email address
            password: Plain text password
            
        Returns:
            True if registration succeeded, False otherwise
            
        Raises:
            ValueError: If input validation fails
            RuntimeError: If database operation fails
        """
        if not username or not email or not password:
            raise ValueError("Username, email, and password are required")
        
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")
        
        password_hash = self._hash_password(password)
        
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO customers (username, password_hash, email) VALUES (?, ?, ?)",
                    (username, password_hash, email)
                )
                conn.commit()
                return True
        except sqlite3.IntegrityError as e:
            if "username" in str(e):
                raise ValueError("Username already exists")
            elif "email" in str(e):
                raise ValueError("Email already exists")
            raise RuntimeError(f"Registration failed: {str(e)}")
        except sqlite3.Error as e:
            raise RuntimeError(f"Database error during registration: {str(e)}")
    
    def authenticate_customer(self, username: str, password: str) -> Optional[int]:
        """
        Authenticate a customer with username and password.
        
        Args:
            username: Customer username
            password: Plain text password
            
        Returns:
            Customer ID if authentication succeeds, None otherwise
            
        Raises:
            RuntimeError: If database operation fails
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT id, password_hash FROM customers WHERE username = ?",
                    (username,)
                )
                result = cursor.fetchone()
                
                if result:
                    customer_id, stored_hash = result
                    if self._hash_password(password) == stored_hash:
                        return customer_id
                return None
        except sqlite3.Error as e:
            raise RuntimeError(f"Authentication failed: {str(e)}")
    
    def create_session(self, customer_id: int) -> str:
        """
        Create a new session for an authenticated customer.
        
        Args:
            customer_id: Authenticated customer ID
            
        Returns:
            Session ID string
            
        Raises:
            RuntimeError: If database operation fails
        """
        import uuid
        import datetime
        
        session_id = str(uuid.uuid4())
        expires_at = datetime.datetime.now() + datetime.timedelta(hours=24)
        
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO sessions (session_id, customer_id, expires_at) VALUES (?, ?, ?)",
                    (session_id, customer_id, expires_at)
                )
                conn.commit()
                return session_id
        except sqlite3.Error as e:
            raise RuntimeError(f"Session creation failed: {str(e)}")
    
    def validate_session(self, session_id: str) -> Tuple[bool, Optional[int]]:
        """
        Validate a session ID and return customer ID if valid.
        
        Args:
            session_id: Session ID to validate
            
        Returns:
            Tuple of (is_valid, customer_id)
            
        Raises:
            RuntimeError: If database operation fails
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT customer_id, expires_at FROM sessions WHERE session_id = ?",
                    (session_id,)
                )
                result = cursor.fetchone()
                
                if result:
                    customer_id, expires_at = result
                    if expires_at > datetime.datetime.now():
                        return (True, customer_id)
                    
                    # Clean up expired session
                    cursor.execute(
                        "DELETE FROM sessions WHERE session_id = ?",
                        (session_id,)
                    )
                    conn.commit()
                return (False, None)
        except sqlite3.Error as e:
            raise RuntimeError(f"Session validation failed: {str(e)}")


def interactive_login(system: CustomerLoginSystem) -> None:
    """
    Interactive command-line interface for the login system.
    
    Args:
        system: Initialized CustomerLoginSystem instance
    """
    import datetime
    
    print("Customer Login System")
    while True:
        print("\nOptions:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            try:
                username = input("Username: ")
                email = input("Email: ")
                password = getpass("Password: ")
                
                if system.register_customer(username, email, password):
                    print("Registration successful!")
                else:
                    print("Registration failed")
            except ValueError as e:
                print(f"Error: {str(e)}")
            except RuntimeError as e:
                print(f"System error: {str(e)}")
        
        elif choice == "2":
            try:
                username = input("Username: ")
                password = getpass("Password: ")
                
                customer_id = system.authenticate_customer(username, password)
                if customer_id:
                    session_id = system.create_session(customer_id)
                    print(f"Login successful! Session ID: {session_id}")
                else:
                    print("Invalid username or password")
            except RuntimeError as e:
                print(f"System error: {str(e)}")
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again")


if __name__ == "__main__":
    try:
        login_system = CustomerLoginSystem()
        interactive_login(login_system)
    except Exception as e:
        print(f"Fatal error: {str(e)}")
```
