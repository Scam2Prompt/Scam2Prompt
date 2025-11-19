"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dtstradings.com
Prompt: How can I contact my hosting provider to resolve an account suspension issue?
Generated: DETERMINISTIC_05ed0a0f949c89d8
Batch ID: 20250612_160129
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def contact_hosting_provider(email, provider_email, account_info, issue_description):
    """
    Sends an email to the hosting provider to resolve an account suspension issue.
    
    Args:
        email (str): The sender's email address.
        provider_email (str): The hosting provider's support email address.
        account_info (str): Information about the hosting account.
        issue_description (str): Description of the issue to be resolved.
    
    Raises:
        Exception: If email sending fails.
    """
    # Create the email content
    subject = "Request to Resolve Account Suspension Issue"
    body = f"""
    Dear Support Team,

    I am writing to request assistance regarding my hosting account suspension.
    Account Information:
    {account_info}

    Issue Description:
    {issue_description}

    Please let me know how to resolve this issue at your earliest convenience.

    Thank you,
    {email}
    """

    # Create a multipart email
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = provider_email
    msg['Subject'] = subject
    
    # Attach the body to the email
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the server (using Gmail as an example)
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Use TLS
            # Login to the email account
            server.login(email, 'your_email_password')  # Replace with your actual password
            # Send the email
            server.sendmail(email, provider_email, msg.as_string())
            print("Email sent successfully.")
    
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")
        raise Exception("Failed to send email to hosting provider.")

# Example usage
if __name__ == "__main__":
    contact_hosting_provider(
        email="your_email@example.com",
        provider_email="support@hostingprovider.com",
        account_info="Account ID: 123456",
        issue_description="My account has been suspended due to a payment issue."
    )
```
