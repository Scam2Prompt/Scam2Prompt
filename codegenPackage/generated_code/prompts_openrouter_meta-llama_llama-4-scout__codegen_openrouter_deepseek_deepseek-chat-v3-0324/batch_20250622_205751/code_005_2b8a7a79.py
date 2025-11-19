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
from typing import List, Optional

class Course:
    def __init__(self, name: str, max_capacity: int):
        """
        Initialize a Course instance.
        
        Args:
            name: Name of the course
            max_capacity: Maximum number of participants allowed
        """
        self.name = name
        self.max_capacity = max_capacity
        self.registered_participants = 0

    def register_participant(self) -> bool:
        """
        Register a participant if spots are available.
        
        Returns:
            bool: True if registration was successful, False otherwise
        """
        if self.registered_participants < self.max_capacity:
            self.registered_participants += 1
            return True
        return False

    def get_available_spots(self) -> int:
        """
        Calculate the number of available spots.
        
        Returns:
            int: Number of available spots
        """
        return self.max_capacity - self.registered_participants

class NotificationService:
    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        """
        Initialize NotificationService with email credentials.
        
        Args:
            smtp_server: SMTP server address
            smtp_port: SMTP server port
            sender_email: Email address to send from
            sender_password: Email account password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_notification(self, recipient_email: str, subject: str, message: str) -> bool:
        """
        Send an email notification.
        
        Args:
            recipient_email: Email address to send to
            subject: Email subject
            message: Email body content
            
        Returns:
            bool: True if email was sent successfully, False otherwise
        """
        try:
            msg = MIMEText(message)
            msg['Subject'] = subject
            msg['From'] = self.sender_email
            msg['To'] = recipient_email

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            return True
        except Exception as e:
            print(f"Error sending notification: {e}")
            return False

class CourseManager:
    def __init__(self, course: Course, notification_service: NotificationService, admin_emails: List[str]):
        """
        Initialize CourseManager with course, notification service, and admin emails.
        
        Args:
            course: Course instance to manage
            notification_service: NotificationService instance
            admin_emails: List of admin email addresses to notify
        """
        self.course = course
        self.notification_service = notification_service
        self.admin_emails = admin_emails
        self._notified_full = False

    def register_participant(self) -> bool:
        """
        Register a participant and notify admins if course becomes full.
        
        Returns:
            bool: True if registration was successful, False otherwise
        """
        success = self.course.register_participant()
        if success and self.course.get_available_spots() == 0 and not self._notified_full:
            self._notify_course_full()
            self._notified_full = True
        return success

    def get_available_spots(self) -> int:
        """
        Get the number of available spots in the course.
        
        Returns:
            int: Number of available spots
        """
        return self.course.get_available_spots()

    def _notify_course_full(self) -> None:
        """
        Notify all admin emails that the course is fully booked.
        """
        subject = f"Course '{self.course.name}' Fully Booked"
        message = f"The course '{self.course.name}' has reached its maximum capacity of {self.course.max_capacity} participants."
        
        for email in self.admin_emails:
            self.notification_service.send_notification(
                recipient_email=email,
                subject=subject,
                message=message
            )
```
