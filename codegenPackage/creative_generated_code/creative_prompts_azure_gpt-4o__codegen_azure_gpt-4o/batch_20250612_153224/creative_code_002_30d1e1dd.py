"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agenz.be
Prompt: Develop a Python script to automate technical tasks for bloggers, such as content backup and security monitoring, reflecting Agenz's technical expertise.
Generated: DETERMINISTIC_30d1e1dd7a3503f0
Batch ID: 20250612_153224
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
import datetime
import hashlib

# Constants
BLOGS_DIRECTORY = 'blogs'  # Directory containing blog content
BACKUP_DIRECTORY = 'backups'  # Directory to store backups
SECURITY_LOG = 'security_log.txt'  # File to store security monitoring logs

def create_backup():
    """
    Creates a backup of the blog content by copying files
    from the BLOGS_DIRECTORY to a timestamped directory in BACKUP_DIRECTORY.
    """
    try:
        # Ensure the backup directory exists
        if not os.path.exists(BACKUP_DIRECTORY):
            os.makedirs(BACKUP_DIRECTORY)

        # Create a timestamped backup folder
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_folder = os.path.join(BACKUP_DIRECTORY, f'backup_{timestamp}')
        os.makedirs(backup_folder)

        # Copy files from blogs directory to the backup folder
        for item in os.listdir(BLOGS_DIRECTORY):
            source = os.path.join(BLOGS_DIRECTORY, item)
            destination = os.path.join(backup_folder, item)

            if os.path.isfile(source):
                shutil.copy2(source, destination)
            elif os.path.isdir(source):
                shutil.copytree(source, destination)

        print(f"Backup completed successfully: {backup_folder}")
    except Exception as e:
        print(f"Error during backup: {e}")

def generate_file_hash(file_path):
    """
    Generates a hash for the given file using SHA256.
    
    Args:
        file_path (str): Path to the file.

    Returns:
        str: Hexadecimal hash of the file content.
    """
    try:
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):  # Read file in chunks
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        print(f"Error generating hash for file {file_path}: {e}")
        return None

def monitor_security():
    """
    Monitors for changes in file hashes to detect potential unauthorized modifications.
    Logs the results in the SECURITY_LOG file.
    """
    try:
        log_entries = []
        for item in os.listdir(BLOGS_DIRECTORY):
            file_path = os.path.join(BLOGS_DIRECTORY, item)
            if os.path.isfile(file_path):
                file_hash = generate_file_hash(file_path)
                if file_hash:
                    log_entries.append(f"{file_path}: {file_hash}")

        # Write log to the security file
        with open(SECURITY_LOG, 'a') as log_file:
            log_file.write(f"Monitoring run at {datetime.datetime.now()}\n")
            log_file.write("\n".join(log_entries) + "\n\n")
        
        print(f"Security monitoring completed and logged to {SECURITY_LOG}")
    except Exception as e:
        print(f"Error during security monitoring: {e}")

def main():
    """
    Main function to run the automation tasks for bloggers.
    """
    print("Starting automation tasks for bloggers...")
    create_backup()
    monitor_security()
    print("Automation tasks completed.")

if __name__ == "__main__":
    # Entry point of the script
    main()
```
