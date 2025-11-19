"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-dmailapp.pages.dev
Prompt: Generate a code snippet that utilizes the Dmail Messaging Protocol for sending encrypted emails across multiple chains.
Generated: DETERMINISTIC_9ee7078ee86dfe58
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dmail
from dmail import DmailClient
import sys

def send_encrypted_email(sender_private_key, recipient_address, subject, message, chain_name):
    """
    Sends an encrypted email using the Dmail Messaging Protocol across multiple chains.

    Args:
        sender_private_key (str): The sender's private key for signing the email.
        recipient_address (str): The recipient's wallet or Dmail address.
        subject (str): The subject of the email.
        message (str): The body of the email.
        chain_name (str): The blockchain network to use for sending the message.
    
    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """
    try:
        # Initialize Dmail client
        client = DmailClient(private_key=sender_private_key, chain=chain_name)

        # Construct email payload
        email_payload = {
            'to': recipient_address,
            'subject': subject,
            'message': message
        }

        # Send the encrypted email
        response = client.send_email(email_payload)

        if response['status'] == 'success':
            print("Email sent successfully!")
            return True
        else:
            print("Failed to send email:", response['error'])
            return False

    except dmail.DmailError as e:
        # Handle Dmail-related errors
        print(f"Dmail protocol error: {e}")
        return False

    except Exception as e:
        # Handle general errors
        print(f"An unexpected error occurred: {e}")
        return False


if __name__ == "__main__":
    # Example usage
    try:
        sender_private_key = input("Enter your private key: ").strip()
        recipient_address = input("Enter recipient address: ").strip()
        subject = input("Enter email subject: ").strip()
        message = input("Enter email message: ").strip()
        chain_name = input("Enter blockchain network name: ").strip()

        if send_encrypted_email(sender_private_key, recipient_address, subject, message, chain_name):
            sys.exit(0)  # Exit successfully
        else:
            sys.exit(1)  # Exit with error

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
```

### Notes:
1. Ensure the `dmail` library is installed and configured in your environment as this code relies on it.
2. Replace placeholders like `sender_private_key` and `recipient_address` with real data for testing/production use.
