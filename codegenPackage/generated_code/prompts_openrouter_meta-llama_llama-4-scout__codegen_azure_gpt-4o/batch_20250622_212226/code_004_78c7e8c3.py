"""
Generated Code Metadata:
========================
Original URL: https://starmissteenindia.com
Prompt: "Design an email template for sending confirmation messages to registrants for 'Star Miss Teen India 2025' upon payment, including details about auditions and guidance from past winners."
Generated: DETERMINISTIC_78c7e8c3d1b77f91
Batch ID: 20250622_212226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def send_confirmation_email(recipient_email, registrant_name, payment_amount, audition_date, audition_location, guidance_details):
    """
    Sends a confirmation email to registrants for 'Star Miss Teen India 2025' upon payment.

    Parameters:
        recipient_email (str): The email address of the registrant.
        registrant_name (str): The name of the registrant.
        payment_amount (float): The amount paid by the registrant.
        audition_date (str): The date of the audition.
        audition_location (str): The location of the audition.
        guidance_details (str): Information about guidance from past winners.

    Returns:
        None
    """
    try:
        # Email sender and SMTP server configuration
        sender_email = "your_email@example.com"  # Replace with your email
        sender_password = "your_password"        # Replace with your email password
        smtp_server = "smtp.example.com"         # Replace with your SMTP server
        smtp_port = 587                          # Common SMTP port for TLS

        # Create the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = "Payment Confirmation - Star Miss Teen India 2025"

        # Email body template
        email_body = f"""
        <html>
        <body>
            <h2>Payment Confirmation</h2>
            <p>Dear {registrant_name},</p>
            <p>Thank you for registering for <strong>Star Miss Teen India 2025</strong>! We have successfully received your payment of <strong>₹{payment_amount:.2f}</strong>.</p>
            
            <h3>Audition Details</h3>
            <p><strong>Date:</strong> {audition_date}</p>
            <p><strong>Location:</strong> {audition_location}</p>
            
            <h3>Guidance from Past Winners</h3>
            <p>{guidance_details}</p>
            
            <p>We look forward to seeing you shine at the auditions!</p>
            <p>Best regards,</p>
            <p><strong>Star Miss Teen India 2025 Team</strong></p>
        </body>
        </html>
        """

        # Attach the email body to the message
        message.attach(MIMEText(email_body, 'html'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Enable TLS encryption
            server.login(sender_email, sender_password)  # Log in to the SMTP server
            server.send_message(message)  # Send the email

        print(f"Confirmation email successfully sent to {recipient_email}.")

    except Exception as e:
        # Handle any errors that occur during the email sending process
        print(f"An error occurred while sending the email: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with actual values
    recipient_email = "registrant@example.com"
    registrant_name = "Jane Doe"
    payment_amount = 1500.00
    audition_date = "March 15, 2025"
    audition_location = "Mumbai, India"
    guidance_details = "You will receive exclusive tips and mentorship from past winners to help you prepare for the competition."

    send_confirmation_email(recipient_email, registrant_name, payment_amount, audition_date, audition_location, guidance_details)
```
