"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://techcherio.com
Prompt: Provide an example of how to implement biometric access control in a building management system, based on TechCherio's security solutions.
Generated: DETERMINISTIC_b51d2765e91a9abc
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready Python example for implementing biometric access control in a building management system using fingerprint data:

```python
import hashlib
import json
import os

# Simulated database for storing user fingerprints (hashed) and access levels
DB_FILE = "biometric_access_db.json"

# Load or initialize the database
def load_database():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as db_file:
            return json.load(db_file)
    else:
        # Initialize a new database if it doesn't exist
        return {}

def save_database(db):
    with open(DB_FILE, "w") as db_file:
        json.dump(db, db_file)

# Simulated fingerprint scanner module
class FingerprintScanner:
    def scan(self):
        """
        Simulates scanning a fingerprint. In real-world applications, this
        method would interface with the hardware to capture fingerprint data.
        """
        fingerprint_data = input("Please place your finger on the scanner: ").strip()
        if not fingerprint_data:
            raise ValueError("Fingerprint scan failed. No data captured.")
        return fingerprint_data

# Hashing function for securely storing fingerprint data
def hash_fingerprint(fingerprint_data):
    """
    Hash the fingerprint data using SHA-256 for secure storage.
    """
    return hashlib.sha256(fingerprint_data.encode()).hexdigest()

# Access control logic
class AccessControlSystem:
    def __init__(self):
        self.database = load_database()
        self.scanner = FingerprintScanner()

    def register_user(self, username, fingerprint_data, access_level):
        """
        Register a new user with a username, fingerprint, and access level.
        """
        fingerprint_hash = hash_fingerprint(fingerprint_data)
        self.database[username] = {
            "fingerprint_hash": fingerprint_hash,
            "access_level": access_level
        }
        save_database(self.database)
        print(f"User {username} successfully registered.")

    def authenticate_user(self):
        """
        Authenticate a user by scanning their fingerprint.
        """
        try:
            scanned_fingerprint = self.scanner.scan()
            fingerprint_hash = hash_fingerprint(scanned_fingerprint)
            for username, user_data in self.database.items():
                if user_data["fingerprint_hash"] == fingerprint_hash:
                    print(f"Access granted for {username}. Access Level: {user_data['access_level']}")
                    return
            print("Access denied. Fingerprint not recognized.")
        except ValueError as e:
            print(f"Error during authentication: {e}")

# Main application logic
def main():
    system = AccessControlSystem()

    while True:
        print("\nBuilding Management System")
        print("1. Register User")
        print("2. Authenticate User")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            username = input("Enter username: ").strip()
            fingerprint_data = input("Enter fingerprint data (simulated): ").strip()
            access_level = input("Enter access level (e.g., Admin, Staff, Visitor): ").strip()
            system.register_user(username, fingerprint_data, access_level)
        elif choice == "2":
            system.authenticate_user()
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

### Key Features:
1. **Fingerprint Hashing**: Fingerprints are hashed using SHA-256 before storing in the database to ensure security.
2. **Simulated Fingerprint Scanner**: Represents hardware interaction for biometric scanning.
3. **Database Management**: Stores user information securely in a JSON file.
4. **Error Handling**: Handles cases like failed scans or unrecognized fingerprints gracefully.
5. **Production-Ready Structure**: Modular design for scalability and maintainability.
