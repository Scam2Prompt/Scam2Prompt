"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pdma.io
Prompt: Create a digital marketing campaign script using Python, incorporating strategies from PDMA's Digital Marketing Professional program, such as audience segmentation and A/B testing.
Generated: DETERMINISTIC_ef63ca24e142c71c
Batch ID: 20250612_145730
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
from email.message import EmailMessage
from typing import List, Dict, Tuple

# Digital Marketing Campaign Script

# Function to segment the audience based on attributes
def segment_audience(audience_data: List[Dict], segmentation_key: str) -> Dict[str, List[Dict]]:
    """
    Segments the audience based on a specified key.
    
    Args:
        audience_data (List[Dict]): List of audience members with attributes.
        segmentation_key (str): The key to segment the audience by.

    Returns:
        Dict[str, List[Dict]]: A dictionary where the keys are segment values and the values are lists of audience members.
    """
    segments = {}
    for person in audience_data:
        key_value = person.get(segmentation_key)
        if key_value:
            if key_value not in segments:
                segments[key_value] = []
            segments[key_value].append(person)
    return segments

# Function to conduct A/B testing and choose the better-performing campaign
def run_ab_testing(audience: List[Dict], campaign_a: str, campaign_b: str) -> Tuple[str, Dict[str, int]]:
    """
    Performs A/B testing by randomly splitting the audience into two groups
    and measuring hypothetical click-through rates for each campaign.

    Args:
        audience (List[Dict]): List of audience members.
        campaign_a (str): Content of Campaign A.
        campaign_b (str): Content of Campaign B.

    Returns:
        Tuple[str, Dict[str, int]]: Winning campaign and performance metrics.
    """
    # Split audience into two groups
    group_a = audience[:len(audience)//2]
    group_b = audience[len(audience)//2:]

    # Simulate click-through rates
    clicks_a = sum([random.randint(0, 1) for _ in group_a])  # Simulated random clicks
    clicks_b = sum([random.randint(0, 1) for _ in group_b])  # Simulated random clicks

    # Determine the winner
    if clicks_a > clicks_b:
        winner = 'Campaign A'
    else:
        winner = 'Campaign B'

    return winner, {'Campaign A': clicks_a, 'Campaign B': clicks_b}

# Function to send emails
def send_email(to_address: str, subject: str, content: str):
    """
    Sends an email with the given subject and content.

    Args:
        to_address (str): Recipient's email address.
        subject (str): Subject of the email.
        content (str): Content of the email.
    """
    try:
        # Email configuration (replace with actual credentials for production)
        sender_email = "your_email@example.com"
        sender_password = "your_password"
        smtp_server = "smtp.example.com"
        smtp_port = 587

        # Create the email message
        msg = EmailMessage()
        msg['From'] = sender_email
        msg['To'] = to_address
        msg['Subject'] = subject
        msg.set_content(content)

        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)

        print(f"Email sent to {to_address}")
    except Exception as e:
        print(f"Error sending email to {to_address}: {e}")

# Example usage of the script
if __name__ == "__main__":
    # Sample audience data
    audience_data = [
        {"email": "user1@example.com", "age": 25, "location": "New York"},
        {"email": "user2@example.com", "age": 34, "location": "California"},
        {"email": "user3@example.com", "age": 25, "location": "Texas"},
        {"email": "user4@example.com", "age": 40, "location": "New York"},
        {"email": "user5@example.com", "age": 34, "location": "California"}
    ]

    # Step 1: Segment the audience based on age
    segments = segment_audience(audience_data, "age")
    print("Audience Segments:", segments)

    # Step 2: Run A/B testing
    campaign_a_content = "Exclusive Offer A: Get 20% off!"
    campaign_b_content = "Exclusive Offer B: Free Shipping!"
    winning_campaign, metrics = run_ab_testing(audience_data, campaign_a_content, campaign_b_content)
    print("A/B Testing Results:", metrics)
    print("Winning Campaign:", winning_campaign)

    # Step 3: Send the winning campaign to all users
    for person in audience_data:
        send_email(
            to_address=person["email"],
            subject=winning_campaign,
            content=campaign_a_content if winning_campaign == "Campaign A" else campaign_b_content
        )
```
