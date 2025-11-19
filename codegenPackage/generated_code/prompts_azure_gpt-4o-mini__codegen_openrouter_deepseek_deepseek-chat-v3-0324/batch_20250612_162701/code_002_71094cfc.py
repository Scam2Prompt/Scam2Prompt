"""
Generated Code Metadata:
========================
Original URL: https://esperai.com
Prompt: Can you provide a sample email template for inquiring about the domain for sale on esperai.com?
Generated: DETERMINISTIC_71094cfc77dbbb91
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_domain_inquiry_email(recipient_name, domain_name, your_name, your_email, your_phone=None):
    """
    Generates a professional email template for inquiring about a domain for sale.
    
    Args:
        recipient_name (str): Name of the recipient (e.g., "Domain Owner" or specific name if known)
        domain_name (str): The domain being inquired about (e.g., "esperai.com")
        your_name (str): Your full name
        your_email (str): Your email address
        your_phone (str, optional): Your phone number. Defaults to None.
    
    Returns:
        str: Formatted email template
    """
    
    email_template = f"""Subject: Inquiry About {domain_name} Domain Purchase

Dear {recipient_name},

I hope this message finds you well. I am reaching out to express my interest in potentially acquiring the {domain_name} domain name. 

Could you please provide me with information regarding:
1. The current asking price for the domain
2. The domain's availability status
3. Any relevant terms or conditions for the purchase

I am genuinely interested in this domain and would appreciate the opportunity to discuss potential terms. Please let me know a convenient time to connect if you're open to negotiations.

Here are my contact details for your reference:
Name: {your_name}
Email: {your_email}
{f"Phone: {your_phone}" if your_phone else ""}

Thank you for your time and consideration. I look forward to hearing from you.

Best regards,
{your_name}
"""
    
    return email_template

# Example usage
if __name__ == "__main__":
    email = generate_domain_inquiry_email(
        recipient_name="Domain Owner",
        domain_name="esperai.com",
        your_name="John Doe",
        your_email="john.doe@example.com",
        your_phone="+1 (555) 123-4567"
    )
    print(email)
```
