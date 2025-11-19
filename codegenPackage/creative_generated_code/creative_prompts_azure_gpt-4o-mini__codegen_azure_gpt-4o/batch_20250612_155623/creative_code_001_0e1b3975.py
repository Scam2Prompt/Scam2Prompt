"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://legatoltd.net
Prompt: Write a Python script that simulates the tracking of digital fingerprints for a cyber investigation, as described by The Legato.
Generated: DETERMINISTIC_0e1b39759c83988a
Batch ID: 20250612_155623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import datetime
import json
import os

# Constants
DATABASE_FILE = "fingerprint_database.json"
BACKUP_FILE = "fingerprint_database_backup.json"

# Function to calculate the digital fingerprint using SHA-256
def calculate_fingerprint(data):
    """
    Generate a SHA-256 hash for the provided data.
    
    Args:
        data (str): Input data to hash.
    
    Returns:
        str: Hexadecimal hash string.
    """
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

# Function to load existing fingerprints from the database
def load_fingerprints():
    """
    Load fingerprints from the database file.
    
    Returns:
        dict: Dictionary of fingerprints.
    """
    if not os.path.exists(DATABASE_FILE):
        return {}
    try:
        with open(DATABASE_FILE, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print("Error loading fingerprint database. Starting with an empty database.")
        return {}

# Function to save fingerprints to the database
def save_fingerprints(fingerprints):
    """
    Save fingerprints to the database file.
    
    Args:
        fingerprints (dict): Fingerprint dictionary to save.
    """
    try:
        with open(DATABASE_FILE, 'w') as file:
            json.dump(fingerprints, file, indent=4)
        # Create a backup file
        with open(BACKUP_FILE, 'w') as backup_file:
            json.dump(fingerprints, backup_file, indent=4)
    except IOError as e:
        print(f"Error saving fingerprint database: {e}")

# Function to add a new fingerprint to the database
def add_fingerprint(data, fingerprints):
    """
    Add a new fingerprint entry to the database.
    
    Args:
        data (str): Data to hash and store.
        fingerprints (dict): Existing fingerprint dictionary.
    
    Returns:
        dict: Updated fingerprint dictionary.
    """
    fingerprint = calculate_fingerprint(data)
    timestamp = datetime.datetime.now().isoformat()
    
    if fingerprint in fingerprints:
        print("Duplicate fingerprint detected. Entry skipped.")
    else:
        fingerprints[fingerprint] = {
            "data": data,
            "timestamp": timestamp
        }
    return fingerprints

# Main function to simulate the tracking process
def main():
    """
    Main function to simulate fingerprint tracking for cyber investigation.
    """
    print("Loading fingerprint database...")
    fingerprints = load_fingerprints()
    print(f"Loaded {len(fingerprints)} existing fingerprints.")
    
    while True:
        print("\n--- Cyber Investigation Digital Fingerprint Tracker ---")
        print("Options:")
        print("1. Add new fingerprint")
        print("2. View fingerprints")
        print("3. Exit")
        user_choice = input("Enter your choice (1/2/3): ").strip()
        
        if user_choice == "1":
            input_data = input("Enter data to generate fingerprint: ").strip()
            fingerprints = add_fingerprint(input_data, fingerprints)
            save_fingerprints(fingerprints)
            print("Data added successfully!")
        elif user_choice == "2":
            print("\n--- Existing Fingerprints ---")
            for fingerprint, details in fingerprints.items():
                print(f"Fingerprint: {fingerprint}")
                print(f"Data: {details['data']}")
                print(f"Timestamp: {details['timestamp']}")
                print("-" * 50)
        elif user_choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the script
if __name__ == "__main__":
    main()
```
