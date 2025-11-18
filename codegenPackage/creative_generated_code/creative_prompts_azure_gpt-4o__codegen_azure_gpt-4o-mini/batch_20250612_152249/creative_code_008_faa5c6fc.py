"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafkreibgcum43j7d4mubge4izowokrtbcswc6llh62jjklhh7g5bzrfd6e.ipfs.dweb.link
Prompt: Write a function to programmatically check the status of an OpenGPU DAO proposal and notify users of voting deadlines.
Generated: DETERMINISTIC_faa5c6fc9a6f5000
Batch ID: 20250612_152249
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.opengpu.org/proposals": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText

# Configuration for email notification
EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD = "your_email_password"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587

# Base URL for OpenGPU DAO API
API_URL = "https://api.opengpu.org/proposals"

def check_proposal_status(proposal_id):
    """
    Checks the status of an OpenGPU DAO proposal.

    :param proposal_id: The ID of the proposal to check
    :return: A dictionary containing proposal details or None if not found
    """
    try:
        response = requests.get(f"{API_URL}/{proposal_id}")
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the proposal details
    except requests.RequestException as e:
        print(f"Error fetching proposal status: {e}")
        return None

def notify_users(proposal, deadline_time):
    """
    Sends an email notification about the proposal status and deadline.

    :param proposal: The proposal details
    :param deadline_time: The deadline time for voting
    """
    subject = f"Voting Deadline Alert for Proposal {proposal['id']}"
    body = (
        f"Proposal Title: {proposal['title']}\n"
        f"Proposal Status: {proposal['status']}\n"
        f"Voting Deadline: {deadline_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"Link to Proposal: {API_URL}/{proposal['id']}\n"
    )
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS  # Or a list of recipients

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to secure connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, [EMAIL_ADDRESS], msg.as_string())
            print(f"Notification sent for proposal {proposal['id']}.")
    except Exception as e:
        print(f"Error sending email notification: {e}")

def main(proposal_id):
    """
    Main function to check proposal status and notify users if voting is ending soon.

    :param proposal_id: The ID of the proposal to check
    """
    proposal = check_proposal_status(proposal_id)
    if proposal:
        # Assuming the proposal has a 'voting_deadline' field in ISO 8601 format
        voting_deadline = datetime.fromisoformat(proposal['voting_deadline'])
        current_time = datetime.now()

        # Check if the voting deadline is within the next 7 days
        if current_time <= voting_deadline <= current_time + timedelta(days=7):
            notify_users(proposal, voting_deadline)
        else:
            print("No notifications needed; the voting deadline is not within the next week.")
    else:
        print("Failed to retrieve proposal details.")

# Example usage
if __name__ == "__main__":
    PROPOSAL_ID = "12345"  # Replace with an actual proposal ID
    main(PROPOSAL_ID)
```
