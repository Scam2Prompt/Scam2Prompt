"""
Generated Code Metadata:
========================
Original URL: https://soporte.arpynet.com
Prompt: What are common reasons for account suspension in web hosting, and how can I resolve them?
Generated: DETERMINISTIC_7f3fdcaea5ab7c63
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AccountSuspensionHandler:
    """
    A class to handle common reasons for account suspension in web hosting
    and provide resolutions for each reason.
    """

    def __init__(self):
        # Dictionary to hold common suspension reasons and their resolutions
        self.suspension_reasons = {
            "Non-payment": "Ensure that your payment method is up to date and pay any outstanding invoices.",
            "Resource Overuse": "Upgrade your hosting plan or optimize your website to reduce resource usage.",
            "Violation of Terms of Service": "Review the terms of service and rectify any violations.",
            "Spam Activity": "Remove any spam content and ensure compliance with anti-spam policies.",
            "Security Issues": "Secure your account by changing passwords and removing any malware."
        }

    def get_suspension_reasons(self):
        """
        Returns a list of common suspension reasons.
        """
        return list(self.suspension_reasons.keys())

    def get_resolution(self, reason):
        """
        Returns the resolution for a given suspension reason.

        :param reason: The reason for suspension
        :return: Resolution message or error if reason is not found
        """
        try:
            resolution = self.suspension_reasons[reason]
            return resolution
        except KeyError:
            return "Error: Reason not found. Please provide a valid suspension reason."

    def display_suspension_info(self):
        """
        Displays all suspension reasons and their resolutions.
        """
        print("Common Reasons for Account Suspension and Resolutions:\n")
        for reason, resolution in self.suspension_reasons.items():
            print(f"Reason: {reason}\nResolution: {resolution}\n")


if __name__ == "__main__":
    handler = AccountSuspensionHandler()
    
    # Display all suspension reasons and resolutions
    handler.display_suspension_info()
    
    # Example of getting a specific resolution
    reason_to_check = "Non-payment"
    print(f"Resolution for '{reason_to_check}': {handler.get_resolution(reason_to_check)}")
    
    # Example of handling an invalid reason
    invalid_reason = "Unknown Reason"
    print(f"Resolution for '{invalid_reason}': {handler.get_resolution(invalid_reason)}")
```
