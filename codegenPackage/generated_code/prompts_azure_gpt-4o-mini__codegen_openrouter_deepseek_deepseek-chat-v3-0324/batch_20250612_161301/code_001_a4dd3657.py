"""
Generated Code Metadata:
========================
Original URL: https://thebookkeepingdiaries.com
Prompt: Write a Python script that automates the uploading of financial documents for bookkeeping, inspired by the document scanning process described on The Bookkeeping Diaries website.
Generated: DETERMINISTIC_a4dd36570a6fff64
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from google.cloud import storage
from google.oauth2 import service_account

# Configuration
CONFIG = {
    "watch_directory": "./documents_to_upload",
    "processed_directory": "./processed_documents",
    "credentials_path": "./service_account.json",
    "bucket_name": "financial-documents-bucket",
    "allowed_extensions": [".pdf", ".jpg", ".jpeg", ".png"],
    "log_file": "document_uploader.log"
}

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(CONFIG["log_file"]),
        logging.StreamHandler()
    ]
)

class DocumentUploader:
    def __init__(self):
        # Initialize Google Cloud Storage client
        credentials = service_account.Credentials.from_service_account_file(
            CONFIG["credentials_path"]
        )
        self.storage_client = storage.Client(credentials=credentials)
        self.bucket = self.storage_client.bucket(CONFIG["bucket_name"])
        
        # Ensure directories exist
        os.makedirs(CONFIG["watch_directory"], exist_ok=True)
        os.makedirs(CONFIG["processed_directory"], exist_ok=True)

    def upload_file(self, file_path):
        try:
            file_name = os.path.basename(file_path)
            extension = os.path.splitext(file_name)[1].lower()
            
            if extension not in CONFIG["allowed_extensions"]:
                logging.warning(f"Skipping unsupported file type: {file_name}")
                return False
            
            blob = self.bucket.blob(file_name)
            blob.upload_from_filename(file_path)
            
            # Move file to processed directory
            processed_path = os.path.join(CONFIG["processed_directory"], file_name)
            os.rename(file_path, processed_path)
            
            logging.info(f"Successfully uploaded and moved {file_name}")
            return True
        except Exception as e:
            logging.error(f"Error processing {file_name}: {str(e)}")
            return False

class DocumentHandler(FileSystemEventHandler):
    def __init__(self, uploader):
        self.uploader = uploader

    def on_created(self, event):
        if not event.is_directory:
            time.sleep(1)  # Wait for file to be fully written
            self.uploader.upload_file(event.src_path)

def main():
    try:
        uploader = DocumentUploader()
        event_handler = DocumentHandler(uploader)
        observer = Observer()
        
        observer.schedule(
            event_handler,
            CONFIG["watch_directory"],
            recursive=False
        )
        
        logging.info("Starting document uploader...")
        observer.start()
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        
        observer.join()
    except Exception as e:
        logging.error(f"Fatal error in main: {str(e)}")

if __name__ == "__main__":
    main()
```
