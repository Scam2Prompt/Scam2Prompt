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
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to send email to students
def send_email(subject, message, recipient_list):
    """
    Sends an email with the specified subject and message to a list of recipients.
    
    Parameters:
        subject (str): The subject of the email.
        message (str): The body content of the email.
        recipient_list (list): A list of email addresses to send the message to.
        
    Raises:
        Exception: Raises an error if the email fails to send.
    """
    try:
        # Set up the SMTP server
        smtp_server = 'smtp.example.com'
        smtp_port = 587
        sender_email = 'your_email@example.com'
        password = 'your_password'
        
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = ', '.join(recipient_list)
        msg['Subject'] = subject
        
        # Attach the message body
        msg.attach(MIMEText(message, 'plain'))
        
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, password)
            server.send_message(msg)
            
        print("Email sent successfully.")
        
    except Exception as e:
        print(f"Failed to send email: {e}")

# Drafting the message about the celebration
def draft_message():
    """
    Drafts a message about the International Day Against Drug Abuse and Illicit Trafficking 
    and the competition organized by Nazirpur Degree College.
    
    Returns:
        str: The drafted message.
    """
    message = (
        "Dear Students,\n\n"
        "We are pleased to announce the celebration of the International Day Against Drug Abuse and Illicit Trafficking, "
        "which will take place on June 26th. This day aims to raise awareness about the harmful effects of drug abuse and "
        "the challenges posed by illicit trafficking.\n\n"
        "In recognition of this important day, Nazirpur Degree College is organizing a competition to engage students in a "
        "meaningful dialogue about drug abuse prevention and the promotion of a drug-free society. \n\n"
        "Details of the Competition:\n"
        "- **Topic:** The Impact of Drug Abuse on Society\n"
        "- **Eligibility:** All students of Nazirpur Degree College\n"
        "- **Submission Deadline:** June 20th\n"
        "- **Prizes:** Exciting prizes for the winners!\n\n"
        "We encourage all students to participate and share their thoughts and ideas. "
        "Let’s work together towards a healthier, drug-free future.\n\n"
        "Best regards,\n"
        "Nazirpur Degree College"
    )
    return message

# Main function to execute the email sending
def main():
    """
    Main function to send the drafted message to students.
    """
    subject = "International Day Against Drug Abuse and Illicit Trafficking Celebration"
    
    # List of student email addresses (example)
    recipients = ['student1@example.com', 'student2@example.com', 'student3@example.com']
    
    # Draft the message
    message = draft_message()
    
    # Send the email
    send_email(subject, message, recipients)

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
```
