"""
Generated Code Metadata:
========================
Original URL: https://taikoi.fi
Prompt: Write a Finnish-language domain reservation confirmation message similar to the one on taikoi.fi.
Generated: DETERMINISTIC_3fd99c16e2942d2c
Batch ID: 20250622_204857
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_confirmation_message(domain_name: str, reservation_id: str, expiry_date: str) -> str:
    """
    Generates a Finnish domain reservation confirmation message.
    
    Args:
        domain_name (str): The domain name being reserved
        reservation_id (str): Unique reservation identifier
        expiry_date (str): Reservation expiry date in format DD.MM.YYYY
    
    Returns:
        str: Formatted confirmation message in Finnish
    """
    message = f"""
Hei,

Kiitos verkkotunnuksen {domain_name} varauksestasi!

Varauksesi tiedot:
- Verkkotunnus: {domain_name}
- Varausnumero: {reservation_id}
- Varaus päättyy: {expiry_date}

Varauksesi on nyt aktiivinen. Muista rekisteröidä verkkotunnus ennen varauksen päättymistä.

Jos sinulla on kysyttävää, ole hyvä ja ota yhteyttä asiakaspalveluumme.

Ystävällisin terveisin,
Taikoi.fi-tiimi
"""
    return message.strip()


def send_confirmation_email(email: str, message: str) -> bool:
    """
    Sends confirmation email to customer.
    
    Args:
        email (str): Recipient email address
        message (str): Confirmation message content
    
    Returns:
        bool: True if email was sent successfully, False otherwise
    """
    try:
        # Implementation would use actual email sending library
        # This is just a placeholder for demonstration
        print(f"Sending email to: {email}")
        print("Message content:")
        print(message)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
```
