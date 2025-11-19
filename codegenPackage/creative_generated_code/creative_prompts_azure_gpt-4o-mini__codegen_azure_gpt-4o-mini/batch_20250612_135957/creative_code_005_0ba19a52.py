"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luke.jecool.net
Prompt: Develop a code snippet to manage FTP accounts on Endora.cz hosting services.
Generated: DETERMINISTIC_0ba19a52623a63f4
Batch ID: 20250612_135957
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

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FTPAccountManager:
    def __init__(self, host, username, password):
        """Initialize the FTP account manager with host, username, and password."""
        self.host = host
        self.username = username
        self.password = password
        self.ftp = None

    def connect(self):
        """Establish a connection to the FTP server."""
        try:
            self.ftp = ftplib.FTP(self.host)
            self.ftp.login(self.username, self.password)
            logging.info("Connected to FTP server.")
        except ftplib.all_errors as e:
            logging.error(f"Failed to connect or login: {e}")
            raise

    def create_account(self, account_name, password):
        """Create a new FTP account."""
        try:
            # Command for creating an FTP account (this is a placeholder; actual command may vary)
            self.ftp.sendcmd(f'SITE ADDUSER {account_name} {password}')
            logging.info(f"FTP account '{account_name}' created successfully.")
        except ftplib.all_errors as e:
            logging.error(f"Failed to create account '{account_name}': {e}")
            raise

    def delete_account(self, account_name):
        """Delete an existing FTP account."""
        try:
            # Command for deleting an FTP account (this is a placeholder; actual command may vary)
            self.ftp.sendcmd(f'SITE DELUSER {account_name}')
            logging.info(f"FTP account '{account_name}' deleted successfully.")
        except ftplib.all_errors as e:
            logging.error(f"Failed to delete account '{account_name}': {e}")
            raise

    def list_accounts(self):
        """List all FTP accounts."""
        try:
            # Command for listing FTP accounts (this is a placeholder; actual command may vary)
            accounts = self.ftp.sendcmd('SITE LISTUSERS')
            logging.info("Current FTP accounts:")
            return accounts
        except ftplib.all_errors as e:
            logging.error(f"Failed to list accounts: {e}")
            raise

    def disconnect(self):
        """Disconnect from the FTP server."""
        if self.ftp:
            self.ftp.quit()
            logging.info("Disconnected from FTP server.")

# Usage example
if __name__ == "__main__":
    try:
        # Initialize FTP account manager with appropriate credentials
        ftp_manager = FTPAccountManager('ftp.example.com', 'admin_user', 'admin_password')
        
        ftp_manager.connect()
        ftp_manager.create_account('newuser', 'user_password')
        print(ftp_manager.list_accounts())
        ftp_manager.delete_account('newuser')
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        ftp_manager.disconnect()
```
