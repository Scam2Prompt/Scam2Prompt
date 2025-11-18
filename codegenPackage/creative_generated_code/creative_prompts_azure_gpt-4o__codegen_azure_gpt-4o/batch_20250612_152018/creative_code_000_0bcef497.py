"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://darulraza.net
Prompt: Write a Python script to automate sending Istikhara requests via email using the contact details provided on the Darul Raza website.
Generated: DETERMINISTIC_0bcef497a3d330c7
Batch ID: 20250612_152018
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
import ssl

# Configuration settings
SMTP_SERVER = "smtp.gmail.com"  # Replace with the SMTP server you are using
SMTP_PORT = 465  # SSL port
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"  # Replace with your email password
RECIPIENT_EMAIL = "contact@darulraza.com"  # Replace with the recipient's email address
SUBJECT = "Istikhara Request"

# Function to send an Istikhara email
def send_istikhara_request(name, phone, email, request_message):
    """
    Sends an Istikhara request via email to the specified recipient.
    
    :param name: Name of the person making the request
    :param phone: Contact phone number
    :param email: Contact email address
    :param request_message: The Istikhara request message
    """
    try:
        # Format the email content
        message = MIMEMultipart()
        message["From"] = EMAIL_ADDRESS
        message["To"] = RECIPIENT_EMAIL
        message["Subject"] = SUBJECT
        
        # Prepare the body of the email
        body = f"""
        Assalamu Alaikum Wa Rahmatullahi Wa Barakatuh,

        I would like to submit an Istikhara request. Here are my details:

        Name: {name}
        Phone: {phone}
        Email: {email}

        Request:
        {request_message}

        JazakAllah Khair for your assistance.

        Regards,
        {name}
        """
        message.attach(MIMEText(body, "plain"))
        
        # Connect to the SMTP server and send the email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, message.as_string())
        
        print("Istikhara request email sent successfully.")
    except Exception as e:
        # Handle any errors that occur during the email-sending process
        print(f"An error occurred while sending the email: {e}")


# Example usage
if __name__ == "__main__":
    # Replace these fields with actual data
    name = "John Doe"
    phone = "1234567890"
    email = "john.doe@example.com"
    request_message = "I am seeking guidance for a decision regarding my career."
    
    send_istikhara_request(name, phone, email, request_message)
```

### Notes:
1. Replace placeholders such as `your_email@example.com`, `your_password`, and `contact@darulraza.com` with actual values.
2. Ensure you use a secure method to store and retrieve credentials (e.g., environment variables or a secrets manager) instead of hardcoding them in production.
3. Make sure the SMTP server and port match your email provider's configuration.
4. Adjust the `RECIPIENT_EMAIL` field to the actual email address provided by Darul Raza for Istikhara requests.
