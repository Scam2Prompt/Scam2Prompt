"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roshako.com
Prompt: Create a function in Python to automate the generation of a quotation request email for industrial products, using Roshako's contact details and product categories.
Generated: DETERMINISTIC_79c04920b0a7482a
Batch ID: 20250612_154355
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

def generate_quotation_email(sender_email, sender_password, recipient_email, product_category, quantity, details):
    """
    Generate and send a quotation request email for industrial products.

    Args:
        sender_email (str): Email address of the sender.
        sender_password (str): Password for the sender's email account.
        recipient_email (str): Email address of the recipient.
        product_category (str): Product category for the quotation request.
        quantity (int): Quantity of the product required.
        details (str): Additional details or specifications for the product.

    Raises:
        ValueError: If any of the input arguments are invalid.
    """

    # Validate input arguments
    if not sender_email or not sender_password or not recipient_email:
        raise ValueError("Sender email, sender password, and recipient email cannot be empty.")
    if not product_category or not isinstance(product_category, str):
        raise ValueError("Product category must be a non-empty string.")
    if not isinstance(quantity, int) or quantity <= 0:
        raise ValueError("Quantity must be a positive integer.")
    if not details or not isinstance(details, str):
        raise ValueError("Details must be a non-empty string.")

    # Create the email subject and body
    subject = f"Quotation Request for {product_category}"
    body = (
        f"Dear Roshako Sales Team,\n\n"
        f"I am writing to request a quotation for the following:\n\n"
        f"Product Category: {product_category}\n"
        f"Quantity: {quantity}\n\n"
        f"Additional Details:\n{details}\n\n"
        f"Please let me know your best offer and the availability of the requested products.\n\n"
        f"Thank you.\n\n"
        f"Best regards,\n"
        f"Your Name"
    )

    try:
        # Set up the email
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Log in using sender's credentials
            server.send_message(message)  # Send the email

        print("Quotation request email sent successfully.")
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
# generate_quotation_email(
#     sender_email="your_email@gmail.com",
#     sender_password="your_password",
#     recipient_email="sales@roshako.com",
#     product_category="Industrial Bearings",
#     quantity=100,
#     details="Require high-performance bearings with a diameter of 50mm."
# )
```
