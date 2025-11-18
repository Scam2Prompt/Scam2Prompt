"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatepeak.io
Prompt: Generate a script that connects users to investment education companies, as described on Immediate Peak, and sends automated email notifications upon successful registration.
Generated: DETERMINISTIC_2dd370f99e5c0f67
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.message import EmailMessage
import sqlite3

# Database configuration
DB_NAME = "users.db"

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"  # Replace with your email password

# Create or connect to the database
def initialize_database():
    """
    Initialize the database and create a table for storing user information
    if it doesn't exist.
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            company TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()

# Register a user
def register_user(name, email, company):
    """
    Register a user in the database.
    Args:
        name (str): Name of the user.
        email (str): Email address of the user.
        company (str): Investment education company they are connecting to.
    Returns:
        bool: True if registration was successful, False otherwise.
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        # Insert user data into the table
        cursor.execute("""
            INSERT INTO users (name, email, company)
            VALUES (?, ?, ?)
        """, (name, email, company))

        connection.commit()
        connection.close()
        send_email_notification(name, email, company)
        return True
    except sqlite3.IntegrityError:
        print(f"Error: Email {email} is already registered.")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

# Send email notification
def send_email_notification(name, email, company):
    """
    Send an automated email notification upon successful registration.
    Args:
        name (str): Name of the user.
        email (str): Email address of the user.
        company (str): Investment education company they are connected to.
    """
    try:
        # Compose email
        msg = EmailMessage()
        msg['Subject'] = "Registration Successful"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = email
        msg.set_content(f"Hello {name},\n\n"
                        f"You have successfully registered to connect with {company}.\n\n"
                        "Thank you for using our platform!\n\n"
                        "Best regards,\nImmediate Peak Team")

        # Connect to the email server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Encrypt the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Email sent successfully to {email}.")
    except Exception as e:
        print(f"Failed to send email to {email}: {e}")

# Main function
def main():
    """
    Main function to initialize the database and allow user registration.
    """
    initialize_database()
    print("Welcome to Immediate Peak!")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    company = input("Enter the investment education company you'd like to connect to: ")

    if register_user(name, email, company):
        print("Registration successful!")
    else:
        print("Registration failed. Please try again.")

if __name__ == "__main__":
    main()
```
