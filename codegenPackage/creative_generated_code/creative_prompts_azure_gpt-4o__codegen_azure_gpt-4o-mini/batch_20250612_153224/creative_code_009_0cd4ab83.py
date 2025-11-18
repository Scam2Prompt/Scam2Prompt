"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://byamed.net
Prompt: Write code to implement a virtual meeting scheduler for brainstorming sessions, inspired by ByAmed.net's "Grab Coffee" consultation process.
Generated: DETERMINISTIC_0cd4ab838cb34ba1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import pytz
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MeetingScheduler:
    def __init__(self, time_zone='UTC'):
        self.time_zone = pytz.timezone(time_zone)
        self.meetings = []

    def schedule_meeting(self, date_time, duration_hours=1):
        """
        Schedule a meeting by adding it to the meetings list.
        
        :param date_time: datetime object for when the meeting is scheduled.
        :param duration_hours: Duration of the meeting in hours (default is 1 hour).
        :raises ValueError: if the date_time is in the past or invalid.
        """
        if date_time < datetime.now(self.time_zone):
            raise ValueError("The scheduled time cannot be in the past.")
        
        end_time = date_time + timedelta(hours=duration_hours)
        meeting = {'start_time': date_time, 'end_time': end_time}
        self.meetings.append(meeting)

    def list_meetings(self):
        """
        List all scheduled meetings.
        """
        return self.meetings

    def send_invitation(self, email, meeting_details):
        """
        Send an email invitation for a meeting.
        
        :param email: Recipient's email address.
        :param meeting_details: Details of the meeting to include in the email.
        :raises Exception: if sending the email fails.
        """
        sender_email = "your_email@example.com"
        sender_password = "your_email_password"

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = "Meeting Invitation"
        
        body = f"You're invited to a meeting!\n\nDetails:\n{meeting_details}"
        msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP('smtp.example.com', 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, email, msg.as_string())
        except Exception as e:
            raise Exception(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    scheduler = MeetingScheduler(time_zone='America/New_York')
    
    # Schedule a meeting
    try:
        meeting_time = scheduler.time_zone.localize(datetime(2023, 10, 20, 15, 0))  # 3 PM on October 20, 2023
        scheduler.schedule_meeting(meeting_time)
        print("Meeting scheduled successfully!")
        
        # List all meetings
        print("Scheduled Meetings:", scheduler.list_meetings())
        
        # Send an invitation
        meeting_details = f"Start: {meeting_time}\nEnd: {meeting_time + timedelta(hours=1)}"
        scheduler.send_invitation("recipient@example.com", meeting_details)
        print("Invitation sent successfully!")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
