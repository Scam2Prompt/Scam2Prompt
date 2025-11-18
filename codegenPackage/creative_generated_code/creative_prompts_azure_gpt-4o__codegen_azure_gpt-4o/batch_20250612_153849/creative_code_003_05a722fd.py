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
import time
import smtplib
from email.message import EmailMessage

# ==============================
# Self-Destructing Note System
# ==============================

class SelfDestructingNote:
    def __init__(self, content, sender_email, receiver_email, destruction_time):
        """
        Initializes a self-destructing note with content, sender email,
        receiver email, and a time (in seconds) after which the note will be destroyed.
        """
        self.content = content
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.destruction_time = destruction_time
        self.is_destroyed = False

    def display_note(self):
        """
        Displays the note content to the receiver. If the note has been destroyed,
        raises an exception.
        """
        if self.is_destroyed:
            raise Exception("This note has already been destroyed.")
        return self.content

    def destroy_note(self):
        """
        Marks the note as destroyed and triggers the email notification to the sender.
        """
        self.is_destroyed = True
        self._send_notification()

    def _send_notification(self):
        """
        Sends an email notification to the sender indicating the note has been destroyed.
        """
        try:
            # Create the email message
            msg = EmailMessage()
            msg.set_content("Your self-destructing note has been successfully destroyed.")
            msg['Subject'] = "Notification: Note Destroyed"
            msg['From'] = 'no-reply@selfdestructingnotes.com'
            msg['To'] = self.sender_email

            # Send the email using SMTP
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                # Use environment variables or a secure vault for these credentials in production
                server.login('your_email@gmail.com', 'your_password')  
                server.send_message(msg)
            
            print("Notification email sent successfully.")
        except Exception as e:
            print(f"Failed to send notification email: {e}")

# ==============================
# Example Usage
# ==============================

if __name__ == "__main__":
    # Create a new self-destructing note
    note = SelfDestructingNote(
        content="This is a secret note.",
        sender_email="sender@example.com",
        receiver_email="receiver@example.com",
        destruction_time=10  # Note will self-destruct after 10 seconds
    )

    print("Note created. Content:")
    print(note.display_note())

    # Wait for the destruction time
    print(f"Note will be destroyed in {note.destruction_time} seconds...")
    time.sleep(note.destruction_time)

    # Destroy the note and send notification
    note.destroy_note()
    print("Note destroyed.")
```

Make sure to replace `your_email@gmail.com` and `your_password` with valid credentials or use a more secure authentication mechanism like OAuth for production environments.
