"""
Generated Code Metadata:
========================
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: Write code to send automated email notifications for weekly promotions on products like "LUVA DE SEGUR WK10 LATEX FORT G" and "TINTA SPRAY VERNIZ."
Generated: DETERMINISTIC_3ca2cf01d36d5b33
Batch ID: 20250612_145144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('email_notifications.log'),
        logging.StreamHandler()
    ]
)

class EmailSender:
    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        """
        Initialize the email sender with SMTP server details.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(
        self,
        recipient_emails: List[str],
        subject: str,
        body: str,
        is_html: bool = False
    ) -> bool:
        """
        Send an email to multiple recipients.
        
        Args:
            recipient_emails: List of recipient email addresses
            subject: Email subject
            body: Email body content
            is_html: Whether the body is HTML formatted
            
        Returns:
            bool: True if email was sent successfully, False otherwise
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = ", ".join(recipient_emails)
            msg['Subject'] = subject

            if is_html:
                msg.attach(MIMEText(body, 'html'))
            else:
                msg.attach(MIMEText(body, 'plain'))

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)

            logging.info(f"Email sent successfully to {len(recipient_emails)} recipients")
            return True
        except Exception as e:
            logging.error(f"Failed to send email: {str(e)}")
            return False


class PromotionNotifier:
    def __init__(self, email_sender: EmailSender):
        self.email_sender = email_sender

    def generate_promotion_html(self, products: List[Dict[str, str]]) -> str:
        """
        Generate HTML content for the promotion email.
        
        Args:
            products: List of product dictionaries with 'name' and 'discount'
            
        Returns:
            str: HTML formatted email content
        """
        html_content = """
        <html>
            <head></head>
            <body>
                <h2>Weekly Promotion Alert!</h2>
                <p>Here are this week's special offers:</p>
                <ul>
        """
        
        for product in products:
            html_content += f"""
                    <li>
                        <strong>{product['name']}</strong> - {product['discount']} OFF!
                    </li>
            """
        
        html_content += """
                </ul>
                <p>Hurry up! These offers are valid only this week.</p>
                <p>Best regards,<br>Your Store Team</p>
            </body>
        </html>
        """
        return html_content

    def send_weekly_promotions(
        self,
        recipient_emails: List[str],
        products: List[Dict[str, str]]
    ) -> bool:
        """
        Send weekly promotion emails to subscribers.
        
        Args:
            recipient_emails: List of recipient email addresses
            products: List of product dictionaries with 'name' and 'discount'
            
        Returns:
            bool: True if email was sent successfully, False otherwise
        """
        if not recipient_emails:
            logging.warning("No recipients specified for weekly promotions")
            return False

        if not products:
            logging.warning("No products specified for weekly promotions")
            return False

        today = datetime.date.today()
        subject = f"Weekly Promotions - {today.strftime('%B %d, %Y')}"
        html_body = self.generate_promotion_html(products)

        return self.email_sender.send_email(
            recipient_emails=recipient_emails,
            subject=subject,
            body=html_body,
            is_html=True
        )


# Example usage
if __name__ == "__main__":
    # Configuration (should be moved to environment variables or config file in production)
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    SENDER_EMAIL = "promotions@example.com"
    SENDER_PASSWORD = "securepassword"

    # Initialize email sender
    email_sender = EmailSender(
        smtp_server=SMTP_SERVER,
        smtp_port=SMTP_PORT,
        sender_email=SENDER_EMAIL,
        sender_password=SENDER_PASSWORD
    )

    # Initialize promotion notifier
    notifier = PromotionNotifier(email_sender)

    # Example data
    subscribers = ["customer1@example.com", "customer2@example.com"]
    weekly_products = [
        {"name": "LUVA DE SEGUR WK10 LATEX FORT G", "discount": "20%"},
        {"name": "TINTA SPRAY VERNIZ", "discount": "15%"}
    ]

    # Send promotions
    success = notifier.send_weekly_promotions(subscribers, weekly_products)
    if success:
        print("Weekly promotions sent successfully!")
    else:
        print("Failed to send weekly promotions")
```
