"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://salonlapista.com.ar
Prompt: Write a Python script that sends an email confirmation to clients after they reserve a party at Salon La Pista, using the provided email address format.
Generated: DETERMINISTIC_24d2217704019cb5
Batch ID: 20250612_162051
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

def send_email_confirmation(client_email, client_name, party_date, party_time):
    """
    Sends an email confirmation to the client after they reserve a party.
    
    Args:
        client_email (str): The email address of the client.
        client_name (str): The name of the client.
        party_date (str): The reserved party date in format 'YYYY-MM-DD'.
        party_time (str): The reserved party time in format 'HH:MM AM/PM'.
    
    Returns:
        None
    """
    # Email Configuration
    sender_email = "your_salon_email@example.com"
    sender_password = "your_secure_password"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the email content
    subject = "Salon La Pista - Party Reservation Confirmation"
    body = f"""
    Dear {client_name},

    Thank you for reserving your party at Salon La Pista!

    Here are your reservation details:
    - Party Date: {party_date}
    - Party Time: {party_time}

    We look forward to hosting your event. If you have any questions, feel free to contact us.

    Best regards,
    Salon La Pista Team
    """

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = client_email
    message["Subject"] = subject

    # Attach the email body
    message.attach(MIMEText(body, "plain"))

    try:
        # Establish connection to the email server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Enable TLS encryption
        server.login(sender_email, sender_password)  # Log in to the email server

        # Send the email
        server.sendmail(sender_email, client_email, message.as_string())
        print(f"Confirmation email successfully sent to {client_email}.")

    except smtplib.SMTPException as e:
        # Handle any errors that occur during email sending
        print(f"Failed to send email: {e}")

    finally:
        # Ensure the server connection is closed
        server.quit()


# Example usage
if __name__ == "__main__":
    # Replace with actual client details for testing
    client_email = "client_email@example.com"
    client_name = "John Doe"
    party_date = "2023-10-15"
    party_time = "6:00 PM"

    send_email_confirmation(client_email, client_name, party_date, party_time)
```

Note: Replace `your_salon_email@example.com` and `your_secure_password` with the actual email address and password associated with your salon's email account. Ensure your email provider allows SMTP access and configure "Less Secure App Access" or use app-specific passwords if necessary for security.
