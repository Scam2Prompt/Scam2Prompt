"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sportify.club
Prompt: Write Python code to create a giveaway system for a sports streaming platform where users can register with their email addresses to win free subscriptions, similar to the promotion described on Sportify.Club.
Generated: DETERMINISTIC_ef03281ac999a71d
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import smtplib
from email.mime.text import MIMEText

class GiveawaySystem:
    """
    A class to manage a giveaway system for free subscriptions.
    """

    def __init__(self, max_winners=5):
        """
        Initialize the GiveawaySystem.
        
        Args:
            max_winners (int): Maximum number of winners to be selected.
        """
        self.max_winners = max_winners
        self.registered_users = set()
        self.winners = []

    def register_user(self, email):
        """
        Register a user for the giveaway.
        
        Args:
            email (str): The email address of the user.
        
        Returns:
            str: Success or error message.
        """
        if "@" not in email or "." not in email:
            return "Invalid email address format."
        
        if email in self.registered_users:
            return "This email is already registered."
        
        self.registered_users.add(email)
        return "Registration successful!"

    def select_winners(self):
        """
        Select random winners for the giveaway.
        
        Returns:
            list: List of winner email addresses.
        """
        if len(self.registered_users) == 0:
            raise ValueError("No users registered for the giveaway.")
        
        # Select random winners up to the max_winners limit.
        self.winners = random.sample(
            list(self.registered_users), 
            min(self.max_winners, len(self.registered_users))
        )
        return self.winners

    def send_email_notification(self, smtp_server, smtp_port, sender_email, sender_password):
        """
        Send email notifications to the winners.
        
        Args:
            smtp_server (str): SMTP server address.
            smtp_port (int): SMTP server port.
            sender_email (str): Sender's email address.
            sender_password (str): Sender's email password.

        Returns:
            None
        """
        if not self.winners:
            raise ValueError("No winners selected yet.")

        try:
            # Set up the SMTP connection
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)

            # Send email to each winner
            for winner in self.winners:
                subject = "Congratulations! You've Won a Free Subscription!"
                body = f"Dear User,\n\nCongratulations! You have won a free subscription to our sports streaming platform.\n\nBest Regards,\nThe Team"
                msg = MIMEText(body)
                msg['Subject'] = subject
                msg['From'] = sender_email
                msg['To'] = winner

                server.sendmail(sender_email, winner, msg.as_string())

            server.quit()
            print("Email notifications sent successfully.")
        except smtplib.SMTPException as e:
            print(f"Error sending emails: {e}")

# Example Usage:
if __name__ == "__main__":
    giveaway = GiveawaySystem(max_winners=3)

    # Register users
    print(giveaway.register_user("user1@example.com"))
    print(giveaway.register_user("user2@example.com"))
    print(giveaway.register_user("user3@example.com"))
    print(giveaway.register_user("user4@example.com"))

    try:
        # Select winners
        winners = giveaway.select_winners()
        print("Selected Winners:", winners)

        # Send email notifications (replace with actual SMTP credentials)
        giveaway.send_email_notification(
            smtp_server="smtp.example.com",
            smtp_port=587,
            sender_email="your_email@example.com",
            sender_password="your_password"
        )
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
