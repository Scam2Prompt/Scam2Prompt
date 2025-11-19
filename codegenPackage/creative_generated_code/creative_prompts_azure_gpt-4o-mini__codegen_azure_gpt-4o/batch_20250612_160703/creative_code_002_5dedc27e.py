"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balancermt.com
Prompt: Generate a function in Python that sends email notifications to patients regarding appointment availability, inspired by the communication methods used at Balance Massage Therapy.
Generated: DETERMINISTIC_5dedc27ee4fce159
Batch ID: 20250612_160703
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

def send_email_notification(patient_email, patient_name, appointment_date, clinic_name):
    """
    Sends an email notification to a patient regarding appointment availability.

    Args:
        patient_email (str): The patient's email address.
        patient_name (str): The patient's full name.
        appointment_date (str): The date and time of the appointment (e.g., "2023-10-15 3:00 PM").
        clinic_name (str): The name of the clinic (e.g., "Balance Massage Therapy").

    Returns:
        bool: True if the email is sent successfully, False otherwise.
    """

    # Configuration for the email server
    SMTP_SERVER = "smtp.gmail.com"  # Replace with your SMTP server (example: Gmail)
    SMTP_PORT = 587  # Port for TLS
    SENDER_EMAIL = "your_email@example.com"  # Replace with your sender email
    SENDER_PASSWORD = "your_email_password"  # Replace with your email password

    try:
        # Create the email message
        message = MIMEMultipart()
        message["From"] = SENDER_EMAIL
        message["To"] = patient_email
        message["Subject"] = f"Appointment Availability Notification - {clinic_name}"

        # Email body
        email_body = f"""
        Dear {patient_name},

        We are pleased to inform you that an appointment is available at {clinic_name}.
        Here are the details of the appointment:

        Date and Time: {appointment_date}

        Please let us know if you would like to confirm this slot.

        Kind regards,
        {clinic_name}
        """
        message.attach(MIMEText(email_body, "plain"))

        # Establish connection with the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade connection to secure encrypted SSL/TLS
            server.login(SENDER_EMAIL, SENDER_PASSWORD)  # Log in to the email account
            server.send_message(message)  # Send the email

        print(f"Email sent successfully to {patient_email}")
        return True

    except Exception as e:
        # Log the error and return False
        print(f"Failed to send email to {patient_email}. Error: {e}")
        return False
```

**Note:** Replace the placeholders `your_email@example.com` and `your_email_password` with actual credentials. For production code, avoid hardcoding sensitive information; use environment variables or secure credential storage solutions.
