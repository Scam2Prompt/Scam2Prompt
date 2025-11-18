"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://westrockhomo.multitransportador.com.br
Prompt: Write code to reset a user's password in the MultiTMS system, ensuring compliance with secure authentication protocols.
Generated: DETERMINISTIC_93fdcf9838065d24
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import random
import string
from typing import Optional, Dict

# Simulated database of users
user_database: Dict[str, str] = {}

def generate_random_password(length: int = 12) -> str:
    """
    Generate a random password consisting of letters and digits.
    
    Args:
        length (int): The length of the password to generate. Default is 12.
    
    Returns:
        str: The generated random password.
    """
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt.
    
    Args:
        password (str): The password to hash.
    
    Returns:
        str: The hashed password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def reset_password(username: str, new_password: Optional[str] = None) -> bool:
    """
    Reset the user's password in the MultiTMS system.
    
    Args:
        username (str): The username of the user whose password is to be reset.
        new_password (Optional[str]): The new password to set. 
                                      If None, a random password will be generated.
    
    Returns:
        bool: True if the password was reset successfully, False otherwise.
    """
    # Check if user exists in the database
    if username not in user_database:
        print(f"Error: User '{username}' not found.")
        return False
    
    # Generate a new random password if not provided
    if new_password is None:
        new_password = generate_random_password()

    # Hash the new password
    hashed_password = hash_password(new_password)

    # Update the user database with the new hashed password
    user_database[username] = hashed_password

    print(f"Password for user '{username}' has been reset successfully.")
    print(f"New Password (please store it securely): {new_password}")
    return True

# Example usage:
if __name__ == "__main__":
    # Prepopulate database with a user for demonstration
    user_database['john_doe'] = hash_password('initialPassword123')

    # Reset the password for 'john_doe'
    reset_password('john_doe')
    
    # Reset the password for a non-existent user
    reset_password('jane_doe')
```
