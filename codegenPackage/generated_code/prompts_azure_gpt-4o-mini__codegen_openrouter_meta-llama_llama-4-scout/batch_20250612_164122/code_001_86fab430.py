"""
Generated Code Metadata:
========================
Original URL: https://handyfix.co.nz
Prompt: Write a Python script that sends an email request to Handyfix for a handyman job, using the provided contact details and service requirements.
Generated: DETERMINISTIC_86fab430257aa604
Batch ID: 20250612_164122
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
import json

def send_handyman_request(contact_name, contact_email, contact_phone, service_address, service_description):
    """
    Send an email request to Handyfix for a handyman job.

    Args:
        contact_name (str): The name of the person requesting the service.
        contact_email (str): The email address of the person requesting the service.
        contact_phone (str): The phone number of the person requesting the service.
        service_address (str): The address where the service is required.
        service_description (str): A brief description of the service required.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """

    # Define the Handyfix email configuration
    HANDYFIX_EMAIL = "handyfix@example.com"
    HANDYFIX_PASSWORD = "handyfix_password"
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587

    try:
        # Create a message
        msg = MIMEMultipart()
        msg['From'] = contact_email
        msg['To'] = HANDYFIX_EMAIL
        msg['Subject'] = "Handyman Service Request"

        # Create the email body
        body = f"""
        Name: {contact_name}
        Email: {contact_email}
        Phone: {contact_phone}
        Address: {service_address}
        Service Description: {service_description}
        """

        # Attach the email body to the message
        msg.attach(MIMEText(body, 'plain'))

        # Set up the SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(HANDYFIX_EMAIL, HANDYFIX_PASSWORD)

        # Send the email
        text = msg.as_string()
        server.sendmail(contact_email, HANDYFIX_EMAIL, text)
        server.quit()

        return True

    except smtplib.SMTPAuthenticationError:
        print("Error: Invalid email credentials.")
        return False
    except smtplib.SMTPException as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def load_config(file_path):
    """
    Load the configuration from a JSON file.

    Args:
        file_path (str): The path to the configuration file.

    Returns:
        dict: The configuration data.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: Configuration file not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: Invalid configuration file.")
        return {}


def main():
    # Load the configuration
    config = load_config('config.json')

    # Define the contact and service details
    contact_name = config.get('contact_name')
    contact_email = config.get('contact_email')
    contact_phone = config.get('contact_phone')
    service_address = config.get('service_address')
    service_description = config.get('service_description')

    # Send the email request
    if contact_name and contact_email and contact_phone and service_address and service_description:
        success = send_handyman_request(contact_name, contact_email, contact_phone, service_address, service_description)
        if success:
            print("Email sent successfully.")
        else:
            print("Failed to send email.")
    else:
        print("Error: Please provide all required details.")


if __name__ == "__main__":
    main()
```
