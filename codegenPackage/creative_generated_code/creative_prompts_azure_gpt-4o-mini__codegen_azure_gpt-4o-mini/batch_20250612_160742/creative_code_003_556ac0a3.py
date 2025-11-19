"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rayatrecruitment.com
Prompt: Develop a code snippet that sends an email confirmation after a successful application fee payment for Rayat Shikshan Sanstha.
Generated: DETERMINISTIC_556ac0a31d73a222
Batch ID: 20250612_160742
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
from typing import Optional

# Function to send email confirmation
def send_email_confirmation(to_email: str, student_name: str, payment_amount: float, payment_date: str, smtp_server: str, smtp_port: int, smtp_user: str, smtp_password: str) -> Optional[str]:
    """
    Sends a confirmation email after a successful application fee payment.

    Args:
        to_email (str): Recipient's email address.
        student_name (str): Name of the student.
        payment_amount (float): The amount paid for application fee.
        payment_date (str): The date when the payment was made.
        smtp_server (str): SMTP server address.
        smtp_port (int): SMTP server port.
        smtp_user (str): SMTP server username.
        smtp_password (str): SMTP server password.

    Returns:
        Optional[str]: Success message or error message.
    """
    # Create the email content
    subject = "Payment Confirmation - Rayat Shikshan Sanstha"
    body = f"""
    Dear {student_name},

    Thank you for your payment of ₹{payment_amount} for the application fee.
    Your payment was successfully received on {payment_date}.

    Best regards,
    Rayat Shikshan Sanstha
    """

    # Create a multipart email message
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body to the message
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server connection
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(smtp_user, smtp_password)  # Log in to the SMTP server
            server.send_message(msg)  # Send the email

        return "Email confirmation sent successfully."
    except smtplib.SMTPException as e:
        # Log the error or handle it according to your application's logging framework
        return f"Error sending email: {str(e)}"
    except Exception as e:
        # General exception handling for unforeseen errors
        return f"An unexpected error occurred: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Define SMTP server details (replace with real values)
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    SMTP_USER = "your_email@example.com"
    SMTP_PASSWORD = "your_email_password"

    # Define payment details (replace with real values)
    recipient_email = "student@example.com"
    student_name = "John Doe"
    payment_amount = 1000.00
    payment_date = "2023-10-01"

    # Send confirmation email
    result = send_email_confirmation(recipient_email, student_name, payment_amount, payment_date, SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD)
    print(result)
```
