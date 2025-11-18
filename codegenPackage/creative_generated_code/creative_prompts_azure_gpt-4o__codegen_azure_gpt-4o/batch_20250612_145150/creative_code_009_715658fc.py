"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://changemypin.com.au
Prompt: Write a detailed explanation of how to implement OTP-based PIN change functionality in a mobile app, using the process described on the Heritage Bank "Change My PIN" page as a reference.
Generated: DETERMINISTIC_715658fc3bf1c2af
Batch ID: 20250612_145150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
import smtplib
from email.message import EmailMessage

# Define constants and configurations
OTP_LENGTH = 6
EMAIL_SERVER = "smtp.example.com"
EMAIL_PORT = 587
EMAIL_USERNAME = "your_email@example.com"
EMAIL_PASSWORD = "your_email_password"

# Mock database for storing user information
users_db = {
    "john_doe": {
        "email": "john_doe@example.com",
        "pin": "1234"
    }
}

# Function to generate a random OTP
def generate_otp(length=OTP_LENGTH):
    """Generates a random OTP of specified length."""
    return ''.join(random.choices(string.digits, k=length))

# Function to send OTP via email
def send_otp_email(email, otp):
    """
    Sends an OTP to the specified email address.
    :param email: Recipient email address
    :param otp: OTP to send
    """
    try:
        msg = EmailMessage()
        msg.set_content(f"Your OTP is: {otp}")
        msg["Subject"] = "Your OTP for PIN Change"
        msg["From"] = EMAIL_USERNAME
        msg["To"] = email

        with smtplib.SMTP(EMAIL_SERVER, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.send_message(msg)
        print("OTP sent successfully.")
    except Exception as e:
        print(f"Failed to send OTP: {e}")

# Function to validate OTP
def validate_otp(input_otp, correct_otp):
    """
    Validates the user-entered OTP against the correct OTP.
    :param input_otp: OTP entered by user
    :param correct_otp: Correct OTP
    :return: Boolean indicating whether the OTP is valid
    """
    return input_otp == correct_otp

# Function to change the PIN
def change_pin(username, new_pin):
    """
    Changes the PIN for a specified user.
    :param username: Username of the user
    :param new_pin: New PIN to be set
    """
    if username in users_db:
        users_db[username]["pin"] = new_pin
        print("PIN changed successfully.")
    else:
        print("User not found.")

# Main function to handle OTP-based PIN change process
def otp_pin_change_process(username):
    """
    Orchestrates the OTP-based PIN change workflow.
    :param username: Username of the user requesting PIN change
    """
    # Step 1: Verify if user exists
    user = users_db.get(username)
    if not user:
        print("Invalid username.")
        return

    # Step 2: Generate OTP and send it to user's email
    otp = generate_otp()
    send_otp_email(user["email"], otp)

    # Step 3: Prompt user for OTP input and validate
    input_otp = input("Enter the OTP sent to your email: ")
    if not validate_otp(input_otp, otp):
        print("Invalid OTP. PIN change aborted.")
        return

    # Step 4: Prompt user for new PIN and update it
    new_pin = input("Enter your new PIN: ")
    if len(new_pin) != 4 or not new_pin.isdigit():
        print("Invalid PIN format. PIN must be 4 digits.")
        return
    change_pin(username, new_pin)

# Example usage
if __name__ == "__main__":
    # Replace 'john_doe' with the actual username
    otp_pin_change_process("john_doe")
```
