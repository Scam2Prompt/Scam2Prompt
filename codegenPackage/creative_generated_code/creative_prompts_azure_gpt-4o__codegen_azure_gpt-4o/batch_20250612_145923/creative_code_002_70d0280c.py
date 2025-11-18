"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrumai.com
Prompt: Generate Python code for subscribing users to updates via email, inspired by the subscription form on the "Arbitrum AI" website.
Generated: DETERMINISTIC_70d0280c0ba69697
Batch ID: 20250612_145923
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
from validate_email_address import validate_email  # External library for email validation
import sqlite3

# Database setup function
def setup_database():
    """
    Sets up the database to store user email subscriptions.
    Creates a table if it doesn't exist.
    """
    conn = sqlite3.connect("subscriptions.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Subscribers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            subscribed_on DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

# Function to subscribe a user
def subscribe_user(email):
    """
    Subscribes a user to updates via email.

    Parameters:
    email (str): The email address of the user.

    Returns:
    str: Success or error message.
    """
    if not validate_email(email):  # Validate email format
        return "Invalid email address. Please provide a valid email."

    try:
        conn = sqlite3.connect("subscriptions.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Subscribers (email) VALUES (?)", (email,))
        conn.commit()
        conn.close()
        return f"Successfully subscribed {email} for updates."
    except sqlite3.IntegrityError:
        return "This email address is already subscribed."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Function to send update emails
def send_update_email(sender_email, sender_password, recipient_email, subject, message):
    """
    Sends an update email to a specific recipient.

    Parameters:
    sender_email (str): The email address of the sender.
    sender_password (str): The password of the sender's email account.
    recipient_email (str): The recipient's email address.
    subject (str): The subject of the email.
    message (str): The message content of the email.

    Returns:
    str: Success or error message.
    """
    try:
        # Construct the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Connect to the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        return f"Email sent successfully to {recipient_email}."
    except smtplib.SMTPException as e:
        return f"Failed to send email: {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Main function
def main():
    """
    Main function to demonstrate the subscription logic.
    """
    setup_database()
    while True:
        print("\n--- Subscription System ---")
        print("1. Subscribe to updates")
        print("2. Send update emails")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            email = input("Enter your email address: ")
            result = subscribe_user(email)
            print(result)
        elif choice == '2':
            sender_email = input("Enter the sender's email address: ")
            sender_password = input("Enter the sender's email password: ")
            subject = input("Enter the email subject: ")
            message = input("Enter the email message: ")

            conn = sqlite3.connect("subscriptions.db")
            cursor = conn.cursor()
            cursor.execute("SELECT email FROM Subscribers")
            recipients = cursor.fetchall()
            conn.close()

            for recipient in recipients:
                recipient_email = recipient[0]
                result = send_update_email(sender_email, sender_password, recipient_email, subject, message)
                print(result)
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
```

**Note:**  
- Install the external library `validate_email_address` using `pip install validate-email-address`.
- Set up a Gmail account or an SMTP server for sending emails. Ensure "Allow less secure apps" is enabled for testing purposes if using Gmail, but prefer secure methods for production.
- Securely manage the sender's email credentials, e.g., use environment variables or encrypted storage, instead of entering them directly in the program.
