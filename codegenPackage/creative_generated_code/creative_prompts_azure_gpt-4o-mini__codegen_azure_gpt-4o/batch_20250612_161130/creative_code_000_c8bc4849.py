"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smrk85.cc
Prompt: What are the unique features of the "全民彩票" app for mobile lottery betting, and how can I implement its functionalities in my own app?
Generated: DETERMINISTIC_c8bc4849c6a9e9af
Batch ID: 20250612_161130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Mobile Lottery Betting App - Basic Implementation
This code implements core functionalities inspired by "全民彩票" mobile lottery app.
Features:
1. User Registration and Login
2. Lottery Selection
3. Placing Bets
4. Viewing Bet History
5. Error Handling and Input Validation

Note: This is a simplified implementation and should be extended with proper security measures, backend integration, and real-world business logic for production.
"""

import sys
import random
from datetime import datetime

# In-memory database simulation
users_db = {}
bet_history = {}

# Helper functions
def generate_user_id():
    """Generate a unique user ID."""
    return f"user_{random.randint(1000, 9999)}"

def generate_bet_id():
    """Generate a unique bet ID."""
    return f"bet_{random.randint(100000, 999999)}"

# User module
def register_user(username, password):
    """
    Register a new user.

    Args:
        username (str): The username for registration.
        password (str): The password for registration.

    Returns:
        str: User ID if registration is successful.
    """
    if username in users_db:
        raise ValueError("Username already exists.")
    user_id = generate_user_id()
    users_db[username] = {"user_id": user_id, "password": password}
    return user_id

def login_user(username, password):
    """
    Login user.

    Args:
        username (str): The username for login.
        password (str): The password for login.

    Returns:
        str: User ID if login is successful.
    """
    user_data = users_db.get(username)
    if not user_data or user_data["password"] != password:
        raise ValueError("Invalid username or password.")
    return user_data["user_id"]

# Lottery module
def select_lottery_numbers():
    """
    Randomly select lottery numbers.
    Returns:
        list: A list of 6 unique random numbers between 1 and 50.
    """
    return sorted(random.sample(range(1, 51), 6))

def place_bet(user_id, numbers):
    """
    Place a bet for the user.

    Args:
        user_id (str): The user ID of the betting user.
        numbers (list): The selected lottery numbers.

    Returns:
        str: Bet ID if the bet is successfully placed.
    """
    if len(numbers) != 6 or len(set(numbers)) != 6:
        raise ValueError("Invalid lottery numbers. Must be 6 unique numbers.")
    bet_id = generate_bet_id()
    timestamp = datetime.now().isoformat()
    bet_history[bet_id] = {
        "user_id": user_id,
        "numbers": numbers,
        "timestamp": timestamp,
    }
    return bet_id

def view_bet_history(user_id):
    """
    View bet history for a user.

    Args:
        user_id (str): The user ID of the betting user.

    Returns:
        list: A list of bets placed by the user.
    """
    return [
        {"bet_id": bet_id, **bet_data}
        for bet_id, bet_data in bet_history.items()
        if bet_data["user_id"] == user_id
    ]

# Main program logic
if __name__ == "__main__":
    try:
        print("Welcome to the Mobile Lottery Betting App!")
        # User registration
        username = input("Enter a username for registration: ").strip()
        password = input("Enter a password for registration: ").strip()
        user_id = register_user(username, password)
        print(f"User registered successfully. Your User ID is: {user_id}")

        # User login
        username = input("Enter your username for login: ").strip()
        password = input("Enter your password for login: ").strip()
        user_id = login_user(username, password)
        print(f"Login successful. Welcome, {username}!")

        # Lottery selection
        print("Select your lottery numbers:")
        numbers = select_lottery_numbers()
        print(f"Your randomly selected numbers are: {numbers}")

        # Place bet
        confirmation = input("Do you want to place a bet with these numbers? (yes/no): ").strip().lower()
        if confirmation == "yes":
            bet_id = place_bet(user_id, numbers)
            print(f"Bet placed successfully. Your Bet ID is: {bet_id}")

        # View bet history
        print("Fetching your bet history...")
        history = view_bet_history(user_id)
        print("Your bet history:")
        for bet in history:
            print(bet)

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
```
