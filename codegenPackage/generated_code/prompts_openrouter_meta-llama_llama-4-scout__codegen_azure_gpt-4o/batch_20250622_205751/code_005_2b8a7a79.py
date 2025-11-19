"""
Generated Code Metadata:
========================
Original URL: https://patenteimpresa.it
Prompt: Write a function to calculate the number of available spots for a free business training course and send notifications when the course is fully booked.
Generated: DETERMINISTIC_2b8a7a796c41431c
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class BusinessTrainingCourse:
    def __init__(self, max_spots):
        """
        Initialize the course with a maximum number of spots and an empty list of registered participants.
        :param max_spots: Maximum number of spots available for the course.
        """
        self.max_spots = max_spots
        self.registered_participants = []

    def register_participant(self, participant_email):
        """
        Register a participant for the course.
        :param participant_email: Email address of the participant.
        :return: A message indicating the registration status.
        """
        try:
            if len(self.registered_participants) < self.max_spots:
                self.registered_participants.append(participant_email)
                return f"Registration successful for {participant_email}."
            else:
                self.send_full_course_notification()
                return "Registration failed: The course is fully booked."
        except Exception as e:
            return f"An error occurred during registration: {str(e)}"

    def available_spots(self):
        """
        Calculate the number of available spots for the course.
        :return: Number of available spots.
        """
        return self.max_spots - len(self.registered_participants)

    def send_full_course_notification(self):
        """
        Send a notification email when the course is fully booked.
        """
        try:
            sender_email = "your_email@example.com"
            sender_password = "your_email_password"
            recipient_email = "admin@example.com"

            # Create the email content
            subject = "Business Training Course Fully Booked"
            body = "The business training course is now fully booked. No more registrations can be accepted."

            # Create the email message
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = recipient_email
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP("smtp.example.com", 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, recipient_email, message.as_string())
        except Exception as e:
            print(f"Failed to send notification email: {str(e)}")

# Example usage
if __name__ == "__main__":
    course = BusinessTrainingCourse(max_spots=5)

    print(course.register_participant("participant1@example.com"))
    print(course.register_participant("participant2@example.com"))
    print(course.register_participant("participant3@example.com"))
    print(course.register_participant("participant4@example.com"))
    print(course.register_participant("participant5@example.com"))
    print(course.register_participant("participant6@example.com"))  # Should trigger the notification
    print(f"Available spots: {course.available_spots()}")
```

**Note:** Replace `your_email@example.com`, `your_email_password`, and `smtp.example.com` with actual credentials and SMTP server details. Ensure sensitive information like email credentials is stored securely in production environments (e.g., using environment variables or a secrets manager).
