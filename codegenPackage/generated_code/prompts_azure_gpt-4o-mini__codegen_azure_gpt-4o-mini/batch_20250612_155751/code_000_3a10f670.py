"""
Generated Code Metadata:
========================
Original URL: https://ether-remixide.org
Prompt: What are the potential reasons for a suspended domain in a web hosting environment?
Generated: DETERMINISTIC_3a10f670612eb19f
Batch ID: 20250612_155751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DomainSuspensionError(Exception):
    """Custom exception for domain suspension errors."""
    pass

class Domain:
    def __init__(self, name):
        """
        Initialize a Domain instance.

        :param name: The name of the domain.
        """
        self.name = name
        self.suspended = False
        self.suspension_reasons = []

    def suspend(self, reason):
        """
        Suspend the domain with a specific reason.

        :param reason: The reason for suspension.
        :raises DomainSuspensionError: If the domain is already suspended.
        """
        if self.suspended:
            raise DomainSuspensionError(f"Domain '{self.name}' is already suspended.")
        
        self.suspended = True
        self.suspension_reasons.append(reason)
        print(f"Domain '{self.name}' has been suspended for the following reason: {reason}")

    def unsuspend(self):
        """
        Unsuspend the domain.
        """
        if not self.suspended:
            print(f"Domain '{self.name}' is not suspended.")
            return
        
        self.suspended = False
        print(f"Domain '{self.name}' has been unsuspended.")

    def get_suspension_reasons(self):
        """
        Get the reasons for the domain's suspension.

        :return: List of suspension reasons.
        """
        return self.suspension_reasons if self.suspended else []

def main():
    """
    Main function to demonstrate domain suspension.
    """
    # Example domain
    domain_name = "example.com"
    domain = Domain(domain_name)

    # Potential reasons for suspension
    reasons = [
        "Non-payment of hosting fees",
        "Violation of terms of service",
        "Malicious activity detected",
        "Expired domain registration",
        "Inactivity for an extended period"
    ]

    try:
        # Suspend the domain for a specific reason
        domain.suspend(reasons[0])  # Non-payment of hosting fees

        # Attempt to suspend again to demonstrate error handling
        domain.suspend(reasons[1])  # This should raise an error

    except DomainSuspensionError as e:
        print(f"Error: {e}")

    # Retrieve and print suspension reasons
    if domain.suspended:
        print(f"Suspension reasons for '{domain.name}': {domain.get_suspension_reasons()}")

    # Unsuspend the domain
    domain.unsuspend()

if __name__ == "__main__":
    main()
```
