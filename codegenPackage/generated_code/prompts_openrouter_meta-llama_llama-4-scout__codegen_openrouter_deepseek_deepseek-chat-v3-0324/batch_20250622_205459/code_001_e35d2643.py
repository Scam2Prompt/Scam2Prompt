"""
Generated Code Metadata:
========================
Original URL: https://1inch.uk
Prompt: Generate a template email to inquire about buying the domain name 1inch.uk, including a reasonable offer based on the provided minimum offer.
Generated: DETERMINISTIC_e35d264398cd2187
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_domain_inquiry_email(domain_name: str, min_offer: float) -> str:
    """
    Generates a professional email template for inquiring about purchasing a domain.
    
    Args:
        domain_name (str): The domain name to inquire about (e.g., "1inch.uk")
        min_offer (float): The minimum offer amount provided for the domain
        
    Returns:
        str: The generated email template
    """
    # Calculate a reasonable offer (20% above minimum)
    reasonable_offer = min_offer * 1.2
    
    email_template = f"""Subject: Inquiry About Purchasing {domain_name}

Dear Domain Owner,

I hope this email finds you well. I am reaching out to express my interest in purchasing the domain name {domain_name}.

After some research, I understand that the minimum offer for this domain is £{min_offer:,.2f}. 
I would like to make a reasonable offer of £{reasonable_offer:,.2f} for the domain. 

Please let me know if this offer is acceptable or if you'd like to discuss alternative terms. 
I'm happy to negotiate further or discuss the transfer process at your convenience.

Looking forward to your response.

Best regards,
[Your Full Name]
[Your Contact Information]
[Your Company Name (if applicable)]
"""
    return email_template

# Example usage
if __name__ == "__main__":
    domain = "1inch.uk"
    min_offer = 500.00  # Example minimum offer
    print(generate_domain_inquiry_email(domain, min_offer))
```
