"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avirodrian.com
Prompt: What are common reasons for a web hosting account to be suspended?
Generated: DETERMINISTIC_3d7a05f3188640eb
Batch ID: 20250612_163305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to list common reasons for a web hosting account suspension.
This program is a simple demonstration that outputs common reasons
for web hosting account suspension.
"""

def get_suspension_reasons():
    """
    Returns a list of common reasons why web hosting accounts get suspended.
    """
    return [
        "Exceeding bandwidth or storage limits",
        "Violation of terms of service",
        "Hosting malicious content (malware, phishing, etc.)",
        "Non-payment or overdue bills",
        "Spamming using hosted email services",
        "High server resource usage causing instability",
        "Unauthorized file sharing or copyright infringement",
        "Suspicious activity flagged by the hosting provider",
        "Using the site for illegal activities",
        "Failure to comply with security policies"
    ]

def display_reasons(reasons):
    """
    Displays the provided list of reasons in a user-friendly format.

    :param reasons: List of reasons for suspension.
    """
    print("Common Reasons for Web Hosting Account Suspension:")
    for idx, reason in enumerate(reasons, start=1):
        print(f"{idx}. {reason}")

def main():
    """
    Main function to execute the program logic.
    """
    try:
        reasons = get_suspension_reasons()
        display_reasons(reasons)
    except Exception as e:
        # Generic error handling for unforeseen issues
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Entry point for the script
    main()
```
