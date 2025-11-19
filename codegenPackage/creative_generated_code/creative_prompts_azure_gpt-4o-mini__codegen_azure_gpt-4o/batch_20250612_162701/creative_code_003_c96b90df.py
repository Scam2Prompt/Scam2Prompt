"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esperai.com
Prompt: What information should I include in my message when contacting the seller of the domain esperai.com?
Generated: DETERMINISTIC_c96b90df249433d8
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def create_message_to_seller(domain_name, buyer_name, buyer_email, offer_price=None):
    """
    Generates a message to contact a domain seller.

    Parameters:
        domain_name (str): The domain name you are interested in purchasing.
        buyer_name (str): Your name as the potential buyer.
        buyer_email (str): Your email address for correspondence.
        offer_price (float, optional): An optional initial offer price for the domain.

    Returns:
        str: A well-formatted message to send to the seller.
    """

    # Validate inputs
    if not domain_name or not isinstance(domain_name, str):
        raise ValueError("Domain name must be a non-empty string.")
    
    if not buyer_name or not isinstance(buyer_name, str):
        raise ValueError("Buyer name must be a non-empty string.")
    
    if not buyer_email or not isinstance(buyer_email, str):
        raise ValueError("Buyer email must be a valid string.")
    
    # Email validation
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_regex, buyer_email):
        raise ValueError("Invalid email format.")

    # Initial message
    message = f"""
    Subject: Inquiry Regarding {domain_name}

    Dear Seller,
    
    My name is {buyer_name}, and I am interested in purchasing the domain "{domain_name}". 
    I would like to discuss the availability of this domain and explore the possibility of acquiring it.
    """
    
    # Add offer price if provided
    if offer_price is not None:
        if not isinstance(offer_price, (int, float)) or offer_price <= 0:
            raise ValueError("Offer price must be a positive number.")
        message += f"""\n    I am willing to offer ${offer_price:,.2f} as an initial price for this domain."""

    # Closing message
    message += f"""
    
    Please feel free to reach out to me at {buyer_email} for further discussion. 
    I look forward to hearing from you soon.
    
    Best regards,
    {buyer_name}
    """

    return message.strip()


if __name__ == "__main__":
    try:
        # Example usage
        domain = "esperai.com"
        name = "John Doe"
        email = "john.doe@example.com"
        offer = 5000  # Optional; set to None if no offer price is provided

        # Generate and print message
        message = create_message_to_seller(domain, name, email, offer)
        print(message)
    except ValueError as e:
        print(f"Error: {e}")
```
