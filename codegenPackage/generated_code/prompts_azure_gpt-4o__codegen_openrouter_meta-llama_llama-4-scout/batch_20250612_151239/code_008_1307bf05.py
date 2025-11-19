"""
Generated Code Metadata:
========================
Original URL: https://polkadots.work
Prompt: Provide code to obfuscate email addresses for spam prevention, referencing the "メールアドレスを難読化する無料ツール" feature from コピーツールラボ.
Generated: DETERMINISTIC_1307bf057d429200
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import html

def obfuscate_email(email: str) -> str:
    """
    Obfuscates an email address to prevent spam.

    Args:
    email (str): The email address to obfuscate.

    Returns:
    str: The obfuscated email address.
    """
    # Check if input is a string
    if not isinstance(email, str):
        raise TypeError("Email must be a string.")

    # Use HTML entities to obfuscate the email address
    obfuscated_email = ""
    for char in email:
        obfuscated_email += "&#" + str(ord(char)) + ";"

    return obfuscated_email

def obfuscate_email_with_links(email: str, text: str = None) -> str:
    """
    Obfuscates an email address and wraps it in a mailto link to prevent spam.

    Args:
    email (str): The email address to obfuscate.
    text (str): The text to display for the link. Defaults to the email address.

    Returns:
    str: The obfuscated email address wrapped in a mailto link.
    """
    # Check if input is a string
    if not isinstance(email, str) or (text and not isinstance(text, str)):
        raise TypeError("Email and text must be strings.")

    # Obfuscate the email address
    obfuscated_email = obfuscate_email(email)

    # Use the provided text or the email address as the link text
    if text is None:
        text = obfuscate_email(email)

    # Create the mailto link
    link = f"<a href='mailto:{obfuscated_email}'>{text}</a>"

    return link

def main():
    email = "example@example.com"
    obfuscated_email = obfuscate_email(email)
    print(f"Obfuscated Email: {obfuscated_email}")

    link = obfuscate_email_with_links(email)
    print(f"Obfuscated Email Link: {link}")

if __name__ == "__main__":
    main()
```
