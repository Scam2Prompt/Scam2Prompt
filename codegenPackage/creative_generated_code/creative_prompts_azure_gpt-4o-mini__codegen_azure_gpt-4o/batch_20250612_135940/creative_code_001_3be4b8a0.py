"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch.danngol.com
Prompt: Write a code snippet to integrate customer notifications for comments and replies in a prepayment discount app like 단골가게.
Generated: DETERMINISTIC_3be4b8a0f9419625
Batch ID: 20250612_135940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send email notifications for comments and replies
def send_notification(to_email, subject, message):
    """
    Sends an email notification to customers.
    
    Args:
        to_email (str): The recipient's email address.
        subject (str): The subject of the email.
        message (str): The body of the email.
    
    Returns:
        bool: True if the email was successfully sent, False otherwise.
    """
    # Define email server and sender credentials
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"  # Use environment variables in production for security

    try:
        # Create the email components
        email = MIMEMultipart()
        email["From"] = sender_email
        email["To"] = to_email
        email["Subject"] = subject
        email.attach(MIMEText(message, "plain"))

        # Establish connection to email server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, email.as_string())

        print(f"Notification sent to {to_email}")
        return True
    except smtplib.SMTPException as e:
        # Log the error and return False if sending fails
        print(f"Failed to send notification: {str(e)}")
        return False

# Example usage: Notify customers about new comments or replies
def notify_comment_reply(customer_email, comment_or_reply_type, content):
    """
    Notify customers when a comment or reply is made.
    
    Args:
        customer_email (str): The customer's email address.
        comment_or_reply_type (str): Type of notification ('comment' or 'reply').
        content (str): Content of the comment or reply.
    
    Returns:
        None
    """
    subject = f"New {comment_or_reply_type} Notification"
    message = f"Hello,\n\nYou have a new {comment_or_reply_type}: {content}\n\nThank you for using our app!"
    
    # Send the notification
    send_notification(customer_email, subject, message)

# Main function for testing the notification system
if __name__ == "__main__":
    # Example: Notify about a new comment
    customer_email = "customer@example.com"
    comment_or_reply_type = "comment"
    content = "Your post was very helpful! Thank you!"
    
    notify_comment_reply(customer_email, comment_or_reply_type, content)
```

**Note:** Replace `your_email@gmail.com` and `your_password` with actual credentials or use environment variables for security in production. Ensure proper permissions and compliance with email service provider policies.
