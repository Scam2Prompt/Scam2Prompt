"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solutechsystem.com.ng
Prompt: Draft a marketing email template for promoting a newly designed NGO website, inspired by the digital marketing strategies of Solutech System.
Generated: DETERMINISTIC_919cd8993e9154f1
Batch ID: 20250612_160408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.ngo-website.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

def send_marketing_email(sender_email, recipient_email, sender_password):
    """
    Sends a marketing email to promote the newly designed NGO website.
    
    Parameters:
    sender_email (str): The email address of the sender.
    recipient_email (str): The email address of the recipient.
    sender_password (str): The password for the sender's email account.
    """

    try:
        # Create the email content
        subject = "Discover Our Newly Designed NGO Website!"
        body_html = """
        <html>
        <head>
            <style>
                .email-container {
                    font-family: Arial, sans-serif;
                    color: #333333;
                    line-height: 1.6;
                }
                .btn {
                    display: inline-block;
                    padding: 10px 20px;
                    color: #fff;
                    background-color: #007BFF;
                    text-decoration: none;
                    border-radius: 5px;
                }
                .btn:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <div class="email-container">
                <h1>Welcome to Our New Website!</h1>
                <p>We are thrilled to announce the launch of our newly redesigned website. 
                Our goal is to provide you with an improved browsing experience and easy access to all the resources and updates about our NGO.</p>
                <p><strong>What’s new?</strong></p>
                <ul>
                    <li>Modern and user-friendly design</li>
                    <li>Enhanced navigation for better usability</li>
                    <li>Updated content showcasing our latest projects and achievements</li>
                </ul>
                <p>We invite you to explore the new website and stay connected with our mission to make a difference.</p>
                <p><a href="https://www.ngo-website.com" class="btn">Visit Our Website</a></p>
                <p>Thank you for your continued support!</p>
                <p>Best regards,</p>
                <p>The NGO Team</p>
            </div>
        </body>
        </html>
        """

        # Create the MIME message
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = recipient_email

        # Attach the HTML body
        msg.attach(MIMEText(body_html, "html"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:  # Assuming Gmail is used
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())

        print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("Error: Authentication failed. Please check your email and password.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage:
# Replace these values with your actual email credentials and recipient email
sender_email = "your_email@example.com"
recipient_email = "recipient_email@example.com"
sender_password = "your_email_password"

# Send the marketing email
send_marketing_email(sender_email, recipient_email, sender_password)
```
