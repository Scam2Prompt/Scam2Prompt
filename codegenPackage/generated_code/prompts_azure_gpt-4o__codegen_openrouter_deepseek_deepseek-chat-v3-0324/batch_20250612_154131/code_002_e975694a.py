"""
Generated Code Metadata:
========================
Original URL: https://ajrobloxgfx.org
Prompt: Generate a Python script to send an email inquiry to [email protected] about customizing a "Front facing" Roblox profile picture.
Generated: DETERMINISTIC_e975694a58f3c67b
Batch ID: 20250612_154131
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
import getpass
import ssl

def send_email_inquiry():
    # Email configuration
    sender_email = input("Enter your email address: ")
    password = getpass.getpass("Enter your email password: ")
    receiver_email = "[email protected]"
    subject = "Inquiry About Custom Front-Facing Roblox Profile Picture"
    
    # Email content
    body = """Dear Roblox Support Team,

I hope this message finds you well. I am interested in customizing a front-facing profile picture for my Roblox account. Could you please provide me with information about:

1. The customization options available
2. Pricing details
3. Estimated turnaround time
4. Any requirements or specifications needed from my side

Thank you for your time and assistance. I look forward to your response.

Best regards,
[Your Name]"""

    # Create message container
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach body to the email
    message.attach(MIMEText(body, "plain"))

    try:
        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Error: Authentication failed. Please check your email and password.")
    except smtplib.SMTPException as e:
        print(f"Error: Unable to send email. {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    send_email_inquiry()
```
