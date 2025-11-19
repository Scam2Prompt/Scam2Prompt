"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://megaetlh.com
Prompt: Generate a Python script that automates the process of transferring domain ownership securely, inspired by the services offered on megaetlh.com.
Generated: DETERMINISTIC_7056c314a26e920c
Batch ID: 20250612_160711
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
import json
import logging
import os
import random
import string
from cryptography.fernet import Fernet

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("domain_transfer.log"),
        logging.StreamHandler()
    ]
)

# Generate a secure key for encrypting sensitive data
KEY_FILE = "encryption_key.key"


def generate_encryption_key():
    """Generate and save a secure encryption key."""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as key_file:
            key_file.write(key)
        logging.info("Encryption key generated and saved.")
    else:
        logging.info("Encryption key already exists.")


def load_encryption_key():
    """Load the encryption key from the local key file."""
    if not os.path.exists(KEY_FILE):
        raise FileNotFoundError("Encryption key not found. Please generate one first.")
    with open(KEY_FILE, 'rb') as key_file:
        return key_file.read()


def encrypt_data(data, key):
    """Encrypt the provided data using the given key."""
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data


def decrypt_data(encrypted_data, key):
    """Decrypt the provided data using the given key."""
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data


def generate_transfer_code(length=16):
    """Generate a secure transfer code."""
    characters = string.ascii_letters + string.digits
    transfer_code = ''.join(random.choice(characters) for _ in range(length))
    return transfer_code


def send_email(sender_email, receiver_email, subject, body, smtp_server, smtp_port, smtp_username, smtp_password):
    """Send an email securely."""
    try:
        # Create a multipart email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(message)
            logging.info(f"Email sent successfully to {receiver_email}.")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")


def transfer_domain(domain_name, sender_email, receiver_email, smtp_config):
    """
    Automate secure domain ownership transfer.

    Args:
        domain_name (str): The name of the domain to transfer.
        sender_email (str): Email of the current domain owner.
        receiver_email (str): Email of the new domain owner.
        smtp_config (dict): Configuration dictionary for the SMTP server.
    """
    try:
        # Generate secure transfer code
        transfer_code = generate_transfer_code()
        logging.info(f"Transfer code generated: {transfer_code}")

        # Encrypt transfer code
        encryption_key = load_encryption_key()
        encrypted_code = encrypt_data(transfer_code, encryption_key)
        logging.info("Transfer code encrypted securely.")

        # Email the transfer code to the receiver
        email_body = (
            f"Domain Transfer Initiation\n\n"
            f"Domain Name: {domain_name}\n"
            f"Transfer Code: {encrypted_code.decode()}\n\n"
            f"Use the transfer code to claim ownership."
        )
        send_email(
            sender_email=sender_email,
            receiver_email=receiver_email,
            subject=f"Domain Transfer for {domain_name}",
            body=email_body,
            smtp_server=smtp_config['server'],
            smtp_port=smtp_config['port'],
            smtp_username=smtp_config['username'],
            smtp_password=smtp_config['password']
        )

        logging.info("Domain transfer email sent successfully.")

    except Exception as e:
        logging.error(f"Error during domain transfer: {e}")


if __name__ == "__main__":
    # Generate encryption key if not exists
    generate_encryption_key()

    # Example domain transfer
    DOMAIN_NAME = "example.com"
    SENDER_EMAIL = "sender@example.com"
    RECEIVER_EMAIL = "receiver@example.com"
    SMTP_CONFIG = {
        'server': 'smtp.example.com',
        'port': 587,
        'username': 'smtp_user',
        'password': 'smtp_password'
    }

    transfer_domain(DOMAIN_NAME, SENDER_EMAIL, RECEIVER_EMAIL, SMTP_CONFIG)
```
