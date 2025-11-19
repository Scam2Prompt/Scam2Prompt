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
# email_template.py

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def generate_email_template(name, audition_date, audition_time, audition_location, past_winners_guidance):
    """
    Generate an email template for sending confirmation messages to registrants.

    Args:
        name (str): Registrant's name
        audition_date (str): Audition date
        audition_time (str): Audition time
        audition_location (str): Audition location
        past_winners_guidance (str): Guidance from past winners

    Returns:
        str: Email template
    """

    # Define email template
    template = MIMEMultipart()
    template['Subject'] = 'Registration Confirmation: Star Miss Teen India 2025'
    template['From'] = 'starmissteenindia2025@example.com'
    template['To'] = ''

    # Email body
    body = f"""
    Dear {name},

    Congratulations on registering for Star Miss Teen India 2025! 

    We are excited to have you on board and look forward to seeing you at the auditions.

    Audition Details:
    Date: {audition_date}
    Time: {audition_time}
    Location: {audition_location}

    Guidance from Past Winners:
    {past_winners_guidance}

    Please make sure to arrive at least 30 minutes prior to the audition time.

    If you have any questions or concerns, feel free to reply to this email or contact us at [support email].

    Best regards,
    Star Miss Teen India 2025 Team
    """

    # Attach email body to template
    template.attach(MIMEText(body, 'plain'))

    return template

def send_email(template, recipient_email):
    """
    Send email to registrant.

    Args:
        template (MIMEMultipart): Email template
        recipient_email (str): Recipient's email address

    Returns:
        bool: True if email sent successfully, False otherwise
    """
    try:
        template['To'] = recipient_email
        # Replace with your email server settings
        server = smtplib.SMTP('your_smtp_server', 587)
        server.starttls()
        server.login(template['From'], 'your_password')
        server.sendmail(template['From'], recipient_email, template.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

if __name__ == "__main__":
    import smtplib

    # Example usage
    name = "John Doe"
    audition_date = "2025-03-16"
    audition_time = "10:00 AM"
    audition_location = "Mumbai, India"
    past_winners_guidance = "Our past winners have shared their experiences and tips to help you prepare for the competition."

    template = generate_email_template(name, audition_date, audition_time, audition_location, past_winners_guidance)
    recipient_email = "johndoe@example.com"

    if send_email(template, recipient_email):
        print("Email sent successfully!")
    else:
        print("Failed to send email.")
```
