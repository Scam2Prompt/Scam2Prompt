"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mtch.pro
Prompt: Create a function to handle user registration via Telegram, including sending a new verification code if requested and updating email addresses.
Generated: DETERMINISTIC_c5eaefd07b675d1b
Batch ID: 20250612_145719
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
from datetime import datetime, timedelta
from typing import Dict

# Mock database to store user data
users_db = {}

# Function to generate a random verification code
def generate_verification_code(length: int = 6) -> str:
    """Generate a random alphanumeric verification code."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# Function to handle user registration and verification via Telegram
def handle_user_registration(user_id: int, email: str, request_type: str = "register") -> Dict:
    """
    Handle user registration and email updates via Telegram.
    
    Args:
        user_id (int): The unique identifier of the user in Telegram.
        email (str): The email address provided by the user.
        request_type (str): Type of request ('register', 'resend_code', or 'update_email').
    
    Returns:
        Dict: A response dictionary with status and message.
    """
    try:
        # Validate the request type
        if request_type not in {"register", "resend_code", "update_email"}:
            return {"status": "error", "message": "Invalid request type."}

        # Check if the user already exists in the database
        user_data = users_db.get(user_id)
        
        # Handle "register" request
        if request_type == "register":
            if user_data:
                return {"status": "error", "message": "User already registered."}
            
            # Generate a new verification code
            verification_code = generate_verification_code()
            expiration_time = datetime.now() + timedelta(minutes=15)  # Code expires in 15 minutes
            
            # Save user data to the database
            users_db[user_id] = {
                "email": email,
                "verification_code": verification_code,
                "code_expiration": expiration_time,
                "is_verified": False
            }
            
            # Simulate sending the verification code via Telegram
            # (In production, integrate with Telegram Bot API to send the code)
            print(f"Verification code sent to user {user_id}: {verification_code}")
            
            return {"status": "success", "message": "Verification code sent."}
        
        # Handle "resend_code" request
        elif request_type == "resend_code":
            if not user_data:
                return {"status": "error", "message": "User not found. Please register first."}
            
            if user_data["is_verified"]:
                return {"status": "error", "message": "User already verified."}
            
            # Generate and send a new verification code
            verification_code = generate_verification_code()
            expiration_time = datetime.now() + timedelta(minutes=15)
            user_data["verification_code"] = verification_code
            user_data["code_expiration"] = expiration_time
            
            # Simulate sending the verification code via Telegram
            print(f"New verification code sent to user {user_id}: {verification_code}")
            
            return {"status": "success", "message": "New verification code sent."}
        
        # Handle "update_email" request
        elif request_type == "update_email":
            if not user_data:
                return {"status": "error", "message": "User not found. Please register first."}
            
            if not user_data["is_verified"]:
                return {"status": "error", "message": "User not verified. Please verify your account first."}
            
            # Update the user's email address
            user_data["email"] = email
            return {"status": "success", "message": "Email address updated successfully."}
    
    except Exception as e:
        # Handle any unexpected errors
        return {"status": "error", "message": f"An internal error occurred: {str(e)}"}

# Example usage
if __name__ == "__main__":
    print(handle_user_registration(12345, "user@example.com", "register"))  # Register a new user
    print(handle_user_registration(12345, "user@example.com", "resend_code"))  # Resend verification code
    print(handle_user_registration(12345, "new_email@example.com", "update_email"))  # Update email address
```
