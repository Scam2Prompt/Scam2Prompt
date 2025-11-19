"""
Generated Code Metadata:
========================
Original URL: https://alelbait.com
Prompt: Write a Python script to manage furniture moving tasks for a company like آل البيت, including scheduling and customer notifications.
Generated: DETERMINISTIC_bca409782d8b8b9d
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Constants for email configuration
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Replace with your SMTP port
EMAIL_USERNAME = "your_email@example.com"  # Replace with your email
EMAIL_PASSWORD = "your_password"  # Replace with your email password

# Furniture moving task class
class FurnitureMovingTask:
    def __init__(self, customer_name, customer_email, address, scheduled_date, description):
        """
        Initialize a furniture moving task.
        :param customer_name: Name of the customer
        :param customer_email: Email of the customer
        :param address: Address for the furniture moving task
        :param scheduled_date: Scheduled date for the task (datetime object)
        :param description: Description of the task
        """
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.address = address
        self.scheduled_date = scheduled_date
        self.description = description

    def __str__(self):
        """
        String representation of the task.
        """
        return f"Task for {self.customer_name} at {self.address} on {self.scheduled_date.strftime('%Y-%m-%d %H:%M')}"

# Task manager class
class TaskManager:
    def __init__(self):
        """
        Initialize the task manager with an empty list of tasks.
        """
        self.tasks = []

    def add_task(self, task):
        """
        Add a new task to the task manager.
        :param task: FurnitureMovingTask object
        """
        if not isinstance(task, FurnitureMovingTask):
            raise ValueError("Invalid task. Must be an instance of FurnitureMovingTask.")
        self.tasks.append(task)

    def list_tasks(self):
        """
        List all tasks in the task manager.
        """
        if not self.tasks:
            print("No tasks scheduled.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def send_notification(self, task):
        """
        Send a notification email to the customer about their scheduled task.
        :param task: FurnitureMovingTask object
        """
        try:
            # Create email message
            msg = MIMEMultipart()
            msg['From'] = EMAIL_USERNAME
            msg['To'] = task.customer_email
            msg['Subject'] = "Furniture Moving Task Scheduled"

            # Email body
            body = f"""
            Dear {task.customer_name},

            Your furniture moving task has been scheduled as follows:
            Address: {task.address}
            Date: {task.scheduled_date.strftime('%Y-%m-%d %H:%M')}
            Description: {task.description}

            Thank you for choosing آل البيت for your furniture moving needs.

            Best regards,
            آل البيت Team
            """
            msg.attach(MIMEText(body, 'plain'))

            # Connect to SMTP server and send email
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
                server.send_message(msg)
                print(f"Notification sent to {task.customer_email}")
        except Exception as e:
            print(f"Failed to send notification: {e}")

# Main function
def main():
    """
    Main function to manage furniture moving tasks.
    """
    task_manager = TaskManager()

    # Example: Adding a task
    try:
        task = FurnitureMovingTask(
            customer_name="John Doe",
            customer_email="john.doe@example.com",
            address="123 Main Street, Cityville",
            scheduled_date=datetime.datetime(2023, 11, 15, 10, 0),
            description="Move furniture from living room to storage."
        )
        task_manager.add_task(task)
        print("Task added successfully.")

        # List tasks
        print("\nScheduled Tasks:")
        task_manager.list_tasks()

        # Send notification
        task_manager.send_notification(task)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
