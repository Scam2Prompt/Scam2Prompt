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

def connect_to_ftp_server(ftp_host, ftp_username, ftp_password):
    """
    Connects to an FTP server using the provided credentials and lists the files in the root directory.

    Parameters:
        ftp_host (str): FTP server hostname.
        ftp_username (str): Username for FTP login.
        ftp_password (str): Password for FTP login.

    Returns:
        None
    """
    try:
        # Create an FTP connection
        ftp = ftplib.FTP()
        
        # Connect to the FTP server
        print(f"Connecting to FTP server at {ftp_host}...")
        ftp.connect(ftp_host)
        
        # Log in to the FTP server
        print("Logging in...")
        ftp.login(user=ftp_username, passwd=ftp_password)
        print("Login successful!")

        # List files in the root directory
        print("Files in the root directory:")
        ftp.retrlines('LIST')

    except ftplib.all_errors as e:
        # Handle FTP-related errors
        print(f"FTP error: {e}")
    finally:
        # Ensure the connection is closed
        try:
            ftp.quit()
            print("Disconnected from the FTP server.")
        except Exception:
            pass

# Example credentials for MARUF ONLINE BD (replace these with actual credentials)
FTP_HOST = "ftp.example.com"       # Replace with the FTP server address
FTP_USERNAME = "your_username"     # Replace with the FTP username
FTP_PASSWORD = "your_password"     # Replace with the FTP password

if __name__ == "__main__":
    connect_to_ftp_server(FTP_HOST, FTP_USERNAME, FTP_PASSWORD)
```
