"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binaryexpertise.com
Prompt: What are the common reasons for an account suspension on a web hosting service?
Generated: DETERMINISTIC_54f932adcdf357e5
Batch ID: 20250612_160203
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
        "Security breaches or hacking attempts"
    ]
    return reasons


def main():
    """
    The main function to display common reasons for account suspension.
    Includes error handling for any unexpected issues.
    """
    try:
        # Retrieve the list of suspension reasons
        suspension_reasons = get_account_suspension_reasons()
        
        # Display the reasons to the user
        print("Common reasons for account suspension on a web hosting service:")
        for index, reason in enumerate(suspension_reasons, start=1):
            print(f"{index}. {reason}")
    
    except Exception as e:
        # Log the error and notify the user
        print(f"An error occurred while retrieving suspension reasons: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
