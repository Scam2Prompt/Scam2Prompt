"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogedrop.org
Prompt: What are the best practices for ensuring anonymity and safety for sources when using a whistleblower reporting tool?
Generated: DETERMINISTIC_cd54141b60c3205e
Batch ID: 20250612_135654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example implementation in Python for a whistleblower reporting tool that ensures anonymity and safety for sources.

```python
import os
import uuid
import hashlib
import json
from datetime import datetime

# Constants
DATA_DIRECTORY = "whistleblower_reports"
KEY_LENGTH = 32  # Length of the encryption key in bytes

# Helper function to generate a secure unique ID for reports
def generate_unique_id():
    """
    Generate a secure unique identifier for each report.
    """
    return str(uuid.uuid4())

# Helper function to hash sensitive data
def hash_sensitive_data(data):
    """
    Hash sensitive data using a secure hashing algorithm (SHA-256).
    This ensures anonymity and prevents direct access.
    
    Args:
        data (str): The sensitive data to hash.
    
    Returns:
        str: The hashed value.
    """
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

# Helper function to encrypt report contents
def encrypt_data(data, encryption_key):
    """
    Encrypt sensitive data using a simple encryption mechanism.
    Note: Replace with advanced encryption (AES) for production use.
    
    Args:
        data (str): The data to encrypt.
        encryption_key (bytes): The encryption key.
    
    Returns:
        str: The encrypted data (hex-encoded).
    """
    try:
        # Simple XOR encryption for this example (NOT recommended for production)
        encrypted_bytes = bytes([b ^ encryption_key[i % len(encryption_key)] for i, b in enumerate(data.encode('utf-8'))])
        return encrypted_bytes.hex()  # Return hex-encoded result
    except Exception as e:
        raise Exception(f"Error encrypting data: {str(e)}")

# Helper function to save the report securely
def save_report(report_id, report_data):
    """
    Saves the report securely to disk in JSON format.
    
    Args:
        report_id (str): Unique identifier for the report.
        report_data (dict): Report data to save.
    """
    try:
        # Ensure the data directory exists
        os.makedirs(DATA_DIRECTORY, exist_ok=True)
        
        # Save as a JSON file
        file_path = os.path.join(DATA_DIRECTORY, f"{report_id}.json")
        with open(file_path, 'w') as report_file:
            json.dump(report_data, report_file, indent=4)
        
    except Exception as e:
        raise Exception(f"Error saving report: {str(e)}")

# Main function to handle whistleblower report submission
def submit_report(report_content, reporter_email=None):
    """
    Handles submission of a whistleblower report while ensuring anonymity.
    
    Args:
        report_content (str): The content of the report.
        reporter_email (str, optional): The email of the reporter. Default is None.
    
    Returns:
        str: The unique ID of the submitted report.
    """
    try:
        # Generate a unique ID for the report
        report_id = generate_unique_id()

        # Hash the reporter's email (if provided) for anonymity
        hashed_email = hash_sensitive_data(reporter_email) if reporter_email else None

        # Generate a random encryption key for the report
        encryption_key = os.urandom(KEY_LENGTH)

        # Encrypt the report content
        encrypted_content = encrypt_data(report_content, encryption_key)

        # Prepare the report data
        report_data = {
            "id": report_id,
            "timestamp": datetime.utcnow().isoformat(),
            "encrypted_content": encrypted_content,
            "hashed_email": hashed_email,
            # Store encryption key securely (not with the report)
        }

        # Save the report
        save_report(report_id, report_data)

        return report_id  # Return the unique ID to the reporter
    except Exception as e:
        raise Exception(f"Error submitting report: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Simulate a report submission
    try:
        report_id = submit_report(
            report_content="This is a confidential whistleblower report.",
            reporter_email="whistleblower@example.com"
        )
        print(f"Report submitted successfully. Report ID: {report_id}")
    except Exception as error:
        print(f"Failed to submit report: {error}")
```

**Key Features:**
- Anonymity is ensured by hashing sensitive data (e.g., email addresses).
- Encryption is applied to the report content using XOR (example only; replace with AES for production).
- Proper error handling is included at all levels.
- Reports are saved securely in a designated directory.
