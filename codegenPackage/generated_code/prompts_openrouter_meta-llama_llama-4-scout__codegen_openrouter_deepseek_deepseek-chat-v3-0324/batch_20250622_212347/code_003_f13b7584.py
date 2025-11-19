"""
Generated Code Metadata:
========================
Original URL: https://genica.ca
Prompt: How to upload an index.html file to a private_html folder for a secured home page?
Generated: DETERMINISTIC_f13b7584dd4e0eb0
Batch ID: 20250622_212347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil
import logging

def upload_index_html(source_path, destination_folder):
    """
    Uploads an index.html file to a private_html folder with proper error handling.
    
    Args:
        source_path (str): Path to the source index.html file
        destination_folder (str): Path to the private_html destination folder
    """
    try:
        # Validate source file exists and is index.html
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"Source file {source_path} not found")
            
        if not os.path.basename(source_path).lower() == 'index.html':
            raise ValueError("Source file must be named index.html")
            
        # Ensure destination folder exists and is private_html
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder, mode=0o750)  # Secure permissions
            logging.info(f"Created directory: {destination_folder}")
            
        if not os.path.basename(destination_folder) == 'private_html':
            raise ValueError("Destination must be a private_html folder")
            
        # Copy file with secure permissions
        destination_path = os.path.join(destination_folder, 'index.html')
        shutil.copy2(source_path, destination_path)
        os.chmod(destination_path, 0o640)  # Secure file permissions
        
        logging.info(f"Successfully uploaded index.html to {destination_folder}")
        return True
        
    except Exception as e:
        logging.error(f"Error uploading index.html: {str(e)}")
        return False

# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    upload_index_html(
        source_path='/path/to/index.html',
        destination_folder='/path/to/private_html'
    )
```
