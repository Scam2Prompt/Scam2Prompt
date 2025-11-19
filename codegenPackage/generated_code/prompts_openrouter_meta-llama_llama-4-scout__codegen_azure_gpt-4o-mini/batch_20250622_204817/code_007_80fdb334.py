"""
Generated Code Metadata:
========================
Original URL: https://www.igadvocacia.com
Prompt: Can you write a sample email that a client might send to IG Advocacia using the contact form on their website?
Generated: DETERMINISTIC_80fdb33431ff915f
Batch ID: 20250622_204817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Sample email generator for IG Advocacia contact form

class Email:
    def __init__(self, sender_name, sender_email, subject, message):
        """
        Initializes the Email object with sender details and message content.

        :param sender_name: str - Name of the sender
        :param sender_email: str - Email address of the sender
        :param subject: str - Subject of the email
        :param message: str - Body of the email
        """
        self.sender_name = sender_name
        self.sender_email = sender_email
        self.subject = subject
        self.message = message

    def validate_email(self):
        """
        Validates the email format.

        :return: bool - True if email is valid, False otherwise
        """
        import re
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, self.sender_email) is not None

    def generate_email(self):
        """
        Generates the formatted email string.

        :return: str - Formatted email
        :raises ValueError: If the email is invalid
        """
        if not self.validate_email():
            raise ValueError("Invalid email address format.")

        email_template = f"""
        From: {self.sender_name} <{self.sender_email}>
        To: contact@igadvocacia.com
        Subject: {self.subject}

        {self.message}
        """
        return email_template.strip()

# Example usage
if __name__ == "__main__":
    try:
        # Sample data for the email
        client_email = Email(
            sender_name="John Doe",
            sender_email="johndoe@example.com",
            subject="Inquiry about Legal Services",
            message="Dear IG Advocacia Team,\n\nI would like to inquire about your legal services regarding contract law. Please let me know how I can proceed.\n\nBest regards,\nJohn Doe"
        )

        # Generate and print the email
        print(client_email.generate_email())

    except ValueError as e:
        print(f"Error: {e}")
```
