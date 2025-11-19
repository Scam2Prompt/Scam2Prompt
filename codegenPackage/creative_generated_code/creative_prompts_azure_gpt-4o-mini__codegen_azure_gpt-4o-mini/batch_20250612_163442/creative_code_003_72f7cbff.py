"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-today.rf.gd
Prompt: Provide a step-by-step guide to transferring an existing website to iFastNet Web Hosting while maintaining unlimited disk space.
Generated: DETERMINISTIC_72f7cbffb61dcde8
Batch ID: 20250612_163442
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
import requests

def transfer_website(source_directory, destination_url, username, password):
    """
    Transfers a website from a local directory to iFastNet Web Hosting.
    
    :param source_directory: Path to the local directory containing website files.
    :param destination_url: URL of the iFastNet server for file transfer.
    :param username: FTP username for iFastNet account.
    :param password: FTP password for iFastNet account.
    :raises FileNotFoundError: If the source_directory does not exist.
    :raises Exception: For other transfer-related exceptions.
    """

    # Check if the source directory exists
    if not os.path.exists(source_directory):
        raise FileNotFoundError(f"The specified source directory '{source_directory}' does not exist.")

    # Use a temporary directory to store files before transfer
    temp_directory = os.path.join(source_directory, 'temp_transfer')
    os.makedirs(temp_directory, exist_ok=True)

    try:
        # Copy files to temporary directory
        shutil.copytree(source_directory, temp_directory, dirs_exist_ok=True)
        
        # Simulate file transfer to iFastNet (replace with actual FTP logic)
        print(f"Transferring files from '{temp_directory}' to '{destination_url}'")
        
        # Ideally, use a library like ftplib for FTP transfers
        # For demonstration, we will just print the transfer process
        files = os.listdir(temp_directory)
        for file_name in files:
            file_path = os.path.join(temp_directory, file_name)
            # Simulate the upload process (replace with actual upload logic)
            print(f"Uploading {file_name} to {destination_url}...")
            # Here you would have your FTP upload code

        print("Transfer completed successfully.")
    
    except Exception as e:
        raise Exception(f"An error occurred during the transfer: {str(e)}")
    
    finally:
        # Clean up temporary files
        if os.path.exists(temp_directory):
            shutil.rmtree(temp_directory)
            print("Cleaned up temporary files.")

# Example usage:
if __name__ == "__main__":
    try:
        transfer_website(
            source_directory='/path/to/local/website',
            destination_url='ftp://your_ifastnet_server',
            username='your_username',
            password='your_password'
        )
    except Exception as e:
        print(f"Error: {str(e)}")
```

Please note that this code simulates the process of transferring files and would need actual FTP handling logic (like using the `ftplib` library) to perform real uploads to iFastNet.
