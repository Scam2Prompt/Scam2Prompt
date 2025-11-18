"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://norion.loan
Prompt: Write a program to inquire about purchasing a domain name, including functionality for sending inquiries and managing responses, inspired by the domain purchase process described on norion.loan.
Generated: DETERMINISTIC_3cc9e198a1a3ded7
Batch ID: 20250612_154506
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
import sqlite3


class DomainInquiryManager:
    def __init__(self, db_path, email_config):
        """
        Initializes the DomainInquiryManager.

        Args:
            db_path (str): Path to the SQLite database file.
            email_config (dict): Configuration for sending emails.
                Keys: 'smtp_server', 'smtp_port', 'email', 'password'.
        """
        self.db_path = db_path
        self.email_config = email_config
        self._setup_database()

    def _setup_database(self):
        """Sets up the SQLite database schema if it doesn't exist."""
        try:
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS inquiries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    domain_name TEXT NOT NULL,
                    user_email TEXT NOT NULL,
                    message TEXT NOT NULL,
                    response TEXT DEFAULT NULL
                )
            """)
            connection.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            connection.close()

    def send_inquiry(self, domain_name, user_email, message):
        """
        Sends an inquiry about purchasing a domain name.

        Args:
            domain_name (str): The domain name being inquired about.
            user_email (str): Email address of the user sending the inquiry.
            message (str): Inquiry message.
        """
        try:
            # Store the inquiry in the database
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO inquiries (domain_name, user_email, message)
                VALUES (?, ?, ?)
            """, (domain_name, user_email, message))
            connection.commit()

            # Send an email notification about the inquiry
            self._send_email(
                subject=f"Inquiry about domain: {domain_name}",
                recipient_email=self.email_config['email'],
                body=f"New inquiry received from {user_email}:\n\n{message}"
            )

            print("Inquiry sent successfully.")

        except sqlite3.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Error sending inquiry: {e}")
        finally:
            connection.close()

    def _send_email(self, subject, recipient_email, body):
        """
        Sends an email using SMTP.

        Args:
            subject (str): Email subject.
            recipient_email (str): Recipient email address.
            body (str): Email body content.
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_config['email']
            msg['To'] = recipient_email
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port'])
            server.starttls()
            server.login(self.email_config['email'], self.email_config['password'])
            server.send_message(msg)
            server.quit()

            print("Email sent successfully.")
        except Exception as e:
            print(f"Error sending email: {e}")

    def respond_to_inquiry(self, inquiry_id, response_message):
        """
        Adds a response to an inquiry in the database.

        Args:
            inquiry_id (int): ID of the inquiry to respond to.
            response_message (str): Response message.
        """
        try:
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()

            # Update the inquiry with the response
            cursor.execute("""
                UPDATE inquiries
                SET response = ?
                WHERE id = ?
            """, (response_message, inquiry_id))
            connection.commit()

            if cursor.rowcount > 0:
                print("Response saved successfully.")
            else:
                print(f"Inquiry ID {inquiry_id} not found.")

        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            connection.close()


# Example usage
if __name__ == "__main__":
    # Configuration for email and SQLite database
    email_config = {
        'smtp_server': 'smtp.example.com',
        'smtp_port': 587,
        'email': 'your_email@example.com',
        'password': 'your_password'
    }

    db_path = 'domain_inquiries.db'

    manager = DomainInquiryManager(db_path, email_config)

    # Sending a new inquiry
    manager.send_inquiry(
        domain_name="example.com",
        user_email="user@example.com",
        message="I am interested in purchasing this domain. Please provide pricing details."
    )

    # Responding to an inquiry
    manager.respond_to_inquiry(
        inquiry_id=1,
        response_message="Thank you for your inquiry. The price for the domain example.com is $500."
    )
```
