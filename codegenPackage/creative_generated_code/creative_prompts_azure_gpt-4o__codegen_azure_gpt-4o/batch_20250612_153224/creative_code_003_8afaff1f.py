"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.slv-valbonne.fr
Prompt: Write a script to automate newsletter distribution for an organization like Sophia Loisirs & Vie, incorporating email templates and a database of subscribers.
Generated: DETERMINISTIC_8afaff1f81155289
Batch ID: 20250612_153224
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database configuration
DB_FILE = 'subscribers.db'

# Email server configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for TLS
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with sender email address
EMAIL_PASSWORD = 'your_password'  # Replace with sender email password

# Email template
EMAIL_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Newsletter</title>
</head>
<body>
    <h1>Welcome to Sophia Loisirs & Vie!</h1>
    <p>Dear {{name}},</p>
    <p>Thank you for subscribing to our newsletter. Here are the latest updates:</p>
    <ul>
        <li>Update 1: Lorem ipsum dolor sit amet.</li>
        <li>Update 2: Consectetur adipiscing elit.</li>
        <li>Update 3: Sed do eiusmod tempor incididunt.</li>
    </ul>
    <p>Best regards,</p>
    <p><strong>Sophia Loisirs & Vie Team</strong></p>
</body>
</html>
"""

def connect_to_database(db_file):
    """Establish a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(db_file)
        logging.info("Connected to the database successfully.")
        return conn
    except sqlite3.Error as e:
        logging.error(f"Error connecting to database: {e}")
        raise

def fetch_subscribers(conn):
    """Fetch subscriber data from the database."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name, email FROM subscribers WHERE subscribed = 1")
        subscribers = cursor.fetchall()
        logging.info(f"Fetched {len(subscribers)} subscribers from the database.")
        return subscribers
    except sqlite3.Error as e:
        logging.error(f"Error fetching subscribers: {e}")
        raise

def send_email(to_email, subject, body):
    """Send an email using the SMTP server."""
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'html'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
            logging.info(f"Email sent successfully to {to_email}.")
    except smtplib.SMTPException as e:
        logging.error(f"Error sending email to {to_email}: {e}")
        raise

def personalize_template(template, name):
    """Personalize the email template with the subscriber's name."""
    return template.replace("{{name}}", name)

def main():
    """Main function to execute the newsletter distribution script."""
    try:
        # Connect to the database
        conn = connect_to_database(DB_FILE)

        # Fetch subscribers
        subscribers = fetch_subscribers(conn)

        # Loop through subscribers and send emails
        for name, email in subscribers:
            personalized_email = personalize_template(EMAIL_TEMPLATE, name)
            send_email(email, "Sophia Loisirs & Vie Newsletter", personalized_email)

        logging.info("Newsletter distribution completed successfully.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        # Close the database connection
        if 'conn' in locals() and conn:
            conn.close()
            logging.info("Database connection closed.")

if __name__ == "__main__":
    main()
```
