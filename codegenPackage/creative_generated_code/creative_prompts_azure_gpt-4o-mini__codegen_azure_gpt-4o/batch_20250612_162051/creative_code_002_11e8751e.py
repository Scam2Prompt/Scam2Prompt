"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bursapleksi.com.tr
Prompt: Create a script that automates sending a price inquiry email to Bursa Pleksi Merkezi for bulk purchases of Plexiglass and Solid Polycarbonate sheets.
Generated: DETERMINISTIC_11e8751e0817b17c
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

def send_price_inquiry_email(company_email, sender_email, sender_password):
    """
    Sends a price inquiry email to Bursa Pleksi Merkezi for bulk purchases of Plexiglass 
    and Solid Polycarbonate sheets.

    Parameters:
        company_email (str): The email address of Bursa Pleksi Merkezi.
        sender_email (str): The sender's email address.
        sender_password (str): The sender's email password for authentication.

    Returns:
        None
    """

    try:
        # Email content
        subject = "Price Inquiry for Bulk Purchases"
        body = """Dear Bursa Pleksi Merkezi,

I hope this message finds you well. I am reaching out to inquire about the pricing for bulk purchases of Plexiglass and Solid Polycarbonate sheets. 
Please provide the following details:

1. Price per sheet for Plexiglass and Solid Polycarbonate for bulk orders.
2. Available sizes and thicknesses.
3. Discount rates for bulk purchases.
4. Estimated delivery times.

Looking forward to your response.

Best regards,
[Your Name]
[Your Contact Information]
"""

        # Create email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = company_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # SMTP server configuration
        smtp_server = "smtp.gmail.com"  # Using Gmail's SMTP server
        smtp_port = 587

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Authenticate
            server.send_message(message)  # Send the email

        print("Price inquiry email successfully sent.")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Input your credentials and recipient email address
    company_email = "bursapleksi@example.com"  # Replace with the actual email address of Bursa Pleksi Merkezi
    sender_email = "your_email@example.com"  # Replace with your email address
    sender_password = "your_password"  # Replace with your email password

    # Send the email
    send_price_inquiry_email(company_email, sender_email, sender_password)
```

**Note**: Replace `bursapleksi@example.com`, `your_email@example.com`, and `your_password` with the actual recipient email, your email, and your email password. Ensure you have enabled "Allow less secure apps" or use an app-specific password for your email account if necessary. Ensure compliance with your email provider's security policies.
