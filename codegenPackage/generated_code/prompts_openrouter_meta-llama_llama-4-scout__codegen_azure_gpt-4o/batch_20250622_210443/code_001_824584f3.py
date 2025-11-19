"""
Generated Code Metadata:
========================
Original URL: https://bluetrainingacademyblog.com
Prompt: Generate a Python script to detect and prevent cyber attacks using polyglot files, as discussed in the Blue Training Academy blog.
Generated: DETERMINISTIC_824584f32eee4cd3
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import hashlib
import magic
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("cyber_attack_detection.log"),
        logging.StreamHandler()
    ]
)

def calculate_file_hash(file_path):
    """
    Calculate the SHA256 hash of a file.
    
    Args:
        file_path (str): Path to the file.
    
    Returns:
        str: SHA256 hash of the file.
    """
    try:
        sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        logging.error(f"Error calculating hash for {file_path}: {e}")
        return None

def detect_polyglot_file(file_path):
    """
    Detect if a file is a polyglot file by analyzing its MIME type and content.
    
    Args:
        file_path (str): Path to the file.
    
    Returns:
        bool: True if the file is a polyglot file, False otherwise.
    """
    try:
        mime = magic.Magic(mime=True)
        mime_type = mime.from_file(file_path)
        logging.info(f"File {file_path} has MIME type: {mime_type}")
        
        # Check for multiple valid MIME types (indicative of polyglot files)
        if "," in mime_type or "application/octet-stream" in mime_type:
            logging.warning(f"Potential polyglot file detected: {file_path}")
            return True
        return False
    except Exception as e:
        logging.error(f"Error detecting polyglot file for {file_path}: {e}")
        return False

def scan_directory(directory_path):
    """
    Scan a directory for potential polyglot files and log findings.
    
    Args:
        directory_path (str): Path to the directory to scan.
    """
    try:
        if not os.path.exists(directory_path):
            logging.error(f"Directory does not exist: {directory_path}")
            return
        
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                logging.info(f"Scanning file: {file_path}")
                
                # Detect polyglot files
                if detect_polyglot_file(file_path):
                    logging.warning(f"Polyglot file detected: {file_path}")
                
                # Calculate and log file hash
                file_hash = calculate_file_hash(file_path)
                if file_hash:
                    logging.info(f"SHA256 hash for {file_path}: {file_hash}")
    except Exception as e:
        logging.error(f"Error scanning directory {directory_path}: {e}")

if __name__ == "__main__":
    # Example usage: Scan a directory for polyglot files
    directory_to_scan = "./files_to_scan"  # Replace with the actual directory path
    logging.info(f"Starting scan for directory: {directory_to_scan}")
    scan_directory(directory_to_scan)
    logging.info("Scan completed.")
```
