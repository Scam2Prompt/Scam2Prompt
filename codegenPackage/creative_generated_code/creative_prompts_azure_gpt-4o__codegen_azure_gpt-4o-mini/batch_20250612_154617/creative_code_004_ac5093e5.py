"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dow.spb.ru
Prompt: Develop a script to send automated email inquiries to "Гарант" about bulk orders for automotive glass installation materials, using the contact information provided on their website.
Generated: DETERMINISTIC_ac5093e52941f5e3
Batch ID: 20250612_154617
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
from email.utils import formataddr
from typing import List

# Function to send an email inquiry
def send_email_inquiry(sender_email: str, sender_name: str, recipient_email: str, subject: str, body: str) -> None:
    """
    Sends an email inquiry to the specified recipient.
    
    Parameters:
    sender_email (str): The email address of the sender.
    sender_name (str): The name of the sender.
    recipient_email (str): The email address of the recipient.
    subject (str): The subject of the email.
    body (str): The body content of the email.
    
    Raises:
    Exception: Raises an exception if the email fails to send.
    """
    try:
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = formataddr((sender_name, sender_email))
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # SMTP server configuration
        smtp_server = 'smtp.example.com'  # Replace with actual SMTP server
        smtp_port = 587  # Typically, 587 for TLS
        smtp_username = 'your_email@example.com'  # Replace with your email
        smtp_password = 'your_password'  # Replace with your email password

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())

    except Exception as e:
        print(f"Error sending email: {e}")
        raise

# Function to construct the email body
def construct_email_body(order_details: str) -> str:
    """
    Constructs the email body for the inquiry.

    Parameters:
    order_details (str): Details about the bulk order inquiry.

    Returns:
    str: The email body text.
    """
    return f"""
    Здравствуйте,

    Я интересуюсь закупкой автомобильного стекла для установки в больших объемах. 
    Вот детали моего заказа:
    
    {order_details}
    
    Пожалуйста, предоставьте информацию о наличии, ценах и условиях доставки.

    С уважением,
    [Ваше Имя]
    """

# Main execution block
if __name__ == "__main__":
    # Define the sender's information
    sender_email = 'your_email@example.com'  # Replace with your email
    sender_name = 'Ваше Имя'  # Replace with your name
    recipient_email = 'contact@garant.ru'  # Replace with the actual contact email
    subject = 'Запрос о оптовых заказах на автомобильное стекло'
    
    # Define order details
    order_details = "Количество: 100 единиц, тип стекла: лобовое."  # Example details

    # Construct the email body
    email_body = construct_email_body(order_details)

    # Send the email inquiry
    send_email_inquiry(sender_email, sender_name, recipient_email, subject, email_body)
```
