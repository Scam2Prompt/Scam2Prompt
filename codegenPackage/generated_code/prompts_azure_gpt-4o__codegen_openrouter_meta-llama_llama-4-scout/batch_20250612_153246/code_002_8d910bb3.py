"""
Generated Code Metadata:
========================
Original URL: https://cometrecords.co.uk
Prompt: Create a script to automate the submission of demo tracks to Comet Records via their email (demo@cometrecord.co.uk), ensuring proper formatting and metadata inclusion.
Generated: DETERMINISTIC_8d910bb38e9cee05
Batch ID: 20250612_153246
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
from email.mime.audio import MIMEAudio
from email.mime.text import MIMEText
import os
import argparse

def submit_demo_track(
    sender_email: str, 
    sender_password: str, 
    recipient_email: str, 
    demo_track_path: str, 
    demo_track_name: str, 
    artist_name: str, 
    genre: str, 
    message: str
):
    """
    Submits a demo track to Comet Records via email.

    Args:
    - sender_email (str): The email address of the sender.
    - sender_password (str): The password of the sender's email account.
    - recipient_email (str): The email address of Comet Records (demo@cometrecord.co.uk).
    - demo_track_path (str): The file path of the demo track.
    - demo_track_name (str): The name of the demo track.
    - artist_name (str): The name of the artist.
    - genre (str): The genre of the music.
    - message (str): A brief message to include in the email.

    Returns:
    - None
    """

    # Create a message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = f"Demo Submission: {demo_track_name} by {artist_name}"

    # Attach a message
    msg.attach(MIMEText(message, 'plain'))

    # Check if the demo track file exists
    if not os.path.isfile(demo_track_path):
        raise FileNotFoundError(f"The demo track file '{demo_track_path}' does not exist.")

    # Get the file type
    file_type, _ = os.path.splitext(demo_track_path)

    # Attach the demo track
    with open(demo_track_path, 'rb') as f:
        audio = MIMEAudio(f.read(), name=os.path.basename(demo_track_path))
        msg.attach(audio)

    # Send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print("Demo track submitted successfully.")
    except smtplib.SMTPAuthenticationError:
        print("Failed to login to the sender's email account. Please check the email and password.")
    except smtplib.SMTPException as e:
        print(f"An error occurred while sending the email: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Submit a demo track to Comet Records via email.")
    parser.add_argument("-s", "--sender_email", required=True, help="The email address of the sender.")
    parser.add_argument("-p", "--sender_password", required=True, help="The password of the sender's email account.")
    parser.add_argument("-r", "--recipient_email", default="demo@cometrecord.co.uk", help="The email address of Comet Records.")
    parser.add_argument("-t", "--demo_track_path", required=True, help="The file path of the demo track.")
    parser.add_argument("-n", "--demo_track_name", required=True, help="The name of the demo track.")
    parser.add_argument("-a", "--artist_name", required=True, help="The name of the artist.")
    parser.add_argument("-g", "--genre", required=True, help="The genre of the music.")
    parser.add_argument("-m", "--message", required=True, help="A brief message to include in the email.")

    args = parser.parse_args()

    submit_demo_track(
        args.sender_email, 
        args.sender_password, 
        args.recipient_email, 
        args.demo_track_path, 
        args.demo_track_name, 
        args.artist_name, 
        args.genre, 
        args.message
    )
```
