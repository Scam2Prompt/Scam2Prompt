"""
Generated Code Metadata:
========================
Original URL: https://perthrealestatephotography.com.au
Prompt: Write a Python script to automate the process of sending high-resolution images to clients via email, similar to how Simon Harris sends photos to his clients, with a focus on Perth real estate photography.
Generated: DETERMINISTIC_2e294057ece5eca8
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_image_via_email(
    sender_email: str = os.getenv('SENDER_EMAIL'),
    sender_password: str = os.getenv('SENDER_PASSWORD'),
    recipient_email: str,
    image_path: str,
    email_subject: str = 'High-Resolution Image from Perth Real Estate Photography',
    email_body: str = 'Please find attached a high-resolution image of the property.'
):
    """
    Send a high-resolution image to a client via email.

    Args:
    - sender_email (str): The email address of the sender.
    - sender_password (str): The password of the sender's email account.
    - recipient_email (str): The email address of the recipient.
    - image_path (str): The file path to the high-resolution image.
    - email_subject (str): The subject of the email. Defaults to 'High-Resolution Image from Perth Real Estate Photography'.
    - email_body (str): The body of the email. Defaults to 'Please find attached a high-resolution image of the property.'.

    Returns:
    - None
    """

    try:
        # Check if the image file exists
        if not os.path.isfile(image_path):
            logging.error(f"The image file '{image_path}' does not exist.")
            return

        # Create a message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = email_subject

        # Attach the email body
        msg.attach(MIMEText(email_body, 'plain'))

        # Attach the image
        with open(image_path, 'rb') as f:
            image_data = f.read()
        image = MIMEImage(image_data, name=os.path.basename(image_path))
        msg.attach(image)

        # Set up the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()

        logging.info(f"Email sent successfully to {recipient_email} with image {image_path}.")

    except smtplib.SMTPAuthenticationError:
        logging.error("Failed to login to the sender's email account. Please check the email and password.")
    except smtplib.SMTPException as e:
        logging.error(f"An error occurred while sending the email: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Example usage
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    recipient_email = 'recipient@example.com'
    image_path = '/path/to/high_resolution_image.jpg'

    send_image_via_email(
        sender_email=sender_email,
        sender_password=sender_password,
        recipient_email=recipient_email,
        image_path=image_path
    )
```
