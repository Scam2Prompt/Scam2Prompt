"""
Generated Code Metadata:
========================
Original URL: https://roshako.com
Prompt: Create a function in Python to automate the generation of a quotation request email for industrial products, using Roshako's contact details and product categories.
Generated: DETERMINISTIC_79c04920b0a7482a
Batch ID: 20250612_154355
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

class QuotationRequestEmail:
    def __init__(self, 
                 sender_email: str, 
                 sender_password: str, 
                 recipient_email: str, 
                 product_category: str, 
                 product_description: str, 
                 quantity: int):
        """
        Initialize the QuotationRequestEmail object.

        Args:
        - sender_email (str): The sender's email address.
        - sender_password (str): The sender's email password.
        - recipient_email (str): The recipient's email address.
        - product_category (str): The product category.
        - product_description (str): The product description.
        - quantity (int): The quantity of products.
        """
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient_email = recipient_email
        self.product_category = product_category
        self.product_description = product_description
        self.quantity = quantity

    def generate_email_content(self) -> str:
        """
        Generate the email content.

        Returns:
        - str: The email content.
        """
        # Roshako's contact details
        company_name = "Roshako"
        company_address = "123 Main St, Anytown, USA 12345"
        phone_number = "+1 123-456-7890"
        email_address = "info@roshako.com"

        # Email content
        subject = f"Quotation Request for {self.product_category} Products"
        body = f"""
Dear {company_name} Team,

I am reaching out to request a quotation for {self.quantity} units of {self.product_category} products. 
The product description is as follows:

{self.product_description}

Please find our contact details below:

- Address: {company_address}
- Phone: {phone_number}
- Email: {email_address}

Thank you for your prompt response.

Best regards,
[Your Name]
"""

        return subject, body

    def send_email(self) -> None:
        """
        Send the quotation request email.
        """
        try:
            # Create a message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email
            subject, body = self.generate_email_content()
            msg['Subject'] = subject

            # Attach the body to the message
            msg.attach(MIMEText(body, 'plain'))

            # Set up the SMTP server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.sender_email, self.sender_password)

            # Send the email
            text = msg.as_string()
            server.sendmail(self.sender_email, self.recipient_email, text)
            server.quit()

            print("Email sent successfully!")

        except smtplib.SMTPAuthenticationError:
            print("Authentication error. Please check your email and password.")
        except smtplib.SMTPException as e:
            print(f"An error occurred: {e}")


def main():
    sender_email = "your-email@gmail.com"
    sender_password = "your-email-password"
    recipient_email = "recipient-email@example.com"
    product_category = "Industrial Pumps"
    product_description = "We are looking for industrial pumps with a flow rate of 1000 L/min."
    quantity = 10

    email = QuotationRequestEmail(sender_email, 
                                  sender_password, 
                                  recipient_email, 
                                  product_category, 
                                  product_description, 
                                  quantity)
    email.send_email()


if __name__ == "__main__":
    main()
```
