"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-atomcapital.com
Prompt: Develop a script to automate the generation of secure passwords for trading accounts, inspired by Atom Capital's emphasis on account security during registration.
Generated: DETERMINISTIC_7b2148c8cb3f6d4f
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
import secrets

def generate_secure_password(length=12, include_symbols=True):
    """
    Generate a secure password for trading accounts.
    
    Parameters:
    - length (int): Length of the password to be generated. Minimum is 8.
    - include_symbols (bool): Whether to include symbols in the password.

    Returns:
    - str: A securely generated password.
    
    Raises:
    - ValueError: If the provided length is less than 8.
    """
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")

    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation if include_symbols else ''

    # Create pool of characters to choose from
    all_characters = lower + upper + digits + symbols

    # Ensure the password contains at least one character from each category
    password = [
        secrets.choice(lower),  # At least one lowercase letter
        secrets.choice(upper),  # At least one uppercase letter
        secrets.choice(digits)   # At least one digit
    ]

    if include_symbols:
        password.append(secrets.choice(symbols))  # Optional: at least one symbol

    # Fill the remaining length of the password randomly
    password += [secrets.choice(all_characters) for _ in range(length - len(password))]

    # Shuffle the result to ensure randomness
    random.shuffle(password)

    return ''.join(password)

def main():
    """
    Main function to generate and print a secure password.
    """
    try:
        password_length = int(input("Enter the desired password length (minimum 8): "))
        include_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
        
        # Generate secure password
        secure_password = generate_secure_password(length=password_length, include_symbols=include_symbols)
        
        # Output the generated password
        print(f"Generated secure password: {secure_password}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
