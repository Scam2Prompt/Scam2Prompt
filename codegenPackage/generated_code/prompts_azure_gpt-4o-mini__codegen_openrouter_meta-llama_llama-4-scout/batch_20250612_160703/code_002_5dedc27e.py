"""
Generated Code Metadata:
========================
Original URL: https://balancermt.com
Prompt: Generate a function in Python that sends email notifications to patients regarding appointment availability, inspired by the communication methods used at Balance Massage Therapy.
Generated: DETERMINISTIC_5dedc27ee4fce159
Batch ID: 20250612_160703
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

def send_appointment_notification(patient_email, patient_name, appointment_details):
    """
    Sends an email notification to a patient regarding appointment availability.

    Args:
        patient_email (str): The patient's email address.
        patient_name (str): The patient's name.
        appointment_details (str): The appointment details.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """

    # Define email configuration
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_PORT = 587
    FROM_EMAIL = "your-email@gmail.com"
    PASSWORD = "your-password"

    try:
        # Create a message
        msg = MIMEMultipart()
        msg['From'] = FROM_EMAIL
        msg['To'] = patient_email
        msg['Subject'] = "Appointment Availability at Balance Massage Therapy"

        # Create the email body
        body = f"""
        Dear {patient_name},

        We are pleased to inform you that an appointment is available at Balance Massage Therapy.
        The appointment details are as follows:
        {appointment_details}

        Please let us know if you would like to schedule this appointment.

        Best regards,
        Balance Massage Therapy
        """

        # Attach the email body to the message
        msg.attach(MIMEText(body, 'plain'))

        # Set up the SMTP server
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(FROM_EMAIL, PASSWORD)

        # Send the email
        text = msg.as_string()
        server.sendmail(FROM_EMAIL, patient_email, text)
        server.quit()

        return True

    except smtplib.SMTPAuthenticationError:
        print("Error: Authentication failed. Please check your email and password.")
        return False

    except smtplib.SMTPException as e:
        print(f"Error: {e}")
        return False

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


# Example usage:
if __name__ == "__main__":
    patient_email = "patient@example.com"
    patient_name = "John Doe"
    appointment_details = "Date: 2024-09-17, Time: 10:00 AM"

    if send_appointment_notification(patient_email, patient_name, appointment_details):
        print("Email sent successfully.")
    else:
        print("Failed to send email.")
```
