"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://japkasai.net
Prompt: Write a function that sends a confirmation email to clients after they book a massage or grooming service at a salon, ensuring it includes details about the treatment and the therapist's qualifications.
Generated: DETERMINISTIC_cc3de1ddcf4235f3
Batch ID: 20250612_164151
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

def send_confirmation_email(client_email, client_name, service_details, therapist_name, therapist_qualification):
    """
    Sends a confirmation email to the client after booking a service.
    
    Args:
        client_email (str): The email address of the client.
        client_name (str): The name of the client.
        service_details (str): Details of the booked service (e.g., massage or grooming).
        therapist_name (str): Name of the assigned therapist.
        therapist_qualification (str): Qualifications of the therapist.
    
    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """
    # Email server settings
    smtp_server = "smtp.example.com"  # Replace with your SMTP server
    smtp_port = 587  # Typical port for SMTP (TLS)
    sender_email = "your_email@example.com"  # Replace with your email address
    sender_password = "your_password"  # Replace with your email password (use environment variables in production)

    try:
        # Create the email content
        subject = "Confirmation of Your Booking"
        body = f"""
        Dear {client_name},

        Thank you for booking a {service_details} at our salon. 

        Your service is scheduled with:
        - Therapist Name: {therapist_name}
        - Qualifications: {therapist_qualification}

        We look forward to providing you with the best care and experience.

        Please let us know if you have any questions or need to reschedule.

        Best regards,
        Salon Team
        """

        # Construct the email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = client_email
        message["Subject"] = subject

        # Attach the email body
        message.attach(MIMEText(body, "plain"))

        # Connect to the email server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Start TLS encryption
            server.login(sender_email, sender_password)  # Login to the email server
            server.sendmail(sender_email, client_email, message.as_string())  # Send the email

        return True  # Email sent successfully

    except Exception as e:
        # Log the error (replace print with proper logging in production)
        print(f"Error sending email: {e}")
        return False  # Email sending failed
```

This code is designed to be production-ready with a focus on simplicity, proper error handling, and maintainability.
