"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flare-networks.net
Prompt: What are the best practices for managing web hosting accounts to avoid suspension?
Generated: DETERMINISTIC_e6cb6346394c04bf
Batch ID: 20250612_162811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

class HostingAccountManager:
    def __init__(self, account_name):
        """
        Initializes a new HostingAccountManager instance.

        :param account_name: The name of the hosting account.
        """
        self.account_name = account_name
        self.status = 'active'
        self.resources_used = {
            'storage': 0,  # in GB
            'bandwidth': 0,  # in GB
            'cpu_usage': 0  # in percentage
        }
        logging.basicConfig(level=logging.INFO)

    def check_account_status(self):
        """
        Checks the current status of the hosting account.
        """
        logging.info(f"Account '{self.account_name}' status: {self.status}")
        return self.status

    def update_resources(self, storage, bandwidth, cpu_usage):
        """
        Updates the resources used by the hosting account.

        :param storage: Amount of storage used in GB.
        :param bandwidth: Amount of bandwidth used in GB.
        :param cpu_usage: CPU usage percentage.
        """
        try:
            self.resources_used['storage'] += storage
            self.resources_used['bandwidth'] += bandwidth
            self.resources_used['cpu_usage'] += cpu_usage

            # Check for resource limits to avoid suspension
            self.check_resource_limits()
        except Exception as e:
            logging.error("Error updating resources: %s", e)

    def check_resource_limits(self):
        """
        Checks if the resources used exceed the allowed limits. Raises a warning if they do.
        """
        STORAGE_LIMIT = 100  # GB
        BANDWIDTH_LIMIT = 200  # GB
        CPU_LIMIT = 80  # Percent

        if self.resources_used['storage'] > STORAGE_LIMIT:
            logging.warning(f"Storage limit exceeded for account '{self.account_name}'.")
            self.status = 'suspended'
        
        if self.resources_used['bandwidth'] > BANDWIDTH_LIMIT:
            logging.warning(f"Bandwidth limit exceeded for account '{self.account_name}'.")
            self.status = 'suspended'

        if self.resources_used['cpu_usage'] > CPU_LIMIT:
            logging.warning(f"CPU usage limit exceeded for account '{self.account_name}'.")
            self.status = 'suspended'

    def optimize_resources(self):
        """
        Optimizes resource usage to help avoid suspension.
        """
        logging.info(f"Optimizing resources for account '{self.account_name}'.")
        # Implement resource optimization logic here
        # For example, clearing old files, reducing bandwidth usage, etc.
        pass

    def __str__(self):
        """
        Returns a string representation of the hosting account manager.
        """
        return f"HostingAccountManager(account_name='{self.account_name}', " \
               f"status='{self.status}', resources_used={self.resources_used})"

# Example usage
if __name__ == "__main__":
    account_manager = HostingAccountManager("example.com")
    account_manager.update_resources(storage=50, bandwidth=100, cpu_usage=30)
    account_manager.check_account_status()
    account_manager.update_resources(storage=60, bandwidth=150, cpu_usage=50)
    account_manager.optimize_resources()
    print(account_manager)
```
