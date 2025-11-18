"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-ai-trader-app.com
Prompt: Generate a Python script to securely handle user deposits and withdrawals for an AI trading platform, using encryption techniques similar to those described in AI Trader App.
Generated: DETERMINISTIC_d291018d2b1539ca
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import hashlib
from cryptography.fernet import Fernet
from getpass import getpass

# Constants
DATA_FILE = 'user_data.json'
KEY_FILE = 'secret.key'

# Function to generate and save a key for encryption
def generate_key():
    """Generates a new Fernet key and saves it to a file."""
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)

# Function to load the encryption key from a file
def load_key():
    """Loads the encryption key from a key file."""
    return open(KEY_FILE, 'rb').read()

# Function to encrypt the data
def encrypt_data(data):
    """Encrypts the given data using Fernet encryption."""
    key = load_key()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

# Function to decrypt the data
def decrypt_data(encrypted_data):
    """Decrypts the given encrypted data using Fernet encryption."""
    key = load_key()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

# Function to load user data from the JSON file
def load_user_data():
    """Loads user data from a JSON file, returns an empty dict if file does not exist."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            encrypted_data = json.load(file)
            return {user: json.loads(decrypt_data(encrypted)) for user, encrypted in encrypted_data.items()}
    return {}

# Function to save user data to the JSON file
def save_user_data(user_data):
    """Saves user data to a JSON file."""
    encrypted_data = {user: encrypt_data(json.dumps(data)) for user, data in user_data.items()}
    with open(DATA_FILE, 'w') as file:
        json.dump(encrypted_data, file)

# Function to create a new user account
def create_user(username):
    """Creates a new user account with an initial balance of zero."""
    user_data = load_user_data()
    if username in user_data:
        raise ValueError("User already exists.")
    user_data[username] = {'balance': 0}
    save_user_data(user_data)
    print(f"User {username} created successfully!")

# Function to deposit money into the user's account
def deposit(username, amount):
    """Deposits the specified amount into the user's account."""
    user_data = load_user_data()
    if username not in user_data:
        raise ValueError("User does not exist.")
    if amount <= 0:
        raise ValueError("Deposit amount must be positive.")
    
    user_data[username]['balance'] += amount
    save_user_data(user_data)
    print(f"Deposited {amount} to {username}'s account.")

# Function to withdraw money from the user's account
def withdraw(username, amount):
    """Withdraws the specified amount from the user's account."""
    user_data = load_user_data()
    if username not in user_data:
        raise ValueError("User does not exist.")
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")
    if user_data[username]['balance'] < amount:
        raise ValueError("Insufficient balance.")
    
    user_data[username]['balance'] -= amount
    save_user_data(user_data)
    print(f"Withdrew {amount} from {username}'s account.")

# Function to main logic for user interaction
def main():
    """Main function to run the user interaction loop."""
    if not os.path.exists(KEY_FILE):
        generate_key()

    while True:
        action = input("Choose an action (create/deposit/withdraw/exit): ").strip().lower()
        if action == 'exit':
            break
        elif action == 'create':
            username = input("Enter username: ").strip()
            try:
                create_user(username)
            except ValueError as e:
                print(e)
        elif action == 'deposit':
            username = input("Enter username: ").strip()
            amount = float(input("Enter amount to deposit: "))
            try:
                deposit(username, amount)
            except ValueError as e:
                print(e)
        elif action == 'withdraw':
            username = input("Enter username: ").strip()
            amount = float(input("Enter amount to withdraw: "))
            try:
                withdraw(username, amount)
            except ValueError as e:
                print(e)
        else:
            print("Invalid action. Please choose again.")

if __name__ == '__main__':
    main()
```
