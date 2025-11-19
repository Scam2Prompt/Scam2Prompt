"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://a5a1874f.blocklist-3ci.pages.dev
Prompt: Explain how to set up a login code email system using Cloudflare Access for user sign-in.
Generated: DETERMINISTIC_8fad9c9cdd06a653
Batch ID: 20250612_163243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code that demonstrates how to integrate Cloudflare Access for user sign-in via login code email:

```python
import requests
import smtplib
from email.mime.text import MIMEText
from typing import Optional
import random
import string

# Function to generate a random login code
def generate_login_code(length: int = 6) -> str:
    """
    Generate a random alphanumeric login code.
    
    :param length: Length of the login code (default is 6 characters).
    :return: A randomly generated login code.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Function to send login code via email
def send_email(to_email: str, login_code: str, smtp_server: str, smtp_port: int, smtp_user: str, smtp_password: str) -> None:
    """
    Send login code to user's email using SMTP.
    
    :param to_email: Recipient's email address.
    :param login_code: The login code to send.
    :param smtp_server: SMTP server address.
    :param smtp_port: SMTP server port.
    :param smtp_user: SMTP username.
    :param smtp_password: SMTP password.
    :raises: Exception if email fails to send.
    """
    try:
        # Create the email message
        subject = "Your Login Code"
        body = f"Your login code is: {login_code}"
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = smtp_user
        msg['To'] = to_email

        # Connect to SMTP server and send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(smtp_user, smtp_password)  # Login to the SMTP server
            server.sendmail(smtp_user, to_email, msg.as_string())  # Send the email
    except Exception as e:
        raise Exception(f"Failed to send email: {e}")

# Function to validate login code
def validate_login_code(input_code: str, generated_code: str) -> bool:
    """
    Validate the user's input login code against the generated code.
    
    :param input_code: The login code input by the user.
    :param generated_code: The originally generated login code.
    :return: True if the codes match, False otherwise.
    """
    return input_code == generated_code

# Example usage
if __name__ == "__main__":
    # Configuration for email and Cloudflare Access
    smtp_config = {
        "smtp_server": "smtp.example.com",
        "smtp_port": 587,
        "smtp_user": "your_email@example.com",
        "smtp_password": "your_email_password"
    }
    
    user_email = input("Enter your email address: ")
    
    # Generate a login code
    login_code = generate_login_code()
    
    # Send the login code to the user's email
    try:
        send_email(
            to_email=user_email,
            login_code=login_code,
            smtp_server=smtp_config["smtp_server"],
            smtp_port=smtp_config["smtp_port"],
            smtp_user=smtp_config["smtp_user"],
            smtp_password=smtp_config["smtp_password"]
        )
        print("Login code sent successfully. Please check your email.")
    except Exception as e:
        print(f"Error sending email: {e}")
        exit(1)

    # Prompt user to input the login code
    user_input_code = input("Enter the login code sent to your email: ")

    # Validate the login code
    if validate_login_code(user_input_code, login_code):
        print("Login successful!")
    else:
        print("Invalid login code. Please try again.")
```

**Note**: This code doesn't interact directly with Cloudflare Access API but lays out a foundation for email-based login codes. Integration with Cloudflare Access would require API keys and specific setup, which should be done following their documentation. Ensure your SMTP credentials are securely stored and avoid hardcoding sensitive data. Use environment variables or a secure vault for production.
