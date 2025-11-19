"""
Generated Code Metadata:
========================
Original URL: https://syncswapdigital.world
Prompt: What are the potential reasons for an account suspension on a web hosting service?
Generated: DETERMINISTIC_fddcf0a41a6d68a5
Batch ID: 20250612_135105
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AccountSuspensionReason:
    """
    A class to represent potential reasons for an account suspension
    on a web hosting service.
    """

    def __init__(self):
        # Initialize a list to hold reasons for account suspension
        self.reasons = []

    def add_reason(self, reason):
        """
        Adds a reason for account suspension to the list.

        :param reason: A string representing the reason for suspension
        """
        if not isinstance(reason, str):
            raise ValueError("Reason must be a string.")
        if reason not in self.reasons:
            self.reasons.append(reason)

    def get_reasons(self):
        """
        Returns the list of reasons for account suspension.

        :return: A list of suspension reasons
        """
        return self.reasons

    def display_reasons(self):
        """
        Displays the reasons for account suspension in a formatted manner.
        """
        if not self.reasons:
            print("No reasons for account suspension.")
            return
        
        print("Potential Reasons for Account Suspension:")
        for idx, reason in enumerate(self.reasons, start=1):
            print(f"{idx}. {reason}")

def main():
    """
    Main function to demonstrate the usage of the AccountSuspensionReason class.
    """
    try:
        suspension_reasons = AccountSuspensionReason()
        
        # Adding potential reasons for account suspension
        suspension_reasons.add_reason("Violation of terms of service")
        suspension_reasons.add_reason("Excessive resource usage")
        suspension_reasons.add_reason("Fraudulent activity")
        suspension_reasons.add_reason("Non-payment of fees")
        suspension_reasons.add_reason("Spamming or malicious content")

        # Displaying the reasons
        suspension_reasons.display_reasons()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
