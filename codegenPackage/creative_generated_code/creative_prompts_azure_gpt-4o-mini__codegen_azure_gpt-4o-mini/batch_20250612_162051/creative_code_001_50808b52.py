"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isbgames.isbeventteam.com
Prompt: Write a promotional email highlighting the unique features of the ISB Games 2024, focusing on the introduction of Bowling and the spirit of sportsmanship among ISB-ers.
Generated: DETERMINISTIC_50808b52901b4863
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
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_promotional_email(recipient_email):
    """
    Sends a promotional email about ISB Games 2024.
    
    Args:
        recipient_email (str): The email address of the recipient.
        
    Raises:
        Exception: Raises an exception if the email could not be sent.
    """
    
    # Email configuration
    sender_email = "noreply@isbgames2024.com"
    sender_name = "ISB Games 2024"
    subject = "Join Us for the Exciting ISB Games 2024!"
    
    # Create the email body
    body = f"""
    Dear ISB Family,

    We are excited to announce the highly anticipated ISB Games 2024! This year's games will be truly special as we introduce the fun and thrilling sport of Bowling, adding a fresh twist to our traditional lineup of sports. 

    Bowling is not just about striking down pins; it embodies teamwork, strategy, and a spirit of friendly competition. We believe that this new addition will foster camaraderie and sportsmanship among all ISB-ers, uniting us in our shared love for sports and competition.

    Join us for a day filled with excitement, laughter, and unforgettable memories. Let's embrace the spirit of sportsmanship together—cheering for our colleagues, celebrating victories, and supporting each other regardless of the outcome.

    Mark your calendars, rally your teams, and gear up for an unforgettable experience at ISB Games 2024!

    Best Regards,
    The ISB Games 2024 Team
    """

    try:
        # Setting up the email server and sending the email
        server = smtplib.SMTP('smtp.example.com', 587)  # Use your SMTP server and port
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(sender_email, "your_password")  # Login to your email account
        
        # Construct the email
        msg = MIMEMultipart()
        msg['From'] = f"{sender_name} <{sender_email}>"
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        # Send the email
        server.send_message(msg)
        
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")
        raise Exception("Failed to send promotional email.") from e
    finally:
        # Clean up and close the server connection
        server.quit()

# Example usage (uncomment to use)
# send_promotional_email("recipient@example.com")
```
