"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://growth-geniuscapital.com.dhlcourierservices.com
Prompt: What are common reasons for a web hosting account to be suspended?
Generated: DETERMINISTIC_3d7a05f3188640eb
Batch ID: 20250612_160156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: web_hosting_suspension_reasons.py

def get_suspension_reasons():
    """
    Returns a list of common reasons why a web hosting account may be suspended.
    
    :return: List of suspension reasons.
    :rtype: list
    """
    return [
        "Outstanding payment or unpaid invoices",
        "Violation of terms of service or acceptable use policy",
        "Exceeding resource limits such as CPU, memory, or storage",
        "Hosting malicious content such as malware or phishing pages",
        "Spamming or sending bulk unsolicited emails",
        "High traffic causing server instability",
        "Copyright infringement or illegal content hosted",
        "Security breaches or compromised account",
        "Failure to renew the hosting plan",
        "Misuse of server resources like excessive cron jobs",
    ]


def display_reasons():
    """
    Displays the suspension reasons to the user in a user-friendly format.
    """
    try:
        reasons = get_suspension_reasons()
        print("Common reasons for web hosting account suspension:")
        for index, reason in enumerate(reasons, start=1):
            print(f"{index}. {reason}")
    except Exception as e:
        # Log the error for debugging purposes (in production, use a logging library)
        print(f"An error occurred while retrieving suspension reasons: {e}")


if __name__ == "__main__":
    # Entry point for the script
    try:
        display_reasons()
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An unexpected error occurred: {e}")
```
