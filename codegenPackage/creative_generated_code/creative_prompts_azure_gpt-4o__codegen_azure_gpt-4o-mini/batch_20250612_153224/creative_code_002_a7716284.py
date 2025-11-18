"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magicbear.com.br
Prompt: Generate code to send automated email notifications (e.g., contato@magicbear.com.br) to parents about updates in a bilingual school program using Python.
Generated: DETERMINISTIC_a771628402f1e6be
Batch ID: 20250612_153224
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
from email.mime.base import MIMEBase
from email import encoders
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Common SMTP port for TLS
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email
EMAIL_PASSWORD = 'your_email_password'  # Replace with your email password

def send_email(to_email: str, subject: str, body: str, attachment_path: str = None):
    """
    Sends an email with the specified subject and body to the given recipient.

    :param to_email: The recipient's email address.
    :param subject: The subject of the email.
    :param body: The body content of the email.
    :param attachment_path: Optional path to a file to attach to the email.
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the body to the email
        msg.attach(MIMEText(body, 'html'))

        # Attach a file if an attachment path is provided
        if attachment_path:
            with open(attachment_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={attachment_path.split("/")[-1]}')
                msg.attach(part)

        # Establish a secure session with the mail server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Start TLS for security
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Log in to the email account
            server.send_message(msg)  # Send the email
            logging.info('Email sent successfully to %s', to_email)

    except FileNotFoundError:
        logging.error('Attachment file not found: %s', attachment_path)
    except smtplib.SMTPAuthenticationError:
        logging.error('Could not authenticate with SMTP server. Check your email and password.')
    except Exception as e:
        logging.error('An error occurred while sending email: %s', str(e))

if __name__ == '__main__':
    # Example usage
    recipient_email = 'contato@magicbear.com.br'
    email_subject = 'Atualizações no Programa Escolar Bilingue'
    email_body = """
    <h1>Olá Pais!</h1>
    <p>Estamos entusiasmados em informá-los sobre as últimas atualizações em nosso programa escolar bilingue.</p>
    <p>Atenciosamente,<br>A Equipe da Escola</p>
    """
    
    # Optionally provide an attachment path if needed
    attachment_file = None  # Change this to the path of the file you want to attach, if any

    send_email(recipient_email, email_subject, email_body, attachment_file)
```
