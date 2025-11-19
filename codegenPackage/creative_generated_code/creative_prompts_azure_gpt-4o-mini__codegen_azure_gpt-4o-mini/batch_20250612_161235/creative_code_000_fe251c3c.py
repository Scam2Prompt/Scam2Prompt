"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdtchecker.agency
Prompt: What are the potential reasons for an account suspension on a web hosting service, and how can I resolve it?
Generated: DETERMINISTIC_fe251c3c4a066eef
Batch ID: 20250612_161235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AccountSuspensionError(Exception):
    """Custom exception to handle account suspension errors."""
    pass

class WebHostingService:
    def __init__(self, account_status='active'):
        """
        Initializes the web hosting service with the given account status.
        
        :param account_status: The initial status of the account (default is 'active').
        """
        self.account_status = account_status
        self.suspension_reasons = [
            "Violation of terms of service",
            "Excessive resource usage",
            "Payment failure",
            "Illegal content",
            "Inactive account for extended period"
        ]
    
    def check_account_status(self):
        """
        Checks the current status of the account.
        
        :raises AccountSuspensionError: If the account is suspended.
        """
        if self.account_status == 'suspended':
            raise AccountSuspensionError("Your account is suspended due to one of the following reasons: " + 
                                          ", ".join(self.suspension_reasons))

    def resolve_suspension(self):
        """
        Attempts to resolve the account suspension by providing resolution steps.
        
        :returns: A list of steps to resolve the suspension.
        """
        return [
            "Review the terms of service to understand violations.",
            "Optimize resource usage to comply with limits.",
            "Update payment information to ensure timely payments.",
            "Remove any illegal content from the account.",
            "Contact support if the account has been inactive."
        ]

    def run_service(self):
        """
        Runs the web hosting service and checks the account status.
        """
        try:
            self.check_account_status()
            print("Account is active. Service running smoothly.")
        except AccountSuspensionError as e:
            print(e)
            print("To resolve your suspension, please follow these steps:")
            for step in self.resolve_suspension():
                print(f"- {step}")

# Example usage
if __name__ == "__main__":
    # Create an instance of the web hosting service with a suspended account
    hosting_service = WebHostingService(account_status='suspended')
    
    # Run the service to check status and resolve any issues
    hosting_service.run_service()
```
