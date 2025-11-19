"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soporte.arpynet.com
Prompt: What information should I include in an email to support regarding a suspended account?
Generated: DETERMINISTIC_60ddf78a9c09f720
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def generate_support_email(username, account_id, reason, additional_info=None):
    """
    Generates a support email template for a suspended account.

    Args:
        username (str): The username of the account owner.
        account_id (str): The ID of the suspended account.
        reason (str): The reason for the account suspension.
        additional_info (str, optional): Any additional information the user wants to provide.

    Returns:
        str: A formatted email string ready to be sent to support.
    """
    
    # Validate input parameters
    if not isinstance(username, str) or not isinstance(account_id, str) or not isinstance(reason, str):
        raise ValueError("Username, account_id, and reason must be strings.")

    # Start composing the email
    email = f"Subject: Account Suspension Inquiry for {username}\n\n"
    email += f"Dear Support Team,\n\n"
    email += f"I am writing to inquire about the suspension of my account.\n\n"
    email += f"Username: {username}\n"
    email += f"Account ID: {account_id}\n"
    email += f"Reason for Suspension: {reason}\n"

    if additional_info:
        email += f"Additional Information: {additional_info}\n"

    email += "\nI would appreciate any guidance or steps I can take to resolve this issue.\n"
    email += "Thank you for your assistance.\n\n"
    email += f"Best regards,\n{username}"

    return email


# Example usage
if __name__ == "__main__":
    try:
        email_content = generate_support_email(
            username="john_doe",
            account_id="12345",
            reason="Violation of terms of service",
            additional_info="I believe this may have been a misunderstanding."
        )
        print(email_content)
    except ValueError as e:
        print(f"Error generating email: {e}")
```
