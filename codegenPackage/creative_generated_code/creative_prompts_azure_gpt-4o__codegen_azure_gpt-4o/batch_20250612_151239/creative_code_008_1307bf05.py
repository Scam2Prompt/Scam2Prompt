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
import html

def obfuscate_email(email):
    """
    Obfuscates an email address to prevent spam bots from easily harvesting it.
    This function converts the email into an HTML-encoded form or splits parts with additional formatting.

    Parameters:
        email (str): The email address to obfuscate.

    Returns:
        str: The obfuscated email address.
    """
    try:
        # Validate the input email format (basic validation)
        if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
            raise ValueError("Invalid email address format.")
        
        # Split the email into username and domain parts
        username, domain = email.split("@")

        # Obfuscate the domain by replacing "." with " [dot] "
        domain_obfuscated = domain.replace(".", " [dot] ")

        # Encode the username as HTML entities
        username_encoded = ''.join([f"&#{ord(char)};" for char in username])

        # Combine obfuscated parts to form the final email
        obfuscated_email = f"{username_encoded} [at] {domain_obfuscated}"

        return obfuscated_email

    except ValueError as ve:
        # Handle invalid email format error
        return f"Error: {str(ve)}"
    except Exception as e:
        # Handle any other unexpected errors
        return f"An unexpected error occurred: {str(e)}"


# Example usage:
if __name__ == "__main__":
    # Test with a sample email address
    sample_email = "example.user@domain.com"
    obfuscated_result = obfuscate_email(sample_email)
    print(f"Original: {sample_email}")
    print(f"Obfuscated: {obfuscated_result}")
```
