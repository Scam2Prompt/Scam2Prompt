"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamsbat.com
Prompt: How can I implement a referral system for an NFT game similar to Hamster Kombat?
Generated: DETERMINISTIC_7b68b291dc3b351c
Batch ID: 20250612_163926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from typing import Dict, Optional

# A dictionary to store user data and their referrals
users: Dict[str, Dict] = {}

# Function to create a unique referral code
def generate_referral_code() -> str:
    """
    Generate a unique referral code using UUID.
    """
    return str(uuid.uuid4())[:8]

# Function to register a new user
def register_user(username: str, referred_by: Optional[str] = None) -> str:
    """
    Register a new user, optionally linking them to a referral code.
    
    Args:
        username (str): The username of the new user.
        referred_by (Optional[str]): The referral code of the user who referred them.

    Returns:
        str: The generated referral code for the new user.
    """
    if username in users:
        raise ValueError("Username already exists.")

    # Check if the referral code is valid
    if referred_by and referred_by not in users:
        raise ValueError("Invalid referral code.")

    # Generate a new referral code for the user
    referral_code = generate_referral_code()
    users[username] = {
        "username": username,
        "referral_code": referral_code,
        "referred_by": referred_by,
        "referrals": []  # List of users referred by this user
    }

    # Update the referrer's referral list
    if referred_by:
        referrer_username = next(
            (key for key, value in users.items() if value["referral_code"] == referred_by), None
        )
        if referrer_username:
            users[referrer_username]["referrals"].append(username)

    return referral_code

# Function to fetch user details
def get_user(username: str) -> Dict:
    """
    Retrieve information about a user.
    
    Args:
        username (str): The username of the user to fetch.

    Returns:
        Dict: The user's details.
    """
    if username not in users:
        raise ValueError("User not found.")

    return users[username]

# Example usage
if __name__ == "__main__":
    try:
        # Register some users
        alice_code = register_user("Alice")
        print(f"Alice's referral code: {alice_code}")

        bob_code = register_user("Bob", referred_by=alice_code)
        print(f"Bob's referral code: {bob_code}")

        charlie_code = register_user("Charlie", referred_by=alice_code)
        print(f"Charlie's referral code: {charlie_code}")

        # Fetch user details
        print("Alice's details:", get_user("Alice"))
        print("Bob's details:", get_user("Bob"))
        print("Charlie's details:", get_user("Charlie"))
    except Exception as e:
        print(f"Error: {e}")
```
