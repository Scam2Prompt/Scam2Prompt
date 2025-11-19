"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soporte.arpynet.com
Prompt: What information should I include in an email to support regarding a suspended account?
Generated: DETERMINISTIC_60ddf78a9c09f720
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# This script generates a template for an email to support regarding a suspended account.
# The user can input relevant details, and the script will ensure proper formatting and inclusion of essential information.

def generate_support_email(name, email, account_id, suspension_date, additional_info=None):
    """
    Generate a well-structured email template for contacting support about a suspended account.

    Args:
        name (str): Full name of the account holder.
        email (str): Email address associated with the account.
        account_id (str): Unique identifier for the account.
        suspension_date (str): Date when the account was suspended.
        additional_info (str, optional): Any extra information the user wants to include.

    Returns:
        str: A formatted email template.
    """
    try:
        # Validate input
        if not name or not email or not account_id or not suspension_date:
            raise ValueError("All mandatory fields (name, email, account_id, suspension_date) must be provided.")

        # Email template
        email_template = f"""
        Subject: Assistance Required for Suspended Account

        Dear Support Team,

        I am writing to request assistance regarding the suspension of my account. Below are the details of my account:

        - Full Name: {name}
        - Email Address: {email}
        - Account ID: {account_id}
        - Suspension Date: {suspension_date}

        {f"Additional Information: {additional_info}\n\n" if additional_info else ""}
        I would appreciate it if you could review this matter and provide information about the reason for the suspension. 
        If there are any actions required on my part to resolve this, please let me know.

        Thank you for your time and assistance. I look forward to your response.

        Best regards,
        {name}
        """
        return email_template.strip()
    except ValueError as ve:
        return f"Error: {str(ve)}"

# Main block to demonstrate usage
if __name__ == "__main__":
    # Example user input
    name = "John Doe"
    email = "john.doe@example.com"
    account_id = "12345XYZ"
    suspension_date = "2023-10-15"
    additional_info = "I believe my account was suspended due to incorrect activity detection."

    # Generate the email
    email_content = generate_support_email(name, email, account_id, suspension_date, additional_info)

    # Output the generated email
    print(email_content)
```
