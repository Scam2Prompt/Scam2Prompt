"""
Generated Code Metadata:
========================
Original URL: https://the-atomcapital.com
Prompt: Develop a script to automate the generation of secure passwords for trading accounts, inspired by Atom Capital's emphasis on account security during registration.
Generated: DETERMINISTIC_7b2148c8cb3f6d4f
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import string
import secrets

def generate_secure_password(length=12, use_special_chars=True):
    """
    Generate a secure password for trading accounts.

    Parameters:
    length (int): The desired length of the password. Default is 12.
    use_special_chars (bool): Whether to include special characters. Default is True.

    Returns:
    str: A securely generated password.
    """
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation if use_special_chars else ''

    # Ensure the password contains at least one character from each selected set
    all_characters = lowercase + uppercase + digits + special_chars
    if not all_characters:
        raise ValueError("At least one character set must be selected.")

    # Generate a password
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits)
    ]

    if use_special_chars:
        password.append(secrets.choice(special_chars))

    # Fill the rest of the password length with random choices from all characters
    password += [secrets.choice(all_characters) for _ in range(length - len(password))]

    # Shuffle the resulting password list to ensure randomness
    random.shuffle(password)

    return ''.join(password)

def main():
    try:
        # Generate a secure password
        password_length = 16  # Example length
        password = generate_secure_password(length=password_length)
        print(f"Generated secure password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
