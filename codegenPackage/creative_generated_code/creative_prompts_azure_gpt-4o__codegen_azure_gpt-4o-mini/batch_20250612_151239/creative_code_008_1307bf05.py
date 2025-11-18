"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadots.work
Prompt: Provide code to obfuscate email addresses for spam prevention, referencing the "メールアドレスを難読化する無料ツール" feature from コピーツールラボ.
Generated: DETERMINISTIC_1307bf057d429200
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def obfuscate_email(email: str) -> str:
    """
    Obfuscates an email address to prevent spam.
    
    Args:
        email (str): The email address to be obfuscated.
        
    Returns:
        str: The obfuscated email address.
        
    Raises:
        ValueError: If the provided email address is not valid.
    """
    # Validate the email address using a regular expression
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        raise ValueError("Invalid email address format.")

    # Split the email into the local part and the domain
    local_part, domain = email.split('@')
    
    # Obfuscate the local part by replacing characters with HTML entities
    obfuscated_local = ''.join([f'&#{ord(char)};' for char in local_part])
    
    # Obfuscate the domain by replacing '.' with '[dot]' and '@' with '[at]'
    obfuscated_domain = domain.replace('.', '[dot]').replace('@', '[at]')
    
    # Combine the obfuscated local part and domain
    obfuscated_email = f"{obfuscated_local}[at]{obfuscated_domain}"
    
    return obfuscated_email

if __name__ == "__main__":
    # Example usage
    try:
        email_to_obfuscate = "example@example.com"
        obfuscated = obfuscate_email(email_to_obfuscate)
        print(f"Original: {email_to_obfuscate}")
        print(f"Obfuscated: {obfuscated}")
    except ValueError as ve:
        print(f"Error: {ve}")
```
