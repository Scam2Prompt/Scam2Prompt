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

Here is the code in Python using the `smtplib` library to send an email confirmation:

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr


def send_email_confirmation(to_email, payment_details):
    """
    Sends an email confirmation after a successful application fee payment.

    Parameters:
        to_email (str): Recipient's email address.
        payment_details (dict): Payment details containing transaction ID, amount, and date.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """
    # Email server configuration
    SMTP_SERVER = "smtp.gmail.com"  # Replace with your SMTP server
    SMTP_PORT = 587  # Standard port for TLS
    SENDER_EMAIL = "your_email@gmail.com"  # Replace with your email address
    SENDER_NAME = "Rayat Shikshan Sanstha"
    SENDER_PASSWORD = "your_password"  # Replace with your email password (use app-specific password if required)

    try:
        # Create the email content
        subject = "Payment Confirmation - Rayat Shikshan Sanstha"
        body = f"""
        Dear User,

        Thank you for your payment to Rayat Shikshan Sanstha.
        Here are your payment details:

        Transaction ID: {payment_details.get('transaction_id')}
        Amount Paid: ₹{payment_details.get('amount')}
        Payment Date: {payment_details.get('date')}

        If you have any questions, feel free to contact us.

        Best regards,
        Rayat Shikshan Sanstha
        """

        # Create MIME message
        msg = MIMEMultipart()
        msg['From'] = formataddr((SENDER_NAME, SENDER_EMAIL))
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Establish a connection to the SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Start TLS encryption
        server.login(SENDER_EMAIL, SENDER_PASSWORD)  # Authenticate
        
        # Send the email
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        
        # Close the connection
        server.quit()
        
        print("Email sent successfully.")
        return True

    except Exception as e:
        # Log the error and return False
        print(f"Failed to send email: {e}")
        return False


# Example usage
if __name__ == "__main__":
    # Example payment details
    payment_info = {
        "transaction_id": "12345ABC",
        "amount": 500,
        "date": "2023-10-25"
    }

    # Replace with recipient's email
    recipient_email = "recipient_email@example.com"

    # Send the email confirmation
    success = send_email_confirmation(recipient_email, payment_info)
    if not success:
        print("There was an error sending the email confirmation.")
```

### Notes:
- Replace placeholders like `your_email@gmail.com` and `your_password` with your actual email credentials.
- Ensure that less secure app access is enabled for your email account or use App Passwords if required.
- Consider integrating a more secure library or API (e.g., SendGrid, AWS SES) for production environments.
