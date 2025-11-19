"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.socrates-gm.com
Prompt: Write a Python script that automates the process of resetting a user's password for an employee portal like Socrates GM, including email verification steps.
Generated: DETERMINISTIC_918394b3cd9363e2
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
import random
import string
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Constants for email configuration
SMTP_SERVER = 'smtp.example.com'  # Change to your SMTP server
SMTP_PORT = 587  # Change to your SMTP port
EMAIL_ADDRESS = 'admin@example.com'  # Your admin email for sending the reset email
EMAIL_PASSWORD = 'your_email_password'  # Your email password

def generate_temp_password(length=12):
    """Generates a random temporary password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    temp_password = ''.join(random.choice(characters) for i in range(length))
    return temp_password

def send_email(to_email, temp_password):
    """Sends an email with the temporary password to the user."""
    subject = "Password Reset Request"
    body = f"Your temporary password is: {temp_password}\nPlease change your password upon logging in."
    
    # Create email message
    message = MIMEMultipart()
    message['From'] = EMAIL_ADDRESS
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(message)
            print(f"Password reset email sent to {to_email}.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def reset_password(email):
    """Resets the user's password and sends a verification email."""
    # Simulate checking if the email exists in the database
    if email not in get_user_emails():
        print("Error: The provided email does not exist.")
        return

    # Generate a temporary password
    temp_password = generate_temp_password()

    # Send the email with the temporary password
    send_email(email, temp_password)

    # Here you'd normally update the user's password in the database
    # For demonstration, we'll just print the new password
    print(f"Temporary password for {email}: {temp_password} (Not stored in a database for security purposes)")

def get_user_emails():
    """Simulates a database of user emails."""
    return ['employee1@example.com', 'employee2@example.com', 'employee3@example.com']

if __name__ == "__main__":
    # Get the email address from the user
    user_email = input("Enter the email address to reset the password: ").strip()

    # Call the reset password function
    reset_password(user_email)
```

**Note:** Please remember to replace `SMTP_SERVER`, `SMTP_PORT`, `EMAIL_ADDRESS`, and `EMAIL_PASSWORD` with your actual email server configuration. Also, ensure that handling of passwords and sensitive information follows best security practices in a production environment.
