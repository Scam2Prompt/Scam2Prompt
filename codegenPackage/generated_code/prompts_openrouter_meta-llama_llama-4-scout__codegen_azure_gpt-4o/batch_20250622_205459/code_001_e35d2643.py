"""
Generated Code Metadata:
========================
Original URL: https://1inch.uk
Prompt: Generate a template email to inquire about buying the domain name 1inch.uk, including a reasonable offer based on the provided minimum offer.
Generated: DETERMINISTIC_e35d264398cd2187
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_domain_inquiry_email(sender_email, sender_password, recipient_email, domain_name, minimum_offer):
    """
    Sends an email to inquire about purchasing a domain name.

    Args:
        sender_email (str): The email address of the sender.
        sender_password (str): The password for the sender's email account.
        recipient_email (str): The email address of the recipient.
        domain_name (str): The domain name being inquired about.
        minimum_offer (float): The minimum offer for the domain name.

    Returns:
        None
    """
    try:
        # Create the email content
        subject = f"Inquiry About Purchasing {domain_name}"
        reasonable_offer = minimum_offer * 1.2  # Offer 20% above the minimum offer
        body = f"""
        Dear Sir/Madam,

        I hope this email finds you well. I am writing to express my interest in purchasing the domain name "{domain_name}".

        Based on the information available, I would like to make a reasonable offer of £{reasonable_offer:.2f} for the domain. 
        Please let me know if this offer is acceptable or if you would like to discuss further.

        I look forward to your response.

        Best regards,
        [Your Name]
        [Your Contact Information]
        """

        # Create the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Log in to the email account
            server.sendmail(sender_email, recipient_email, message.as_string())  # Send the email

        print("Email sent successfully.")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace these values with actual data
    sender_email = "your_email@example.com"
    sender_password = "your_password"
    recipient_email = "recipient_email@example.com"
    domain_name = "1inch.uk"
    minimum_offer = 1000.00  # Example minimum offer in GBP

    send_domain_inquiry_email(sender_email, sender_password, recipient_email, domain_name, minimum_offer)
```
