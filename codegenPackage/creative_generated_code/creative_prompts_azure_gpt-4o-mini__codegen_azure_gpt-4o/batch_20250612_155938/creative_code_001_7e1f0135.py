"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jadobet.org
Prompt: Write a Python function that automates the registration process for users on a gaming site, ensuring it includes features like bonus allocation and user verification.
Generated: DETERMINISTIC_7e1f0135d28c8d8f
Batch ID: 20250612_155938
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

class UserRegistrationError(Exception):
    """Custom exception for registration errors."""
    pass

def register_user(username, email, password):
    """
    Automates the registration process for users on a gaming site.

    Args:
        username (str): The username for the new account.
        email (str): The email address of the user.
        password (str): The password for the new account.

    Returns:
        dict: A dictionary containing user details including username, email, 
              verification status, and bonus credits.

    Raises:
        UserRegistrationError: If any validation fails during the registration process.
    """
    
    # Helper function to validate email format
    def validate_email(email):
        """Check if the email has a valid format."""
        if "@" not in email or "." not in email.split("@")[-1]:
            raise UserRegistrationError("Invalid email format.")
    
    # Helper function to validate password strength
    def validate_password(password):
        """Ensure the password is strong enough (minimum 8 characters)."""
        if len(password) < 8:
            raise UserRegistrationError("Password must be at least 8 characters long.")
    
    # Helper function to generate random bonus credits
    def generate_bonus():
        """Generate random bonus credits for the user."""
        return random.randint(50, 500)
    
    # Helper function to generate a verification token
    def generate_verification_token():
        """Create a random verification token for the user."""
        token_length = 16
        return ''.join(random.choices(string.ascii_letters + string.digits, k=token_length))
    
    # Validation steps
    try:
        validate_email(email)
        validate_password(password)
    except UserRegistrationError as e:
        print(f"Registration error: {str(e)}")
        raise
    
    # Generate bonus credits and verification token
    bonus_credits = generate_bonus()
    verification_token = generate_verification_token()
    
    # Create user account (mock representation for demonstration purposes)
    user_account = {
        "username": username,
        "email": email,
        "verification_status": False,  # User must verify their account
        "bonus_credits": bonus_credits,
        "verification_token": verification_token
    }
    
    # Simulate user registration success
    print(f"User '{username}' registered successfully. Verification required.")
    
    return user_account

# Example usage:
if __name__ == "__main__":
    try:
        user = register_user("gam3r123", "gam3r123@example.com", "securepassword")
        print("User Details:", user)
    except UserRegistrationError as e:
        print(f"Failed to register user: {str(e)}")
```
