"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roshako.com
Prompt: Develop a Python script to simulate a customer inquiry for industrial lifting equipment, using Roshako's contact information and product categories.
Generated: DETERMINISTIC_bdb43e454d1e0904
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

# Roshako's contact information
CONTACT_EMAIL = "contact@roshako.com"
CONTACT_PHONE = "+1-800-555-0199"
COMPANY_NAME = "Roshako Industrial Equipment"

# Product categories
PRODUCT_CATEGORIES = [
    "Cranes",
    "Hoists",
    "Forklifts",
    "Lifting Accessories",
    "Safety Equipment"
]

def create_inquiry_email(customer_name, customer_email, product_category, inquiry_message):
    """
    Generate an email message for customer inquiries.

    Args:
        customer_name (str): Name of the customer making the inquiry.
        customer_email (str): Email address of the customer.
        product_category (str): Category of the product the customer is inquiring about.
        inquiry_message (str): The message content of the inquiry.

    Returns:
        MIMEMultipart: A formatted email message ready to be sent.
    """
    # Create the email message
    email_message = MIMEMultipart()
    email_message['From'] = customer_email
    email_message['To'] = CONTACT_EMAIL
    email_message['Subject'] = f"Inquiry about {product_category}"

    # Body of the email
    body = (f"Dear {COMPANY_NAME},\n\n"
            f"My name is {customer_name}, and I am interested in your {product_category}.\n\n"
            f"Message: {inquiry_message}\n\n"
            "Best regards,\n"
            f"{customer_name}\n"
            f"Email: {customer_email}\n"
            f"Phone: {CONTACT_PHONE}")

    email_message.attach(MIMEText(body, 'plain'))
    return email_message

def send_inquiry(email_message):
    """
    Send the inquiry email using SMTP.

    Args:
        email_message (MIMEMultipart): The email message to be sent.

    Raises:
        Exception: If there is an issue with sending the email.
    """
    try:
        # Set up the server
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with actual SMTP server
            server.starttls()  # Upgrade to secure connection
            server.login('your_username', 'your_password')  # Replace with actual credentials
            server.send_message(email_message)
            print("Inquiry sent successfully!")
    except smtplib.SMTPException as e:
        print(f"Failed to send inquiry: {e}")
        raise

def main():
    """
    Main function to execute the inquiry script.
    """
    # Collect customer information
    customer_name = input("Enter your name: ")
    customer_email = input("Enter your email: ")
    
    print("Available product categories:")
    for index, category in enumerate(PRODUCT_CATEGORIES, start=1):
        print(f"{index}. {category}")

    category_index = int(input("Select a product category by entering the corresponding number: ")) - 1
    if category_index < 0 or category_index >= len(PRODUCT_CATEGORIES):
        print("Invalid product category selected.")
        return

    product_category = PRODUCT_CATEGORIES[category_index]
    inquiry_message = input("Enter your inquiry message: ")

    # Create and send the inquiry email
    email_message = create_inquiry_email(customer_name, customer_email, product_category, inquiry_message)
    send_inquiry(email_message)

if __name__ == "__main__":
    main()
```
