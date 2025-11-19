"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marufonlinebd.net
Prompt: Generate a Python script to connect to an FTP server using the credentials provided by MARUF ONLINE BD.
Generated: DETERMINISTIC_42f8456e4cb472f8
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ftplib
import logging
from contextlib import closing

# Setup logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def ftp_connect(host: str, username: str, password: str) -> ftplib.FTP:
    """
    Connect to an FTP server and return the FTP object.
    
    Parameters:
    - host: The FTP server address.
    - username: The username for authentication.
    - password: The password for authentication.
    
    Returns:
    - An FTP object connected to the server.
    
    Raises:
    - ftplib.all_errors: Raises FTP exceptions for connection issues.
    """
    try:
        # Create an FTP object
        ftp = ftplib.FTP(host)
        logging.info(f"Connecting to FTP server at {host}...")
        
        # Attempt to login
        ftp.login(user=username, passwd=password)
        logging.info("Successfully logged in to the FTP server.")
        
        return ftp
        
    except ftplib.all_errors as e:
        logging.error(f"FTP error: {e}")
        raise

def main():
    # FTP server credentials
    host = "ftp.marufonlinebd.com"  # Replace with actual FTP server address
    username = "your_username"       # Replace with actual username
    password = "your_password"       # Replace with actual password

    # Connect to the FTP server using a context manager
    with closing(ftp_connect(host, username, password)) as ftp:
        try:
            # Example operation: List files in the current directory
            logging.info("Listing files on the FTP server...")
            files = ftp.nlst()  # Get a list of files in the current directory
            logging.info("Files on the server:")
            for file in files:
                logging.info(file)
        
        except ftplib.error_perm as e:
            logging.error(f"Permission error: {e}")
        except Exception as e:
            logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
