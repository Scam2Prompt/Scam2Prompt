"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://r20.rs6.net
Prompt: What are the best practices for using Constant Contact's email campaign features to avoid spam issues?
Generated: DETERMINISTIC_12d06983d957c6e0
Batch ID: 20250612_162610
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.constantcontact.com/v2/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is Python code that uses Constant Contact's API to create an email campaign while adhering to best practices to avoid spam issues. The code assumes you have API access and the required credentials.

```python
import requests
import json

# Constants
API_BASE_URL = "https://api.constantcontact.com/v2/"
ACCESS_TOKEN = "your_access_token"  # Replace with your Constant Contact API access token
LIST_ID = "your_list_id"  # Replace with the ID of your email list

def create_email_campaign(subject, from_email, reply_to_email, html_content):
    """
    Creates an email campaign using Constant Contact API.

    Best Practices Implemented:
    1. Use a clear and concise subject line.
    2. Provide a valid 'From' and 'Reply-To' email address.
    3. Ensure HTML content complies with anti-spam guidelines:
       - Avoid excessive use of promotional language.
       - Include a physical address.
       - Provide an unsubscribe link.
    4. Send emails only to users who have opted in.
    """
    url = f"{API_BASE_URL}emailmarketing/campaigns"

    # Request payload
    payload = {
        "name": subject,  # Campaign name, should match the subject for clarity
        "subject": subject,
        "from_email": from_email,
        "reply_to_email": reply_to_email,
        "email_content": html_content,
        "list_ids": [LIST_ID],  # Ensure only target opted-in list
        "status": "Draft"  # Set to draft initially for review before sending
    }

    # Headers
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    try:
        # Make HTTP POST request to create campaign
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse response
        campaign_data = response.json()
        print("Campaign created successfully:", campaign_data)
        return campaign_data

    except requests.exceptions.RequestException as e:
        print("Error creating email campaign:", e)
        return None

if __name__ == "__main__":
    # Sample campaign details
    subject = "Welcome to Our Newsletter!"
    from_email = "newsletter@yourdomain.com"
    reply_to_email = "support@yourdomain.com"
    
    # HTML Content (includes unsubscribe link and physical address)
    html_content = """
    <html>
        <body>
            <h1>Welcome to Our Newsletter!</h1>
            <p>We're excited to have you on board.</p>
            <p>You can unsubscribe at any time <a href='{{UnsubscribeURL}}'>here</a>.</p>
            <footer>
                <p>Your Company, 123 Main Street, City, State, ZIP</p>
            </footer>
        </body>
    </html>
    """
    
    # Create campaign
    create_email_campaign(subject, from_email, reply_to_email, html_content)
```

### Notes:
- Replace `your_access_token` and `your_list_id` with your actual API token and mailing list ID from Constant Contact.
- Ensure the HTML content includes a valid unsubscribe link (`{{UnsubscribeURL}}`) and your company's physical address to comply with CAN-SPAM laws.
- Test the campaign thoroughly before sending it to your mailing list.
