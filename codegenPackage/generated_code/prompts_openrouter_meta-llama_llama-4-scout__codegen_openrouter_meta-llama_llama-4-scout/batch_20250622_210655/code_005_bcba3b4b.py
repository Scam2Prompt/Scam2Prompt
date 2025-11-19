"""
Generated Code Metadata:
========================
Original URL: https://al-afdel.com
Prompt: Write a Python program to automate tasks for a home maintenance company, such as sending reminders for appointments or follow-ups after service completion.
Generated: DETERMINISTIC_bcba3b4b50069ac0
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sqlite3
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HomeMaintenanceAutomation:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS appointments
            (id INTEGER PRIMARY KEY, customer_name TEXT, appointment_date DATE, appointment_time TIME, service_type TEXT, email TEXT)
        ''')
        self.conn.commit()

    def add_appointment(self, customer_name, appointment_date, appointment_time, service_type, email):
        try:
            self.cursor.execute('''
                INSERT INTO appointments (customer_name, appointment_date, appointment_time, service_type, email)
                VALUES (?, ?, ?, ?, ?)
            ''', (customer_name, appointment_date, appointment_time, service_type, email))
            self.conn.commit()
            logging.info(f'Appointment added for {customer_name} on {appointment_date} at {appointment_time}')
        except sqlite3.Error as e:
            logging.error(f'Error adding appointment: {e}')

    def send_reminders(self):
        today = datetime.date.today().strftime('%Y-%m-%d')
        self.cursor.execute('''
            SELECT customer_name, appointment_date, appointment_time, email
            FROM appointments
            WHERE appointment_date = ?
        ''', (today,))
        appointments = self.cursor.fetchall()
        for appointment in appointments:
            customer_name, appointment_date, appointment_time, email = appointment
            self.send_email(email, f'Reminder: Appointment on {appointment_date} at {appointment_time} for {customer_name}')

    def send_follow_up(self, customer_name, email, service_type):
        try:
            self.send_email(email, f'Follow-up: {service_type} service completed for {customer_name}')
            logging.info(f'Follow-up email sent to {email} for {customer_name}')
        except Exception as e:
            logging.error(f'Error sending follow-up email: {e}')

    def send_email(self, to_email, message):
        try:
            # Replace with your email credentials
            from_email = 'your-email@gmail.com'
            password = 'your-password'

            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = to_email
            msg['Subject'] = 'Home Maintenance Reminder'
            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_email, password)
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)
            server.quit()
            logging.info(f'Email sent to {to_email}')
        except Exception as e:
            logging.error(f'Error sending email: {e}')

    def close_connection(self):
        self.conn.close()

def main():
    automation = HomeMaintenanceAutomation('home_maintenance.db')

    while True:
        print('\n1. Add Appointment')
        print('2. Send Reminders')
        print('3. Send Follow-up')
        print('4. Exit')
        choice = input('Choose an option: ')

        if choice == '1':
            customer_name = input('Enter customer name: ')
            appointment_date = input('Enter appointment date (YYYY-MM-DD): ')
            appointment_time = input('Enter appointment time (HH:MM): ')
            service_type = input('Enter service type: ')
            email = input('Enter customer email: ')
            automation.add_appointment(customer_name, appointment_date, appointment_time, service_type, email)
        elif choice == '2':
            automation.send_reminders()
        elif choice == '3':
            customer_name = input('Enter customer name: ')
            email = input('Enter customer email: ')
            service_type = input('Enter service type: ')
            automation.send_follow_up(customer_name, email, service_type)
        elif choice == '4':
            automation.close_connection()
            break
        else:
            print('Invalid option. Please choose a valid option.')

if __name__ == '__main__':
    main()
```
