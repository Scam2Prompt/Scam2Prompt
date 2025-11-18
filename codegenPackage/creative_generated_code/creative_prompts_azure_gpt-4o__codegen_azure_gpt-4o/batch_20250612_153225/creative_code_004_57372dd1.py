"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolcrespo.com.br
Prompt: Develop a Python script to automate the delivery of personalized workout plans via an exclusive app, ensuring the plans are generated within 4 days after a physical evaluation.
Generated: DETERMINISTIC_57372dd1add4798b
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Database simulation
# Normally, this would be replaced by a real database connection
physical_evaluations = [
    {"user_id": 1, "name": "John Doe", "email": "john@example.com", "evaluation_date": "2023-10-01"},
    {"user_id": 2, "name": "Jane Smith", "email": "jane@example.com", "evaluation_date": "2023-10-02"},
]

# Function to generate a personalized workout plan
def generate_workout_plan(user_name):
    """
    Creates a personalized workout plan.
    
    Args:
        user_name (str): Name of the user for personalization.
    
    Returns:
        str: A sample workout plan in text format.
    """
    return f"Hi {user_name},\n\nHere is your personalized workout plan:\n\nDay 1: Cardio & Abs\nDay 2: Strength Training\nDay 3: Rest\nDay 4: Yoga\n\nStay consistent and motivated!\n\nBest regards,\nYour Fitness Team"

# Function to send email with the workout plan
def send_email(to_email, subject, body):
    """
    Sends an email using SMTP.
    
    Args:
        to_email (str): Recipient's email address.
        subject (str): Subject of the email.
        body (str): Body content of the email.
    
    Raises:
        Exception: If email sending fails.
    """
    try:
        # Email configuration
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "your_email@gmail.com"
        sender_password = "your_email_password"

        # Creating the email
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Sending the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())

        print(f"Email sent successfully to {to_email}")

    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {e}")

# Function to automate workout plan delivery
def automate_workout_delivery(evaluations):
    """
    Automates the delivery of workout plans based on evaluation dates.
    
    Args:
        evaluations (list): List of evaluations containing user details and evaluation dates.
    """
    today = datetime.date.today()

    for evaluation in evaluations:
        user_name = evaluation["name"]
        user_email = evaluation["email"]
        evaluation_date = datetime.datetime.strptime(evaluation["evaluation_date"], "%Y-%m-%d").date()
        
        # Check if the workout plan needs to be delivered (4 days after evaluation)
        if (today - evaluation_date).days >= 4:
            workout_plan = generate_workout_plan(user_name)
            subject = "Your Personalized Workout Plan"
            send_email(user_email, subject, workout_plan)

# Main execution
if __name__ == "__main__":
    """
    Entry point for the script. Ensures workout plans are delivered correctly.
    """
    automate_workout_delivery(physical_evaluations)
```
