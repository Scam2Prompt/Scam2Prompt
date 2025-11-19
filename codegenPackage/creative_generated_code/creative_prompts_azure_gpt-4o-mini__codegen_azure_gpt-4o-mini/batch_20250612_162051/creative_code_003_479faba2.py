"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cefor.org.br
Prompt: Develop a function that sends notifications to users about upcoming events and volunteer opportunities at CEFOR, including details about the Casa Abrigo and Projeto Vida.
Generated: DETERMINISTIC_479faba29081e744
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
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_notification(recipients: List[str], subject: str, body: str) -> None:
    """
    Send an email notification to a list of recipients.

    Parameters:
    recipients (List[str]): List of email addresses to send the notification to.
    subject (str): The subject of the email.
    body (str): The body content of the email.
    
    Raises:
    ValueError: If the recipients list is empty.
    Exception: For other errors related to email sending.
    """
    
    if not recipients:
        logging.error("Recipients list is empty.")
        raise ValueError("Recipients list cannot be empty.")

    sender_email = "your_email@example.com"
    sender_password = "your_email_password"
    
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject
    
    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        # Set up the server
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Login to the email server
            server.sendmail(sender_email, recipients, msg.as_string())  # Send the email
            logging.info(f"Notification sent successfully to {', '.join(recipients)}.")
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")
        raise

def notify_users_about_events(users: List[Dict[str, str]], event_details: Dict[str, str]) -> None:
    """
    Notify users about upcoming events and volunteer opportunities.

    Parameters:
    users (List[Dict[str, str]]): List of user dictionaries containing 'name' and 'email'.
    event_details (Dict[str, str]): Dictionary containing event details including 'title', 'date', 'description'.

    Raises:
    Exception: If there is an error in preparing notifications.
    """
    
    try:
        for user in users:
            email = user.get('email')
            if email:
                subject = f"Upcoming Event: {event_details['title']}"
                body = (f"Hello {user['name']},\n\n"
                        f"We are excited to inform you about an upcoming event:\n"
                        f"Title: {event_details['title']}\n"
                        f"Date: {event_details['date']}\n"
                        f"Description: {event_details['description']}\n\n"
                        "We hope to see you there!\n\n"
                        "Best regards,\n"
                        "CEFOR Team")
                
                send_notification([email], subject, body)
            else:
                logging.warning(f"User {user['name']} does not have a valid email address.")
    except Exception as e:
        logging.error(f"An error occurred while notifying users: {e}")
        raise

# Example usage
if __name__ == "__main__":
    users_list = [
        {'name': 'Alice', 'email': 'alice@example.com'},
        {'name': 'Bob', 'email': 'bob@example.com'}
    ]
    
    event_info = {
        'title': 'Volunteer Day at Casa Abrigo',
        'date': '2023-11-15',
        'description': 'Join us for a day of volunteering at Casa Abrigo to support our community.'
    }
    
    notify_users_about_events(users_list, event_info)
```
