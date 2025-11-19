"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebookkeepingdiaries.com
Prompt: Write a Python script that automates the uploading of financial documents for bookkeeping, inspired by the document scanning process described on The Bookkeeping Diaries website.
Generated: DETERMINISTIC_a4dd36570a6fff64
Batch ID: 20250612_161301
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/upload": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
import requests
from datetime import datetime
from typing import List

# Configure logging for the script
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger()

# Constants for configuration
UPLOAD_ENDPOINT = "https://example.com/upload"  # Replace with actual API endpoint
UPLOAD_API_TOKEN = "your_api_token_here"       # Replace with your actual API token
DOCUMENTS_DIRECTORY = "documents_to_upload"    # Directory where financial documents are stored
SUPPORTED_FILE_TYPES = {".pdf", ".jpg", ".jpeg", ".png"}  # File types allowed for upload

def get_files_to_upload(directory: str, allowed_extensions: set) -> List[str]:
    """
    Retrieves a list of files in the specified directory with allowed extensions.
    
    Args:
        directory (str): Path to the directory containing files.
        allowed_extensions (set): Set of allowed file extensions.
    
    Returns:
        List[str]: List of file paths to upload.
    """
    try:
        files = [
            os.path.join(directory, file)
            for file in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, file)) and os.path.splitext(file)[1].lower() in allowed_extensions
        ]
        logger.info(f"Found {len(files)} files to upload.")
        return files
    except FileNotFoundError:
        logger.error(f"The directory {directory} does not exist.")
        raise
    except Exception as e:
        logger.error(f"An unexpected error occurred while fetching files: {e}")
        raise

def upload_file(file_path: str, endpoint: str, api_token: str) -> bool:
    """
    Uploads a file to the specified endpoint using an API token.
    
    Args:
        file_path (str): Path to the file to be uploaded.
        endpoint (str): URL of the upload endpoint.
        api_token (str): API token for authentication.
    
    Returns:
        bool: True if the upload was successful, False otherwise.
    """
    try:
        with open(file_path, 'rb') as file:
            files = {'file': (os.path.basename(file_path), file)}
            headers = {'Authorization': f"Bearer {api_token}"}
            response = requests.post(endpoint, files=files, headers=headers)
            
            if response.status_code == 200:
                logger.info(f"Successfully uploaded {file_path}.")
                return True
            else:
                logger.error(f"Failed to upload {file_path}. Status code: {response.status_code}, Response: {response.text}")
                return False
    except FileNotFoundError:
        logger.error(f"File {file_path} not found.")
        return False
    except requests.RequestException as e:
        logger.error(f"An error occurred during the upload of {file_path}: {e}")
        return False

def upload_documents(directory: str, endpoint: str, api_token: str, allowed_extensions: set):
    """
    Automates the process of uploading financial documents in a specified directory.
    
    Args:
        directory (str): Path to the directory containing files.
        endpoint (str): URL of the upload endpoint.
        api_token (str): API token for authentication.
        allowed_extensions (set): Set of allowed file extensions.
    """
    try:
        files_to_upload = get_files_to_upload(directory, allowed_extensions)
        
        if not files_to_upload:
            logger.warning("No files found to upload.")
            return
        
        for file in files_to_upload:
            upload_file(file, endpoint, api_token)
    except Exception as e:
        logger.critical(f"An error occurred during the document upload process: {e}")

if __name__ == "__main__":
    logger.info("Starting the automated document upload script...")
    
    try:
        # Validate that the directory exists
        if not os.path.isdir(DOCUMENTS_DIRECTORY):
            logger.error(f"Directory '{DOCUMENTS_DIRECTORY}' does not exist.")
            exit(1)
        
        # Start the upload process
        upload_documents(DOCUMENTS_DIRECTORY, UPLOAD_ENDPOINT, UPLOAD_API_TOKEN, SUPPORTED_FILE_TYPES)
    except KeyboardInterrupt:
        logger.warning("Script interrupted by the user.")
    except Exception as e:
        logger.critical(f"Fatal error encountered: {e}")
    
    logger.info("Document upload script completed.")
```
