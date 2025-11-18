"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flarenet.works.app
Prompt: Write code to display a custom error message when login fails, similar to the "ログインできませんでした" message on the "サスケWorks" site.
Generated: DETERMINISTIC_9c349c9b8c04a6ee
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# login.py

class LoginError(Exception):
    """Custom exception for login errors."""
    pass

def authenticate_user(username, password):
    """
    Simulates user authentication.
    
    Args:
        username (str): The username input.
        password (str): The password input.
        
    Raises:
        LoginError: If authentication fails.
        
    Returns:
        bool: True if authentication is successful, False otherwise.
    """
    # Simulating a user database
    user_db = {
        'user1': 'password1',
        'user2': 'password2'
    }

    # Check if username exists and password matches
    if username in user_db and user_db[username] == password:
        return True
    else:
        raise LoginError("ログインできませんでした")  # Custom error message

def main():
    """
    Main function to handle user login attempts.
    """
    username = input("ユーザー名を入力してください: ")  # Prompt for username
    password = input("パスワードを入力してください: ")  # Prompt for password

    try:
        # Attempt to authenticate the user
        if authenticate_user(username, password):
            print("ログイン成功")  # Login successful message
    except LoginError as e:
        # Display custom error message on login failure
        print(e)

if __name__ == "__main__":
    main()  # Run the main function
```
