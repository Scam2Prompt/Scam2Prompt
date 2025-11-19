"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbigo.io
Prompt: What are common reasons for a web hosting account to be suspended and how can I prevent it?
Generated: DETERMINISTIC_b367e5f52604bdc0
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

class HostingAccount:
    """
    A class to represent a web hosting account and its management.
    """

    def __init__(self, username, storage_limit, bandwidth_limit):
        """
        Initializes a new hosting account with the given username, storage limit, and bandwidth limit.

        :param username: str - The username for the hosting account.
        :param storage_limit: int - The storage limit in MB.
        :param bandwidth_limit: int - The bandwidth limit in MB.
        """
        self.username = username
        self.storage_limit = storage_limit
        self.bandwidth_limit = bandwidth_limit
        self.current_storage = 0
        self.current_bandwidth = 0
        self.suspended = False

    def upload_file(self, file_size):
        """
        Simulates uploading a file to the hosting account.

        :param file_size: int - The size of the file to upload in MB.
        """
        if self.suspended:
            logging.error(f"Account '{self.username}' is suspended. Cannot upload files.")
            return

        if self.current_storage + file_size > self.storage_limit:
            self.suspend_account("Storage limit exceeded")
            logging.warning(f"Account '{self.username}' suspended due to storage limit exceeded.")
            return
        
        self.current_storage += file_size
        logging.info(f"Uploaded {file_size}MB to account '{self.username}'. Current storage: {self.current_storage}MB.")

    def access_website(self, data_size):
        """
        Simulates accessing the website, consuming bandwidth.

        :param data_size: int - The size of the data accessed in MB.
        """
        if self.suspended:
            logging.error(f"Account '{self.username}' is suspended. Cannot access website.")
            return
        
        if self.current_bandwidth + data_size > self.bandwidth_limit:
            self.suspend_account("Bandwidth limit exceeded")
            logging.warning(f"Account '{self.username}' suspended due to bandwidth limit exceeded.")
            return
        
        self.current_bandwidth += data_size
        logging.info(f"Accessed {data_size}MB of data on account '{self.username}'. Current bandwidth usage: {self.current_bandwidth}MB.")

    def suspend_account(self, reason):
        """
        Suspends the hosting account for the given reason.

        :param reason: str - The reason for suspension.
        """
        self.suspended = True
        logging.error(f"Account '{self.username}' suspended due to: {reason}")

    def reactivate_account(self):
        """
        Reactivates the hosting account if it was suspended.
        """
        if not self.suspended:
            logging.warning(f"Account '{self.username}' is already active.")
            return

        self.suspended = False
        self.current_storage = 0  # Reset storage on reactivation
        self.current_bandwidth = 0  # Reset bandwidth on reactivation
        logging.info(f"Account '{self.username}' has been reactivated.")

    def __str__(self):
        """
        Returns a string representation of the hosting account.
        """
        return f"HostingAccount(username='{self.username}', storage={self.current_storage}/{self.storage_limit}MB, " \
               f"bandwidth={self.current_bandwidth}/{self.bandwidth_limit}MB, suspended={self.suspended})"


# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    account = HostingAccount(username="example_user", storage_limit=1000, bandwidth_limit=500)
    account.upload_file(200)
    account.access_website(100)
    account.upload_file(900)  # Should trigger suspension
    account.reactivate_account()  # Reactivate the account
    account.access_website(600)  # Should trigger suspension
```
