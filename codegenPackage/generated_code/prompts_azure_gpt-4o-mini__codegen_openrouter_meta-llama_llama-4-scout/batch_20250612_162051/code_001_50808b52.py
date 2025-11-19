"""
Generated Code Metadata:
========================
Original URL: https://isbgames.isbeventteam.com
Prompt: Write a promotional email highlighting the unique features of the ISB Games 2024, focusing on the introduction of Bowling and the spirit of sportsmanship among ISB-ers.
Generated: DETERMINISTIC_50808b52901b4863
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_promotional_email(subject, message, from_addr, to_addr, password):
    """
    Send a promotional email to subscribers.

    Args:
        subject (str): The subject of the email.
        message (str): The body of the email.
        from_addr (str): The sender's email address.
        to_addr (str): The recipient's email address.
        password (str): The sender's email password.

    Returns:
        None
    """
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    body = message
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_addr, password)
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()

def main():
    try:
        # Define email parameters
        subject = "Get Ready for ISB Games 2024: Where Sportsmanship Meets Fun!"
        message = """
        Dear ISB-ers,

        We are thrilled to announce that the ISB Games 2024 is just around the corner, and this year, we're introducing an exciting new sport to our lineup: Bowling!

        The ISB Games has always been a celebration of the spirit of sportsmanship, teamwork, and camaraderie that defines our school community. With the addition of Bowling, we're expecting an even more thrilling competition that will bring out the best in all of us.

        Here are some of the unique features you can look forward to:

        - A fun-filled day of sports and games for all ISB-ers
        - The introduction of Bowling as a new sport
        - Opportunities to bond with friends and make new ones
        - A showcase of the school's spirit of sportsmanship and teamwork

        Mark your calendars for [Date] and get ready to be part of an unforgettable experience!

        Best regards,
        [Your Name]
        """
        from_addr = "your-email@gmail.com"
        to_addr = "recipient-email@example.com"
        password = "your-email-password"

        # Send the promotional email
        send_promotional_email(subject, message, from_addr, to_addr, password)
        print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("Authentication error: Please check your email and password.")
    except smtplib.SMTPException as e:
        print("SMTP error: ", str(e))
    except Exception as e:
        print("Error: ", str(e))

if __name__ == "__main__":
    main()
```
