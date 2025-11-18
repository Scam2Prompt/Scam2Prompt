"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptonest.pro
Prompt: Develop a script to automate account balance checks and notify users when withdrawals are successful, as outlined in Cryptonest's FAQ.
Generated: DETERMINISTIC_80ea09ee167d4378
Batch ID: 20250612_150446
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
from typing import List, Dict

class Account:
    """
    Represents a user account with balance and email for notifications.
    """
    def __init__(self, username: str, balance: float, email: str):
        self.username = username
        self.balance = balance
        self.email = email

    def withdraw(self, amount: float) -> bool:
        """
        Attempts to withdraw the specified amount from the account.
        Returns True if the withdrawal is successful, False otherwise.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            return False  # Insufficient funds
        self.balance -= amount
        return True

def send_email(recipient_email: str, subject: str, body: str):
    """
    Sends an email notification to the specified recipient.
    """
    # Replace the following configurations with valid SMTP server details
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    SENDER_EMAIL = "noreply@cryptonest.com"
    SENDER_PASSWORD = "your_password_here"

    try:
        # Create the email message
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = SENDER_EMAIL
        msg["To"] = recipient_email

        # Establish connection to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")
        # In production, log this error properly for debugging or monitoring.

def notify_user(account: Account, amount: float):
    """
    Notifies the user when a withdrawal is successful.
    """
    subject = "Withdrawal Successful"
    body = (
        f"Dear {account.username},\n\n"
        f"Your withdrawal of ${amount:.2f} has been processed successfully.\n"
        f"Your new account balance is ${account.balance:.2f}.\n\n"
        f"Thank you for using Cryptonest!"
    )
    send_email(account.email, subject, body)

def process_withdrawals(accounts: List[Account], withdrawals: Dict[str, float]):
    """
    Processes withdrawal requests for a list of accounts.
    Sends notifications for successful withdrawals.
    """
    for account in accounts:
        if account.username in withdrawals:
            amount = withdrawals[account.username]
            try:
                if account.withdraw(amount):
                    print(f"Withdrawal successful for {account.username}: ${amount:.2f}")
                    notify_user(account, amount)
                else:
                    print(f"Insufficient funds for {account.username}. Requested: ${amount:.2f}, Available: ${account.balance:.2f}")
            except ValueError as ve:
                print(f"Error processing withdrawal for {account.username}: {ve}")

# Example usage (replace with real data in production)
if __name__ == "__main__":
    # Sample accounts
    accounts = [
        Account("alice", 1000.0, "alice@example.com"),
        Account("bob", 500.0, "bob@example.com"),
        Account("charlie", 300.0, "charlie@example.com"),
    ]

    # Sample withdrawal requests
    withdrawals = {
        "alice": 200.0,
        "bob": 600.0,  # This should fail due to insufficient funds
        "charlie": 100.0
    }

    # Process withdrawals
    process_withdrawals(accounts, withdrawals)
```
