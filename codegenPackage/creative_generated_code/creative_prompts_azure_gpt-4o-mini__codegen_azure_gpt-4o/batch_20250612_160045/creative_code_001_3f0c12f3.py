"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanbet.co
Prompt: Write a script that automates user registration and bonus allocation for a gaming website similar to BaxBet.
Generated: DETERMINISTIC_3f0c12f38658ef0f
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import uuid
from datetime import datetime

# Database simulation (In production, use a proper database like PostgreSQL, MySQL, etc.)
database = {
    "users": [],
}

# User registration function
def register_user(username, email):
    """
    Registers a new user, validates input, assigns unique IDs, and adds a bonus amount.
    
    Args:
        username (str): The username of the user.
        email (str): The email address of the user.
    
    Returns:
        dict: A dictionary containing user information on successful registration.
    Raises:
        ValueError: If any validation fails.
    """
    # Input validation
    if not username or len(username) < 3:
        raise ValueError("Username must be at least 3 characters long.")
    
    if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("Invalid email format.")

    # Check for duplicates
    if any(user['email'] == email for user in database['users']):
        raise ValueError("Email is already registered.")
    
    if any(user['username'] == username for user in database['users']):
        raise ValueError("Username is already taken.")

    # Generate unique user ID
    user_id = str(uuid.uuid4())

    # Assign bonus amount
    bonus = 100  # In production, this may come from a configuration file

    # Create user data entry
    user_data = {
        "id": user_id,
        "username": username,
        "email": email,
        "registration_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "bonus": bonus,
    }

    # Save user to the database
    database['users'].append(user_data)

    return user_data

# Main script execution
if __name__ == "__main__":
    try:
        # Example user data (In production, use input() or a web interface for collecting user data)
        username = "gamer123"
        email = "gamer123@example.com"

        # Register the user
        new_user = register_user(username, email)
        
        # Output result
        print("User registered successfully!")
        print(f"User ID: {new_user['id']}")
        print(f"Username: {new_user['username']}")
        print(f"Email: {new_user['email']}")
        print(f"Registration Date: {new_user['registration_date']}")
        print(f"Bonus Amount: {new_user['bonus']}")

    except ValueError as e:
        # Handle validation errors
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
```
