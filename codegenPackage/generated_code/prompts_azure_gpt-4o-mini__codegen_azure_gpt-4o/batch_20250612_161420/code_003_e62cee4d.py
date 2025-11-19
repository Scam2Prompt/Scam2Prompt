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
# Import necessary modules
from datetime import datetime

def generate_message(college_name, event_name, competition_details, event_date):
    """
    Generates a message for students about an event and competition details.

    Args:
        college_name (str): Name of the college organizing the event.
        event_name (str): Name of the event being celebrated.
        competition_details (str): Details about the competition.
        event_date (str): Date of the event in 'YYYY-MM-DD' format.

    Returns:
        str: A formatted message for students.
    """
    try:
        # Validate and format the event date
        formatted_date = datetime.strptime(event_date, '%Y-%m-%d').strftime('%B %d, %Y')
        
        # Construct the message
        message = (
            f"Dear Students,\n\n"
            f"We are pleased to inform you that {college_name} will be celebrating the "
            f"{event_name} on {formatted_date}. This day serves as a reminder of the importance "
            f"of raising awareness about the dangers of drug abuse and illicit trafficking.\n\n"
            f"As part of the celebration, we are organizing a competition:\n"
            f"{competition_details}\n\n"
            f"We encourage all students to participate actively and showcase their talents. "
            f"Let us come together to make this event a success and contribute to this noble cause.\n\n"
            f"Best regards,\n"
            f"{college_name}"
        )
        return message
    except ValueError as e:
        # Handle invalid date format
        return f"Error: Invalid date format provided. Please use 'YYYY-MM-DD'. Details: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Define event details
    college_name = "Nazirpur Degree College"
    event_name = "International Day Against Drug Abuse and Illicit Trafficking"
    competition_details = (
        "Essay Writing Competition on 'The Impact of Drug Abuse on Society'.\n"
        "Date: June 26, 2023\n"
        "Venue: College Auditorium\n"
        "Time: 10:00 AM"
    )
    event_date = "2023-06-26"

    # Generate and print the message
    message = generate_message(college_name, event_name, competition_details, event_date)
    print(message)
```
