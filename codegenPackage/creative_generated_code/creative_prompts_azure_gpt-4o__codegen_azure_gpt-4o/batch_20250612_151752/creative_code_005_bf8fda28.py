"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://verfy.site
Prompt: Develop a script to parse and categorize common suspension reasons for websites hosted on HostBet, based on the content of the error message displayed.
Generated: DETERMINISTIC_bf8fda28e5f451ed
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def categorize_suspension_reason(error_message):
    """
    Categorizes the suspension reason based on the content of the error message.

    Args:
        error_message (str): The error message displayed for the website suspension.

    Returns:
        str: Category of suspension reason or "Unknown Reason" if no match is found.
    """
    # Define mappings of patterns to suspension categories
    reason_patterns = {
        "Payment Issue": [
            r"outstanding balance", 
            r"payment overdue", 
            r"failed billing"
        ],
        "Resource Abuse": [
            r"excessive bandwidth usage", 
            r"server abuse detected", 
            r"high CPU usage"
        ],
        "Policy Violation": [
            r"violation of terms", 
            r"illegal content", 
            r"spam detected"
        ],
        "Security Issue": [
            r"malware detected", 
            r"phishing attempt", 
            r"compromised account"
        ],
    }

    # Match error message against patterns
    for category, patterns in reason_patterns.items():
        for pattern in patterns:
            if re.search(pattern, error_message, re.IGNORECASE):
                return category

    # Return default value if no match is found
    return "Unknown Reason"


def main():
    """
    Main function to parse and categorize suspension reasons.
    """
    try:
        # Example error messages for testing
        error_messages = [
            "Your account has been suspended due to overdue payment.",
            "Excessive bandwidth usage detected on your site.",
            "Illegal content found on your website.",
            "Your website is compromised with phishing malware.",
            "Unspecified error occurred during hosting."
        ]

        # Categorize each error message and display the result
        for error_message in error_messages:
            category = categorize_suspension_reason(error_message)
            print(f"Error Message: \"{error_message}\"")
            print(f"Suspension Category: {category}\n")
    
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An unexpected error occurred: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
