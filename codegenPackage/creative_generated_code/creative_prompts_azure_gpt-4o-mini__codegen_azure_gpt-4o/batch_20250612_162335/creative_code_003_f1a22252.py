"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://transactionfinder.in
Prompt: What are the common scam types outlined by Transaction Finder, and how can I protect myself from them?
Generated: DETERMINISTIC_f1a222521d9c67aa
Batch ID: 20250612_162335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define common scam types as outlined by Transaction Finder
SCAM_TYPES = {
    "Phishing": "Fraudulent attempts to obtain sensitive information by posing as a trustworthy entity.",
    "Investment Scams": "Offers of high-return investments that are typically fake or involve Ponzi schemes.",
    "Online Shopping Scams": "Fake e-commerce websites that trick users into paying for goods they never receive.",
    "Romance Scams": "Tricking individuals into sending money to a fraudster posing as a romantic partner.",
    "Tech Support Scams": "Pretending to be technical support to gain access to personal information or extort money.",
    "Lottery Scams": "Notification of winning a prize or lottery that requires payment to claim rewards.",
    "Impersonation Scams": "Fraudsters pretending to be officials, family, or friends to solicit money.",
}

# Function to list common scam types
def list_scam_types():
    """
    Returns the list of common scam types.
    """
    return SCAM_TYPES

# Function to provide tips on how to protect yourself
def protection_tips():
    """
    Returns a list of tips on how to protect yourself from scams.
    """
    return [
        "Never share sensitive information like passwords or financial details over email or phone.",
        "Verify the authenticity of websites and emails before taking action.",
        "Avoid clicking suspicious links or attachments from unknown senders.",
        "Be cautious of unsolicited offers or requests for money.",
        "Use strong and unique passwords for online accounts.",
        "Enable two-factor authentication wherever possible.",
        "Monitor your bank statements and report suspicious transactions immediately.",
        "Educate yourself about common fraud tactics."
    ]

# Main function to display scam information and protection tips
def main():
    """
    Main function to display scam types and how to protect against them.
    """
    try:
        print("Common Scam Types:")
        for scam, description in list_scam_types().items():
            print(f"- {scam}: {description}")
        
        print("\nHow to Protect Yourself:")
        for tip in protection_tips():
            print(f"- {tip}")

    except Exception as e:
        # Log or handle unexpected errors
        print(f"An error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
