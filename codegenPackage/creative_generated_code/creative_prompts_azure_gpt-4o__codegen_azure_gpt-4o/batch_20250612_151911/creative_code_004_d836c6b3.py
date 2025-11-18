"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ksp.onsiteapp.co
Prompt: Write a script to validate user login credentials and redirect them to a team-specific dashboard, similar to the functionality implied on the King Salman Park site.
Generated: DETERMINISTIC_d836c6b3c5814e04
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import hashlib
import re

# Mock database for demonstration purposes
# In a production environment, replace this with a real database
USER_DATABASE = {
    "team1_user": {"password_hash": hashlib.sha256("password123".encode()).hexdigest(), "team": "team1"},
    "team2_user": {"password_hash": hashlib.sha256("securepass".encode()).hexdigest(), "team": "team2"}
}

# Function to validate user credentials and redirect to team dashboard
def validate_credentials_and_redirect(username, password):
    """
    Validates the login credentials provided by the user and redirects them to their team-specific dashboard.

    :param username: str - The username provided by the user
    :param password: str - The password provided by the user
    :return: str - A message indicating the result of the login attempt
    """
    try:
        # Validate input
        if not username or not password:
            return "Error: Username and password cannot be empty."

        if not re.match("^[a-zA-Z0-9_]+$", username):
            return "Error: Invalid username format. Use only letters, numbers, and underscores."
        
        # Check if the username exists in the database
        user_data = USER_DATABASE.get(username)
        if not user_data:
            return "Error: Invalid username or password."
        
        # Hash the provided password to compare with stored hash
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        # Validate the password
        if user_data["password_hash"] != password_hash:
            return "Error: Invalid username or password."
        
        # Redirect to team-specific dashboard
        team = user_data["team"]
        return f"Success: Redirecting to {team} dashboard..."
    
    except Exception as e:
        # Handle unexpected errors gracefully
        return f"Error: An unexpected error occurred - {str(e)}"

# Example usage
if __name__ == "__main__":
    # Simulate user input
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")

    # Validate credentials and perform appropriate action
    result = validate_credentials_and_redirect(username_input, password_input)
    print(result)
```
