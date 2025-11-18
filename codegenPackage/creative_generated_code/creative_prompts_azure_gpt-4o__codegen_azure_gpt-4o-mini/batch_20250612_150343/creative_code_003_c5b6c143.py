"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: Provide a code example for integrating an email automation tool to send quotes for glass installation projects, using customer inputs like dimensions, glass type, and installation location.
Generated: DETERMINISTIC_c5b6c143a1eb70fe
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSender:
    """Class to handle sending emails for glass installation quotes."""
    
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initializes the EmailSender with SMTP server details.
        
        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param username: SMTP account username
        :param password: SMTP account password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient_email, subject, body):
        """
        Sends an email using the SMTP server.
        
        :param recipient_email: Email address of the recipient
        :param subject: Subject of the email
        :param body: Body content of the email
        """
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Attach the message body
        msg.attach(MIMEText(body, 'plain'))
        
        try:
            # Set up the server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS
                server.login(self.username, self.password)
                server.send_message(msg)
            print("Email sent successfully!")
        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")

def generate_quote(dimensions, glass_type, location):
    """
    Generates a quote for a glass installation based on user input.
    
    :param dimensions: Dimensions of the glass (width, height)
    :param glass_type: Type of glass required
    :param location: Installation location details
    :return: Formatted quote string
    """
    # Simple pricing logic for demonstration purposes
    base_price_per_sqft = 20  # Example base price per square foot
    width, height = dimensions
    area = width * height
    total_price = area * base_price_per_sqft
    
    quote = (
        f"Quote for Glass Installation\n"
        f"---------------------------\n"
        f"Dimensions: {width} x {height} sqft\n"
        f"Glass Type: {glass_type}\n"
        f"Installation Location: {location}\n"
        f"Total Price: ${total_price:.2f}\n"
    )
    
    return quote

def main():
    # User inputs for the installation project
    dimensions = (5, 10)  # Width and height in feet
    glass_type = "Tempered Glass"
    location = "Living Room Window"
    recipient_email = "customer@example.com"

    # Generate the quote
    quote = generate_quote(dimensions, glass_type, location)

    # Email configuration
    smtp_server = 'smtp.example.com'
    smtp_port = 587  # Standard port for TLS
    username = 'your_email@example.com'
    password = 'your_password'  # Use environment variables for sensitive information in production

    # Create an instance of EmailSender
    email_sender = EmailSender(smtp_server, smtp_port, username, password)

    # Send the quote via email
    email_sender.send_email(recipient_email, "Your Glass Installation Quote", quote)

if __name__ == '__main__':
    main()
```
