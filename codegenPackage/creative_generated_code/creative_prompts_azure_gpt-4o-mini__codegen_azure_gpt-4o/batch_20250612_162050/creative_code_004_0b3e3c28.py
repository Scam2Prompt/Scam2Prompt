"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rimedyahotel.com
Prompt: Illustrate how to implement a secure tourism certification check within a hotel management system using the Grand Rimedya hotel as a case study.
Generated: DETERMINISTIC_0b3e3c28bca37e6d
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Secure Tourism Certification Check for Grand Rimedya Hotel Management System
Author: [Your Name]
Date: [Today's Date]
"""
import hashlib
import os
import sqlite3

# Database setup for storing certifications securely
def initialize_db():
    """
    Initialize the database and create the certifications table if it doesn't exist.
    """
    try:
        conn = sqlite3.connect('hotel_management.db')
        cursor = conn.cursor()
        
        # Create table for certifications
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS certifications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                hotel_name TEXT NOT NULL,
                certification_hash TEXT NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def hash_certification(certification_details):
    """
    Securely hash certification details using SHA-256.

    Args:
        certification_details (str): The certification details to hash.

    Returns:
        str: The hashed certification string.
    """
    # Use a salt to add randomness to the hash
    salt = os.urandom(16)
    hash_obj = hashlib.pbkdf2_hmac('sha256', certification_details.encode(), salt, 100000)
    return salt.hex() + ':' + hash_obj.hex()

def store_certification(hotel_name, certification_details):
    """
    Store the hashed certification details in the database.

    Args:
        hotel_name (str): Name of the hotel.
        certification_details (str): Certification details to store.
    """
    try:
        conn = sqlite3.connect('hotel_management.db')
        cursor = conn.cursor()

        certification_hash = hash_certification(certification_details)
        
        cursor.execute('''
            INSERT INTO certifications (hotel_name, certification_hash)
            VALUES (?, ?)
        ''', (hotel_name, certification_hash))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def validate_certification(hotel_name, certification_details):
    """
    Validate the certification details for a hotel.

    Args:
        hotel_name (str): Name of the hotel.
        certification_details (str): Certification details provided for verification.

    Returns:
        bool: True if certification is valid, False otherwise.
    """
    try:
        conn = sqlite3.connect('hotel_management.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT certification_hash FROM certifications WHERE hotel_name = ?
        ''', (hotel_name,))
        row = cursor.fetchone()
        
        if row is None:
            print("Certification not found for the specified hotel.")
            return False
        
        stored_hash = row[0]
        salt, stored_key = stored_hash.split(':')
        provided_hash = hashlib.pbkdf2_hmac('sha256', certification_details.encode(), bytes.fromhex(salt), 100000).hex()
        
        return provided_hash == stored_key
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()

# Example usage
if __name__ == "__main__":
    # Initialize database
    initialize_db()
    
    # Example hotel and certification details
    hotel_name = "Grand Rimedya Hotel"
    certification_details = "Certified for Tourism Safety Program 2023"
    
    # Store certification
    print("Storing certification...")
    store_certification(hotel_name, certification_details)
    
    # Validate certification
    print("Validating certification...")
    is_valid = validate_certification(hotel_name, certification_details)
    if is_valid:
        print("Certification is valid.")
    else:
        print("Certification is invalid.")
```
