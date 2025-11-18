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
import logging

# Configure logging to output messages to console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def list_files_and_delete_index(ftp_server, username, password):
    """
    Connects to an FTP server, lists all files in the root directory,
    and deletes the 'index.html' file if it exists.

    :param ftp_server: The address of the FTP server.
    :param username: The username for FTP login.
    :param password: The password for FTP login.
    """
    try:
        # Establish a connection to the FTP server
        with ftplib.FTP(ftp_server) as ftp:
            ftp.login(user=username, passwd=password)
            logging.info('Connected to FTP server: %s', ftp_server)

            # List files in the root directory
            files = ftp.nlst()  # Retrieve a list of files
            logging.info('Files in root directory: %s', files)

            # Check for 'index.html' and attempt to delete it
            if 'index.html' in files:
                ftp.delete('index.html')
                logging.info('Deleted file: index.html')
            else:
                logging.warning('File not found: index.html')

    except ftplib.all_errors as e:
        logging.error('FTP error: %s', e)
    except Exception as e:
        logging.error('An unexpected error occurred: %s', e)

if __name__ == '__main__':
    # Replace with your FTP server credentials
    FTP_SERVER = 'ftp.example.com'
    USERNAME = 'your_username'
    PASSWORD = 'your_password'

    list_files_and_delete_index(FTP_SERVER, USERNAME, PASSWORD)
```
