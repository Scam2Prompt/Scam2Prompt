"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ndhc.edu.bd
Prompt: Draft a message for students about the celebration of the International Day Against Drug Abuse and Illicit Trafficking, including details about the competition organized by Nazirpur Degree College.
Generated: DETERMINISTIC_e62cee4d2a229c8e
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary module for email/message creation
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def draft_message():
    """
    Generates a draft message for students about the celebration of the International Day
    Against Drug Abuse and Illicit Trafficking, including details about a competition.
    Returns:
        str: A formatted email message.
    """
    try:
        # Initialize the email message
        message = MIMEMultipart()
        message['Subject'] = "Join Us: International Day Against Drug Abuse and Illicit Trafficking Celebration"
        message['From'] = "info@nazirpurdegreecollege.edu"
        message['To'] = "students@nazirpurdegreecollege.edu"

        # Write the body of the message
        body = """
        Dear Students,

        We are pleased to announce that Nazirpur Degree College will be celebrating 
        the International Day Against Drug Abuse and Illicit Trafficking on June 26th.

        As part of the celebration, we are organizing a competition to encourage 
        awareness and creativity on this important topic. Here are the details:

        Event: Poster Design and Essay Writing Competition
        Theme: "Say No to Drugs, Yes to Life"
        Date: June 26th, 2023
        Time: 10:00 AM to 3:00 PM
        Venue: Nazirpur Degree College Auditorium

        Guidelines:
        - Poster designs should be original and reflect the theme of the event.
        - Essays should be between 500-700 words and must be submitted by 12:00 PM on June 26th.

        Prizes:
        Winners will receive certificates and exciting prizes!

        We invite all students to take part in this meaningful initiative. Together, let's 
        raise awareness and stand against drug abuse and illicit trafficking.

        For registration and inquiries, please contact:
        Email: events@nazirpurdegreecollege.edu
        Phone: +880-123-4567890

        Let’s make this event a memorable one. We look forward to your active participation!

        Best regards,
        Nazirpur Degree College Administration
        """

        # Attach the body to the email message
        message.attach(MIMEText(body, 'plain'))

        # Return the complete email as a string
        return message.as_string()

    except Exception as e:
        # Log an error message if something goes wrong
        return f"An error occurred while drafting the message: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Call the function and print the generated message
    email_message = draft_message()
    print(email_message)
```
