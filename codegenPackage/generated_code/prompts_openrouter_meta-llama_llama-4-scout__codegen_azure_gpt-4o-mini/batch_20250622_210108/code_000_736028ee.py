"""
Generated Code Metadata:
========================
Original URL: https://waltztechsec.com
Prompt: Write a Python script for secure email recovery using two-factor authentication and encryption, as described by WaltzTech Security's email recovery services.
Generated: DETERMINISTIC_736028ee8b2afa82
Batch ID: 20250622_210108
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
import os
import random
import string
import hashlib
import base64
from cryptography.fernet import Fernet
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass

# Generate a secure random key for encryption
def generate_key():
    return Fernet.generate_key()

# Encrypt the recovery code using Fernet symmetric encryption
def encrypt_code(code, key):
    fernet = Fernet(key)
    encrypted_code = fernet.encrypt(code.encode())
    return encrypted_code

# Decrypt the recovery code
def decrypt_code(encrypted_code, key):
    fernet = Fernet(key)
    decrypted_code = fernet.decrypt(encrypted_code).decode()
    return decrypted_code

# Send an email with the recovery code
def send_email(to_email, recovery_code):
    from_email = os.getenv('EMAIL_USER')
    password = os.getenv('EMAIL_PASS')

    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = 'Your Email Recovery Code'

    body = f'Your recovery code is: {recovery_code}'
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)
            print("Recovery code sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

# Generate a random recovery code
def generate_recovery_code(length=6):
    characters = string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Main function for email recovery
def email_recovery():
    print("Welcome to the Email Recovery Service")
    
    # Get user email
    user_email = input("Enter your email address: ")

    # Generate and encrypt recovery code
    recovery_code = generate_recovery_code()
    key = generate_key()
    encrypted_code = encrypt_code(recovery_code, key)

    # Send the recovery code to the user's email
    send_email(user_email, recovery_code)

    # Prompt user for the recovery code
    user_input_code = input("Enter the recovery code sent to your email: ")

    # Check if the entered code matches the original
    if user_input_code == recovery_code:
        print("Recovery successful! You can now reset your password.")
        # Here you would typically allow the user to reset their password
    else:
        print("Invalid recovery code. Please try again.")

if __name__ == "__main__":
    email_recovery()
```

**Note:** Ensure to set the environment variables `EMAIL_USER` and `EMAIL_PASS` with your email credentials before running the script. This script uses Gmail's SMTP server; adjust the SMTP settings as necessary for other email providers.
