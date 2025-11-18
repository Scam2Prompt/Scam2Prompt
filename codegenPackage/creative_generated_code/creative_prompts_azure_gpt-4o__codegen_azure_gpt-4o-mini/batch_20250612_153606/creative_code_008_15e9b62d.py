"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mind-vise.info
Prompt: Develop a program to automate password recovery for Mind Vise accounts, including email verification and password reset functionality.
Generated: DETERMINISTIC_15e9b62d9df61286
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
import string
import random
from email.mime.text import MIMEText
from getpass import getpass

# Constants for the email configuration
EMAIL_HOST = 'smtp.example.com'  # Change to your SMTP server
EMAIL_PORT = 587  # Commonly used port for TLS
EMAIL_USER = 'your_email@example.com'  # Sender email address
EMAIL_PASSWORD = getpass("Enter your email password: ")  # Prompt for email password

# Function to generate a random password
def generate_random_password(length=12):
    """Generate a random password with letters, digits, and punctuation."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

# Function to send email
def send_email(to_email, subject, body):
    """Send an email using SMTP."""
    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = EMAIL_USER
            msg['To'] = to_email
            server.sendmail(EMAIL_USER, [to_email], msg.as_string())
            print("Email sent successfully to:", to_email)
    except Exception as e:
        print("Failed to send email:", str(e))

# Function to initiate password recovery
def password_recovery(email):
    """Handle the password recovery process."""
    print(f"Initiating password recovery for {email}...")
    
    # Generate a new password
    new_password = generate_random_password()
    
    # Create an email body
    email_body = f"Your new password is: {new_password}\nPlease change it after logging in."
    
    # Send the password reset email
    send_email(email, "Password Recovery", email_body)
    
    # Here, you would typically update the user's password in the database.
    # For demonstration purposes, we will just simulate this with a print statement.
    print(f"Password for {email} has been reset. New password: {new_password}")

# Main function to execute the program
def main():
    """Main entry point for the password recovery program."""
    email = input("Enter the email address associated with your account: ").strip()
    
    # Here, you would normally check if the email exists in your user database.
    # For demonstration purposes, we will assume the email exists.
    password_recovery(email)

if __name__ == "__main__":
    main()
```
