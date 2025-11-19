"""
Generated Code Metadata:
========================
Original URL: https://auqualhairservices.com
Prompt: Develop a script that automates the process of sending follow-up emails to clients who have undergone hair transplant procedures at AuQual Hair Services.
Generated: DETERMINISTIC_75d22547a161cd7d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3
from datetime import datetime, timedelta

# Database configuration
DATABASE = 'clients.db'

# Email configuration
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'

def get_clients_due_for_followup():
    """
    Fetch clients who underwent hair transplant procedures
    and are due for a follow-up email.
    
    Returns:
        list of tuples: Each tuple contains client information.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # Calculate the date for follow-up (30 days after the procedure)
        followup_date = datetime.now() - timedelta(days=30)
        
        # Query to select clients due for follow-up
        query = """
        SELECT name, email FROM clients
        WHERE procedure_date <= ? AND followup_sent = 0
        """
        cursor.execute(query, (followup_date,))
        clients = cursor.fetchall()
        
        return clients
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        if conn:
            conn.close()

def send_email(to_email, client_name):
    """
    Send a follow-up email to the specified client.
    
    Args:
        to_email (str): The recipient's email address.
        client_name (str): The name of the client.
    """
    subject = "Follow-Up on Your Hair Transplant Procedure"
    body = f"Dear {client_name},\n\nWe hope you are doing well! This is a friendly follow-up regarding your recent hair transplant procedure at AuQual Hair Services. If you have any questions or need assistance, please feel free to reach out.\n\nBest regards,\nAuQual Hair Services"

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print(f"Email sent to {client_name} at {to_email}")
    except Exception as e:
        print(f"Failed to send email to {client_name}: {e}")

def update_followup_status(client_email):
    """
    Update the follow-up status of the client in the database.
    
    Args:
        client_email (str): The email of the client to update.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # Update the follow-up status to indicate the email has been sent
        cursor.execute("UPDATE clients SET followup_sent = 1 WHERE email = ?", (client_email,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error while updating follow-up status: {e}")
    finally:
        if conn:
            conn.close()

def main():
    """
    Main function to automate the follow-up email process.
    """
    clients = get_clients_due_for_followup()
    
    for client in clients:
        client_name, client_email = client
        send_email(client_email, client_name)
        update_followup_status(client_email)

if __name__ == "__main__":
    main()
```
