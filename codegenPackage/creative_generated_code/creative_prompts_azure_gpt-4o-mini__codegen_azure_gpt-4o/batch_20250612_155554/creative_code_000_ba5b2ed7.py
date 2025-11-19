"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://internetcomputer.cc
Prompt: What are the common reasons for an account suspension on web hosting services?
Generated: DETERMINISTIC_ba5b2ed7d31e23aa
Batch ID: 20250612_155554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script lists common reasons for account suspension on web hosting services.
The code is designed to be clean, efficient, and well-documented.
"""

def get_account_suspension_reasons():
    """
    Returns a list of common reasons why accounts are suspended on web hosting services.
    
    :return: A list of strings describing the reasons for account suspension.
    """
    return [
        "Violation of Terms of Service",
        "Unpaid invoices or overdue payments",
        "Excessive resource usage (CPU, RAM, bandwidth)",
        "Hosting illegal or prohibited content",
        "Spamming or sending unsolicited emails",
        "Security breaches or hosting malicious software",
        "Copyright infringement (e.g., pirated software, media)",
        "Non-compliance with local laws and regulations",
        "Overuse or abuse of shared hosting resources",
        "Fraudulent activities or fake account information"
    ]

def main():
    """
    Main function to display common reasons for account suspension.
    """
    try:
        reasons = get_account_suspension_reasons()
        print("Common Reasons for Account Suspension on Web Hosting Services:")
        print("-" * 60)
        for idx, reason in enumerate(reasons, start=1):
            print(f"{idx}. {reason}")
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Entry point of the script
    main()
```
