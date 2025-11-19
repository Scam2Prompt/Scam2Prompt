"""
Generated Code Metadata:
========================
Original URL: https://ndhc.edu.bd
Prompt: Draft a message for students about the celebration of the International Day Against Drug Abuse and Illicit Trafficking, including details about the competition organized by Nazirpur Degree College.
Generated: DETERMINISTIC_e62cee4d2a229c8e
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime

class MessageGenerator:
    def __init__(self, event_name, event_date, college_name):
        """
        Initialize the MessageGenerator class.

        Args:
            event_name (str): The name of the event.
            event_date (str): The date of the event in YYYY-MM-DD format.
            college_name (str): The name of the college organizing the event.
        """
        self.event_name = event_name
        self.event_date = datetime.strptime(event_date, "%Y-%m-%d").strftime("%B %d, %Y")
        self.college_name = college_name

    def generate_message(self):
        """
        Generate a message for students about the celebration of the International Day Against Drug Abuse and Illicit Trafficking.

        Returns:
            str: The generated message.
        """
        try:
            message = f"Dear Students,\n\n"
            message += f"We are pleased to announce that {self.college_name} is organizing a competition to celebrate the International Day Against Drug Abuse and Illicit Trafficking, also known as {self.event_name}.\n\n"
            message += f"The event will take place on {self.event_date} and is open to all students.\n\n"
            message += "The competition aims to raise awareness about the dangers of drug abuse and illicit trafficking, and to encourage students to take an active role in promoting a healthy and safe lifestyle.\n\n"
            message += "We invite all interested students to participate in this competition and make it a success.\n\n"
            message += "For more information, please contact your college administration.\n\n"
            message += "Best regards,\n"
            message += f"{self.college_name} Administration"
            return message
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None


def main():
    event_name = "International Day Against Drug Abuse and Illicit Trafficking"
    event_date = "2024-06-26"
    college_name = "Nazirpur Degree College"

    generator = MessageGenerator(event_name, event_date, college_name)
    message = generator.generate_message()

    if message:
        print(message)


if __name__ == "__main__":
    main()
```
