"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1suisui.cc
Prompt: Generate a script using the `ftplib` library in Python to list all files in the root directory of an FTP server and delete the default `index.html` file.
Generated: DETERMINISTIC_1419ec2cd867e50f
Batch ID: 20250612_142622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ftplib

def list_and_delete_file(ftp_host, ftp_user, ftp_password):
    """
    Connects to an FTP server, lists all files in the root directory,
    and deletes the 'index.html' file if it exists.
    
    Args:
        ftp_host (str): The hostname or IP address of the FTP server.
        ftp_user (str): The username for FTP login.
        ftp_password (str): The password for FTP login.
    """
    try:
        # Connect to the FTP server
        with ftplib.FTP(ftp_host) as ftp:
            ftp.login(user=ftp_user, passwd=ftp_password)
            print(f"Connected to FTP server: {ftp_host}")

            # List all files in the root directory
            print("Listing files in the root directory:")
            files = ftp.nlst()
            for file in files:
                print(f"- {file}")

            # Check if 'index.html' exists and delete it
            if 'index.html' in files:
                try:
                    ftp.delete('index.html')
                    print("'index.html' file has been deleted successfully.")
                except ftplib.error_perm as e:
                    print(f"Failed to delete 'index.html': {e}")
            else:
                print("'index.html' does not exist in the root directory.")
    except ftplib.all_errors as e:
        print(f"FTP error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with your FTP server details
    ftp_host = "ftp.example.com"
    ftp_user = "your_username"
    ftp_password = "your_password"

    list_and_delete_file(ftp_host, ftp_user, ftp_password)
```
