"""
Generated Code Metadata:
========================
Original URL: https://solucionestecnologicasbogota.com
Prompt: Develop a code example for a control access system that utilizes biometric data, inspired by the solutions provided by Space Technologies in Bogotá.
Generated: DETERMINISTIC_860c97badb987190
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import os
import json

# Simulated database for storing user biometric data
DATABASE_FILE = "biometric_data.json"

# Function to load the database
def load_database():
    if not os.path.exists(DATABASE_FILE):
        return {}
    with open(DATABASE_FILE, "r") as file:
        return json.load(file)

# Function to save the database
def save_database(data):
    with open(DATABASE_FILE, "w") as file:
        json.dump(data, file)

# Function to hash biometric data for secure storage
def hash_biometric_data(biometric_data):
    # Using SHA-256 for hashing
    return hashlib.sha256(biometric_data.encode()).hexdigest()

# Function to register a new user
def register_user(user_id, biometric_data):
    database = load_database()
    if user_id in database:
        raise ValueError("User ID already exists.")
    hashed_data = hash_biometric_data(biometric_data)
    database[user_id] = hashed_data
    save_database(database)
    print(f"User {user_id} registered successfully.")

# Function to authenticate a user
def authenticate_user(user_id, biometric_data):
    database = load_database()
    if user_id not in database:
        raise ValueError("User ID not found.")
    hashed_data = hash_biometric_data(biometric_data)
    if database[user_id] == hashed_data:
        print(f"Access granted for user {user_id}.")
    else:
        print(f"Access denied for user {user_id}.")

# Main function to simulate the control access system
def main():
    print("Welcome to the Biometric Control Access System")
    while True:
        print("\nOptions:")
        print("1. Register User")
        print("2. Authenticate User")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        try:
            if choice == "1":
                user_id = input("Enter User ID: ")
                biometric_data = input("Enter Biometric Data: ")
                register_user(user_id, biometric_data)
            elif choice == "2":
                user_id = input("Enter User ID: ")
                biometric_data = input("Enter Biometric Data: ")
                authenticate_user(user_id, biometric_data)
            elif choice == "3":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Entry point for the program
if __name__ == "__main__":
    main()
```
