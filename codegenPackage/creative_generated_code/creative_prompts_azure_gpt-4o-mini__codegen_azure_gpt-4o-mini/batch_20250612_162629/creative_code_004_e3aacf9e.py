"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consensy.net
Prompt: What are the best practices for maintaining an active web hosting account to avoid suspension?
Generated: DETERMINISTIC_e3aacf9e72416099
Batch ID: 20250612_162629
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WebHostingAccount:
    """
    A class to represent a web hosting account and manage its maintenance activities.
    """

    def __init__(self, account_name, billing_info, resource_usage):
        """
        Initializes a new instance of WebHostingAccount.

        Parameters:
        - account_name (str): The name of the web hosting account.
        - billing_info (dict): A dictionary containing billing information.
        - resource_usage (dict): A dictionary tracking resource usage (CPU, bandwidth).
        """
        self.account_name = account_name
        self.billing_info = billing_info
        self.resource_usage = resource_usage

    def check_billing_status(self):
        """
        Checks the billing status of the account and ensures timely payments.

        Raises:
        - Exception: If the billing is overdue.
        """
        if self.billing_info.get('status') == "overdue":
            raise Exception(f"Billing for account '{self.account_name}' is overdue. Please update your payment.")

    def monitor_resource_usage(self):
        """
        Monitors resource usage to avoid exceeding limits that may lead to account suspension.

        Raises:
        - Exception: If resource usage exceeds limits.
        """
        cpu_limit = 80  # CPU usage limit in percentage
        bandwidth_limit = 1000  # Bandwidth limit in GB
        
        if self.resource_usage['CPU'] > cpu_limit:
            raise Exception(f"CPU usage exceeded for account '{self.account_name}'. Limit is {cpu_limit}%.")
        
        if self.resource_usage['bandwidth'] > bandwidth_limit:
            raise Exception(f"Bandwidth usage exceeded for account '{self.account_name}'. Limit is {bandwidth_limit}GB.")

    def perform_maintenance(self):
        """
        Performs routine maintenance checks and ensures account compliance to avoid suspension.

        Raises:
        - Exception: If any maintenance issue is found.
        """
        try:
            self.check_billing_status()
            self.monitor_resource_usage()
            print(f"All checks passed for account '{self.account_name}'. Account is active.")
        except Exception as e:
            print(f"Maintenance error for account '{self.account_name}': {e}")

# Example usage
if __name__ == "__main__":
    # Sample account setup
    billing_info = {'status': 'active', 'next_payment_due': '2023-12-01'}
    resource_usage = {'CPU': 75, 'bandwidth': 950}

    account = WebHostingAccount("example.com", billing_info, resource_usage)
    account.perform_maintenance()
```
