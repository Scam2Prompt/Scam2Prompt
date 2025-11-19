"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftrealisticevm.com
Prompt: What are the common reasons for an account suspension on a web hosting service?
Generated: DETERMINISTIC_54f932adcdf357e5
Batch ID: 20250612_162728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# A Python script to simulate retrieving common reasons for account suspension on a web hosting service.

def get_account_suspension_reasons():
    """
    This function returns a list of common reasons 
    for account suspension on a web hosting service.
    """
    reasons = [
        "Non-payment or overdue invoices",
        "Hosting malware or malicious software",
        "Excessive resource usage (CPU, memory, bandwidth)",
        "Violation of Terms of Service (ToS)",
        "Spamming or sending unsolicited emails",
        "Hosting prohibited content (illegal or copyrighted material)",
        "Fraudulent activity or impersonation",
        "Repeated violations after warnings",
    ]
    return reasons


def main():
    """
    Main function to retrieve and display account suspension reasons.
    Includes error handling to ensure smooth execution.
    """
    try:
        # Retrieve reasons for account suspension
        suspension_reasons = get_account_suspension_reasons()
        
        # Display the reasons to the user
        print("Common Reasons for Account Suspension on a Web Hosting Service:")
        for idx, reason in enumerate(suspension_reasons, start=1):
            print(f"{idx}. {reason}")
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred while retrieving suspension reasons: {e}")


if __name__ == "__main__":
    # Entry point of the program
    main()
```
