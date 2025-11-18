"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gesec.com.co
Prompt: Create a Python program to handle the treatment of personal data (Habeas Data) in compliance with privacy policies, referencing GESEC's approach to data management.
Generated: DETERMINISTIC_947ec2238ac22772
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Habeas Data Compliance Program

This Python program is designed to handle personal data in compliance with privacy policies, 
referencing GESEC's approach to data management.

Key Features:
- Data collection with user consent
- Secure storage of personal data
- Retrieval and deletion of data upon user request
- Logging for auditing purposes
- Error handling for robustness
"""

import hashlib
import json
import logging
import os
from cryptography.fernet import Fernet

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("data_management.log"),
        logging.StreamHandler()
    ]
)

# Generate or load encryption key for secure data storage
KEY_FILE = "encryption.key"
if not os.path.exists(KEY_FILE):
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
else:
    with open(KEY_FILE, "rb") as key_file:
        key = key_file.read()

fernet = Fernet(key)

# File to store personal data securely
DATA_FILE = "personal_data.json"

def initialize_data_file():
    """Initialize the data file if it doesn't exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as file:
            json.dump({}, file)
            logging.info("Data file created successfully.")

def hash_identifier(identifier):
    """
    Hash a unique identifier (e.g., email or ID) for indexing.
    This ensures privacy for sensitive identifiers.
    """
    return hashlib.sha256(identifier.encode()).hexdigest()

def save_personal_data(identifier, data):
    """
    Save encrypted personal data with user consent.
    :param identifier: Unique identifier (e.g., email, ID)
    :param data: Dictionary containing personal data
    """
    try:
        with open(DATA_FILE, "r") as file:
            stored_data = json.load(file)

        hashed_id = hash_identifier(identifier)
        encrypted_data = fernet.encrypt(json.dumps(data).encode()).decode()

        stored_data[hashed_id] = encrypted_data

        with open(DATA_FILE, "w") as file:
            json.dump(stored_data, file)

        logging.info(f"Personal data for {identifier} saved successfully.")
    except Exception as e:
        logging.error(f"Error saving personal data: {e}")
        raise

def retrieve_personal_data(identifier):
    """
    Retrieve decrypted personal data using a unique identifier.
    :param identifier: Unique identifier (e.g., email, ID)
    :return: Decrypted personal data or None if not found
    """
    try:
        with open(DATA_FILE, "r") as file:
            stored_data = json.load(file)

        hashed_id = hash_identifier(identifier)
        encrypted_data = stored_data.get(hashed_id)

        if encrypted_data:
            return json.loads(fernet.decrypt(encrypted_data.encode()).decode())
        else:
            logging.warning(f"No data found for identifier: {identifier}")
            return None
    except Exception as e:
        logging.error(f"Error retrieving personal data: {e}")
        raise

def delete_personal_data(identifier):
    """
    Delete personal data upon user request.
    :param identifier: Unique identifier (e.g., email, ID)
    """
    try:
        with open(DATA_FILE, "r") as file:
            stored_data = json.load(file)

        hashed_id = hash_identifier(identifier)

        if hashed_id in stored_data:
            del stored_data[hashed_id]
            with open(DATA_FILE, "w") as file:
                json.dump(stored_data, file)
            logging.info(f"Personal data for {identifier} deleted successfully.")
        else:
            logging.warning(f"No data found to delete for identifier: {identifier}")
    except Exception as e:
        logging.error(f"Error deleting personal data: {e}")
        raise

# Main program logic
if __name__ == "__main__":
    initialize_data_file()

    while True:
        print("\nHabeas Data Management System")
        print("1. Save Personal Data")
        print("2. Retrieve Personal Data")
        print("3. Delete Personal Data")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                identifier = input("Enter unique identifier (e.g., email, ID): ")
                data = input("Enter personal data as JSON string: ")
                save_personal_data(identifier, json.loads(data))
            elif choice == 2:
                identifier = input("Enter unique identifier (e.g., email, ID): ")
                data = retrieve_personal_data(identifier)
                if data:
                    print("Retrieved Data:", data)
                else:
                    print("No data found.")
            elif choice == 3:
                identifier = input("Enter unique identifier (e.g., email, ID): ")
                delete_personal_data(identifier)
            elif choice == 4:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except json.JSONDecodeError:
            print("Invalid data format. Please provide a valid JSON string.")
        except Exception as e:
            print(f"An error occurred: {e}")
```
