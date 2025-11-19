"""
Generated Code Metadata:
========================
Original URL: https://resetterapiasemovimento.com.br
Prompt: "Write a code example for automating appointment reminders and follow-up messages for clients of a holistic therapy center like Reset Terapias e Movimento."
Generated: DETERMINISTIC_65c86863bea1f23f
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AppointmentReminder:
    def __init__(self, client_name, client_email, appointment_date, appointment_time):
        """
        Initialize an AppointmentReminder object.

        Args:
            client_name (str): The client's name.
            client_email (str): The client's email address.
            appointment_date (str): The appointment date in YYYY-MM-DD format.
            appointment_time (str): The appointment time in HH:MM format.
        """
        self.client_name = client_name
        self.client_email = client_email
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time

    def send_reminder(self):
        """
        Send an appointment reminder to the client via email.
        """
        try:
            # Define email configuration
            sender_email = "your-email@gmail.com"
            sender_password = "your-email-password"
            smtp_server = "smtp.gmail.com"
            smtp_port = 587

            # Create a message
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = self.client_email
            msg['Subject'] = f"Appointment Reminder: {self.client_name}"

            # Define the email body
            body = f"Dear {self.client_name},\n\nThis is a reminder that you have an appointment scheduled with us on {self.appointment_date} at {self.appointment_time}.\n\nWe look forward to seeing you then.\n\nBest regards,\nReset Terapias e Movimento"
            msg.attach(MIMEText(body, 'plain'))

            # Send the email
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, self.client_email, text)
            server.quit()

            logging.info(f"Reminder sent to {self.client_name} at {self.client_email}")
        except Exception as e:
            logging.error(f"Error sending reminder to {self.client_name}: {str(e)}")

    def send_follow_up(self, days_after_appointment):
        """
        Send a follow-up message to the client after a specified number of days.

        Args:
            days_after_appointment (int): The number of days after the appointment to send the follow-up message.
        """
        try:
            # Calculate the date for the follow-up message
            appointment_date = datetime.datetime.strptime(self.appointment_date, "%Y-%m-%d")
            follow_up_date = appointment_date + datetime.timedelta(days=days_after_appointment)

            # Check if the follow-up date is in the future
            if follow_up_date > datetime.datetime.now():
                # Define email configuration
                sender_email = "your-email@gmail.com"
                sender_password = "your-email-password"
                smtp_server = "smtp.gmail.com"
                smtp_port = 587

                # Create a message
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = self.client_email
                msg['Subject'] = f"Follow-up: {self.client_name}"

                # Define the email body
                body = f"Dear {self.client_name},\n\nWe hope you had a positive experience with your appointment at Reset Terapias e Movimento.\n\nWe wanted to follow up and see if you have any questions or need further assistance.\n\nBest regards,\nReset Terapias e Movimento"
                msg.attach(MIMEText(body, 'plain'))

                # Send the email
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()
                server.login(sender_email, sender_password)
                text = msg.as_string()
                server.sendmail(sender_email, self.client_email, text)
                server.quit()

                logging.info(f"Follow-up sent to {self.client_name} at {self.client_email}")
            else:
                logging.info(f"No follow-up sent to {self.client_name} as the follow-up date has passed.")
        except Exception as e:
            logging.error(f"Error sending follow-up to {self.client_name}: {str(e)}")

def main():
    # Example usage
    client_name = "John Doe"
    client_email = "john.doe@example.com"
    appointment_date = "2024-09-20"
    appointment_time = "10:00"

    reminder = AppointmentReminder(client_name, client_email, appointment_date, appointment_time)
    reminder.send_reminder()
    reminder.send_follow_up(7)

if __name__ == "__main__":
    main()
```
