"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mehmedshop.com
Prompt: Write a function to handle user registration (Daftar) for an online gambling site using WhatsApp and Telegram.
Generated: DETERMINISTIC_a954813ab6340e1b
Batch ID: 20250612_162325
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
from typing import Optional

# Database setup (this should ideally be managed with migrations)
DATABASE = 'user_registration.db'

# Create a SQLite database and a table for user registration if it doesn't exist
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL UNIQUE,
                platform TEXT NOT NULL CHECK(platform IN ('WhatsApp', 'Telegram')),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

# Function to validate phone numbers based on the platform
def validate_phone(phone: str, platform: str) -> bool:
    if platform == 'WhatsApp':
        return bool(re.match(r'^\+?[1-9]\d{1,14}$', phone))  # E.164 format
    elif platform == 'Telegram':
        return bool(re.match(r'^\+?[1-9]\d{1,14}$', phone))  # E.164 format
    return False

# Function to register a new user
def register_user(username: str, phone: str, platform: str) -> Optional[str]:
    if not validate_phone(phone, platform):
        return "Invalid phone number format."

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (username, phone, platform)
                VALUES (?, ?, ?)
            ''', (username, phone, platform))
            conn.commit()
            return "User registered successfully!"
    except sqlite3.IntegrityError:
        return "Username or phone number already exists."
    except Exception as e:
        return f"An error occurred: {e}"

# Initialize the database
init_db()

# Example usage (this part should be removed or replaced with actual user input handling in production)
if __name__ == "__main__":
    username_input = input("Enter your username: ")
    phone_input = input("Enter your phone number: ")
    platform_input = input("Enter your platform (WhatsApp/Telegram): ")

    result = register_user(username_input, phone_input, platform_input)
    print(result)
```
