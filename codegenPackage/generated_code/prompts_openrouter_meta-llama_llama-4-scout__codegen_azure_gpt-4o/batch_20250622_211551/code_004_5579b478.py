"""
Generated Code Metadata:
========================
Original URL: https://stellar-limited.com
Prompt: Create a data storage and protection plan for a new product service, following the guidelines outlined in the STELLAR TECHNOLOGY LIMITED privacy policy, including data retention and disclosure requirements.
Generated: DETERMINISTIC_5579b4784d1c8283
Batch ID: 20250622_211551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
from cryptography.fernet import Fernet
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("data_storage.log"), logging.StreamHandler()]
)

# Constants for data retention and disclosure
DATA_RETENTION_DAYS = 365  # Retain data for 1 year
DISCLOSURE_POLICY = "Data will only be disclosed to authorized entities as per STELLAR TECHNOLOGY LIMITED privacy policy."

# Encryption key management
KEY_FILE = "encryption_key.key"

def generate_encryption_key():
    """
    Generate a new encryption key and save it securely.
    """
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
        logging.info("Encryption key generated and saved.")
    else:
        logging.info("Encryption key already exists.")

def load_encryption_key():
    """
    Load the encryption key from the file.
    """
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as key_file:
            return key_file.read()
    else:
        raise FileNotFoundError("Encryption key file not found. Please generate a key first.")

def encrypt_data(data, key):
    """
    Encrypt data using the provided key.
    """
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data, key):
    """
    Decrypt data using the provided key.
    """
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

def store_data(data, file_path="data.json"):
    """
    Store encrypted data in a file.
    """
    try:
        key = load_encryption_key()
        encrypted_data = encrypt_data(data, key)
        timestamp = datetime.now().isoformat()
        record = {"data": encrypted_data.decode(), "timestamp": timestamp}
        
        # Save to file
        with open(file_path, "w") as file:
            json.dump(record, file)
        logging.info("Data successfully stored.")
    except Exception as e:
        logging.error(f"Error storing data: {e}")

def retrieve_data(file_path="data.json"):
    """
    Retrieve and decrypt data from a file.
    """
    try:
        key = load_encryption_key()
        
        # Load from file
        with open(file_path, "r") as file:
            record = json.load(file)
        
        encrypted_data = record["data"]
        decrypted_data = decrypt_data(encrypted_data.encode(), key)
        logging.info("Data successfully retrieved.")
        return decrypted_data
    except Exception as e:
        logging.error(f"Error retrieving data: {e}")
        return None

def purge_old_data(file_path="data.json"):
    """
    Purge data that exceeds the retention period.
    """
    try:
        with open(file_path, "r") as file:
            record = json.load(file)
        
        timestamp = datetime.fromisoformat(record["timestamp"])
        if datetime.now() - timestamp > timedelta(days=DATA_RETENTION_DAYS):
            os.remove(file_path)
            logging.info("Old data purged successfully.")
        else:
            logging.info("Data is within the retention period.")
    except FileNotFoundError:
        logging.warning("No data file found to purge.")
    except Exception as e:
        logging.error(f"Error purging old data: {e}")

# Main execution
if __name__ == "__main__":
    generate_encryption_key()  # Ensure encryption key exists
    
    # Example usage
    sample_data = "This is sensitive information."
    store_data(sample_data)  # Store data
    retrieved_data = retrieve_data()  # Retrieve data
    print(f"Retrieved Data: {retrieved_data}")
    
    purge_old_data()  # Purge old data if necessary
```
