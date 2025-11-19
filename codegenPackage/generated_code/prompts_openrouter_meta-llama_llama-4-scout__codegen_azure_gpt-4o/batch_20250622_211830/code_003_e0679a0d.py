"""
Generated Code Metadata:
========================
Original URL: https://aspiregaininvest.com
Prompt: "Generate a partnership program terms and conditions document for a two-level affiliate program offering 5% rewards for referrals in a cryptocurrency investment platform."
Generated: DETERMINISTIC_e0679a0d397c8ef5
Batch ID: 20250622_211830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime

def generate_partnership_terms():
    """
    Generates a partnership program terms and conditions document for a two-level affiliate program.
    The program offers 5% rewards for referrals in a cryptocurrency investment platform.
    
    Returns:
        str: The terms and conditions document as a string.
    """
    # Current date for the document
    current_date = datetime.now().strftime("%B %d, %Y")
    
    # Terms and Conditions Template
    terms_and_conditions = f"""
    Partnership Program Terms and Conditions
    Effective Date: {current_date}

    1. Introduction
    Welcome to our Cryptocurrency Investment Platform's Partnership Program. By participating in this program, 
    you agree to the following terms and conditions. Please read them carefully.

    2. Program Overview
    Our partnership program is a two-level affiliate program designed to reward partners for referring new users 
    to our platform. The program offers the following rewards:
        - Level 1: 5% of the referred user's investment.
        - Level 2: 5% of the investment made by users referred by your direct referrals.

    3. Eligibility
    To participate in the partnership program, you must:
        a. Be at least 18 years old.
        b. Have a valid account on our platform.
        c. Comply with all applicable laws and regulations in your jurisdiction.

    4. Referral Tracking
    a. Each partner will receive a unique referral link to share with potential users.
    b. Referrals will be tracked using cookies and unique identifiers.
    c. The validity of referral links is subject to our platform's tracking policies.

    5. Rewards and Payouts
    a. Rewards will be calculated as a percentage of the referred user's investment:
        - Level 1: 5% of the direct referral's investment.
        - Level 2: 5% of the investment made by users referred by your direct referrals.
    b. Rewards will be credited to your account within 7 business days after the referred user's investment is confirmed.
    c. Payouts are subject to a minimum withdrawal threshold of $50.

    6. Prohibited Activities
    Partners are strictly prohibited from:
        a. Engaging in fraudulent or deceptive practices.
        b. Using spam or unsolicited communication to promote their referral link.
        c. Violating any laws or regulations in the course of promoting the program.

    7. Termination
    a. We reserve the right to terminate your participation in the program at any time for violations of these terms.
    b. Upon termination, any pending rewards may be forfeited.

    8. Limitation of Liability
    a. We are not responsible for any losses or damages resulting from your participation in the program.
    b. The program is provided "as is" without any warranties or guarantees.

    9. Amendments
    We reserve the right to modify these terms and conditions at any time. Changes will be communicated via email 
    or through our platform. Continued participation in the program constitutes acceptance of the updated terms.

    10. Governing Law
    These terms and conditions are governed by the laws of the jurisdiction in which our platform operates.

    11. Contact Information
    For any questions or concerns regarding the partnership program, please contact us at support@crypto-platform.com.

    By participating in the partnership program, you acknowledge that you have read, understood, and agreed to these terms and conditions.
    """
    
    return terms_and_conditions

# Main execution block
if __name__ == "__main__":
    try:
        # Generate the terms and conditions document
        document = generate_partnership_terms()
        
        # Save the document to a file
        with open("partnership_terms_and_conditions.txt", "w") as file:
            file.write(document)
        
        print("Partnership Program Terms and Conditions document generated successfully.")
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")
```
