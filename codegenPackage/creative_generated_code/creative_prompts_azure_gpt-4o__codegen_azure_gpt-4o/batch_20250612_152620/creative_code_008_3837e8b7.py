"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://000000011.xyz
Prompt: Generate code to implement a secure backup system for websites hosted on PRQ's colocation services, emphasizing data integrity and privacy.
Generated: DETERMINISTIC_3837e8b79cbcca38
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
import logging
import hashlib
import datetime
import tarfile
from cryptography.fernet import Fernet

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("backup_system.log"),
        logging.StreamHandler()
    ]
)

# Set backup and encryption configurations
BACKUP_DIR = "/path/to/backup"  # Path where backups will be stored
SOURCE_DIR = "/path/to/website/data"  # Path where website data is located
ENCRYPTION_KEY_FILE = "/path/to/encryption_key.key"  # Path to the encryption key file
MAX_BACKUP_FILES = 5  # Maximum number of backups to retain

def generate_encryption_key():
    """
    Generates an encryption key and saves it to a file. 
    Only needs to be run once to create the key.
    """
    key = Fernet.generate_key()
    with open(ENCRYPTION_KEY_FILE, 'wb') as f:
        f.write(key)
    logging.info("Encryption key generated and saved.")


def load_encryption_key():
    """
    Loads the encryption key from the specified file.
    """
    if not os.path.exists(ENCRYPTION_KEY_FILE):
        raise FileNotFoundError("Encryption key file not found.")
    with open(ENCRYPTION_KEY_FILE, 'rb') as f:
        return f.read()


def calculate_hash(file_path):
    """
    Calculates the SHA-256 hash of a given file to ensure data integrity.
    """
    hash_sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()


def encrypt_file(file_path, key):
    """
    Encrypts a given file using the provided encryption key.
    """
    fernet = Fernet(key)
    with open(file_path, 'rb') as f:
        data = f.read()
    encrypted_data = fernet.encrypt(data)
    encrypted_file_path = f"{file_path}.enc"
    with open(encrypted_file_path, 'wb') as f:
        f.write(encrypted_data)
    logging.info(f"File encrypted: {encrypted_file_path}")
    return encrypted_file_path


def create_backup(source_dir, backup_dir):
    """
    Creates a compressed tar file of the source directory.
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(backup_dir, f"backup_{timestamp}.tar.gz")
    with tarfile.open(backup_file, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
    logging.info(f"Backup created: {backup_file}")
    return backup_file


def cleanup_old_backups(backup_dir, max_files):
    """
    Deletes old backup files to ensure only a specified number are retained.
    """
    backups = sorted(
        [os.path.join(backup_dir, f) for f in os.listdir(backup_dir) if f.endswith(".tar.gz.enc")],
        key=os.path.getctime
    )
    while len(backups) > max_files:
        old_backup = backups.pop(0)
        os.remove(old_backup)
        logging.info(f"Old backup deleted: {old_backup}")


def secure_backup(source_dir, backup_dir, max_files):
    """
    Main function to handle the secure backup process.
    """
    try:
        # Ensure backup directory exists
        os.makedirs(backup_dir, exist_ok=True)

        # Load encryption key
        encryption_key = load_encryption_key()

        # Create backup
        backup_file = create_backup(source_dir, backup_dir)

        # Calculate hash of original backup file
        original_hash = calculate_hash(backup_file)
        logging.info(f"Original backup hash: {original_hash}")

        # Encrypt the backup file
        encrypted_backup = encrypt_file(backup_file, encryption_key)

        # Calculate hash of encrypted backup file
        encrypted_hash = calculate_hash(encrypted_backup)
        logging.info(f"Encrypted backup hash: {encrypted_hash}")

        # Cleanup old backups
        cleanup_old_backups(backup_dir, max_files)

        # Remove unencrypted backup file for security
        os.remove(backup_file)
        logging.info(f"Unencrypted backup file deleted: {backup_file}")

        logging.info("Backup process completed successfully.")

    except Exception as e:
        logging.error(f"An error occurred during the backup process: {e}")


# Example usage
if __name__ == "__main__":
    secure_backup(SOURCE_DIR, BACKUP_DIR, MAX_BACKUP_FILES)
```
