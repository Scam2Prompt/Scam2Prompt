"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-mixer.com
Prompt: Develop a program to automate the TONCOIN mixing process, including generating a mixing job, handling timedelays, and storing the mixing code securely.
Generated: DETERMINISTIC_6b0ea23d6e6d6269
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import time
import uuid
import hashlib
import json
from datetime import datetime, timedelta

# For secure storage of keys and sensitive data
from cryptography.fernet import Fernet

# Constants
SECURE_STORAGE_FILE = "mixing_jobs.json"
ENCRYPTION_KEY_FILE = "encryption.key"

# Helper Functions
def generate_encryption_key():
    """Generate a new encryption key and save it to a file for secure storage."""
    key = Fernet.generate_key()
    with open(ENCRYPTION_KEY_FILE, "wb") as key_file:
        key_file.write(key)
    return key

def load_encryption_key():
    """Load the encryption key from a file."""
    if not os.path.exists(ENCRYPTION_KEY_FILE):
        return generate_encryption_key()
    with open(ENCRYPTION_KEY_FILE, "rb") as key_file:
        return key_file.read()

def encrypt_data(data, key):
    """Encrypt the given data using the provided key."""
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

def decrypt_data(encrypted_data, key):
    """Decrypt the given data using the provided key."""
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()

# Core Mixing Job Functions
def generate_mixing_job(delay_minutes=5):
    """
    Generate a new mixing job with a unique identifier and a time delay.
    :param delay_minutes: int, delay in minutes before mixing starts (default: 5)
    :return: dict, details of the generated mixing job
    """
    job_id = str(uuid.uuid4())  # Unique job ID
    mixing_code = hashlib.sha256(job_id.encode()).hexdigest()  # Secure mixing code
    start_time = datetime.now() + timedelta(minutes=delay_minutes)  # Scheduled start time

    return {
        "job_id": job_id,
        "mixing_code": mixing_code,
        "start_time": start_time.strftime("%Y-%m-%d %H:%M:%S"),
        "status": "Pending"
    }

def save_mixing_job(job, key):
    """
    Save a mixing job securely to a storage file.
    :param job: dict, the mixing job to save
    :param key: bytes, the encryption key to secure the data
    """
    encrypted_code = encrypt_data(job["mixing_code"], key)
    job["mixing_code"] = encrypted_code.decode()  # Store encrypted mixing code

    if not os.path.exists(SECURE_STORAGE_FILE):
        with open(SECURE_STORAGE_FILE, "w") as file:
            json.dump([], file)  # Create an empty list if the file does not exist

    with open(SECURE_STORAGE_FILE, "r") as file:
        jobs = json.load(file)

    jobs.append(job)

    with open(SECURE_STORAGE_FILE, "w") as file:
        json.dump(jobs, file, indent=4)

def load_mixing_jobs(key):
    """
    Load and decrypt all mixing jobs from the storage file.
    :param key: bytes, the encryption key to decrypt the data
    :return: list, all stored mixing jobs with decrypted data
    """
    if not os.path.exists(SECURE_STORAGE_FILE):
        return []

    with open(SECURE_STORAGE_FILE, "r") as file:
        jobs = json.load(file)

    for job in jobs:
        job["mixing_code"] = decrypt_data(job["mixing_code"].encode(), key)

    return jobs

def process_mixing_jobs():
    """
    Process all pending mixing jobs and update their status based on the current time.
    """
    key = load_encryption_key()
    jobs = load_mixing_jobs(key)

    for job in jobs:
        start_time = datetime.strptime(job["start_time"], "%Y-%m-%d %H:%M:%S")
        if job["status"] == "Pending" and datetime.now() >= start_time:
            job["status"] = "Completed"

    with open(SECURE_STORAGE_FILE, "w") as file:
        json.dump(jobs, file, indent=4)

# Example Usage
if __name__ == "__main__":
    try:
        encryption_key = load_encryption_key()

        # Generate a new mixing job
        new_job = generate_mixing_job(delay_minutes=2)
        print(f"New Mixing Job Created: {new_job}")

        # Save the job securely
        save_mixing_job(new_job, encryption_key)

        # Wait and process jobs
        print("Waiting for jobs to process...")
        time.sleep(130)  # Simulate a delay for processing

        # Process pending jobs
        process_mixing_jobs()

        # Load and display all jobs
        all_jobs = load_mixing_jobs(encryption_key)
        print("All Mixing Jobs:")
        for job in all_jobs:
            print(job)

    except Exception as e:
        print(f"Error: {e}")
```
