"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://farazhaidermusic.com
Prompt: Develop a function that sends an email update about Faraz Haider's new album releases to a list of subscribers using a mailing library.
Generated: DETERMINISTIC_18eaf1dd3df179d6
Batch ID: 20250612_162050
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

def send_album_update(subscribers, sender_email, sender_password, smtp_server, smtp_port, album_name, release_date, artist_name):
    """
    Sends an email update about a new album release to a list of subscribers.

    Parameters:
        subscribers (list): List of email addresses to send the update.
        sender_email (str): Sender's email address.
        sender_password (str): Sender's email account password.
        smtp_server (str): SMTP server address.
        smtp_port (int): SMTP server port.
        album_name (str): Name of the new album.
        release_date (str): Release date of the album.
        artist_name (str): Name of the artist (e.g., 'Faraz Haider').

    Returns:
        None
    """
    try:
        # Create the email subject and message body
        subject = f"Exciting News! {artist_name}'s New Album: {album_name} Released!"
        body = f"""
        Hello,

        We’re thrilled to announce that {artist_name} has released a new album titled "{album_name}" on {release_date}!

        Be sure to check it out and spread the word among fellow music lovers.

        Best regards,
        Music Updates Team
        """
        
        # Loop through subscribers and send emails
        for subscriber in subscribers:
            # Create a MIME message
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = subscriber
            msg['Subject'] = subject

            # Attach the email body to the message
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure encrypted SSL/TLS
                server.login(sender_email, sender_password)  # Log in to the SMTP server
                server.sendmail(sender_email, subscriber, msg.as_string())  # Send the email

        print("Emails have been sent successfully!")
    
    except smtplib.SMTPException as e:
        print(f"Error occurred while sending emails: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    subscribers_list = ["subscriber1@example.com", "subscriber2@example.com"]
    sender_email_address = "your_email@example.com"
    sender_email_password = "your_password"
    smtp_server_address = "smtp.example.com"
    smtp_port_number = 587
    album_title = "Echoes of Harmony"
    release_date_info = "2023-10-15"
    artist_name_info = "Faraz Haider"

    send_album_update(
        subscribers=subscribers_list,
        sender_email=sender_email_address,
        sender_password=sender_email_password,
        smtp_server=smtp_server_address,
        smtp_port=smtp_port_number,
        album_name=album_title,
        release_date=release_date_info,
        artist_name=artist_name_info
    )
```
