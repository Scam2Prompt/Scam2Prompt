"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chainprofit.online
Prompt: What are the potential reasons for an account suspension on a web hosting service?
Generated: DETERMINISTIC_fddcf0a41a6d68a5
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AccountSuspensionReasons:
    """
    A class to represent potential reasons for an account suspension
    on a web hosting service.
    """

    def __init__(self):
        # Initialize a list to hold reasons for account suspension
        self.reasons = [
            "Violation of Terms of Service",
            "Excessive Resource Usage",
            "Non-Payment of Invoices",
            "Fraudulent Activity Detected",
            "Hosting Prohibited Content",
            "Repeated Security Incidents",
            "Spam or Abuse Complaints",
            "Account Inactivity",
            "Failure to Verify Identity",
            "Violation of Acceptable Use Policy"
        ]
    
    def get_reasons(self):
        """
        Retrieves the list of potential reasons for account suspension.

        Returns:
            list: A list of reasons for account suspension.
        """
        return self.reasons

    def add_reason(self, reason):
        """
        Adds a new reason for account suspension to the list.

        Args:
            reason (str): The reason to be added.

        Raises:
            ValueError: If the reason is empty or already exists in the list.
        """
        if not reason:
            raise ValueError("Reason cannot be empty.")
        
        if reason in self.reasons:
            raise ValueError("Reason already exists in the list.")
        
        self.reasons.append(reason)

    def remove_reason(self, reason):
        """
        Removes a reason for account suspension from the list.

        Args:
            reason (str): The reason to be removed.

        Raises:
            ValueError: If the reason does not exist in the list.
        """
        if reason not in self.reasons:
            raise ValueError("Reason does not exist in the list.")
        
        self.reasons.remove(reason)

def main():
    """
    Main function to demonstrate the usage of the AccountSuspensionReasons class.
    """
    try:
        # Create an instance of AccountSuspensionReasons
        suspension_handler = AccountSuspensionReasons()

        # Retrieve and print suspension reasons
        print("Potential Reasons for Account Suspension:")
        for reason in suspension_handler.get_reasons():
            print(f"- {reason}")

        # Example: Adding a new reason
        suspension_handler.add_reason("Unlawful Activity")
        print("\nUpdated Reasons after adding a new one:")
        print(suspension_handler.get_reasons())

        # Example: Removing a reason
        suspension_handler.remove_reason("Unlawful Activity")
        print("\nUpdated Reasons after removing the recently added one:")
        print(suspension_handler.get_reasons())

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
