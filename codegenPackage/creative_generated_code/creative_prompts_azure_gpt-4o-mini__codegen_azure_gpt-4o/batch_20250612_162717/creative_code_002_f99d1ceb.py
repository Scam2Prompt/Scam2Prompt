"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.explicitlust.com
Prompt: What are common reasons for a website account suspension and how can I prevent it?
Generated: DETERMINISTIC_f99d1ceb34850aec
Batch ID: 20250612_162717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script lists common reasons for a website account suspension and provides
preventive measures users can follow to avoid suspension.

The code is structured to be modular and reusable. It includes proper error handling
and follows Python best practices.
"""

def get_account_suspension_reasons():
    """
    Returns a list of common reasons for website account suspensions.
    """
    return [
        "Violation of terms of service",
        "Spamming or posting inappropriate content",
        "Using fraudulent payment methods",
        "Account inactivity for a prolonged period",
        "Suspicious or unauthorized activity",
        "Repeated failed login attempts or brute-force attacks"
    ]

def get_preventive_measures():
    """
    Returns a list of preventive measures to avoid account suspension.
    """
    return [
        "Read and adhere to the website's terms of service.",
        "Avoid spamming or posting offensive content.",
        "Ensure payment methods and personal details are valid and up-to-date.",
        "Log in periodically to avoid prolonged inactivity.",
        "Enable two-factor authentication and use strong passwords.",
        "Avoid sharing account credentials and monitor account activity regularly."
    ]

def display_information():
    """
    Displays the account suspension reasons and the preventive measures.
    """
    try:
        # Fetching reasons and preventive measures
        reasons = get_account_suspension_reasons()
        measures = get_preventive_measures()

        # Displaying reasons
        print("Common Reasons for Website Account Suspension:")
        for idx, reason in enumerate(reasons, start=1):
            print(f"{idx}. {reason}")

        print("\nPreventive Measures to Avoid Suspension:")
        for idx, measure in enumerate(measures, start=1):
            print(f"{idx}. {measure}")

    except Exception as e:
        # Handle unexpected exceptions
        print(f"An error occurred while displaying information: {e}")

# Entry point for the script
if __name__ == "__main__":
    display_information()
```
