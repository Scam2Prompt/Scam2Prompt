"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://networkitcnetworkmo.com
Prompt: Generate code to parse email headers and identify accidental deliveries in emails sent through VertiStream.
Generated: DETERMINISTIC_07ffd0ce561a38bf
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import email
import re
from email.parser import Parser

def parse_email_headers(raw_email_data):
    """
    Parses email headers from raw email data and identifies accidental deliveries in emails
    sent through VertiStream.

    Args:
        raw_email_data (str): The raw email data as a string.

    Returns:
        dict: A dictionary containing header fields and a flag indicating accidental delivery.
    """
    try:
        # Parse the email using the email.parser.Parser
        email_message = Parser().parsestr(raw_email_data)

        # Extract all headers into a dictionary
        headers = dict(email_message.items())

        # Check if the email is sent through VertiStream
        accidental_delivery = False
        if 'X-Mailer' in headers:
            mailer_info = headers['X-Mailer']
            
            # VertiStream emails might have specific patterns in headers or X-Mailer field
            if 'VertiStream' in mailer_info:
                # Look for accidental delivery keywords in headers
                for key, value in headers.items():
                    if re.search(r'accidental delivery', value, re.IGNORECASE):
                        accidental_delivery = True
                        break

        # Return parsed headers and accidental delivery flag
        return {
            'headers': headers,
            'accidental_delivery': accidental_delivery
        }

    except Exception as e:
        # Handle any parsing errors gracefully
        return {
            'error': str(e),
            'accidental_delivery': False
        }

# Example usage:
if __name__ == "__main__":
    raw_email = """Subject: Test Email
From: sender@example.com
To: receiver@example.com
X-Mailer: VertiStream
X-Note: Accidental Delivery

This is a test email."""
    
    result = parse_email_headers(raw_email)
    print(result)
```
