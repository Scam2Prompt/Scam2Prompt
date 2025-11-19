"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infy.uk
Prompt: Describe how to report abuse on a website hosted by InfinityFree, including the necessary details to include in the report.
Generated: DETERMINISTIC_ffec9880ac0fa4ef
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to report abuse on a website hosted by InfinityFree.
It collects necessary details from the user and generates an email template for submitting an abuse report.
"""

import re

def validate_email(email):
    """
    Validate the format of an email address.
    :param email: str, email address to validate
    :return: bool, True if email is valid, False otherwise
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def collect_abuse_report_details():
    """
    Collects details of the abuse report from the user.
    :return: dict, containing the abuse report details
    """
    print("InfinityFree Abuse Report Form")
    print("Please provide the following details:")

    # Collect the URL of the offending website
    offending_url = input("Enter the URL of the website you are reporting (required): ").strip()
    if not offending_url:
        raise ValueError("The URL of the offending website is required.")

    # Collect the reason for reporting the website
    reason = input("Enter the reason for reporting the website (required): ").strip()
    if not reason:
        raise ValueError("The reason for reporting the website is required.")

    # Collect the user's name
    user_name = input("Enter your name (optional): ").strip()

    # Collect the user's email address
    user_email = input("Enter your email address (optional, for follow-up): ").strip()
    if user_email and not validate_email(user_email):
        raise ValueError("Invalid email address format.")

    # Collect additional details
    additional_details = input("Enter any additional details (optional): ").strip()

    return {
        "offending_url": offending_url,
        "reason": reason,
        "user_name": user_name,
        "user_email": user_email,
        "additional_details": additional_details,
    }

def generate_email_template(report_details):
    """
    Generates an email template for reporting abuse to InfinityFree.
    :param report_details: dict, containing the abuse report details
    :return: str, formatted email template
    """
    email_body = f"""
Subject: Abuse Report - InfinityFree Hosting

Dear InfinityFree Abuse Team,

I would like to report the following website for abuse:

Offending URL: {report_details['offending_url']}
Reason for report: {report_details['reason']}

"""
    if report_details['user_name']:
        email_body += f"Reported by: {report_details['user_name']}\n"

    if report_details['user_email']:
        email_body += f"Contact Email: {report_details['user_email']}\n"

    if report_details['additional_details']:
        email_body += f"Additional Details: {report_details['additional_details']}\n"

    email_body += f"""
Please investigate this matter at your earliest convenience.

Thank you,
InfinityFree User
"""
    return email_body.strip()

def main():
    """
    Main function to collect abuse report details and generate the email template.
    """
    try:
        report_details = collect_abuse_report_details()
        email_template = generate_email_template(report_details)
        print("\nGenerated Abuse Report Email:")
        print("-" * 40)
        print(email_template)
        print("-" * 40)
        print("\nPlease copy and paste the above email template and send it to abuse@infinityfree.net.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
