"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mehmedshop.com
Prompt: Write a function to handle user registration (Daftar) for an online gambling site using WhatsApp and Telegram.
Generated: DETERMINISTIC_a954813ab6340e1b
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from typing import Tuple

# Database simulation (replace with actual database implementation in production)
users_db = {}

# Function to validate phone number
def validate_phone_number(phone: str) -> bool:
    """
    Validates the phone number format.
    Accepts international and local formats.
    """
    pattern = r'^\+?[1-9]\d{1,14}$'
    return bool(re.match(pattern, phone))

# Function to validate username
def validate_username(username: str) -> bool:
    """
    Validates the username format.
    Only allows alphanumeric characters and underscores.
    """
    pattern = r'^[a-zA-Z0-9_]{3,20}$'
    return bool(re.match(pattern, username))

# Function to handle user registration
def daftar(platform: str, username: str, phone: str) -> Tuple[bool, str]:
    """
    Handles user registration for WhatsApp and Telegram gambling platform.
    
    Args:
        platform (str): The platform used for registration ("WhatsApp" or "Telegram").
        username (str): The username selected by the user.
        phone (str): The phone number of the user.
        
    Returns:
        Tuple[bool, str]: A tuple containing success status and a message.
    """
    try:
        # Validate platform
        if platform.lower() not in ["whatsapp", "telegram"]:
            return False, "Invalid platform. Please use 'WhatsApp' or 'Telegram'."
        
        # Validate username
        if not validate_username(username):
            return False, "Invalid username. Must be 3-20 characters, alphanumeric or underscore."
        
        # Validate phone number
        if not validate_phone_number(phone):
            return False, "Invalid phone number. Must be a valid format."
        
        # Check for existing user
        if phone in users_db:
            return False, f"Phone number {phone} is already registered. Please use a different number."
        
        # Register user
        users_db[phone] = {"platform": platform, "username": username}
        return True, f"Success! User '{username}' registered via {platform}."
    
    except Exception as e:
        return False, f"An error occurred during registration: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Simulating user registration
    success, message = daftar("WhatsApp", "John_Doe", "+1234567890")
    print(message)  # Output the result

    success, message = daftar("Telegram", "JaneDoe123", "+9876543210")
    print(message)  # Output the result
```
