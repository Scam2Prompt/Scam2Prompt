"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: Write a script to automate sending email reminders for polygraph test appointments, using the contact details format provided on the Euro Poligraf Center website.
Generated: DETERMINISTIC_d75822c9808c7f27
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import json

def load_config(file_path):
    """
    Loads configuration from a JSON file.

    Args:
        file_path (str): Path to the configuration file.

    Returns:
        dict: Configuration data.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Configuration file '{file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse configuration file - {e}")
        return None

def send_email_reminder(config, appointment):
    """
    Sends an email reminder for a polygraph test appointment.

    Args:
        config (dict): Configuration data.
        appointment (dict): Appointment details.
    """
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Set up the SMTP server
    with smtplib.SMTP_SSL(config['smtp_server'], config['smtp_port'], context=context) as server:
        server.login(config['smtp_username'], config['smtp_password'])

        # Create the email message
        message = MIMEMultipart()
        message['From'] = config['smtp_username']
        message['To'] = appointment['email']
        message['Subject'] = f"Reminder: Polygraph Test Appointment on {appointment['date']}"

        # Email body
        body = f"""
        Dear {appointment['name']},

        This is a reminder that you have a polygraph test appointment scheduled on {appointment['date']} at {appointment['time']}.

        Please arrive 15 minutes prior to your appointment time.

        If you need to reschedule or have any questions, please contact us at {config['smtp_username']}.

        Best regards,
        Euro Poligraf Center
        """
        message.attach(MIMEText(body, 'plain'))

        try:
            # Send the email
            server.sendmail(config['smtp_username'], appointment['email'], message.as_string())
            print(f"Email reminder sent to {appointment['email']}")
        except smtplib.SMTPException as e:
            print(f"Error: Failed to send email to {appointment['email']} - {e}")

def main():
    # Load configuration
    config = load_config('config.json')
    if config is None:
        return

    # Example appointment data
    appointments = [
        {
            'name': 'John Doe',
            'email': 'john@example.com',
            'date': '2024-09-20',
            'time': '10:00 AM'
        },
        {
            'name': 'Jane Doe',
            'email': 'jane@example.com',
            'date': '2024-09-21',
            'time': '2:00 PM'
        }
    ]

    # Send email reminders
    for appointment in appointments:
        send_email_reminder(config, appointment)

if __name__ == '__main__':
    main()
```

**config.json example:**
```json
{
    "smtp_server": "smtp.example.com",
    "smtp_port": 465,
    "smtp_username": "your_email@example.com",
    "smtp_password": "your_email_password"
}
```
