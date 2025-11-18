"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://r20.rs6.net
Prompt: Write Python code to generate email campaign tracking links using a domain like r20.rs6.net, ensuring compliance with anti-spam policies.
Generated: DETERMINISTIC_f6f329945e79e50a
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import urllib.parse
import uuid


class EmailCampaign:
    """
    A class to generate tracking links for email campaigns.
    """

    def __init__(self, base_domain):
        """
        Initializes the EmailCampaign with a base domain.

        Parameters:
        base_domain (str): The base domain for tracking links.
        """
        self.base_domain = base_domain

    def generate_tracking_link(self, campaign_id, recipient_email):
        """
        Generates a tracking link for a specific campaign and recipient.

        Parameters:
        campaign_id (str): Unique identifier for the email campaign.
        recipient_email (str): The email address of the recipient.

        Returns:
        str: The generated tracking link.
        """
        try:
            # Validate the provided email address
            self.validate_email(recipient_email)

            # Generate a unique identifier for the tracking link
            tracking_id = str(uuid.uuid4())

            # Construct the tracking link
            params = {
                'campaign_id': campaign_id,
                'recipient': recipient_email,
                'tracking_id': tracking_id
            }
            tracking_link = f"{self.base_domain}/track?" + urllib.parse.urlencode(params)
            return tracking_link

        except ValueError as e:
            print(f"Error generating tracking link: {e}")
            return None

    @staticmethod
    def validate_email(email):
        """
        Validates the given email address.

        Parameters:
        email (str): The email address to validate.

        Raises:
        ValueError: If the email address is invalid.
        """
        if '@' not in email or '.' not in email.split('@')[1]:
            raise ValueError("Invalid email address format.")


def main():
    # Example usage
    base_domain = "r20.rs6.net"
    campaign = EmailCampaign(base_domain)

    # Sample data
    campaign_id = "12345"
    recipient_email = "example@example.com"

    # Generate the tracking link
    tracking_link = campaign.generate_tracking_link(campaign_id, recipient_email)

    if tracking_link:
        print(f"Generated tracking link: {tracking_link}")


if __name__ == "__main__":
    main()
```
