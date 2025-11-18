"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.solid.com.py
Prompt: Generate code for a notification system that updates clients about the progress of their translation requests, inspired by Solid SRL's focus on timely delivery.
Generated: DETERMINISTIC_603a958ed8e1137e
Batch ID: 20250612_153224
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
import time
from threading import Thread
from queue import Queue, Empty

# Define a class for Translation Requests
class TranslationRequest:
    def __init__(self, requester_email, translation_id):
        self.requester_email = requester_email
        self.translation_id = translation_id
        self.progress = 0

    def update_progress(self, progress):
        """Update the progress of the translation request."""
        self.progress = progress
        self.notify_user()

    def notify_user(self):
        """Send an email notification to the requester about the progress."""
        email_sender = "your-email@example.com"  # Replace with your sender email
        email_password = "your-password"  # Replace with your email password

        # Set up the email server
        try:
            msg = MIMEMultipart()
            msg['From'] = email_sender
            msg['To'] = self.requester_email
            msg['Subject'] = f'Translation Progress Update: {self.translation_id}'

            body = f'Your translation request {self.translation_id} is now at {self.progress}% progress.'
            msg.attach(MIMEText(body, 'plain'))

            # Sending the email
            with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with your SMTP server
                server.starttls()
                server.login(email_sender, email_password)
                server.send_message(msg)

            print(f'Notification sent to {self.requester_email} about translation {self.translation_id}.')
        except Exception as e:
            print(f'Failed to send email notification: {e}')

# Define a class for handling translation requests
class TranslationManager:
    def __init__(self):
        self.requests = []
        self.queue = Queue()

    def add_request(self, translation_request):
        """Add a new translation request to the manager."""
        self.requests.append(translation_request)
        self.queue.put(translation_request)

    def process_requests(self):
        """Process translation requests and update progress."""
        while not self.queue.empty():
            try:
                request = self.queue.get_nowait()
                # Simulate translation work being done
                for progress in range(0, 101, 20):  # Update progress in increments of 20%
                    time.sleep(1)  # Simulate time delay for translation work
                    request.update_progress(progress)
            except Empty:
                break

    def start_processing(self):
        """Start processing translation requests in a separate thread."""
        processing_thread = Thread(target=self.process_requests)
        processing_thread.start()
        return processing_thread

# Example Usage:
if __name__ == "__main__":
    manager = TranslationManager()
    # Add translation requests
    manager.add_request(TranslationRequest("client1@example.com", "TR12345"))
    manager.add_request(TranslationRequest("client2@example.com", "TR12346"))

    # Start processing requests
    processing_thread = manager.start_processing()
    processing_thread.join()  # Wait for the processing thread to complete
```

Make sure to replace placeholder values with actual email credentials and SMTP server details for the code to function properly.
