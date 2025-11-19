"""
Generated Code Metadata:
========================
Original URL: https://rapidresponder.net
Prompt: "Develop a client support ticketing system with transparency features, including email notifications and status updates for cases like phishing tactic recovery."
Generated: DETERMINISTIC_0e88d2dd5feae868
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ticketing_system.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sqlite3
from enum import Enum

# Define ticket status enum
class TicketStatus(Enum):
    NEW = 1
    IN_PROGRESS = 2
    RESOLVED = 3
    CLOSED = 4

# Define database connection class
class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tickets
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             subject TEXT, 
             description TEXT, 
             status INTEGER, 
             email TEXT)
        ''')
        self.conn.commit()

    def insert_ticket(self, subject, description, email):
        self.cursor.execute('''
            INSERT INTO tickets (subject, description, status, email) 
            VALUES (?, ?, ?, ?)
        ''', (subject, description, TicketStatus.NEW.value, email))
        self.conn.commit()
        return self.cursor.lastrowid

    def update_ticket(self, id, status):
        self.cursor.execute('''
            UPDATE tickets SET status = ? 
            WHERE id = ?
        ''', (status.value, id))
        self.conn.commit()

    def get_ticket(self, id):
        self.cursor.execute('''
            SELECT * FROM tickets 
            WHERE id = ?
        ''', (id,))
        return self.cursor.fetchone()

    def close_connection(self):
        self.conn.close()

# Define email notification class
class EmailNotifier:
    def __init__(self, smtp_server, from_email, password):
        self.smtp_server = smtp_server
        self.from_email = from_email
        self.password = password

    def send_email(self, to_email, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(self.smtp_server, 587)
        server.starttls()
        server.login(self.from_email, self.password)
        text = msg.as_string()
        server.sendmail(self.from_email, to_email, text)
        server.quit()

# Define ticket service class
class TicketService:
    def __init__(self, db, email_notifier):
        self.db = db
        self.email_notifier = email_notifier

    def create_ticket(self, subject, description, email):
        try:
            id = self.db.insert_ticket(subject, description, email)
            self.email_notifier.send_email(email, 'Ticket Created', f'Ticket {id} created successfully')
            return id
        except Exception as e:
            print(f'Error creating ticket: {e}')

    def update_ticket_status(self, id, status):
        try:
            ticket = self.db.get_ticket(id)
            if ticket:
                self.db.update_ticket(id, status)
                self.email_notifier.send_email(ticket[4], 'Ticket Status Update', f'Ticket {id} status updated to {status.name}')
            else:
                print(f'Ticket {id} not found')
        except Exception as e:
            print(f'Error updating ticket status: {e}')

# Main function
def main():
    db = Database('ticketing_system.db')
    email_notifier = EmailNotifier('smtp.gmail.com', 'your-email@gmail.com', 'your-password')
    ticket_service = TicketService(db, email_notifier)

    while True:
        print('1. Create Ticket')
        print('2. Update Ticket Status')
        print('3. Exit')
        choice = input('Choose an option: ')

        if choice == '1':
            subject = input('Enter ticket subject: ')
            description = input('Enter ticket description: ')
            email = input('Enter your email: ')
            id = ticket_service.create_ticket(subject, description, email)
            print(f'Ticket created with id: {id}')
        elif choice == '2':
            id = int(input('Enter ticket id: '))
            print('1. In Progress')
            print('2. Resolved')
            print('3. Closed')
            status_choice = input('Choose a status: ')
            if status_choice == '1':
                status = TicketStatus.IN_PROGRESS
            elif status_choice == '2':
                status = TicketStatus.RESOLVED
            elif status_choice == '3':
                status = TicketStatus.CLOSED
            else:
                print('Invalid status choice')
                continue
            ticket_service.update_ticket_status(id, status)
        elif choice == '3':
            break
        else:
            print('Invalid option')

    db.close_connection()

if __name__ == '__main__':
    main()
```
