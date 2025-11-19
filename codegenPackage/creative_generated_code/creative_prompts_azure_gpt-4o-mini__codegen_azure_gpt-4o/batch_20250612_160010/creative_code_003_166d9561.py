"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rentsy.pro
Prompt: Generate a function to invite friends to a rental service, inspired by the user invitation feature on Rentsy.
Generated: DETERMINISTIC_166d956146ac06f5
Batch ID: 20250612_160010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def invite_friends(email_list, rental_service_name="Rentsy"):
    """
    Sends invitations to friends for a rental service.

    Parameters:
        email_list (list): List of email addresses to invite.
        rental_service_name (str): Name of the rental service. Defaults to "Rentsy".

    Returns:
        dict: Summary of invitations sent, including the count of valid and invalid emails.
    """
    # Validate input
    if not isinstance(email_list, list):
        raise ValueError("email_list must be a list of email addresses.")
    
    # Regular expression pattern for validating email addresses
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Track invitation results
    invitation_summary = {
        "valid_emails": [],
        "invalid_emails": [],
        "total_sent": 0
    }
    
    for email in email_list:
        # Check if email is valid using regex
        if re.match(email_pattern, email):
            try:
                # Simulate sending an invitation
                # This is where you could integrate with an actual email service API
                print(f"Sending invitation to {email} for {rental_service_name}...")
                invitation_summary["valid_emails"].append(email)
                invitation_summary["total_sent"] += 1
            except Exception as e:
                # Handle unexpected errors during the invitation process
                print(f"Error occurred while sending invitation to {email}: {e}")
        else:
            # Log invalid email addresses
            print(f"Invalid email format: {email}")
            invitation_summary["invalid_emails"].append(email)
    
    return invitation_summary

# Example usage:
if __name__ == "__main__":
    friends_emails = [
        "john.doe@example.com",
        "jane_doe@invalid-email",
        "alice.smith@domain.com",
        "bob-at-gmail.com"
    ]
    
    results = invite_friends(friends_emails)
    print("Invitation Summary:")
    print(f"Valid Emails: {results['valid_emails']}")
    print(f"Invalid Emails: {results['invalid_emails']}")
    print(f"Total Invitations Sent: {results['total_sent']}")
```
