"""
Generated Code Metadata:
========================
Original URL: https://qubetic.co
Prompt: What are common reasons for website account suspension and how can I prevent them?
Generated: DETERMINISTIC_30c7ca274cd2c74f
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script outlines common reasons for website account suspension and prevention measures.
It serves as a reference guide for users to maintain good account standing.
"""

def get_account_suspension_reasons():
    """
    Returns a dictionary of common account suspension reasons and prevention tips.
    
    Returns:
        dict: Keys are reasons for suspension, values are prevention measures.
    """
    reasons = {
        "Violation of Terms of Service": 
            "Carefully read and adhere to the platform's Terms of Service and Community Guidelines.",
        
        "Suspicious Activity/Unauthorized Access": 
            "Use strong passwords, enable 2FA, and monitor account activity regularly.",
        
        "Spamming or Excessive Automation": 
            "Avoid sending bulk messages or using bots unless explicitly permitted.",
        
        "Inappropriate Content": 
            "Post only content that complies with platform rules regarding nudity, hate speech, etc.",
        
        "Copyright Infringement": 
            "Only share content you have rights to or that falls under fair use.",
        
        "Fraudulent Activity": 
            "Never engage in scams, phishing, or misrepresentation.",
        
        "Multiple Policy Violations": 
            "Address any warnings promptly and correct behavior after first offenses.",
        
        "Inactive Account": 
            "Log in periodically if the platform has activity requirements.",
        
        "False Information": 
            "Provide accurate personal and payment information where required.",
        
        "Chargebacks/Payment Issues": 
            "Ensure payment methods are valid and disputes are resolved properly."
    }
    return reasons

def display_prevention_guide():
    """
    Displays a formatted guide of suspension reasons and prevention measures.
    """
    reasons = get_account_suspension_reasons()
    
    print("Website Account Suspension Prevention Guide")
    print("=" * 45)
    print("\nCommon reasons for suspension and how to prevent them:\n")
    
    for i, (reason, prevention) in enumerate(reasons.items(), 1):
        print(f"{i}. {reason}")
        print(f"   Prevention: {prevention}\n")

if __name__ == "__main__":
    try:
        display_prevention_guide()
    except Exception as e:
        print(f"An error occurred while generating the guide: {e}")
```
