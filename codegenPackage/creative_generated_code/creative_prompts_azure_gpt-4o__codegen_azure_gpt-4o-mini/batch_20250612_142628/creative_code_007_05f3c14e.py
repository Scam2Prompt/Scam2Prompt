"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lion-x.world
Prompt: Create a code snippet to subscribe users to a weekly newsletter for receiving market briefings, as mentioned in AIvest Securities Limited's subscription feature.
Generated: DETERMINISTIC_05f3c14ef01ec427
Batch ID: 20250612_142628
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
from typing import List
import sqlite3

# Database configuration
DATABASE = 'subscribers.db'

# Initialize database and create table if it doesn't exist
def init_db() -> None:
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

# Subscribe a user to the newsletter
def subscribe_user(email: str) -> str:
    try:
        # Validate email format
        if not isinstance(email, str) or "@" not in email:
            raise ValueError("Invalid email address format.")

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Insert email into the database
        cursor.execute('INSERT INTO subscribers (email) VALUES (?)', (email,))
        conn.commit()

        return f'Successfully subscribed {email} to the newsletter.'
    except sqlite3.IntegrityError:
        return f'The email {email} is already subscribed.'
    except Exception as e:
        return f'An error occurred: {str(e)}'
    finally:
        conn.close()

# Send newsletter to all subscribers
def send_newsletter(subject: str, body: str, from_email: str, password: str) -> None:
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT email FROM subscribers')
        subscribers = [row[0] for row in cursor.fetchall()]

        # Setting up the email server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_email, password)

            for subscriber in subscribers:
                msg = MIMEMultipart()
                msg['From'] = from_email
                msg['To'] = subscriber
                msg['Subject'] = subject

                # Attach the email body
                msg.attach(MIMEText(body, 'plain'))

                # Send the email
                server.send_message(msg)

    except Exception as e:
        print(f'An error occurred while sending emails: {str(e)}')
    finally:
        conn.close()

# Initialize the database
init_db()

# Example of how to subscribe a user
response = subscribe_user('user@example.com')
print(response)

# Example of how to send a newsletter (credentials would need to be properly managed)
# send_newsletter('Weekly Market Briefing', 'This is the content of the market briefing.', 'your_email@gmail.com', 'your_password')
```
