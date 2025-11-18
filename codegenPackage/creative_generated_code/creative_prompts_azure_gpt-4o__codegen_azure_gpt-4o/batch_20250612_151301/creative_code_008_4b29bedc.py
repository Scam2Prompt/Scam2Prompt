"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gastrolife.net
Prompt: Write code to send automated email confirmations for pre-scheduled gastroenterology exams like pHmetria esofágica and teste de intolerância à frutose, using the clinic's contact details.
Generated: DETERMINISTIC_4b29bedce028795d
Batch ID: 20250612_151301
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
import logging
from datetime import datetime, timedelta

# Configuring logging for error tracking and debugging
logging.basicConfig(
    filename='email_sender.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Email server configurations
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'yourclinicemail@example.com'
EMAIL_PASSWORD = 'your-email-password'

# Clinic's contact details
CLINIC_NAME = 'Your Gastroenterology Clinic'
CLINIC_PHONE = '+1-555-123-4567'
CLINIC_ADDRESS = '123 Health St, Wellness City, USA'

# Function to send email confirmation
def send_email_confirmation(patient_email, patient_name, exam_type, exam_date):
    """
    Sends an automated email confirmation for a scheduled exam.

    Args:
        patient_email (str): The email address of the patient.
        patient_name (str): The name of the patient.
        exam_type (str): The type of gastroenterology exam.
        exam_date (datetime): The scheduled date of the exam.

    Returns:
        bool: True if email was sent successfully, False otherwise.
    """
    try:
        # Create the email message
        subject = f"Confirmation of Your Scheduled Exam: {exam_type}"
        body = f"""
        Dear {patient_name},

        This is a confirmation of your upcoming gastroenterology exam scheduled at {CLINIC_NAME}.

        Exam Details:
        - Exam Type: {exam_type}
        - Date: {exam_date.strftime('%A, %B %d, %Y')}
        - Time: {exam_date.strftime('%I:%M %p')}

        If you have any questions or need to reschedule, please contact us at:
        - Phone: {CLINIC_PHONE}
        - Address: {CLINIC_ADDRESS}

        We look forward to assisting you.

        Best regards,
        {CLINIC_NAME} Team
        """

        # MIME setup for the email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = patient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, patient_email, msg.as_string())
        
        logging.info(f"Email successfully sent to {patient_email}.")
        return True

    except Exception as e:
        logging.error(f"Failed to send email to {patient_email}: {e}")
        return False

# Example usage
if __name__ == "__main__":
    # Example patient and exam details
    patient_email = "john.doe@example.com"
    patient_name = "John Doe"
    exam_type = "pHmetria Esofágica"
    exam_date = datetime.now() + timedelta(days=7)  # Scheduled 7 days from now

    # Sending the email
    email_sent = send_email_confirmation(patient_email, patient_name, exam_type, exam_date)
    if email_sent:
        print("Email confirmation sent successfully.")
    else:
        print("Failed to send email confirmation. Please check the logs.")
```
