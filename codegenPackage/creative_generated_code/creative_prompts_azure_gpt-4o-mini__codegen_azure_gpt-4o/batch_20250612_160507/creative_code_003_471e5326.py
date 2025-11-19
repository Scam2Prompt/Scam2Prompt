"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch.uk
Prompt: Write a script that automates sending an inquiry message for the domain 1inch.uk, including user details and offer amount.
Generated: DETERMINISTIC_471e53269842f824
Batch ID: 20250612_160507
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

def send_inquiry(domain, user_details, offer_amount):
    """
    Sends an inquiry email regarding a domain purchase.

    Args:
        domain (str): The domain name being inquired about.
        user_details (dict): Information about the user (name, email, phone).
        offer_amount (float): The user's purchase offer amount.
    """
    # Email configuration
    smtp_server = "smtp.gmail.com"  # Use the appropriate SMTP server
    smtp_port = 587  # Port for TLS
    sender_email = "your_email@gmail.com"  # Replace with your email address
    sender_password = "your_password"  # Replace with your email password
    recipient_email = "contact@domainbroker.com"  # Replace with the recipient's email address

    try:
        # Create the email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = f"Inquiry about purchasing domain: {domain}"

        # Email body
        email_body = f"""
        Hello,

        I am interested in purchasing the domain {domain}. 

        Here are my details:
        Name: {user_details.get('name')}
        Email: {user_details.get('email')}
        Phone: {user_details.get('phone')}
        
        My offer amount: ${offer_amount:.2f}

        Please let me know if this domain is available and if we can proceed with the purchase.

        Best regards,
        {user_details.get('name')}
        """
        message.attach(MIMEText(email_body, "plain"))

        # Connect to the SMTP server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS for security
        server.login(sender_email, sender_password)  # Log in to the server
        server.send_message(message)  # Send the email
        print("Inquiry email sent successfully!")
    except Exception as e:
        print(f"Failed to send inquiry email: {e}")
    finally:
        # Ensure the server connection is closed
        server.quit()

# Example usage
if __name__ == "__main__":
    domain_name = "1inch.uk"
    user_info = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "+1234567890"
    }
    offer = 5000.00  # Offer amount in USD

    send_inquiry(domain_name, user_info, offer)
```

**Notes:**
- Replace `your_email@gmail.com` and `your_password` with valid credentials for the sender email.
- Replace `contact@domainbroker.com` with the actual recipient's email address.
- Make sure proper email security practices are followed, such as using environment variables or secure vaults for storing sensitive data like email credentials.
