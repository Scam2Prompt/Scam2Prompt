"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mfxhk.com
Prompt: Develop a Python program that integrates two-factor authentication (2FA) for user login, inspired by MFX-Online Trade's default security measures.
Generated: DETERMINISTIC_3323ebaf9a7c1d83
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import smtplib
import sys
from email.mime.text import MIMEText

# User database (For demonstration purposes, normally you'd use a secure database)
USER_DB = {
    "test_user": {
        "password": "secure_password123",
        "email": "test_user@example.com"
    }
}

# Function to send 2FA code via email
def send_2fa_code(email, code):
    try:
        # Email server configuration (Replace with actual credentials in production)
        smtp_server = "smtp.example.com"  # Replace with your SMTP server
        smtp_port = 587  # Replace with your SMTP port
        smtp_user = "your_email@example.com"  # Replace with your email
        smtp_password = "your_password"  # Replace with your email password
        
        msg = MIMEText(f"Your 2FA code is: {code}")
        msg["Subject"] = "Your 2FA Code"
        msg["From"] = smtp_user
        msg["To"] = email
        
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, email, msg.as_string())
        print("2FA code sent successfully.")
    except Exception as e:
        print(f"Failed to send 2FA code: {e}")
        sys.exit(1)

# Function to generate a random 2FA code
def generate_2fa_code():
    return random.randint(100000, 999999)  # Six-digit code

# Main login function with 2FA
def login():
    print("Welcome to MFX-Online Trade!")
    
    # Prompt user for credentials
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    
    # Validate username and password
    user = USER_DB.get(username)
    if not user or user["password"] != password:
        print("Invalid username or password.")
        return
    
    # Generate and send 2FA code
    email = user["email"]
    two_factor_code = generate_2fa_code()
    send_2fa_code(email, two_factor_code)
    
    # Prompt user for the 2FA code
    print("A 2FA code has been sent to your registered email.")
    entered_code = input("Enter the 2FA code: ").strip()
    
    # Validate 2FA code
    if str(entered_code) == str(two_factor_code):
        print("Login successful!")
    else:
        print("Invalid 2FA code.")
        return

# Entry point of the program
if __name__ == "__main__":
    try:
        login()
    except KeyboardInterrupt:
        print("\nProgram interrupted by the user.")
```
