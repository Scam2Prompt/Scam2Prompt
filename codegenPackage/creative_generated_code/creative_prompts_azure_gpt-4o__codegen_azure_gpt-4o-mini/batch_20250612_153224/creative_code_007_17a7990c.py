"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Write code to implement a notification system that alerts healthcare professionals about new job openings matching their profile in real-time.
Generated: DETERMINISTIC_17a7990c4c2ce192
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
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict
import time
import sqlite3

class NotificationSystem:
    def __init__(self, db_path: str, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        """Initializes the NotificationSystem with database and email server information."""
        self.db_path = db_path
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
    
    def connect_db(self):
        """Connects to the SQLite database."""
        try:
            conn = sqlite3.connect(self.db_path)
            return conn
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            return None

    def fetch_matching_jobs(self, profile: Dict) -> List[Dict]:
        """
        Fetches new job openings from the database that match the provided profile.
        
        Args:
            profile (Dict): The healthcare professional's profile data.
        
        Returns:
            List[Dict]: A list of matching job openings.
        """
        conn = self.connect_db()
        if not conn:
            return []
        
        cursor = conn.cursor()
        query = """
        SELECT title, description, location FROM job_openings
        WHERE specialty = ? AND experience <= ? AND is_active = 1
        """
        cursor.execute(query, (profile['specialty'], profile['experience']))
        jobs = cursor.fetchall()
        conn.close()
        
        # Convert jobs to a list of dictionaries
        return [{'title': job[0], 'description': job[1], 'location': job[2]} for job in jobs]

    def send_email(self, recipient: str, job_list: List[Dict]):
        """
        Sends an email to the specified recipient containing the list of new job openings.
        
        Args:
            recipient (str): The email address of the healthcare professional.
            job_list (List[Dict]): The list of job openings to include in the email.
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient
            msg['Subject'] = "New Job Openings Matching Your Profile"
            
            body = "Here are the new job openings that match your profile:\n\n"
            for job in job_list:
                body += f"Title: {job['title']}\nDescription: {job['description']}\nLocation: {job['location']}\n\n"
                
            msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            
            print(f"Email sent to {recipient}")
        except Exception as e:
            print(f"Failed to send email to {recipient}. Error: {e}")

    def notify_professionals(self, profile: Dict, recipient: str):
        """
        Notifies a healthcare professional about new job openings.
        
        Args:
            profile (Dict): The healthcare professional's profile data.
            recipient (str): The email address of the healthcare professional.
        """
        job_list = self.fetch_matching_jobs(profile)
        if job_list:
            self.send_email(recipient, job_list)
        else:
            print("No matching job openings found.")

    def start_monitoring(self, profile: Dict, recipient: str, interval: int = 60):
        """
        Starts a loop that checks for new job openings at a specified interval.
        
        Args:
            profile (Dict): The healthcare professional's profile data.
            recipient (str): The email address of the healthcare professional.
            interval (int): Time in seconds between checks.
        """
        try:
            while True:
                self.notify_professionals(profile, recipient)
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Monitoring stopped.")

# Example usage:
if __name__ == "__main__":
    # Define profile and recipient
    healthcare_profile = {'specialty': 'Nurse', 'experience': 3}
    recipient_email = 'healthcare_professional@example.com'
    
    # Initialize the NotificationSystem
    notifier = NotificationSystem(
        db_path='job_openings.db',
        smtp_server='smtp.example.com',
        smtp_port=587,
        sender_email='your_email@example.com',
        sender_password='your_password'
    )
    
    # Start monitoring for new job openings
    notifier.start_monitoring(healthcare_profile, recipient_email, interval=300)  # Check every 5 minutes
```
