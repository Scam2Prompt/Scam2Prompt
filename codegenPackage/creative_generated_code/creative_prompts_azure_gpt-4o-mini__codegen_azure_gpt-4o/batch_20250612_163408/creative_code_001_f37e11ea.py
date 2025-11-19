"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://diverbox.com.pe
Prompt: Write a code snippet for a user login system that includes error handling for forgotten usernames or passwords, inspired by the functionality on diverbox.com.pe.
Generated: DETERMINISTIC_f37e11ea43d7ce97
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import sqlite3

# --- Database initialization ---
def initialize_database():
    """
    Initializes the SQLite database and creates a users table if it doesn't exist.
    """
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# --- User registration ---
def register_user(username, password, email):
    """
    Registers a new user by storing their username, hashed password, and email.
    """
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    try:
        # Hash the password before saving it
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        # Insert user data into the database
        cursor.execute('INSERT INTO users (username, password_hash, email) VALUES (?, ?, ?)',
                       (username, password_hash, email))
        conn.commit()
        print(f"User '{username}' registered successfully.")
    except sqlite3.IntegrityError as e:
        print("Error: Username or email already exists. Please try again.")
    finally:
        conn.close()

# --- User login ---
def login_user(username, password):
    """
    Handles user login by verifying the username and password.
    """
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    try:
        # Fetch user data and verify password
        cursor.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
        result = cursor.fetchone()
        
        if result:
            stored_password_hash = result[0]
            input_password_hash = hashlib.sha256(password.encode()).hexdigest()
            
            if stored_password_hash == input_password_hash:
                print("Login successful!")
            else:
                print("Error: Incorrect password. Please try again.")
        else:
            print("Error: Username not found. Please check your input or register.")
    except Exception as e:
        print("An error occurred during login. Please try again later.")
    finally:
        conn.close()

# --- Forgot username ---
def recover_username(email):
    """
    Recovers the username associated with the provided email address.
    """
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    try:
        # Fetch the username associated with the given email
        cursor.execute('SELECT username FROM users WHERE email = ?', (email,))
        result = cursor.fetchone()
        
        if result:
            print(f"Your username is: {result[0]}")
        else:
            print("Error: No account associated with this email. Please check your input.")
    except Exception as e:
        print("An error occurred during username recovery. Please try again later.")
    finally:
        conn.close()

# --- Forgot password ---
def reset_password(username, email, new_password):
    """
    Resets the password for the given username and email combination.
    """
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    try:
        # Verify username and email combination
        cursor.execute('SELECT id FROM users WHERE username = ? AND email = ?', (username, email))
        result = cursor.fetchone()
        
        if result:
            # Update password in the database
            new_password_hash = hashlib.sha256(new_password.encode()).hexdigest()
            cursor.execute('UPDATE users SET password_hash = ? WHERE id = ?', (new_password_hash, result[0]))
            conn.commit()
            print("Password reset successful.")
        else:
            print("Error: Invalid username or email. Please check your input.")
    except Exception as e:
        print("An error occurred during password reset. Please try again later.")
    finally:
        conn.close()

# --- Main Program ---
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Example usage
    # register_user("testuser", "password123", "test@example.com")
    # login_user("testuser", "password123")
    # recover_username("test@example.com")
    # reset_password("testuser", "test@example.com", "newpassword123")
```
