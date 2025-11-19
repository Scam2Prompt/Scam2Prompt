"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kaltiacomunidadeducativamontessori.com
Prompt: How can I contact my hosting provider to resolve an account suspension issue?
Generated: DETERMINISTIC_05ed0a0f949c89d8
Batch ID: 20250612_162051
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
        issue_description (str): A description of the issue.
    
    Raises:
        Exception: If email sending fails.
    """
    # Create the email subject and body
    subject = "Urgent: Account Suspension Issue"
    body = f"""
    Dear Support Team,

    I am writing to request assistance regarding my hosting account that has been suspended. 
    Account Information:
    {account_info}
    
    Issue Description:
    {issue_description}

    Please let me know how I can resolve this issue at your earliest convenience.

    Thank you,
    {email}
    """

    # Set up the email server
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = provider_email
        msg['Subject'] = subject
        
        # Attach the body to the email
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the email server
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with actual SMTP server
            server.starttls()  # Upgrade the connection to secure
            server.login(email, 'your_password')  # Replace with actual login credentials
            server.send_message(msg)  # Send the email

        print("Email sent successfully.")

    except smtplib.SMTPException as e:
        print(f"Error occurred while sending email: {e}")
        raise Exception("Failed to send email to hosting provider.")

# Example usage
if __name__ == "__main__":
    sender_email = "your_email@example.com"  # Replace with actual sender email
    provider_email_address = "support@hostingprovider.com"  # Replace with actual provider email
    account_details = "Account Name: example_account, Account ID: 123456"
    issue_details = "My account has been suspended without prior notice."

    contact_hosting_provider(sender_email, provider_email_address, account_details, issue_details)
```
