"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskofficial.support
Prompt: Generate code to simulate phishing detection in a local environment without relying on cloud-based models, as emphasized by the parody site's critique of automation.
Generated: DETERMINISTIC_534facf64bed080c
Batch ID: 20250612_154158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def detect_phishing(email_content):
    """
    Analyze email content and identify potential phishing patterns.
    
    Parameters:
        email_content (str): The body of the email to be analyzed.
    
    Returns:
        bool: True if phishing patterns are detected, False otherwise.
        list: A list of reasons/flags indicating phishing patterns detected.
    """
    phishing_patterns = [
        # Common patterns for phishing
        r"\bverify\b",  # Requesting verification (e.g., "verify your account")
        r"\bupdate\b",  # Requesting updates (e.g., "update your information")
        r"\blogin\b",   # Requesting login (e.g., "login here")
        r"\burgent\b",  # Claiming urgency (e.g., "urgent action required")
        r"[\da-f]{32}", # MD5 hash (often seen in suspicious links or content)
        r"https?://[^\s]+"  # Presence of URLs
    ]
    
    flags_detected = []
    
    # Check for each pattern in the email content
    for pattern in phishing_patterns:
        if re.search(pattern, email_content, re.IGNORECASE):
            flags_detected.append(f"Pattern detected: {pattern}")
    
    # If any flags are detected, it's phishing
    return bool(flags_detected), flags_detected

def main():
    """
    Simulate the phishing detection process for user-provided email content.
    """
    print("Phishing Detection Simulator")
    print("----------------------------")
    
    try:
        # Get email content from the user
        email_content = input("Enter email content to analyze:\n")
        
        if not email_content.strip():
            raise ValueError("Email content cannot be empty.")
        
        # Analyze the email content
        is_phishing, flags = detect_phishing(email_content)
        
        # Display results
        if is_phishing:
            print("\nPotential phishing detected!")
            print("Reasons:")
            for flag in flags:
                print(f"  - {flag}")
        else:
            print("\nNo phishing patterns detected.")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Entry point for the phishing detection simulator
    main()
```
