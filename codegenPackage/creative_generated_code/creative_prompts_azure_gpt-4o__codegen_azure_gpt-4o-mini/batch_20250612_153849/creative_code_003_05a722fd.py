"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://privnote.co
Prompt: Provide an example of how to integrate email notifications into a self-destructing note system, notifying the sender when the note is destroyed, as outlined on privnote.co.
Generated: DETERMINISTIC_05a722fd2dd6fc6c
Batch ID: 20250612_153849
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
import time
import threading

class SelfDestructingNote:
    def __init__(self, content, recipient_email, destruction_time):
        """
        Initializes a self-destructing note.

        :param content: The content of the note.
        :param recipient_email: Email address of the recipient.
        :param destruction_time: Time in seconds after which the note will self-destruct.
        """
        self.content = content
        self.recipient_email = recipient_email
        self.destruction_time = destruction_time
        self.is_destroyed = False

    def send_notification(self):
        """
        Sends an email notification to the recipient once the note is destroyed.
        """
        try:
            # Email configuration
            sender_email = "youremail@example.com"  # Replace with your email
            sender_password = "yourpassword"          # Replace with your email password
            subject = "Your Secure Note has been Destroyed"
            body = "Your note has been destroyed after the set time."
            
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = self.recipient_email
            msg['Subject'] = subject
            
            # Attach the body with the msg instance
            msg.attach(MIMEText(body, 'plain'))
            
            # Setup the server
            with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with your SMTP server
                server.starttls()  # Secure the connection
                server.login(sender_email, sender_password)
                server.send_message(msg)
        
        except Exception as e:
            print(f"Error sending email: {e}")

    def destroy_note(self):
        """
        Waits for the specified time and then destroys the note.
        """
        time.sleep(self.destruction_time)
        self.is_destroyed = True
        print("Note destroyed.")
        self.send_notification()

    def start(self):
        """
        Starts the self-destruct timer in a separate thread.
        """
        threading.Thread(target=self.destroy_note).start()


# Example usage:
if __name__ == "__main__":
    note_content = "This is a self-destructing note."
    recipient_email = "recipient@example.com"  # Replace with recipient email
    destruction_time = 10  # Self-destruct in 10 seconds

    note = SelfDestructingNote(note_content, recipient_email, destruction_time)
    note.start()

    # Main application can continue running while the note self-destructs
    print("Note is created and will self-destruct in 10 seconds.")
```
