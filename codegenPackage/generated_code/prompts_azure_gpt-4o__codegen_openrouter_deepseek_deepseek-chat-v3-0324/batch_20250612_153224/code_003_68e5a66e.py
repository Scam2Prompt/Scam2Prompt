"""
Generated Code Metadata:
========================
Original URL: https://felipemunozreparaciones.es
Prompt: Write a script using Python's `smtplib` library to send follow-up emails to customers who have requested plumbing or electrical services, referencing the services offered in Murcia.
Generated: DETERMINISTIC_68e5a66e3537552d
Batch ID: 20250612_153224
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
import csv
import os
from dotenv import load_dotenv
from typing import List, Dict

# Load environment variables from .env file
load_dotenv()

class EmailSender:
    """
    A class to handle sending follow-up emails to customers who requested services.
    """
    
    def __init__(self):
        self.smtp_server = os.getenv('SMTP_SERVER')
        self.smtp_port = int(os.getenv('SMTP_PORT', 587))
        self.sender_email = os.getenv('SENDER_EMAIL')
        self.sender_password = os.getenv('SENDER_PASSWORD')
        self.recipients_file = 'customers.csv'
        
        # Validate required environment variables
        if not all([self.smtp_server, self.sender_email, self.sender_password]):
            raise ValueError("Missing required environment variables: SMTP_SERVER, SENDER_EMAIL, SENDER_PASSWORD")
    
    def load_recipients(self) -> List[Dict[str, str]]:
        """
        Load recipient data from CSV file.
        
        Returns:
            List of dictionaries containing recipient data.
            
        Raises:
            FileNotFoundError: If the recipients file doesn't exist.
            Exception: For other CSV reading errors.
        """
        try:
            with open(self.recipients_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        except FileNotFoundError:
            raise FileNotFoundError(f"Recipients file '{self.recipients_file}' not found.")
        except Exception as e:
            raise Exception(f"Error reading recipients file: {str(e)}")
    
    def create_email(self, recipient: Dict[str, str]) -> MIMEMultipart:
        """
        Create a personalized email for the recipient.
        
        Args:
            recipient: Dictionary containing recipient data.
            
        Returns:
            MIMEMultipart email message.
        """
        service_type = recipient.get('service_type', '').lower()
        
        # Determine service-specific content
        if service_type == 'plumbing':
            service_details = """
            <p>We offer comprehensive plumbing services in Murcia including:</p>
            <ul>
                <li>Pipe repairs and installations</li>
                <li>Leak detection and repair</li>
                <li>Water heater installation</li>
                <li>Drain cleaning</li>
            </ul>
            """
        elif service_type == 'electrical':
            service_details = """
            <p>Our electrical services in Murcia include:</p>
            <ul>
                <li>Electrical system installations</li>
                <li>Circuit breaker repairs</li>
                <li>Lighting installations</li>
                <li>Electrical safety inspections</li>
            </ul>
            """
        else:
            service_details = "<p>We offer a wide range of home services in Murcia.</p>"
        
        # Create message container
        msg = MIMEMultipart('alternative')
        msg['From'] = self.sender_email
        msg['To'] = recipient['email']
        msg['Subject'] = f"Follow-up on your {service_type} service request in Murcia"
        
        # Create email body
        text = f"""Hi {recipient.get('name', 'Customer')},
        
Thank you for your recent inquiry about {service_type} services in Murcia.
We would like to follow up and provide more information about our services.

Please reply to this email or call us at +34 123 456 789 to schedule an appointment.

Best regards,
Your Service Team
        """
        
        html = f"""\
        <html>
            <body>
                <p>Hi {recipient.get('name', 'Customer')},</p>
                <p>Thank you for your recent inquiry about {service_type} services in Murcia.</p>
                {service_details}
                <p>Please reply to this email or call us at <strong>+34 123 456 789</strong> to schedule an appointment.</p>
                <p>Best regards,<br>Your Service Team</p>
            </body>
        </html>
        """
        
        # Attach both plain text and HTML versions
        msg.attach(MIMEText(text, 'plain'))
        msg.attach(MIMEText(html, 'html'))
        
        return msg
    
    def send_emails(self) -> None:
        """
        Send follow-up emails to all recipients.
        
        Raises:
            Exception: For any SMTP-related errors.
        """
        try:
            recipients = self.load_recipients()
            if not recipients:
                print("No recipients found.")
                return
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                
                for recipient in recipients:
                    try:
                        msg = self.create_email(recipient)
                        server.sendmail(
                            self.sender_email,
                            recipient['email'],
                            msg.as_string()
                        )
                        print(f"Email sent to {recipient['email']}")
                    except Exception as e:
                        print(f"Failed to send email to {recipient.get('email', 'unknown')}: {str(e)}")
                        
        except smtplib.SMTPException as e:
            raise Exception(f"SMTP error occurred: {str(e)}")
        except Exception as e:
            raise Exception(f"Error sending emails: {str(e)}")

if __name__ == "__main__":
    try:
        email_sender = EmailSender()
        email_sender.send_emails()
    except Exception as e:
        print(f"Error: {str(e)}")
```
